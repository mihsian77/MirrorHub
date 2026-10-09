# MirrorHub 接入规范

其他项目接入 MirrorHub 只需 3 步：拉取配置 → 过滤在线节点 → 选最快的拼接 URL。

## ⚠️ 使用条款（必读）

MirrorHub 节点数据采用 **MIT 协议**开源，欢迎自由接入使用，但需遵守以下条款：

1. **来源声明**：使用 MirrorHub 节点数据的产品，必须在设置/关于等用户可见的 UI 中显示来源声明，例如"节点由 MirrorHub 提供"并附仓库链接。
2. **禁止冒充**：不得将 MirrorHub 节点库冒充为自有节点库，不得移除数据中的 `source` / `attribution_required` 字段。
3. **二次分发**：基于 MirrorHub 数据二次分发或修改时，需保留 MIT 协议和版权声明。
4. **合规接入列表**：欢迎提交 PR 将你的项目加入合规接入列表（见 README）。

`active-nodes.json` 中已嵌入 `attribution_required: true` 字段，请接入方读取该字段并在 UI 中显示 `attribution_text`。

---

## 1. 配置文件地址

### 推荐：active-nodes.json（一键接入）

只包含在线节点的完整信息，已按延迟排序，最多 20 个，每 6 小时自动更新。**大多数项目只需拉取这一个文件。**

```
https://raw.githubusercontent.com/mihsian77/MirrorHub/main/active-nodes.json
```

返回格式：
```json
{
  "source": "MirrorHub",
  "source_url": "https://github.com/mihsian77/MirrorHub",
  "license": "MIT",
  "attribution_required": true,
  "attribution_text": "节点由 MirrorHub 提供",
  "attribution_url": "https://github.com/mihsian77/MirrorHub",
  "usage_policy": "...",
  "updated_at": "2026-10-07T03:07:24Z",
  "total_online": 20,
  "nodes": [
    {"id": "gh-llkk-cc", "name": "Gh", "domain": "gh.llkk.cc", "category": "universal_proxy", "latency_ms": 250}
  ]
}
```

### 完整数据（高级用法）

```
# 全部节点列表（含离线/不稳定，手动+自动维护）
https://raw.githubusercontent.com/mihsian77/MirrorHub/main/nodes.json

# 健康状态（每6小时自动更新，含延迟历史）
https://raw.githubusercontent.com/mihsian77/MirrorHub/main/status.json

# 待验证节点（新发现的，未测速）
https://raw.githubusercontent.com/mihsian77/MirrorHub/main/pending.json

# 已失效节点历史档案
https://raw.githubusercontent.com/mihsian77/MirrorHub/main/graveyard.json
```

建议缓存 active-nodes.json 6小时，status.json 1小时，避免频繁请求。

## 2. 节点分类

| 分类 | 用途 | URL 模板 |
|------|------|---------|
| `universal_proxy` | 通用，支持 release/archive/blob/raw/clone | `https://{domain}/{github_url}` |
| `web_mirror` | GitHub 网页镜像，可浏览 | `https://{domain}/{path}` |
| `clone_specialized` | 仅 git clone | `https://{domain}/github.com/{owner}/{repo}.git` |
| `cdn_raw` | 仅 raw/blob 小文件，不支持 release | `https://{domain}/gh/{owner}/{repo}@{ref}/{path}` |

## 3. 选节点逻辑（使用 active-nodes.json）

```
1. 拉取 active-nodes.json
2. 检查 attribution_required，在 UI 中显示 attribution_text
3. nodes 数组已按 latency_ms 升序排列，直接取前 3-5 个作为候选
4. 下载时依次尝试，失败自动切换下一个
5. 全部失败时回退到直连 GitHub
```

## 4. 拼接下载 URL 示例

**Release 附件下载（通用代理）：**
```
原始: https://github.com/owner/repo/releases/download/v1.0/file.zip
加速: https://gh-proxy.com/https://github.com/owner/repo/releases/download/v1.0/file.zip
```

**Raw 文件下载（CDN Raw）：**
```
原始: https://raw.githubusercontent.com/owner/repo/main/file.json
加速: https://cdn.jsdelivr.net/gh/owner/repo@main/file.json
```

**Git Clone（Clone 专用）：**
```
原始: git clone https://github.com/owner/repo.git
加速: git clone https://gitclone.com/github.com/owner/repo.git
```

## 5. 来源声明实现示例

接入方应在设置页面或关于页面显示来源声明。以下是各语言的最小实现：

**Kotlin（Android）：**
```kotlin
// 拉取节点配置时读取来源声明
val config = JSONObject(response.body!!.string())
if (config.optBoolean("attribution_required")) {
    val text = config.optString("attribution_text", "节点由 MirrorHub 提供")
    val url = config.optString("attribution_url", "https://github.com/mihsian77/MirrorHub")
    // 在设置页显示：text + 点击跳转 url
}
```

**Python：**
```python
config = requests.get(ACTIVE_NODES_URL).json()
if config.get("attribution_required"):
    print(f"{config['attribution_text']}: {config['attribution_url']}")
```

## 6. 注意事项

- 公益节点可能随时失效，务必实现失败自动切换
- CDN Raw 节点不支持大文件（>50MB）和 release 附件
- 网页镜像节点可能不支持 API 调用
- 建议本地缓存节点列表，不要每次下载都重新拉取
- 新节点先在 pending.json 中，测速成功后自动进入 nodes.json
- **请务必在 UI 中保留 MirrorHub 来源声明**
