#!/usr/bin/env python3
"""MirrorHub 节点测速脚本
测试所有节点的延迟和可用性，输出结果到 test-results.json
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error
import ssl
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
NODES_FILE = os.path.join(HERE, "..", "nodes.json")
PENDING_FILE = os.path.join(HERE, "..", "pending.json")
OUTPUT_FILE = os.path.join(HERE, "..", "test-results.json")

# 测试用的小文件（octocat/Hello-World 的 README，只有几字节）
TEST_RAW_URL = "https://raw.githubusercontent.com/octocat/Hello-World/master/README"
TEST_RELEASE_URL = "https://github.com/octocat/Hello-World/releases/download/v1.0.0/README.md"

# 带宽测速样本（Linux 仓库稳定大文件，经代理下载累计字节测 MB/s）
BANDWIDTH_SAMPLES = [
    "https://raw.githubusercontent.com/torvalds/linux/master/README",
    "https://raw.githubusercontent.com/torvalds/linux/master/MAINTAINERS",
]
BANDWIDTH_MAX_BYTES = 512 * 1024  # 最多下载 512KB 计时
BANDWIDTH_TIMEOUT = 15

TIMEOUT = 10  # 秒
MAX_WORKERS = 15

# 忽略 SSL 证书错误（部分公益节点证书有问题）
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def build_test_urls(node: dict, category: str) -> list:
    """根据节点类型构建测试 URL 列表（通用代理返回 raw+release 两个）"""
    url = node["url"]
    template = node.get("url_template")

    if category == "cdn_raw":
        if template:
            return [template.format(node_url=url, owner="octocat", repo="Hello-World", ref="master", path="README")]
        return [f"https://{url}/gh/octocat/Hello-World@master/README"]

    if category == "clone_specialized":
        if template:
            base = template.format(node_url=url, owner="octocat", repo="Hello-World")
            return [base.replace(".git", ".git/info/refs?service=git-upload-pack")]
        return [f"{url}/github.com/octocat/Hello-World.git/info/refs?service=git-upload-pack"]

    if category == "web_mirror":
        return [url]

    # 通用代理：同时测 raw 和 release，只要一个成功就算在线
    urls = []
    if template:
        if "{github_url}" in template:
            urls.append(template.format(node_url=url, github_url=TEST_RAW_URL))
            urls.append(template.format(node_url=url, github_url=TEST_RELEASE_URL))
        elif "{path}" in template:
            urls.append(template.format(node_url=url, path="octocat/Hello-World/master/README"))
        else:
            urls.append(f"{url}/{TEST_RAW_URL}")
            urls.append(f"{url}/{TEST_RELEASE_URL}")
    else:
        urls.append(f"{url}/{TEST_RAW_URL}")
        urls.append(f"{url}/{TEST_RELEASE_URL}")
    return urls


def _try_url(test_url: str) -> tuple:
    """尝试请求一个 URL，返回 (success, latency_ms, http_status, error)"""
    try:
        req = urllib.request.Request(test_url, headers={
            "User-Agent": "MirrorHub-HealthCheck/1.0",
            "Accept": "*/*"
        })
        start = time.time()
        resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
        elapsed = (time.time() - start) * 1000
        resp.read(1024)
        resp.close()
        if resp.status in (200, 301, 302, 304, 307, 308):
            return (True, round(elapsed), resp.status, None)
        return (False, round(elapsed), resp.status, f"HTTP {resp.status}")
    except urllib.error.HTTPError as e:
        elapsed = (time.time() - start) * 1000 if 'start' in dir() else None
        if e.code in (301, 302, 304, 307, 308):
            return (True, round(elapsed) if elapsed else None, e.code, None)
        return (False, round(elapsed) if elapsed else None, e.code, f"HTTP {e.code}")
    except Exception as e:
        return (False, None, None, str(e)[:100])


def measure_bandwidth(proxy_url: str, category: str) -> float:
    """经代理下载样本文件测带宽，返回 MB/s。

    顺序下载样本直到累计 512KB 或文件读尽，计时算吞吐。
    只有通用代理/CDN 形态支持 raw 路径下载；网页镜像/Clone 专用跳过。
    """
    if category in ("web_mirror", "clone_specialized"):
        return None
    if os.environ.get("BANDWIDTH_TEST", "1") == "0":
        return None
    total_bytes = 0
    start = time.time()
    for sample in BANDWIDTH_SAMPLES:
        if total_bytes >= BANDWIDTH_MAX_BYTES:
            break
        test_url = f"{proxy_url.rstrip('/')}/{sample}"
        try:
            req = urllib.request.Request(test_url, headers={
                "User-Agent": "MirrorHub-HealthCheck/1.0",
                "Accept": "*/*",
            })
            resp = urllib.request.urlopen(req, timeout=BANDWIDTH_TIMEOUT, context=ctx)
            remaining = BANDWIDTH_MAX_BYTES - total_bytes
            while remaining > 0:
                chunk = resp.read(min(65536, remaining))
                if not chunk:
                    break
                total_bytes += len(chunk)
                remaining -= len(chunk)
            resp.close()
        except Exception:
            break
    elapsed = time.time() - start
    if total_bytes < 8192 or elapsed <= 0:
        return None
    return round(total_bytes / 1024 / 1024 / elapsed, 2)


def test_node(node_id: str, node: dict, category: str) -> dict:
    """测试单个节点，尝试多个 URL，取最快的成功结果"""
    test_urls = build_test_urls(node, category)
    result = {
        "id": node_id,
        "category": category,
        "test_url": test_urls[0],
        "test_urls": test_urls,
        "status": "unknown",
        "latency_ms": None,
        "http_status": None,
        "error": None,
        "succeeded_url": None,
        "bandwidth_mbps": None,
    }

    best_latency = None
    last_error = None

    for test_url in test_urls:
        success, latency, http_status, error = _try_url(test_url)
        if success:
            if best_latency is None or (latency and latency < best_latency):
                best_latency = latency
                result["latency_ms"] = latency
                result["http_status"] = http_status
                result["test_url"] = test_url
                result["succeeded_url"] = test_url
            result["status"] = "online"
            result["error"] = None
        else:
            last_error = error

    if result["status"] != "online":
        result["status"] = "offline"
        result["error"] = last_error
    else:
        # 在线节点追加带宽测速
        result["bandwidth_mbps"] = measure_bandwidth(node["url"], category)

    return result


def main():
    # 读取节点
    with open(NODES_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)

    # 收集所有节点
    all_nodes = []
    for cat_name, cat_data in config["categories"].items():
        for node in cat_data["nodes"]:
            all_nodes.append((node["id"], node, cat_name))

    # 读取 pending 节点
    if os.path.exists(PENDING_FILE):
        with open(PENDING_FILE, "r", encoding="utf-8") as f:
            pending = json.load(f)
        for node in pending.get("nodes", []):
            all_nodes.append((node["id"], node, node.get("category", "universal_proxy")))

    print(f"开始测速，共 {len(all_nodes)} 个节点，并发 {MAX_WORKERS}...")

    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(test_node, nid, node, cat): nid for nid, node, cat in all_nodes}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            status_icon = "✅" if result["status"] == "online" else "⚠️" if result["status"] == "unstable" else "❌"
            latency = f"{result['latency_ms']}ms" if result['latency_ms'] else "timeout"
            print(f"  {status_icon} {result['id']}: {latency}")

    # 统计
    online = sum(1 for r in results if r["status"] == "online")
    unstable = sum(1 for r in results if r["status"] == "unstable")
    offline = sum(1 for r in results if r["status"] == "offline")

    output = {
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "summary": {
            "total": len(results),
            "online": online,
            "unstable": unstable,
            "offline": offline
        },
        "results": results
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n测速完成：✅ {online} 在线，⚠️ {unstable} 不稳定，❌ {offline} 离线")
    print(f"结果已保存到 {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
