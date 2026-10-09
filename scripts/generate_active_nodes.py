#!/usr/bin/env python3
"""生成 active-nodes.json
只包含在线节点的完整信息（id, name, domain, category, latency_ms），按延迟升序排列。
供其他项目（如 EmuHub-CN）远程拉取，一次请求即可获得可用节点列表。
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
NODES_FILE = os.path.join(HERE, "..", "nodes.json")
STATUS_FILE = os.path.join(HERE, "..", "status.json")
OUTPUT_FILE = os.path.join(HERE, "..", "active-nodes.json")

MAX_NODES = 20  # 最多返回 20 个最快的在线节点


def load_json(path, default=None):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default if default is not None else {}


def main():
    config = load_json(NODES_FILE, {"categories": {}})
    status = load_json(STATUS_FILE, {"nodes": {}, "checked_at": "未知"})

    # 展平所有节点
    all_nodes = {}
    for cat_name, cat in config["categories"].items():
        for n in cat["nodes"]:
            all_nodes[n["id"]] = (cat_name, n)

    # 过滤在线节点，按延迟排序
    active = []
    for nid, e in status["nodes"].items():
        if e["status"] == "online" and nid in all_nodes:
            cat, n = all_nodes[nid]
            lat = e.get("avg_latency_ms") or e.get("latency_ms") or 99999
            # 从 url 提取 domain
            domain = n["url"].replace("https://", "").replace("http://", "").rstrip("/")
            active.append({
                "id": n["id"],
                "name": n["name"],
                "domain": domain,
                "category": cat,
                "latency_ms": lat,
                "bandwidth_mbps": e.get("bandwidth_mbps")
            })

    active.sort(key=lambda x: x["latency_ms"])
    active = active[:MAX_NODES]

    output = {
        "source": "MirrorHub",
        "source_url": "https://github.com/mihsian77/MirrorHub",
        "license": "MIT",
        "attribution_required": True,
        "attribution_text": "节点由 MirrorHub 提供",
        "attribution_url": "https://github.com/mihsian77/MirrorHub",
        "usage_policy": "欢迎接入使用，但请在产品 UI 中保留来源声明。二次分发需遵守 MIT 协议并保留版权声明。",
        "updated_at": status.get("checked_at", "未知"),
        "total_online": len(active),
        "nodes": active
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✅ active-nodes.json 已生成")
    print(f"  在线节点: {len(active)} 个")
    print(f"  更新时间: {output['updated_at']}")
    if active:
        print(f"  Top 3: {active[0]['domain']}({active[0]['latency_ms']}ms), "
              f"{active[1]['domain']}({active[1]['latency_ms']}ms), "
              f"{active[2]['domain']}({active[2]['latency_ms']}ms)")


if __name__ == "__main__":
    main()
