# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-14T03:40:42Z**，每 6 小时刷新一次。当前 ✅ **95** 在线 / ⚠️ **15** 不稳定 / ⚰️ **37** 已失效归档。

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
| 1 | 64ms | Microsoftedge | 0.87 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 86ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 115ms | Githubstatus | 1.41 MB/s | `https://githubstatus.com` | 通用代理 |
| 4 | 121ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 5 | 125ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 6 | 136ms | Training | 0.29 MB/s | `https://training.ti.com` | 通用代理 |
| 7 | 136ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 8 | 157ms | Thumb | 2.94 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 9 | 185ms | Git | 3.08 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 10 | 186ms | Gp | 2.31 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 11 | 188ms | Github | 2.27 MB/s | `https://github.788787.xyz` | 通用代理 |
| 12 | 190ms | Github | 2.94 MB/s | `https://github.880824.xyz` | 通用代理 |
| 13 | 191ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 14 | 192ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 15 | 194ms | Git | 2.49 MB/s | `https://git.820828.xyz` | 通用代理 |
| 16 | 199ms | GH-Proxy | 1.29 MB/s | `https://gh-proxy.com` | 通用代理 |
| 17 | 199ms | Gh | 2.27 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 18 | 212ms | Ghproxy | 2.84 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 19 | 213ms | Gh | 2.43 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 20 | 213ms | Github | 2.09 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 21 | 214ms | Gh | 3.23 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 22 | 217ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 23 | 225ms | Img | - | `https://img.shields.io` | 通用代理 |
| 24 | 233ms | Github | 2.02 MB/s | `https://github.ihnic.com` | 通用代理 |
| 25 | 235ms | Gh | 0.54 MB/s | `https://gh.39.al` | 通用代理 |
| 26 | 237ms | GH Monlor | 1.86 MB/s | `https://gh.monlor.com` | 通用代理 |
| 27 | 237ms | Ghproxy | 2.28 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 28 | 246ms | Ampcode | 0.29 MB/s | `https://ampcode.com` | 通用代理 |
| 29 | 247ms | Cursor | 0.74 MB/s | `https://cursor.com` | 通用代理 |
| 30 | 258ms | Tvv | 2.47 MB/s | `https://tvv.tw` | 通用代理 |
| 31 | 260ms | Gh | 1.78 MB/s | `https://gh.idayer.com` | 通用代理 |
| 32 | 260ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 33 | 268ms | FastGit CC | 1.22 MB/s | `https://fastgit.cc` | 通用代理 |
| 34 | 289ms | Gh | 2.62 MB/s | `https://gh.1k.ink` | 通用代理 |
| 35 | 292ms | Ghproxy | 0.53 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 36 | 304ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 37 | 317ms | GH Nxnow | 0.68 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 38 | 318ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 39 | 323ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 40 | 328ms | Ggg | 2.26 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 41 | 339ms | Npee Down | 0.03 MB/s | `https://down.npee.cn` | 通用代理 |
| 42 | 349ms | Gh | 0.44 MB/s | `https://gh.padao.fun` | 通用代理 |
| 43 | 351ms | CrashMC CDN | 1.78 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 44 | 354ms | Kenyu | 2.49 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 45 | 362ms | Aps | 0.06 MB/s | `https://aps.com` | 通用代理 |
| 46 | 369ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 47 | 371ms | 30006000 | 0.52 MB/s | `https://30006000.xyz` | 通用代理 |
| 48 | 382ms | GH-Proxy YGXZ | 0.03 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 49 | 386ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 50 | 433ms | GHFast | 0.15 MB/s | `https://ghfast.top` | 通用代理 |
| 51 | 438ms | GHProxy Net | 0.14 MB/s | `https://ghproxy.net` | 通用代理 |
| 52 | 438ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 53 | 439ms | Github | 2.43 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 54 | 449ms | Gh | 0.79 MB/s | `https://gh.noki.icu` | 通用代理 |
| 55 | 461ms | Github | 0.46 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 56 | 485ms | Ednovas Mirror | 0.17 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 57 | 504ms | Aosmd | 0.2 MB/s | `https://aosmd.com` | 通用代理 |
| 58 | 515ms | Gh | 0.53 MB/s | `https://gh.halonice.com` | 通用代理 |
| 59 | 544ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 60 | 559ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 61 | 564ms | YYLX Git | 0.14 MB/s | `https://git.yylx.win` | 通用代理 |
| 62 | 631ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 63 | 636ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 64 | 645ms | GH-Proxy Org | 1.48 MB/s | `https://gh-proxy.org` | 通用代理 |
| 65 | 650ms | Github | 0.43 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 66 | 692ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 67 | 712ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 68 | 713ms | Getgit | 1.76 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 69 | 724ms | Fastfile | 1.68 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 70 | 726ms | Github | 2.24 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 71 | 733ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 72 | 740ms | Your-domain | 0.03 MB/s | `https://your-domain.com` | 通用代理 |
| 73 | 761ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 74 | 767ms | Git | 0.19 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 75 | 791ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 76 | 820ms | Ghproxy | 0.23 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 77 | 833ms | Hk | 1.05 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 78 | 1028ms | Web | - | `https://web.4399.com` | 通用代理 |
| 79 | 1087ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 80 | 1192ms | Github | 2.47 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 81 | 1247ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 82 | 1308ms | Ghproxy | 0.25 MB/s | `https://ghproxy.cc` | 通用代理 |
| 83 | 1322ms | Github | 0.13 MB/s | `https://github.chenc.dev` | 通用代理 |
| 84 | 1382ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 85 | 1418ms | Git | 0.31 MB/s | `https://git.669966.xyz` | 通用代理 |
| 86 | 1452ms | Cf | 0.24 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 87 | 1549ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 88 | 1569ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 89 | 1860ms | Img | - | `https://img.ink` | 通用代理 |
| 90 | 1885ms | Ghproxy | 0.14 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 91 | 2577ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 92 | 3095ms | G | 0.16 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 93 | 3410ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 94 | 5748ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 95 | 6111ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（15 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Boki Mirror (`github-boki-moe`) | 20 次 |
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| GHP Keleyaa (`ghp-keleyaa-com`) | 20 次 |
| GH Chjina (`gh-chjina-com`) | 20 次 |
| GHPXY Hwinzniej (`ghpxy-hwinzniej-top`) | 20 次 |
| GH ZWY (`gh-zwy-one`) | 16 次 |
| Lixxing Proxy (`github-proxy-lixxing-top`) | 20 次 |
| Gh (`gh-ddlc-top`) | 3 次 |
| ghproxy.homeboyc.cn (`ghproxy-homeboyc-cn`) | 16 次 |
| toolwa.com/github (`toolwa-com-github`) | 16 次 |
| github.akams.cn (`github-akams-cn`) | 16 次 |
| Gh (`gh-dpik-top`) | 1 次 |
| Gh (`gh-b52m-cn`) | 1 次 |
| Github (`github-dpik-top`) | 3 次 |
| Proxy (`proxy-vvvv-ee`) | 2 次 |

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
