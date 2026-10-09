#!/usr/bin/env python3
"""MirrorHub 飞书推送脚本
读取 changes.json，将状态变化推送到飞书群
"""
import json
import os
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CHANGES_FILE = os.path.join(HERE, "..", "changes.json")
STATUS_FILE = os.path.join(HERE, "..", "status.json")

WEBHOOK = os.environ.get("FEISHU_WEBHOOK", "")


def send_feishu(title: str, lines: list) -> bool:
    if not WEBHOOK:
        print("[skip] 未配置 FEISHU_WEBHOOK，跳过推送")
        return False
    payload = {
        "msg_type": "text",
        "content": {
            "text": title + "\n" + "\n".join(lines)
        }
    }
    try:
        req = urllib.request.Request(
            WEBHOOK,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        urllib.request.urlopen(req, timeout=10)
        print(f"✅ 飞书推送成功: {title}")
        return True
    except Exception as e:
        print(f"⚠️ 飞书推送失败: {e}")
        return False


def main():
    if not os.path.exists(CHANGES_FILE):
        print("无 changes.json，跳过")
        return

    with open(CHANGES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    changes = data.get("changes", [])
    if not changes:
        print("无状态变化，跳过推送")
        return

    # 读取状态摘要
    status = {}
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r", encoding="utf-8") as f:
            status = json.load(f)
    summary = status.get("summary", {})

    # 分类变化
    new_nodes = [c for c in changes if c["type"] == "new_node"]
    recovered = [c for c in changes if c["type"] == "recovered"]
    unstable = [c for c in changes if c["type"] == "unstable"]
    dead = [c for c in changes if c["type"] == "dead"]

    lines = []
    lines.append(f"检查时间: {data.get('generated_at', '?')}")
    lines.append("")

    if new_nodes:
        lines.append(f"🆕 新节点加入 ({len(new_nodes)}):")
        for c in new_nodes:
            lines.append(f"  - {c['id']} ({c.get('category', '?')}) - {c.get('latency', '?')}ms")
        lines.append("")

    if recovered:
        lines.append(f"✅ 节点恢复 ({len(recovered)}):")
        for c in recovered:
            lines.append(f"  - {c['id']}: {c['from']} → online ({c.get('latency', '?')}ms)")
        lines.append("")

    if unstable:
        lines.append(f"⚠️ 节点不稳定 ({len(unstable)}):")
        for c in unstable:
            lines.append(f"  - {c['id']}: 连续失败 {c.get('failures', '?')} 次")
        lines.append("")

    if dead:
        lines.append(f"⚰️ 节点彻底失效 ({len(dead)}):")
        for c in dead:
            lines.append(f"  - {c['id']}: 连续失败 {c.get('failures', '?')} 次，已移入 graveyard")
        lines.append("")

    if summary:
        lines.append(f"📊 当前状态: ✅{summary.get('online',0)} ⚠️{summary.get('unstable',0)} ❓{summary.get('unverified',0)} ⚰️{summary.get('dead',0)}")

    title = f"[MirrorHub] 健康检查 - {len(changes)} 项变化"
    send_feishu(title, lines)


if __name__ == "__main__":
    main()
