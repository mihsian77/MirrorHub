# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-14T21:20:26Z**，每 6 小时刷新一次。当前 ✅ **101** 在线 / ⚠️ **18** 不稳定 / ⚰️ **37** 已失效归档。

## 核心特性

- **119 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 67ms | Goreportcard | 0.06 MB/s | `https://goreportcard.com` | 通用代理 |
| 2 | 75ms | Microsoftedge | 0.92 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 85ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 4 | 87ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 114ms | Githubstatus | 2.05 MB/s | `https://githubstatus.com` | 通用代理 |
| 6 | 119ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 7 | 143ms | Training | 0.17 MB/s | `https://training.ti.com` | 通用代理 |
| 8 | 144ms | Thumb | 2.86 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 9 | 169ms | Github | 2.35 MB/s | `https://github.880824.xyz` | 通用代理 |
| 10 | 176ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 11 | 176ms | Git | 2.24 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 12 | 178ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 13 | 180ms | Gp | 2.09 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 14 | 190ms | Gh | 1.78 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 15 | 190ms | Github | 1.8 MB/s | `https://github.788787.xyz` | 通用代理 |
| 16 | 194ms | Axios-http | 0.78 MB/s | `https://axios-http.com` | 通用代理 |
| 17 | 198ms | Gh | 1.9 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 18 | 200ms | Github | 1.58 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 19 | 207ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 20 | 208ms | Github | 2.52 MB/s | `https://github.ihnic.com` | 通用代理 |
| 21 | 209ms | Git | 2.14 MB/s | `https://git.820828.xyz` | 通用代理 |
| 22 | 213ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 23 | 219ms | Img | - | `https://img.shields.io` | 通用代理 |
| 24 | 225ms | Sub | 0.27 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 25 | 229ms | Ghproxy | 0.9 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 26 | 230ms | Gh | 2.23 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 27 | 230ms | Ghproxy | 0.67 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 28 | 232ms | GH Monlor | 1.36 MB/s | `https://gh.monlor.com` | 通用代理 |
| 29 | 240ms | Gh | 0.26 MB/s | `https://gh.39.al` | 通用代理 |
| 30 | 241ms | Ampcode | 0.2 MB/s | `https://ampcode.com` | 通用代理 |
| 31 | 242ms | Cursor | 0.75 MB/s | `https://cursor.com` | 通用代理 |
| 32 | 248ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 33 | 254ms | Tvv | 2.4 MB/s | `https://tvv.tw` | 通用代理 |
| 34 | 256ms | FastGit CC | 1.15 MB/s | `https://fastgit.cc` | 通用代理 |
| 35 | 269ms | Gh | 1.65 MB/s | `https://gh.1k.ink` | 通用代理 |
| 36 | 281ms | 30006000 | 0.58 MB/s | `https://30006000.xyz` | 通用代理 |
| 37 | 284ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 38 | 290ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 39 | 300ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 40 | 315ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 41 | 317ms | Kenyu | 2.53 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 42 | 333ms | CrashMC CDN | 1.7 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 43 | 335ms | GH Nxnow | 0.87 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 44 | 337ms | Npee Down | 0.01 MB/s | `https://down.npee.cn` | 通用代理 |
| 45 | 341ms | Gh | 0.44 MB/s | `https://gh.padao.fun` | 通用代理 |
| 46 | 346ms | GH-Proxy YGXZ | 0.01 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 47 | 356ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 48 | 373ms | Aps | 0.02 MB/s | `https://aps.com` | 通用代理 |
| 49 | 374ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 50 | 398ms | Github | 0.37 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 51 | 399ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 52 | 423ms | Ednovas Mirror | 0.51 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 53 | 430ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 54 | 432ms | GHProxy Net | 0.36 MB/s | `https://ghproxy.net` | 通用代理 |
| 55 | 443ms | Gh | 0.72 MB/s | `https://gh.noki.icu` | 通用代理 |
| 56 | 451ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 57 | 478ms | Gh | 0.59 MB/s | `https://gh.halonice.com` | 通用代理 |
| 58 | 507ms | Msdn | 0.1 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 59 | 523ms | Aosmd | 0.23 MB/s | `https://aosmd.com` | 通用代理 |
| 60 | 564ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 61 | 575ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 62 | 584ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 63 | 619ms | Github | 1.16 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 64 | 653ms | Github | 0.36 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 65 | 674ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 66 | 696ms | Hk | 1.11 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 67 | 705ms | YYLX Git | 0.32 MB/s | `https://git.yylx.win` | 通用代理 |
| 68 | 724ms | Github | 2.16 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 69 | 731ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 70 | 735ms | Fastfile | 1.29 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 71 | 745ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 72 | 750ms | Git | 0.17 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 73 | 760ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 74 | 805ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 75 | 810ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 76 | 847ms | GHFast | 0.29 MB/s | `https://ghfast.top` | 通用代理 |
| 77 | 886ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 78 | 978ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 79 | 979ms | Ggg | 2.27 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 80 | 985ms | GH-Proxy Org | 0.97 MB/s | `https://gh-proxy.org` | 通用代理 |
| 81 | 1014ms | Getgit | 2.05 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 82 | 1037ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 83 | 1080ms | Web | - | `https://web.4399.com` | 通用代理 |
| 84 | 1152ms | Gh | 0.65 MB/s | `https://gh.dpik.top` | 通用代理 |
| 85 | 1252ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 86 | 1276ms | Github | 0.13 MB/s | `https://github.chenc.dev` | 通用代理 |
| 87 | 1278ms | Ghproxy | 0.24 MB/s | `https://ghproxy.cc` | 通用代理 |
| 88 | 1469ms | Cf | 0.24 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 89 | 1624ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 90 | 1665ms | Github | 2.27 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 91 | 1751ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 92 | 1922ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 93 | 2154ms | Img | - | `https://img.ink` | 通用代理 |
| 94 | 2224ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 95 | 2238ms | Ghproxy | 0.15 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 96 | 2358ms | G | 0.16 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 97 | 2935ms | Gh | 0.07 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 98 | 3436ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 99 | 4603ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 100 | 6451ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 101 | 12316ms | 5555 | 0.06 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（18 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GH-Proxy (`gh-proxy-com`) | 2 次 |
| Boki Mirror (`github-boki-moe`) | 23 次 |
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| GHP Keleyaa (`ghp-keleyaa-com`) | 23 次 |
| GH Chjina (`gh-chjina-com`) | 23 次 |
| GHPXY Hwinzniej (`ghpxy-hwinzniej-top`) | 23 次 |
| GH ZWY (`gh-zwy-one`) | 19 次 |
| Lixxing Proxy (`github-proxy-lixxing-top`) | 23 次 |
| jsDelivr TestingCF (`jsdelivr-testingcf`) | 1 次 |
| Gh (`gh-ddlc-top`) | 6 次 |
| Gh (`gh-idayer-com`) | 3 次 |
| ghproxy.homeboyc.cn (`ghproxy-homeboyc-cn`) | 19 次 |
| toolwa.com/github (`toolwa-com-github`) | 19 次 |
| github.akams.cn (`github-akams-cn`) | 19 次 |
| Ghproxy (`ghproxy-imciel-com`) | 3 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Github (`github-dpik-top`) | 6 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 112 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **119** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（37 个）。

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
