# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-16T20:33:43Z**，每 6 小时刷新一次。当前 ✅ **112** 在线 / ⚠️ **11** 不稳定 / ⚰️ **42** 已失效归档。

## 核心特性

- **123 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 42ms | Linkedin | 0.5 MB/s | `https://linkedin.com` | 通用代理 |
| 2 | 49ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 3 | 78ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 4 | 85ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 5 | 86ms | Microsoftedge | 1.22 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 6 | 100ms | Githubstatus | 1.71 MB/s | `https://githubstatus.com` | 通用代理 |
| 7 | 116ms | Thumb | 5.57 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 8 | 120ms | Goreportcard | 0.05 MB/s | `https://goreportcard.com` | 通用代理 |
| 9 | 140ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 10 | 144ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 11 | 159ms | Img | - | `https://img.shields.io` | 通用代理 |
| 12 | 163ms | GH-Proxy | 1.33 MB/s | `https://gh-proxy.com` | 通用代理 |
| 13 | 164ms | Training | 0.2 MB/s | `https://training.ti.com` | 通用代理 |
| 14 | 167ms | GH Monlor | 1.63 MB/s | `https://gh.monlor.com` | 通用代理 |
| 15 | 175ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 16 | 175ms | Github | 2.07 MB/s | `https://github.880824.xyz` | 通用代理 |
| 17 | 183ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 18 | 183ms | Github | 2.67 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 19 | 190ms | Gp | 1.95 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 20 | 190ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 21 | 196ms | Github | 2.19 MB/s | `https://github.788787.xyz` | 通用代理 |
| 22 | 198ms | Git | 2.19 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 23 | 207ms | Axios-http | 1.27 MB/s | `https://axios-http.com` | 通用代理 |
| 24 | 207ms | Gh | 2.14 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 25 | 208ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 26 | 212ms | Cursor | 0.73 MB/s | `https://cursor.com` | 通用代理 |
| 27 | 213ms | Ghproxy | 0.55 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 28 | 213ms | Sub | 0.37 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 29 | 217ms | Gh | 1.88 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 30 | 218ms | Gh | 2.02 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 31 | 219ms | Gh | 0.4 MB/s | `https://gh.halonice.com` | 通用代理 |
| 32 | 222ms | Git | 2.36 MB/s | `https://git.820828.xyz` | 通用代理 |
| 33 | 236ms | Ampcode | 0.32 MB/s | `https://ampcode.com` | 通用代理 |
| 34 | 247ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 35 | 249ms | Gh | 0.51 MB/s | `https://gh.39.al` | 通用代理 |
| 36 | 249ms | Ghproxy | 1.84 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 37 | 249ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 38 | 252ms | Github | 1.67 MB/s | `https://github.ihnic.com` | 通用代理 |
| 39 | 253ms | Github | 0.55 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 40 | 254ms | FastGit CC | 1.01 MB/s | `https://fastgit.cc` | 通用代理 |
| 41 | 257ms | Gh | 0.77 MB/s | `https://gh.1k.ink` | 通用代理 |
| 42 | 257ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 43 | 265ms | Oem | - | `https://oem.re` | 通用代理 |
| 44 | 267ms | Tvv | 1.84 MB/s | `https://tvv.tw` | 通用代理 |
| 45 | 298ms | Aps | 0.05 MB/s | `https://aps.com` | 通用代理 |
| 46 | 298ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 47 | 301ms | Npee Down | 0.02 MB/s | `https://down.npee.cn` | 通用代理 |
| 48 | 311ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 49 | 313ms | 30006000 | 0.57 MB/s | `https://30006000.xyz` | 通用代理 |
| 50 | 314ms | GH-Proxy YGXZ | 0.01 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 51 | 318ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 52 | 327ms | Gh | 0.4 MB/s | `https://gh.padao.fun` | 通用代理 |
| 53 | 332ms | CrashMC CDN | 1.04 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 54 | 334ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 55 | 339ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 56 | 347ms | Hk | 1.17 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 57 | 350ms | Kenyu | 2.8 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 58 | 351ms | Api | 0.03 MB/s | `https://api.solov.cc` | 通用代理 |
| 59 | 355ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 60 | 362ms | GH Nxnow | 0.63 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 61 | 382ms | Gh | 0.86 MB/s | `https://gh.noki.icu` | 通用代理 |
| 62 | 394ms | Github | 2.18 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 63 | 409ms | GHProxy Net | 0.37 MB/s | `https://ghproxy.net` | 通用代理 |
| 64 | 411ms | Msdn | 0.13 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 65 | 426ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 66 | 435ms | Ednovas Mirror | 0.48 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 67 | 501ms | Aosmd | 0.24 MB/s | `https://aosmd.com` | 通用代理 |
| 68 | 511ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 69 | 516ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 70 | 566ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 71 | 578ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 72 | 580ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 73 | 588ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 74 | 602ms | Github | 1.34 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 75 | 606ms | GH-Proxy Org | 1.34 MB/s | `https://gh-proxy.org` | 通用代理 |
| 76 | 655ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 77 | 673ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 78 | 724ms | Github | 0.41 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 79 | 745ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 80 | 750ms | Getgit | 1.93 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 81 | 750ms | YYLX Git | 0.5 MB/s | `https://git.yylx.win` | 通用代理 |
| 82 | 752ms | GHFast | 0.45 MB/s | `https://ghfast.top` | 通用代理 |
| 83 | 792ms | Fastfile | 1.21 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 84 | 798ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 85 | 817ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 86 | 819ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 87 | 864ms | Git | 0.18 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 88 | 896ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 89 | 924ms | Github | 2.18 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 90 | 957ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 91 | 982ms | Mimo | 0.15 MB/s | `https://mimo.mi.com` | 通用代理 |
| 92 | 1066ms | Web | - | `https://web.4399.com` | 通用代理 |
| 93 | 1091ms | Ggg | 2.33 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 94 | 1226ms | Gh | 1.65 MB/s | `https://gh.dpik.top` | 通用代理 |
| 95 | 1253ms | Github | 0.13 MB/s | `https://github.chenc.dev` | 通用代理 |
| 96 | 1298ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 97 | 1309ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 98 | 1332ms | Ghproxy | 0.24 MB/s | `https://ghproxy.cc` | 通用代理 |
| 99 | 1396ms | Git | 0.19 MB/s | `https://git.669966.xyz` | 通用代理 |
| 100 | 1408ms | SLink | 0.01 MB/s | `https://slink.ltd` | 通用代理 |
| 101 | 1518ms | Cf | 0.2 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 102 | 1802ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 103 | 1802ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 104 | 2040ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 105 | 2090ms | Img | - | `https://img.ink` | 通用代理 |
| 106 | 2217ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 107 | 2627ms | G | 0.15 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 108 | 2793ms | Ghproxy | 0.14 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 109 | 2977ms | Gh | 0.08 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 110 | 3389ms | GHProxy MonkeyRay | 0.09 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 111 | 6189ms | Proxy | 0.04 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 112 | 9623ms | 5555 | 0.04 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（11 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| GH ZWY (`gh-zwy-one`) | 27 次 |
| GitClone (`gitclone-com`) | 3 次 |
| Gh (`gh-ddlc-top`) | 14 次 |
| Gh (`gh-idayer-com`) | 3 次 |
| ghproxy.homeboyc.cn (`ghproxy-homeboyc-cn`) | 27 次 |
| toolwa.com/github (`toolwa-com-github`) | 27 次 |
| github.akams.cn (`github-akams-cn`) | 27 次 |
| Ghproxy (`ghproxy-imciel-com`) | 7 次 |
| Github (`github-dpik-top`) | 14 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 116 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **123** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（42 个）。

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
