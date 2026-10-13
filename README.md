# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-13T13:38:40Z**，每 6 小时刷新一次。当前 ✅ **95** 在线 / ⚠️ **15** 不稳定 / ⚰️ **37** 已失效归档。

## 核心特性

- **110 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 67ms | Microsoftedge | 0.78 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 93ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 115ms | Githubstatus | 1.29 MB/s | `https://githubstatus.com` | 通用代理 |
| 4 | 119ms | Training | 0.23 MB/s | `https://training.ti.com` | 通用代理 |
| 5 | 135ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 6 | 142ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 7 | 159ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 8 | 182ms | Gh | 0.6 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 9 | 184ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 10 | 186ms | Gp | 0.61 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 11 | 195ms | Git | 0.93 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 12 | 195ms | Github | 0.74 MB/s | `https://github.880824.xyz` | 通用代理 |
| 13 | 196ms | Github | 0.58 MB/s | `https://github.788787.xyz` | 通用代理 |
| 14 | 196ms | Thumb | 0.72 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 15 | 200ms | Git | 0.78 MB/s | `https://git.820828.xyz` | 通用代理 |
| 16 | 212ms | Gh | 0.56 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 17 | 214ms | GH-Proxy | 1.47 MB/s | `https://gh-proxy.com` | 通用代理 |
| 18 | 220ms | Github | 0.66 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 19 | 221ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 20 | 222ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 21 | 224ms | Img | - | `https://img.shields.io` | 通用代理 |
| 22 | 225ms | Gh | 0.57 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 23 | 232ms | Gh | 1.11 MB/s | `https://gh.39.al` | 通用代理 |
| 24 | 240ms | GH Monlor | 1.3 MB/s | `https://gh.monlor.com` | 通用代理 |
| 25 | 243ms | Github | 0.77 MB/s | `https://github.ihnic.com` | 通用代理 |
| 26 | 246ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 27 | 250ms | Tvv | 0.66 MB/s | `https://tvv.tw` | 通用代理 |
| 28 | 255ms | Ampcode | 0.14 MB/s | `https://ampcode.com` | 通用代理 |
| 29 | 255ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 30 | 258ms | Cursor | 0.41 MB/s | `https://cursor.com` | 通用代理 |
| 31 | 260ms | Ghproxy | 0.68 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 32 | 263ms | FastGit CC | 0.48 MB/s | `https://fastgit.cc` | 通用代理 |
| 33 | 275ms | Ghproxy | 0.91 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 34 | 291ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 35 | 298ms | Ggg | 0.6 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 36 | 302ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 37 | 303ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 38 | 306ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 39 | 317ms | GH Nxnow | 0.26 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 40 | 320ms | Gh | 1.02 MB/s | `https://gh.1k.ink` | 通用代理 |
| 41 | 327ms | Gh | 0.64 MB/s | `https://gh.padao.fun` | 通用代理 |
| 42 | 340ms | Aps | 0.11 MB/s | `https://aps.com` | 通用代理 |
| 43 | 348ms | Kenyu | 0.84 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 44 | 354ms | Npee Down | 0.02 MB/s | `https://down.npee.cn` | 通用代理 |
| 45 | 364ms | GH-Proxy YGXZ | 0.04 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 46 | 365ms | CrashMC CDN | 0.37 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 47 | 371ms | 30006000 | 0.6 MB/s | `https://30006000.xyz` | 通用代理 |
| 48 | 400ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 49 | 407ms | Gh | 0.49 MB/s | `https://gh.noki.icu` | 通用代理 |
| 50 | 409ms | Github | 0.63 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 51 | 431ms | Github | 0.81 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 52 | 452ms | GHProxy Net | 0.03 MB/s | `https://ghproxy.net` | 通用代理 |
| 53 | 456ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 54 | 465ms | Ednovas Mirror | 0.29 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 55 | 481ms | GHFast | 0.69 MB/s | `https://ghfast.top` | 通用代理 |
| 56 | 507ms | Gh | 0.18 MB/s | `https://gh.halonice.com` | 通用代理 |
| 57 | 548ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 58 | 566ms | YYLX Git | 0.48 MB/s | `https://git.yylx.win` | 通用代理 |
| 59 | 592ms | Aosmd | 0.13 MB/s | `https://aosmd.com` | 通用代理 |
| 60 | 602ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 61 | 625ms | Your-domain | 0.04 MB/s | `https://your-domain.com` | 通用代理 |
| 62 | 627ms | Github | 0.56 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 63 | 643ms | GH-Proxy Org | 0.94 MB/s | `https://gh-proxy.org` | 通用代理 |
| 64 | 650ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 65 | 675ms | SLink | 0.02 MB/s | `https://slink.ltd` | 通用代理 |
| 66 | 690ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 67 | 711ms | Github | 1.17 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 68 | 723ms | Git | 0.22 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 69 | 730ms | Getgit | 0.54 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 70 | 736ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 71 | 740ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 72 | 754ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 73 | 756ms | Fastfile | 0.52 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 74 | 808ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 75 | 819ms | Ghproxy | 0.34 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 76 | 1028ms | Hk | 1.53 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 77 | 1108ms | Web | - | `https://web.4399.com` | 通用代理 |
| 78 | 1118ms | Gh | 0.53 MB/s | `https://gh.dpik.top` | 通用代理 |
| 79 | 1230ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 80 | 1233ms | Github | 0.78 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 81 | 1287ms | Ghproxy | 0.21 MB/s | `https://ghproxy.cc` | 通用代理 |
| 82 | 1293ms | Github | 0.16 MB/s | `https://github.chenc.dev` | 通用代理 |
| 83 | 1310ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 84 | 1331ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 85 | 1377ms | GHFile Geekertao | 0.11 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 86 | 1379ms | Img | - | `https://img.ink` | 通用代理 |
| 87 | 1435ms | Cf | 0.2 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 88 | 1597ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 89 | 1649ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 90 | 2359ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 91 | 3053ms | Gh | 0.06 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 92 | 3218ms | G | 0.05 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 93 | 3501ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 94 | 5848ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 95 | 6954ms | GitClone | - | `https://gitclone.com` | Clone 专用 |


### ⚠️ 不稳定节点（15 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Boki Mirror (`github-boki-moe`) | 18 次 |
| GHP Keleyaa (`ghp-keleyaa-com`) | 18 次 |
| GH Chjina (`gh-chjina-com`) | 18 次 |
| GHPXY Hwinzniej (`ghpxy-hwinzniej-top`) | 18 次 |
| GH ZWY (`gh-zwy-one`) | 14 次 |
| Lixxing Proxy (`github-proxy-lixxing-top`) | 18 次 |
| Gh (`gh-ddlc-top`) | 1 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| ghproxy.homeboyc.cn (`ghproxy-homeboyc-cn`) | 14 次 |
| toolwa.com/github (`toolwa-com-github`) | 14 次 |
| github.akams.cn (`github-akams-cn`) | 14 次 |
| Ghproxy (`ghproxy-imciel-com`) | 1 次 |
| Ghproxy (`ghproxy-mirror-skybyte-me`) | 1 次 |
| Git (`git-669966-xyz`) | 3 次 |
| Github (`github-dpik-top`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 103 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **110** | |

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
