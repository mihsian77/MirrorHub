#!/usr/bin/env python3
"""MirrorHub Python 接入示例
用法：复制本文件到项目中，调用 get_fastest_download_url()
"""
import json
import time
import urllib.request
from typing import Optional

NODES_URL = "https://raw.githubusercontent.com/mihsian77/MirrorHub/main/nodes.json"
STATUS_URL = "https://raw.githubusercontent.com/mihsian77/MirrorHub/main/status.json"
CACHE_TTL = 3600  # 1小时

_nodes_cache = None
_status_cache = None
_last_fetch = 0


def _fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "MirrorHub-Client/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _ensure_cache():
    global _nodes_cache, _status_cache, _last_fetch
    if time.time() - _last_fetch < CACHE_TTL and _nodes_cache is not None:
        return
    try:
        nodes_config = _fetch_json(NODES_URL)
        status_config = _fetch_json(STATUS_URL)
        # 展平所有节点
        all_nodes = {}
        for cat_data in nodes_config.get("categories", {}).values():
            for node in cat_data.get("nodes", []):
                all_nodes[node["id"]] = node
        _nodes_cache = all_nodes
        _status_cache = status_config.get("nodes", {})
        _last_fetch = time.time()
    except Exception:
        # 拉取失败时使用旧缓存
        pass


def get_fastest_download_url(github_url: str, traffic_type: str = "release") -> Optional[str]:
    """获取最快的可用下载 URL，无可用节点时返回 None（调用方用直连）"""
    _ensure_cache()
    if not _nodes_cache or not _status_cache:
        return None

    # 过滤在线且支持该流量类型的节点，按平均延迟排序
    candidates = []
    for nid, node in _nodes_cache.items():
        status = _status_cache.get(nid, {})
        if status.get("status") == "online" and traffic_type in node.get("supports", []):
            latency = status.get("avg_latency_ms") or status.get("latency_ms") or 99999
            candidates.append((latency, node))

    candidates.sort(key=lambda x: x[0])

    # 拼接 URL（取最快的）
    for _, node in candidates[:3]:
        template = node.get("url_template") or "{node_url}/{github_url}"
        return (template
                .replace("{node_url}", node["url"])
                .replace("{github_url}", github_url))

    return None


def get_online_nodes(traffic_type: str = "release") -> list:
    """获取所有在线节点列表（按延迟排序）"""
    _ensure_cache()
    if not _nodes_cache or not _status_cache:
        return []

    result = []
    for nid, node in _nodes_cache.items():
        status = _status_cache.get(nid, {})
        if status.get("status") == "online" and traffic_type in node.get("supports", []):
            result.append({
                "id": nid,
                "name": node["name"],
                "url": node["url"],
                "latency_ms": status.get("avg_latency_ms") or status.get("latency_ms"),
            })
    result.sort(key=lambda x: x["latency_ms"] or 99999)
    return result


if __name__ == "__main__":
    # 使用示例
    url = "https://github.com/octocat/Hello-World/releases/download/v1.0.0/README.md"
    accelerated = get_fastest_download_url(url)
    if accelerated:
        print(f"加速 URL: {accelerated}")
    else:
        print("无可用加速节点，使用直连")

    print("\n在线节点（release 下载）:")
    for n in get_online_nodes("release")[:10]:
        print(f"  {n['latency_ms']:>6}ms  {n['name']:<20} {n['url']}")
