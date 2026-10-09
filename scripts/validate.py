#!/usr/bin/env python3
"""MirrorHub 配置校验脚本
检查 nodes.json / sources.json / pending.json 的格式正确性
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NODES_FILE = os.path.join(HERE, "..", "nodes.json")
SOURCES_FILE = os.path.join(HERE, "..", "sources.json")
PENDING_FILE = os.path.join(HERE, "..", "pending.json")

REQUIRED_NODE_FIELDS = ["id", "name", "url", "supports"]
VALID_CATEGORIES = ["universal_proxy", "web_mirror", "clone_specialized", "cdn_raw"]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    errors = []
    warnings = []

    # 1. 校验 nodes.json
    print("校验 nodes.json...")
    try:
        config = load_json(NODES_FILE)
    except Exception as e:
        errors.append(f"nodes.json 解析失败: {e}")
        config = None

    if config:
        all_ids = set()
        if "categories" not in config:
            errors.append("nodes.json 缺少 categories 字段")
        else:
            for cat_name, cat_data in config["categories"].items():
                if cat_name not in VALID_CATEGORIES:
                    warnings.append(f"未知分类: {cat_name}")
                if "nodes" not in cat_data:
                    errors.append(f"分类 {cat_name} 缺少 nodes 字段")
                    continue
                for node in cat_data["nodes"]:
                    # 检查必填字段
                    for field in REQUIRED_NODE_FIELDS:
                        if field not in node:
                            errors.append(f"节点 {node.get('id', '?')} 缺少字段: {field}")
                    # 检查 ID 重复
                    nid = node.get("id")
                    if nid:
                        if nid in all_ids:
                            errors.append(f"重复的节点 ID: {nid}")
                        all_ids.add(nid)
                    # 检查 URL 格式
                    url = node.get("url", "")
                    if url and not url.startswith(("http://", "https://")) and "." not in url:
                        warnings.append(f"节点 {nid} 的 URL 格式可疑: {url}")
                    # 检查 supports
                    supports = node.get("supports", [])
                    if not supports:
                        warnings.append(f"节点 {nid} 的 supports 为空")

        total = sum(len(c.get("nodes", [])) for c in config["categories"].values())
        expected_total = config.get("total_nodes", 0)
        if total != expected_total:
            errors.append(f"total_nodes 字段({expected_total})与实际节点数({total})不一致")
        print(f"  节点总数: {total}，ID 无重复: {len(all_ids) == total}")

    # 2. 校验 sources.json
    print("校验 sources.json...")
    try:
        sources = load_json(SOURCES_FILE)
        if "sources" not in sources:
            errors.append("sources.json 缺少 sources 字段")
        else:
            for s in sources["sources"]:
                if "id" not in s or "file_url" not in s:
                    errors.append(f"来源 {s.get('id', '?')} 缺少 id 或 file_url")
        print(f"  来源数: {len(sources.get('sources', []))}")
    except Exception as e:
        errors.append(f"sources.json 解析失败: {e}")

    # 3. 校验 pending.json
    print("校验 pending.json...")
    try:
        pending = load_json(PENDING_FILE)
        pending_ids = set()
        for node in pending.get("nodes", []):
            nid = node.get("id")
            if nid in pending_ids:
                errors.append(f"pending 中重复的节点 ID: {nid}")
            pending_ids.add(nid)
        print(f"  待验证节点数: {len(pending.get('nodes', []))}")
    except Exception as e:
        errors.append(f"pending.json 解析失败: {e}")

    # 输出结果
    print(f"\n{'='*40}")
    if errors:
        print(f"❌ 发现 {len(errors)} 个错误:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("✅ 无错误")

    if warnings:
        print(f"⚠️  {len(warnings)} 个警告:")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
