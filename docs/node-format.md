# 节点格式说明

## nodes.json 结构

```json
{
  "version": "1.0",
  "updated_at": "2026-10-06T00:00:00Z",
  "total_nodes": 69,
  "categories": {
    "universal_proxy": {
      "description": "通用前缀式代理",
      "default_url_template": "{node_url}/{github_url}",
      "nodes": [...]
    }
  }
}
```

## 节点字段

| 字段 | 必填 | 说明 |
|------|------|------|
| `id` | ✅ | 唯一标识，域名替换 `.` 为 `-` |
| `name` | ✅ | 显示名称 |
| `url` | ✅ | 节点域名或完整 URL |
| `supports` | ✅ | 支持的流量类型：`release`/`archive`/`blob`/`raw`/`clone`/`web` |
| `url_template` | ❌ | 自定义 URL 模板，覆盖分类默认模板 |
| `location` | ❌ | 服务器位置 |
| `provider` | ❌ | 运营方 |
| `notes` | ❌ | 备注 |

## url_template 变量

| 变量 | 说明 |
|------|------|
| `{node_url}` | 节点 URL |
| `{github_url}` | 完整的 GitHub URL |
| `{owner}` | 仓库所有者 |
| `{repo}` | 仓库名 |
| `{ref}` | 分支/tag/commit |
| `{path}` | 文件路径 |

## status.json 节点状态字段

| 字段 | 说明 |
|------|------|
| `status` | `online`/`unstable`/`offline`/`dead`/`unverified` |
| `latency_ms` | 最近一次测速延迟（毫秒） |
| `avg_latency_ms` | 最近10次平均延迟 |
| `consecutive_failures` | 连续失败次数 |
| `last_check` | 最后检查时间 |
| `first_failed_at` | 首次失败时间 |
| `history` | 最近10次延迟记录 |

## 状态流转

```
unverified ──测速成功──→ online
online ──连续3次失败──→ unstable
unstable ──测速成功──→ online
unstable ──连续28次失败(7天)──→ dead（移入 graveyard.json）
```

## pending.json 待验证节点

新发现的节点先进入 pending.json，经过一次测速成功后自动加入 nodes.json。

额外字段：
- `category`：预期分类
- `added_at`：加入时间
- `source`：来源（`auto_sync`/`manual`/`code_search`）

## graveyard.json 已失效节点

彻底失效的节点移入 graveyard.json，保留历史记录。如果节点恢复，可以手动移回 pending.json 重新验证。

额外字段：
- `category`：原分类
- `removed_at`：移除时间
- `reason`：移除原因
- `first_failed_at`：首次失败时间
