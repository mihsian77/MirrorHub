#!/usr/bin/env python3
"""MirrorHub 状态更新脚本
读取测速结果，更新 status.json，处理节点生命周期，自动排序，清理失效节点
输出 changes.json 用于飞书推送
"""
import json
import os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
NODES_FILE = os.path.join(HERE, "..", "nodes.json")
STATUS_FILE = os.path.join(HERE, "..", "status.json")
PENDING_FILE = os.path.join(HERE, "..", "pending.json")
GRAVEYARD_FILE = os.path.join(HERE, "..", "graveyard.json")
TEST_RESULTS_FILE = os.path.join(HERE, "..", "test-results.json")
CHANGES_FILE = os.path.join(HERE, "..", "changes.json")

# 连续失败 N 次标记为 unstable
UNSTABLE_THRESHOLD = 3
# 连续失败 N 天标记为 dead（每6小时测一次，7天=28次）
DEAD_THRESHOLD = 28


def load_json(path, default=None):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default if default is not None else {}


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    now = datetime.now(timezone.utc)
    now_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    nodes_config = load_json(NODES_FILE, {"categories": {}})
    status = load_json(STATUS_FILE, {"nodes": {}, "summary": {}})
    pending = load_json(PENDING_FILE, {"nodes": []})
    graveyard = load_json(GRAVEYARD_FILE, {"nodes": []})
    test_results = load_json(TEST_RESULTS_FILE, {"results": []})

    changes = []  # 状态变化记录，用于飞书推送
    result_map = {r["id"]: r for r in test_results.get("results", [])}

    # 1. 更新正式节点状态
    dead_nodes = []
    for cat_name, cat_data in nodes_config["categories"].items():
        for node in cat_data["nodes"]:
            nid = node["id"]
            result = result_map.get(nid)
            prev = status["nodes"].get(nid, {})

            # 初始化状态记录
            if nid not in status["nodes"]:
                status["nodes"][nid] = {
                    "status": "unverified",
                    "latency_ms": None,
                    "avg_latency_ms": None,
                    "consecutive_failures": 0,
                    "last_check": None,
                    "first_failed_at": None,
                    "history": []
                }

            entry = status["nodes"][nid]
            entry["last_check"] = now_str

            if result and result["status"] == "online":
                # 成功
                old_status = entry["status"]
                entry["status"] = "online"
                entry["latency_ms"] = result["latency_ms"]
                entry["bandwidth_mbps"] = result.get("bandwidth_mbps")
                entry["consecutive_failures"] = 0
                entry["first_failed_at"] = None
                # 计算平均延迟（最近10次）
                history = entry.get("history", [])
                history.append(result["latency_ms"])
                entry["history"] = history[-10:]
                entry["avg_latency_ms"] = round(sum(history) / len(history))
                if old_status in ("unstable", "offline", "unverified"):
                    changes.append({"id": nid, "type": "recovered", "from": old_status, "to": "online", "latency": result["latency_ms"]})
            else:
                # 失败
                entry["consecutive_failures"] = entry.get("consecutive_failures", 0) + 1
                if not entry.get("first_failed_at"):
                    entry["first_failed_at"] = now_str
                old_status = entry["status"]

                if entry["consecutive_failures"] >= DEAD_THRESHOLD:
                    entry["status"] = "dead"
                    dead_nodes.append((nid, node, cat_name))
                    changes.append({"id": nid, "type": "dead", "from": old_status, "to": "dead", "failures": entry["consecutive_failures"]})
                elif entry["consecutive_failures"] >= UNSTABLE_THRESHOLD:
                    entry["status"] = "unstable"
                    if old_status == "online":
                        changes.append({"id": nid, "type": "unstable", "from": "online", "to": "unstable", "failures": entry["consecutive_failures"]})
                else:
                    entry["status"] = "unstable" if entry["consecutive_failures"] > 0 else "unverified"

    # 2. 处理彻底失效的节点：移入 graveyard，从 nodes.json 移除
    if dead_nodes:
        for nid, node, cat_name in dead_nodes:
            # 加入 graveyard
            graveyard["nodes"].append({
                **node,
                "category": cat_name,
                "removed_at": now_str,
                "reason": f"连续 {DEAD_THRESHOLD} 次测速失败",
                "first_failed_at": status["nodes"][nid].get("first_failed_at")
            })
            # 从 nodes.json 移除
            cat_data = nodes_config["categories"][cat_name]
            cat_data["nodes"] = [n for n in cat_data["nodes"] if n["id"] != nid]
            # 从 status 移除
            del status["nodes"][nid]
        graveyard["updated_at"] = now_str
        nodes_config["total_nodes"] = sum(len(c["nodes"]) for c in nodes_config["categories"].values())

    # 3. 处理 pending 节点：测速成功自动加入 nodes.json
    new_pending = []
    for node in pending["nodes"]:
        nid = node["id"]
        result = result_map.get(nid)
        if result and result["status"] == "online":
            # 加入正式列表
            cat = node.get("category", "universal_proxy")
            if cat not in nodes_config["categories"]:
                nodes_config["categories"][cat] = {"description": "", "nodes": []}
            node.pop("category", None)
            node.pop("added_at", None)
            nodes_config["categories"][cat]["nodes"].append(node)
            status["nodes"][nid] = {
                "status": "online",
                "latency_ms": result["latency_ms"],
                "avg_latency_ms": result["latency_ms"],
                "bandwidth_mbps": result.get("bandwidth_mbps"),
                "consecutive_failures": 0,
                "last_check": now_str,
                "first_failed_at": None,
                "history": [result["latency_ms"]]
            }
            changes.append({"id": nid, "type": "new_node", "category": cat, "latency": result["latency_ms"]})
        else:
            new_pending.append(node)
    pending["nodes"] = new_pending
    pending["updated_at"] = now_str
    nodes_config["total_nodes"] = sum(len(c["nodes"]) for c in nodes_config["categories"].values())

    # 4. 按延迟排序 status（生成排序后的列表）
    sorted_online = sorted(
        [(nid, e) for nid, e in status["nodes"].items() if e["status"] == "online" and e.get("avg_latency_ms")],
        key=lambda x: x[1]["avg_latency_ms"]
    )
    status["sorted_by_latency"] = [nid for nid, _ in sorted_online]

    # 5. 更新 summary
    all_statuses = [e["status"] for e in status["nodes"].values()]
    status["summary"] = {
        "total": len(status["nodes"]),
        "online": all_statuses.count("online"),
        "unstable": all_statuses.count("unstable"),
        "offline": all_statuses.count("offline"),
        "dead": all_statuses.count("dead"),
        "unverified": all_statuses.count("unverified")
    }
    status["checked_at"] = now_str
    nodes_config["updated_at"] = now_str

    # 6. 保存所有文件
    save_json(NODES_FILE, nodes_config)
    save_json(STATUS_FILE, status)
    save_json(PENDING_FILE, pending)
    save_json(GRAVEYARD_FILE, graveyard)
    save_json(CHANGES_FILE, {"generated_at": now_str, "changes": changes})

    # 7. 输出报告
    print(f"状态更新完成：{now_str}")
    print(f"  总计: {status['summary']['total']}")
    print(f"  ✅ 在线: {status['summary']['online']}")
    print(f"  ⚠️ 不稳定: {status['summary']['unstable']}")
    print(f"  ❌ 未验证: {status['summary']['unverified']}")
    print(f"  ⚰️ 已失效(移入graveyard): {len(graveyard['nodes'])}")
    if changes:
        print(f"\n状态变化 ({len(changes)} 项):")
        for c in changes:
            print(f"  - [{c['type']}] {c['id']}: {c.get('from','?')} → {c.get('to','?')}")
    else:
        print("\n无状态变化")


if __name__ == "__main__":
    main()
