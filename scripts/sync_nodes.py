#!/usr/bin/env python3
"""MirrorHub 节点同步脚本

发现新节点的两条通道：
1. 来源清单（sources.json）：按 extract_method 拉取文本提取域名
   - regex_domains: 代理前缀+github.com 模式（精确）
   - regex_domains_generic: 任意 https 域名（宽泛，测速兜底淘汰）
2. GitHub Code Search：按 code_search_keywords 搜索包含代理域名的代码仓库，
   自动发现新节点项目并提取域名（workflow 用内置 GITHUB_TOKEN，本地无 token 时跳过）

新域名统一进入 pending.json，由 test_nodes.py 测速验证后转 active。
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
NODES_FILE = os.path.join(HERE, "..", "nodes.json")
PENDING_FILE = os.path.join(HERE, "..", "pending.json")
SOURCES_FILE = os.path.join(HERE, "..", "sources.json")

# 非代理域名黑名单：GitHub 官方、包源、常见无关站点（generic 提取用）
EXCLUDE_DOMAINS = {
    "github.com", "raw.githubusercontent.com", "gist.github.com",
    "api.github.com", "codeload.github.com", "objects.githubusercontent.com",
    "githubusercontent.com", "avatars.githubusercontent.com",
    "camo.githubusercontent.com", "user-images.githubusercontent.com",
    "github.githubassets.com", "github.io", "github.blog",
    "pypi.org", "mirrors.aliyun.com", "mirrors.cloud.tencent.com",
    "pypi.mirrors.ustc.edu.cn", "mirrors.ustc.edu.cn", "mirrors.sustech.edu.cn",
    "anaconda.com", "conda.io",
    "example.com", "google.com", "googleapis.com", "youtube.com", "wikipedia.org",
    "cloudflare.com", "cloudflareinsights.com", "static.cloudflareinsights.com",
    "jsdelivr.net", "unpkg.com", "npmjs.com", "gitee.com", "gitlab.com",
    "bing.com", "baidu.com", "qq.com", "weixin.qq.com", "w3.org", "mozilla.org",
    "schema.org", "googletagmanager.com", "pagead2.googlesyndication.com",
    "optout.networkadvertising.org", "moretools.app", "moregames.app",
    "docker.com", "hub.docker.com", "microsoft.com", "apple.com",
    "amazon.com", "aws.amazon.com",
    # 自动发现噪声：开发/部署平台、无关网站
    "chromium.org", "crbug.com", "apps.apple.com", "chromewebstore.google.com",
    "console.cloud.google.com", "deploy.workers.cloudflare.com",
    "dash.cloudflare.com", "dns.google", "domain.com", "addons.mozilla.org",
    "api.star-history.com", "docker-proxy.example.com", "crashmc.com",
}

# 域名黑名单，命中直接跳过（用于 generic 提取的轻量预筛）
GENERIC_EXCLUDE_SUFFIXES = (".github.io", ".jsdelivr.net", ".googleapis.com", ".cloudfront.net")


def load_json(path, default=None):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default if default is not None else {}


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def clean_domain(raw: str) -> str:
    """去掉域名尾部误带的分隔符/标点"""
    return re.sub(r'[)\]},;。，；、]+$', '', raw).lower()


def extract_domains_from_text(text: str) -> set:
    """精确提取：代理前缀 + /https://github.com 或 /github.com/ 模式"""
    domains = set()
    for m in re.finditer(r'https?://([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})/https?://github\.com', text):
        domain = clean_domain(m.group(1))
        if domain not in EXCLUDE_DOMAINS:
            domains.add(domain)
    for m in re.finditer(r'https?://([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})/github\.com/', text):
        domain = clean_domain(m.group(1))
        if domain not in EXCLUDE_DOMAINS:
            domains.add(domain)
    return domains


def extract_domains_generic(text: str) -> set:
    """宽泛提取：所有 https URL 的域名，排除黑名单。

    抓进来的非代理域名会经测速淘汰（raw/release 探测失败→pending→graveyard），
    所以这里只需要挡住明显的无关系统域名。
    """
    domains = set()
    for m in re.finditer(r'https?://([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)', text):
        domain = clean_domain(m.group(1))
        if domain.startswith("www."):
            domain = domain[4:]
        if not domain or domain in EXCLUDE_DOMAINS:
            continue
        if domain.endswith(GENERIC_EXCLUDE_SUFFIXES):
            continue
        # 只收标准域名形态（至少两段），避免 IP/内网
        if domain.count(".") >= 1 and domain[-1].isalpha():
            domains.add(domain)
    return domains


