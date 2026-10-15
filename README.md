# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-15T03:21:42Z**，每 6 小时刷新一次。当前 ✅ **108** 在线 / ⚠️ **12** 不稳定 / ⚰️ **37** 已失效归档。

## 核心特性

- **120 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 58ms | Goreportcard | 0.05 MB/s | `https://goreportcard.com` | 通用代理 |
| 2 | 72ms | Microsoftedge | 1.4 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 74ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 4 | 84ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 108ms | Githubstatus | 3.58 MB/s | `https://githubstatus.com` | 通用代理 |
| 6 | 113ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 7 | 130ms | Thumb | 5.91 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 8 | 135ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 9 | 136ms | Training | 0.35 MB/s | `https://training.ti.com` | 通用代理 |
| 10 | 162ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 11 | 164ms | Axios-http | 1.15 MB/s | `https://axios-http.com` | 通用代理 |
| 12 | 165ms | Github | 2.4 MB/s | `https://github.880824.xyz` | 通用代理 |
| 13 | 167ms | Git | 4.01 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 14 | 168ms | Sub | 0.36 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 15 | 172ms | Gp | 2.67 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 16 | 178ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 17 | 180ms | Gh | 2.79 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 18 | 184ms | Github | 3.12 MB/s | `https://github.788787.xyz` | 通用代理 |
| 19 | 191ms | GH-Proxy | 2.29 MB/s | `https://gh-proxy.com` | 通用代理 |
| 20 | 192ms | Gh | 2.57 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 21 | 192ms | Github | 3.56 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 22 | 202ms | Git | 3.28 MB/s | `https://git.820828.xyz` | 通用代理 |
| 23 | 203ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 24 | 205ms | Github | 3.26 MB/s | `https://github.ihnic.com` | 通用代理 |
| 25 | 213ms | Img | - | `https://img.shields.io` | 通用代理 |
| 26 | 214ms | Ghproxy | 3.81 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 27 | 215ms | Ghproxy | 0.57 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 28 | 216ms | GH Monlor | 1.5 MB/s | `https://gh.monlor.com` | 通用代理 |
| 29 | 218ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 30 | 222ms | Gh | 3.53 MB/s | `https://gh.idayer.com` | 通用代理 |
| 31 | 222ms | Ghproxy | 2.2 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 32 | 224ms | Gh | 2.22 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 33 | 231ms | Cursor | 0.97 MB/s | `https://cursor.com` | 通用代理 |
| 34 | 232ms | Ampcode | 0.21 MB/s | `https://ampcode.com` | 通用代理 |
| 35 | 249ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 36 | 251ms | Gh | 3.45 MB/s | `https://gh.1k.ink` | 通用代理 |
| 37 | 251ms | Gh | 0.56 MB/s | `https://gh.39.al` | 通用代理 |
| 38 | 254ms | FastGit CC | 1.53 MB/s | `https://fastgit.cc` | 通用代理 |
| 39 | 262ms | Tvv | 2.4 MB/s | `https://tvv.tw` | 通用代理 |
| 40 | 267ms | Github | 0.37 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 41 | 273ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 42 | 284ms | 30006000 | 0.49 MB/s | `https://30006000.xyz` | 通用代理 |
| 43 | 292ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 44 | 297ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 45 | 303ms | Kenyu | 1.67 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 46 | 322ms | CrashMC CDN | 2.01 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 47 | 322ms | Npee Down | 0.02 MB/s | `https://down.npee.cn` | 通用代理 |
| 48 | 327ms | Msdn | 0.18 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 49 | 332ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 50 | 340ms | GH-Proxy YGXZ | 0.02 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 51 | 344ms | Gh | 0.39 MB/s | `https://gh.padao.fun` | 通用代理 |
| 52 | 345ms | GH Nxnow | 0.45 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 53 | 349ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 54 | 361ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 55 | 367ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 56 | 373ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 57 | 409ms | GHProxy Net | 0.33 MB/s | `https://ghproxy.net` | 通用代理 |
| 58 | 415ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 59 | 419ms | Ednovas Mirror | 0.51 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 60 | 431ms | Gh | 0.78 MB/s | `https://gh.noki.icu` | 通用代理 |
| 61 | 470ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 62 | 476ms | Gh | 0.48 MB/s | `https://gh.halonice.com` | 通用代理 |
| 63 | 491ms | Aosmd | 0.33 MB/s | `https://aosmd.com` | 通用代理 |
| 64 | 507ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 65 | 570ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 66 | 582ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 67 | 588ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 68 | 598ms | Github | 3.23 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 69 | 634ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 70 | 653ms | Hk | 1.35 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 71 | 656ms | Github | 0.42 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 72 | 699ms | YYLX Git | 0.2 MB/s | `https://git.yylx.win` | 通用代理 |
| 73 | 704ms | Github | 2.55 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 74 | 723ms | Fastfile | 2.68 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 75 | 731ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 76 | 747ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 77 | 758ms | Ghproxy | 0.22 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 78 | 805ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 79 | 829ms | GHFast | 0.48 MB/s | `https://ghfast.top` | 通用代理 |
| 80 | 851ms | Git | 0.15 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 81 | 900ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 82 | 901ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 83 | 972ms | GH-Proxy Org | 1.41 MB/s | `https://gh-proxy.org` | 通用代理 |
| 84 | 973ms | Ggg | 3.05 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 85 | 1003ms | Getgit | 3.26 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 86 | 1013ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 87 | 1041ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 88 | 1077ms | Web | - | `https://web.4399.com` | 通用代理 |
| 89 | 1169ms | Gh | 2.35 MB/s | `https://gh.dpik.top` | 通用代理 |
| 90 | 1276ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 91 | 1282ms | Ghproxy | 0.18 MB/s | `https://ghproxy.cc` | 通用代理 |
| 92 | 1304ms | Github | 0.12 MB/s | `https://github.chenc.dev` | 通用代理 |
| 93 | 1321ms | GHFile Geekertao | 1.19 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 94 | 1371ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 95 | 1456ms | Cf | 0.24 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 96 | 1510ms | Git | 0.28 MB/s | `https://git.669966.xyz` | 通用代理 |
| 97 | 1661ms | Github | 3.19 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 98 | 1768ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 99 | 1902ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 100 | 2170ms | Img | - | `https://img.ink` | 通用代理 |
| 101 | 2406ms | G | 0.16 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 102 | 2547ms | Wget | - | `https://wget.la` | 通用代理 |
| 103 | 2669ms | Ghproxy | 0.15 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 104 | 2897ms | Gh | 0.11 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 105 | 3342ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 106 | 4151ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 107 | 6156ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 108 | 11174ms | 5555 | 0.04 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Boki Mirror (`github-boki-moe`) | 24 次 |
| GHP Keleyaa (`ghp-keleyaa-com`) | 24 次 |
| GH Chjina (`gh-chjina-com`) | 24 次 |
| GHPXY Hwinzniej (`ghpxy-hwinzniej-top`) | 24 次 |
| GH ZWY (`gh-zwy-one`) | 20 次 |
| Lixxing Proxy (`github-proxy-lixxing-top`) | 24 次 |
| Gh (`gh-ddlc-top`) | 7 次 |
| ghproxy.homeboyc.cn (`ghproxy-homeboyc-cn`) | 20 次 |
| toolwa.com/github (`toolwa-com-github`) | 20 次 |
| github.akams.cn (`github-akams-cn`) | 20 次 |
| Github (`github-dpik-top`) | 7 次 |
| Proxy (`proxy-vvvv-ee`) | 2 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 113 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **120** | |

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
