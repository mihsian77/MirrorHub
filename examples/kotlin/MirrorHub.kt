// MirrorHub Kotlin 接入示例（active-nodes.json 一键接入版）
// 用法：复制 MirrorHub.kt 到项目中
//   1. 调用 MirrorHub.refresh() 拉取最新节点
//   2. 调用 MirrorHub.getAttribution() 获取来源声明，在设置页 UI 中显示
//   3. 调用 MirrorHub.getFastestDownloadUrl() 获取加速后的下载 URL
//
// ⚠️ 使用条款：必须在 UI 中显示 MirrorHub 来源声明（见 getAttribution()）
package com.example.mirrorhub

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
import java.net.URL

@Serializable
data class ActiveNode(
    val id: String,
    val name: String,
    val domain: String,
    val category: String,
    val latency_ms: Long
)

@Serializable
data class ActiveNodesResponse(
    val source: String = "",
    val source_url: String = "",
    val license: String = "",
    val attribution_required: Boolean = false,
    val attribution_text: String = "节点由 MirrorHub 提供",
    val attribution_url: String = "https://github.com/mihsian77/MirrorHub",
    val updated_at: String = "",
    val total_online: Int = 0,
    val nodes: List<ActiveNode> = emptyList()
)

/** 来源声明数据类，用于在 UI 中显示 */
data class Attribution(
    val required: Boolean,
    val text: String,
    val url: String
)

object MirrorHub {
    private const val ACTIVE_NODES_URL =
        "https://raw.githubusercontent.com/mihsian77/MirrorHub/main/active-nodes.json"

    private var cache: ActiveNodesResponse? = null
    private var lastFetch = 0L
    private const val CACHE_TTL = 6 * 3600_000L // 6小时

    private val json = Json { ignoreUnknownKeys = true }

    /**
     * 拉取最新在线节点列表（已按延迟排序）。
     * 建议在 App 启动或进入设置页时调用。
     */
    suspend fun refresh(): Boolean = withContext(Dispatchers.IO) {
        if (System.currentTimeMillis() - lastFetch < CACHE_TTL && cache != null) {
            return@withContext true
        }
        try {
            val text = URL(ACTIVE_NODES_URL).readText()
            cache = json.decodeFromString(ActiveNodesResponse.serializer(), text)
            lastFetch = System.currentTimeMillis()
            true
        } catch (e: Exception) {
            false // 拉取失败，使用旧缓存或空列表
        }
    }

    /**
     * 获取来源声明。接入方必须在设置/关于等用户可见 UI 中显示此声明。
     * 示例：
     *   val attr = MirrorHub.getAttribution()
     *   if (attr.required) {
     *       Text(attr.text)  // "节点由 MirrorHub 提供"
     *       // 点击跳转 attr.url
     *   }
     */
    fun getAttribution(): Attribution {
        val data = cache ?: ActiveNodesResponse()
        return Attribution(
            required = data.attribution_required,
            text = data.attribution_text,
            url = data.attribution_url
        )
    }

    /**
     * 获取最快的可用下载 URL。
     * active-nodes.json 已按延迟排序，直接取第一个可用的。
     * @param githubUrl 原始 GitHub 下载 URL
     * @param category 节点分类过滤，默认 universal_proxy（通用）
     * @return 加速后的 URL，无可用节点时返回 null（调用方应回退直连）
     */
    fun getFastestDownloadUrl(githubUrl: String, category: String = "universal_proxy"): String? {
        val nodes = cache?.nodes ?: return null
        // 按分类过滤（cdn_raw 只用于小文件，universal_proxy 通用）
        val filtered = if (category == "all") nodes else nodes.filter { it.category == category }
        // 已按 latency_ms 排序，取第一个
        val node = filtered.firstOrNull() ?: return null
        return when (node.category) {
            "cdn_raw" -> rewriteCdnRaw(githubUrl, node.domain)
            else -> "https://${node.domain}/$githubUrl" // universal_proxy / web_mirror
        }
    }

    /** 获取所有可用节点（用于手动选择界面） */
    fun getAllNodes(): List<ActiveNode> = cache?.nodes ?: emptyList()

    /** CDN Raw 专用 URL 重写 */
    private fun rewriteCdnRaw(githubUrl: String, domain: String): String {
        val rawPrefix = "https://raw.githubusercontent.com/"
        if (!githubUrl.startsWith(rawPrefix)) return githubUrl
        val path = githubUrl.removePrefix(rawPrefix)
        val segments = path.split("/")
        if (segments.size < 4) return githubUrl
        val (owner, repo, ref) = segments.take(3)
        val filePath = segments.drop(3).joinToString("/")
        return "https://$domain/gh/$owner/$repo@$ref/$filePath"
    }
}

// 使用示例：
//
// // 1. App 启动时拉取节点
// lifecycleScope.launch { MirrorHub.refresh() }
//
// // 2. 设置页显示来源声明（必须）
// val attr = MirrorHub.getAttribution()
// if (attr.required) {
//     Text("${attr.text} ↗", modifier = Modifier.clickable { openUrl(attr.url) })
// }
//
// // 3. 下载时获取加速 URL
// val url = MirrorHub.getFastestDownloadUrl(githubUrl) ?: githubUrl // 失败回退直连
// download(url)