def code_search_domains(sources_cfg: dict) -> set:
    """自动发现：GitHub repo search 搜代理相关项目 → 抓 README 提取新节点。

    用 repo search（认证 30 req/min）而不是 code search（10 req/min，runner IP
    极易 429）。搜到的新仓库打印出来，域名统一进 pending 测速验证。
    workflow 用内置 GITHUB_TOKEN；本地无 token 时跳过。
    """
    token = os.environ.get("GITHUB_TOKEN", "")
    keywords = sources_cfg.get("code_search_keywords", [])
    if not token:
        print("  ⏭ 无 GITHUB_TOKEN，跳过自动发现（workflow 中自动启用）")
        return set()
    if not keywords:
        print("  ⏭ code_search_keywords 为空，跳过自动发现")
        return set()

    domains = set()
    print(f"\n自动发现（repo search，{len(keywords)} 个关键词）:")
    for kw in keywords:
        q = urllib.parse.quote(kw)
        req = urllib.request.Request(
            f"https://api.github.com/search/repositories?q={q}&sort=updated&per_page=5",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "User-Agent": "MirrorHub-Sync/1.0",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.load(resp)
            items = data.get("items", [])
            print(f"  「{kw}」: {len(items)} 个仓库")
            for repo in items:
                full = repo.get("full_name", "")
                branch = repo.get("default_branch", "main")
                if not full:
                    continue
                found = set()
                for b in {branch, "main", "master"}:
                    try:
                        rreq = urllib.request.Request(
                            f"https://raw.githubusercontent.com/{full}/{b}/README.md",
                            headers={"User-Agent": "MirrorHub-Sync/1.0"},
                        )
                        with urllib.request.urlopen(rreq, timeout=15) as rresp:
                            text = rresp.read().decode("utf-8", errors="ignore")
                        found = extract_domains_generic(text)
                        if found:
                            break
                    except Exception:
                        continue
                if found:
                    print(f"    → {full}: +{len(found)} 域名")
                    domains |= found
            time.sleep(2)  # repo search 30 req/min，留余量
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"  ❌「{kw}」: 429 限流，等待 60s 重试一次")
                time.sleep(60)
                try:
                    with urllib.request.urlopen(req, timeout=20) as resp:
                        data = json.load(resp)
                    for repo in data.get("items", []):
                        full = repo.get("full_name", "")
                        branch = repo.get("default_branch", "main")
                        found = set()
                        for b in {branch, "main", "master"}:
                            try:
                                rreq = urllib.request.Request(
                                    f"https://raw.githubusercontent.com/{full}/{b}/README.md",
                                    headers={"User-Agent": "MirrorHub-Sync/1.0"},
                                )
                                with urllib.request.urlopen(rreq, timeout=15) as rresp:
                                    text = rresp.read().decode("utf-8", errors="ignore")
                                found = extract_domains_generic(text)
                                if found:
                                    break
                            except Exception:
                                continue
                        if found:
                            print(f"    → {full}: +{len(found)} 域名")
                            domains |= found
                except Exception as e2:
                    print(f"  ❌「{kw}」重试失败: {e2}")
            else:
                print(f"  ❌「{kw}」: {e}")
            time.sleep(2)
        except Exception as e:
            print(f"  ❌「{kw}」: {e}")
            time.sleep(2)
    return domains


def generate_node_id(domain: str) -> str:
    """从域名生成节点 ID"""
    return domain.replace(".", "-").replace("/", "-").strip("-")


def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    sources = load_json(SOURCES_FILE, {"sources": []})
    nodes_config = load_json(NODES_FILE, {"categories": {}})
    pending = load_json(PENDING_FILE, {"nodes": []})

    # 收集已有节点的域名
    existing_domains = set()
    for cat_data in nodes_config["categories"].values():
        for node in cat_data["nodes"]:
            url = node["url"].rstrip("/")
            domain = re.sub(r'^https?://', '', url).split("/")[0].lower()
            existing_domains.add(domain)
    for node in pending["nodes"]:
        url = node["url"].rstrip("/")
        domain = re.sub(r'^https?://', '', url).split("/")[0].lower()
        existing_domains.add(domain)

    print(f"已有节点域名: {len(existing_domains)} 个")

    new_domains = set()
    # 通道 1：来源清单
    for source in sources.get("sources", []):
        if not source.get("enabled", True):
            continue
        name = source.get("name", "?")
        method = source.get("extract_method", "regex_domains")
        print(f"\n同步来源: {name}（{method}）")
        try:
            # 直录域名：sources.json 条目可直接给 domains 列表（裸域名/少量已知节点）
            declared = source.get("domains")
            if declared:
                domains = {clean_domain(d) for d in declared if d}
            else:
                req = urllib.request.Request(source["file_url"], headers={"User-Agent": "MirrorHub-Sync/1.0"})
                text = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", errors="ignore")
                domains = (extract_domains_generic(text) if method == "regex_domains_generic"
                           else extract_domains_from_text(text))
            new_count = 0
            for d in domains:
                if d not in existing_domains and d not in new_domains:
                    new_domains.add(d)
                    new_count += 1
            print(f"  提取到 {len(domains)} 个域名，其中 {new_count} 个是新的")
        except Exception as e:
            print(f"  ❌ 同步失败: {e}")

    # 通道 2：Code Search 自动发现
    cs_domains = code_search_domains(sources)
    if cs_domains:
        cs_new = {d for d in cs_domains if d not in existing_domains and d not in new_domains}
        print(f"  Code Search 新增: {len(cs_new)} 个")
        new_domains |= cs_new

    # 新节点加入 pending
    added = 0
    for domain in sorted(new_domains):
        nid = generate_node_id(domain)
        if any(n["id"] == nid for n in pending["nodes"]):
            continue
        pending["nodes"].append({
            "id": nid,
            "name": domain.split(".")[0].capitalize(),
            "url": f"https://{domain}",
            "supports": ["release", "archive", "blob", "raw", "clone"],
            "category": "universal_proxy",
            "added_at": now,
            "source": "auto_sync",
        })
        added += 1

    pending["updated_at"] = now
    save_json(PENDING_FILE, pending)

    print(f"\n同步完成：发现 {len(new_domains)} 个新域名，加入 pending {added} 个")
    if new_domains:
        print("新域名列表：")
        for d in sorted(new_domains):
            print(f"  - {d}")


if __name__ == "__main__":
    main()
