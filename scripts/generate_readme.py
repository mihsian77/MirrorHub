#!/usr/bin/env python3
"""动态生成 README.md
从 nodes.json / status.json / graveyard.json 读取最新数据，生成包含实时节点排行的 README
"""
import json
import os
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
NODES_FILE = os.path.join(HERE, "..", "nodes.json")
STATUS_FILE = os.path.join(HERE, "..", "status.json")
GRAVEYARD_FILE = os.path.join(HERE, "..", "graveyard.json")
README_FILE = os.path.join(HERE, "..", "README.md")


def load_json(path, default=None):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default if default is not None else {}


def main():
    config = load_json(NODES_FILE, {"categories": {}, "total_nodes": 0})
    status = load_json(STATUS_FILE, {"nodes": {}, "summary": {}, "checked_at": "未知"})
    graveyard = load_json(GRAVEYARD_FILE, {"nodes": []})

    # 展平所有节点
    all_nodes = {}
    for cat_name, cat in config["categories"].items():
        for n in cat["nodes"]:
            all_nodes[n["id"]] = (cat_name, n)

    # 在线节点按延迟排序
    online = []
    for nid, e in status["nodes"].items():
        if e["status"] == "online" and nid in all_nodes:
            cat, n = all_nodes[nid]
            lat = e.get("avg_latency_ms") or e.get("latency_ms") or 99999
            online.append((lat, n["name"], n["url"], cat, e.get("bandwidth_mbps")))
    online.sort()

    # 不稳定节点
    unstable = []
    for nid, e in status["nodes"].items():
        if e["status"] == "unstable" and nid in all_nodes:
            cat, n = all_nodes[nid]
            unstable.append((nid, n["name"], e.get("consecutive_failures", 0)))

    # 分类统计
    cat_counts = {cat: len(data["nodes"]) for cat, data in config["categories"].items()}
    cat_labels = {
        "universal_proxy": "通用代理",
        "web_mirror": "网页镜像",
        "clone_specialized": "Clone 专用",
        "cdn_raw": "CDN Raw"
    }

    summary = status.get("summary", {})
    checked_at = status.get("checked_at", "未知")

    # 生成在线节点表格
    online_table = ""
    for i, (lat, name, url, cat, bw) in enumerate(online, 1):
        label = cat_labels.get(cat, cat)
        bw_txt = f"{bw} MB/s" if bw else "-"
        online_table += f"| {i} | {lat}ms | {name} | {bw_txt} | `{url}` | {label} |\n"

    # 生成不稳定节点表格（如果有的话）
    unstable_section = ""
    if unstable:
        unstable_section = f"""
### ⚠️ 不稳定节点（{len(unstable)} 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
"""
        for nid, name, fails in unstable:
            unstable_section += f"| {name} (`{nid}`) | {fails} 次 |\n"

    # 分类统计表格
    cat_table = ""
    for cat, count in cat_counts.items():
        label = cat_labels.get(cat, cat)
        desc = {
            "universal_proxy": "通用，支持 release/archive/blob/raw/clone",
            "web_mirror": "GitHub 网页完整镜像，可直接浏览",
            "clone_specialized": "仅 git clone 加速",
            "cdn_raw": "CDN 加速，仅 raw/blob 小文件"
        }.get(cat, "")
        cat_table += f"| `{cat}` | {count} | {desc} |\n"

    readme = f"""# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **{checked_at}**，每 6 小时刷新一次。当前 ✅ **{summary.get('online', 0)}** 在线 / ⚠️ **{summary.get('unstable', 0)}** 不稳定 / ⚰️ **{len(graveyard['nodes'])}** 已失效归档。

## 核心特性

- **{config['total_nodes']} 个节点**，{len(cat_counts)} 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
{online_table}
{unstable_section}
## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
{cat_table}| **合计** | **{config['total_nodes']}** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（{len(graveyard['nodes'])} 个）。

## 快速接入

### 1. 拉取配置

```
节点列表:  https://raw.githubusercontent.com/mihsian77/MirrorHub/main/nodes.json
健康状态:  https://raw.githubusercontent.com/mihsian77/MirrorHub/main/status.json
```

### 2. 选节点

```
1. 从 status.json 过滤 status == "online" 的节点
2. 按 avg_latency_ms 升序排序
3. 取前 3 个作为候选，下载时依次尝试，失败自动切换
```

### 3. 拼接 URL

```
# 通用代理（release/archive/blob/raw）
https://gh-proxy.com/https://github.com/owner/repo/releases/download/v1.0/file.zip

# CDN Raw（仅小文件，不支持 release）
https://cdn.jsdelivr.net/gh/owner/repo@main/file.json

# Git Clone
git clone https://gitclone.com/github.com/owner/repo.git
```

详细接入规范见 [docs/integration.md](docs/integration.md)。

## 接入示例

| 语言 | 文件 | 说明 |
|------|------|------|
| Kotlin | [examples/kotlin/MirrorHub.kt](examples/kotlin/MirrorHub.kt) | Android 项目直接复制使用 |
| Python | [examples/python/mirrorhub.py](examples/python/mirrorhub.py) | 单文件，import 即用 |
| Shell | [examples/shell/mirrorhub.sh](examples/shell/mirrorhub.sh) | source 后调用函数 |

## 自动维护机制

```
每 6 小时（GitHub Actions）:
  1. 同步节点 ← 从来源仓库拉取 + Code Search 发现新域名
  2. 测速所有节点（含待验证的）← 并发15，同时测 raw+release，超时10s
  3. 更新状态:
     - 新节点测速成功 → 自动加入 nodes.json
     - 连续失败 → 标记 unstable，接入项目自动过滤
     - 连续 7 天失败 → 移入 graveyard（彻底失效）
     - 不稳定节点测速成功 → 恢复 online
  4. 自动重新生成本 README（节点排行实时更新）
  5. 按平均延迟排序
  6. 状态变化 → 飞书推送
  7. 提交所有更新回仓库
```

节点状态流转和字段说明见 [docs/node-format.md](docs/node-format.md)。

## 提交新节点

发现了新的 GitHub 加速节点？欢迎提交！

1. 提 Issue：标题 `[新节点] https://xxx.com`，描述节点支持的功能
2. 或直接提 PR：在 `nodes.json` 对应分类中添加节点，字段格式见 [docs/node-format.md](docs/node-format.md)

新节点会先进入 `pending.json`，经过一次自动测速成功后自动加入正式列表。

## 数据来源

- 初始节点导入自 [AClon314/mirror-cn](https://github.com/AClon314/mirror-cn)（MIT），已清理失效节点
- 持续自动同步来源仓库，见 [sources.json](sources.json)
- 公益节点由社区维护，可能随时失效，请务必实现失败自动切换

## 许可证

MIT
"""

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"✅ README 已动态生成")
    print(f"  更新时间: {checked_at}")
    print(f"  在线节点: {len(online)}")
    print(f"  不稳定节点: {len(unstable)}")
    print(f"  已失效归档: {len(graveyard['nodes'])}")


if __name__ == "__main__":
    main()
