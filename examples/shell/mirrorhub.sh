#!/bin/bash
# MirrorHub Shell 接入示例
# 用法：source mirrorhub.sh，然后调用 get_fastest_url "github_url"

MIRRORHUB_NODES_URL="https://raw.githubusercontent.com/mihsian77/MirrorHub/main/nodes.json"
MIRRORHUB_STATUS_URL="https://raw.githubusercontent.com/mihsian77/MirrorHub/main/status.json"
MIRRORHUB_CACHE_DIR="/tmp/mirrorhub"
MIRRORHUB_CACHE_TTL=3600

# 确保缓存目录
mkdir -p "$MIRRORHUB_CACHE_DIR"

# 拉取配置（带缓存）
_mirrorhub_fetch() {
    local url="$1"
    local cache_file="$2"
    local now=$(date +%s)
    local mtime=0
    if [ -f "$cache_file" ]; then
        mtime=$(stat -c %Y "$cache_file" 2>/dev/null || echo 0)
    fi
    if [ $((now - mtime)) -lt "$MIRRORHUB_CACHE_TTL" ]; then
        cat "$cache_file"
    else
        curl -s --max-time 10 "$url" | tee "$cache_file"
    fi
}

# 获取最快的可用下载 URL
# 用法: get_fastest_url "https://github.com/owner/repo/releases/download/v1.0/file.zip"
get_fastest_url() {
    local github_url="$1"
    local nodes_file="$MIRRORHUB_CACHE_DIR/nodes.json"
    local status_file="$MIRRORHUB_CACHE_DIR/status.json"

    _mirrorhub_fetch "$MIRRORHUB_NODES_URL" "$nodes_file" > /dev/null
    _mirrorhub_fetch "$MIRRORHUB_STATUS_URL" "$status_file" > /dev/null

    # 用 python3 解析（大多数系统都有）
    if command -v python3 > /dev/null 2>&1; then
        python3 -c "
import json
with open('$nodes_file') as f: nodes = json.load(f)
with open('$status_file') as f: status = json.load(f)
all_nodes = {}
for cat in nodes.get('categories', {}).values():
    for n in cat.get('nodes', []):
        all_nodes[n['id']] = n
online = []
for nid, n in all_nodes.items():
    s = status.get('nodes', {}).get(nid, {})
    if s.get('status') == 'online' and 'release' in n.get('supports', []):
        lat = s.get('avg_latency_ms') or s.get('latency_ms') or 99999
        online.append((lat, n))
online.sort(key=lambda x: x[0])
for _, n in online[:3]:
    tpl = n.get('url_template') or '{node_url}/{github_url}'
    print(tpl.replace('{node_url}', n['url']).replace('{github_url}', '$github_url'))
    break
"
    else
        # 无 python3 时的降级：直接用第一个已知节点
        echo "https://gh-proxy.com/$github_url"
    fi
}

# 列出所有在线节点
list_online_nodes() {
    local nodes_file="$MIRRORHUB_CACHE_DIR/nodes.json"
    local status_file="$MIRRORHUB_CACHE_DIR/status.json"
    _mirrorhub_fetch "$MIRRORHUB_NODES_URL" "$nodes_file" > /dev/null
    _mirrorhub_fetch "$MIRRORHUB_STATUS_URL" "$status_file" > /dev/null
    python3 -c "
import json
with open('$nodes_file') as f: nodes = json.load(f)
with open('$status_file') as f: status = json.load(f)
all_nodes = {}
for cat in nodes.get('categories', {}).values():
    for n in cat.get('nodes', []):
        all_nodes[n['id']] = n
online = []
for nid, n in all_nodes.items():
    s = status.get('nodes', {}).get(nid, {})
    if s.get('status') == 'online':
        lat = s.get('avg_latency_ms') or s.get('latency_ms') or 99999
        online.append((lat, n['name'], n['url']))
online.sort(key=lambda x: x[0])
for lat, name, url in online[:20]:
    print(f'{lat:>6}ms  {name:<25} {url}')
"
}

# 使用示例：
# source mirrorhub.sh
# url=$(get_fastest_url "https://github.com/owner/repo/releases/download/v1.0/file.zip")
# curl -L -o file.zip "$url"
# list_online_nodes
