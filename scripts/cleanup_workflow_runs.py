#!/usr/bin/env python3
"""清理旧的 GitHub Actions 工作流运行记录，只保留本次运行
用法: python3 cleanup_workflow_runs.py <repo> <token> <current_run_id>
"""
import sys
import os
import urllib.request
import json


def api_request(url, token, method="GET"):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github+json")
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status == 204:
                return {}
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 204:
            return {}
        print(f"  API 错误 {e.code}: {e.read().decode()[:100]}")
        return {}


def main():
    if len(sys.argv) < 4:
        print("用法: python3 cleanup_workflow_runs.py <repo> <token> <current_run_id>")
        sys.exit(1)

    repo = sys.argv[1]
    token = sys.argv[2]
    current_run_id = int(sys.argv[3])

    print(f"仓库: {repo}")
    print(f"本次运行 ID: {current_run_id}")

    # 获取所有运行记录
    url = f"https://api.github.com/repos/{repo}/actions/runs?per_page=100"
    data = api_request(url, token)
    runs = data.get("workflow_runs", [])
    print(f"总运行记录: {len(runs)} 条")

    deleted = 0
    for run in runs:
        rid = run["id"]
        if rid != current_run_id:
            del_url = f"https://api.github.com/repos/{repo}/actions/runs/{rid}"
            api_request(del_url, token, method="DELETE")
            print(f"  ✅ 删除: {rid} ({run['status']})")
            deleted += 1

    print(f"\n清理完成: 删除 {deleted} 条旧记录，保留本次运行")


if __name__ == "__main__":
    main()
