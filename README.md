# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-19T12:15:51Z**，每 6 小时刷新一次。当前 ✅ **136** 在线 / ⚠️ **12** 不稳定 / ⚰️ **46** 已失效归档。

## 核心特性

- **148 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 61ms | Microsoftedge | 0.02 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 72ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 73ms | Linkedin | 0.17 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 81ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 5 | 95ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 6 | 96ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 7 | 107ms | Githubstatus | 0.94 MB/s | `https://githubstatus.com` | 通用代理 |
| 8 | 111ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 9 | 118ms | App | 0.1 MB/s | `https://app.netlify.com` | 通用代理 |
| 10 | 127ms | Thumb | 0.99 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 11 | 131ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 12 | 142ms | Git | 1.67 MB/s | `https://git.820828.xyz` | 通用代理 |
| 13 | 145ms | Git | 1.7 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 14 | 151ms | Github | 1.44 MB/s | `https://github.880824.xyz` | 通用代理 |
| 15 | 151ms | Gp | 1.9 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 16 | 153ms | Training | 0.13 MB/s | `https://training.ti.com` | 通用代理 |
| 17 | 154ms | Github | 1.34 MB/s | `https://github.788787.xyz` | 通用代理 |
| 18 | 154ms | Github | 1.49 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 19 | 156ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 20 | 164ms | Gh | 1.43 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 21 | 169ms | Gh | 1.2 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 22 | 169ms | Ghproxy | 1.4 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 23 | 171ms | Github | 1.72 MB/s | `https://github.ihnic.com` | 通用代理 |
| 24 | 175ms | GH Monlor | 0.82 MB/s | `https://gh.monlor.com` | 通用代理 |
| 25 | 177ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 26 | 177ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 27 | 183ms | Img | - | `https://img.shields.io` | 通用代理 |
| 28 | 184ms | Tvv | 1.46 MB/s | `https://tvv.tw` | 通用代理 |
| 29 | 185ms | Gh | 1.47 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 30 | 188ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 31 | 192ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 32 | 193ms | GH-Proxy | 1.0 MB/s | `https://gh-proxy.com` | 通用代理 |
| 33 | 201ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 34 | 205ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 35 | 211ms | Axios-http | 0.34 MB/s | `https://axios-http.com` | 通用代理 |
| 36 | 215ms | FastGit CC | 1.03 MB/s | `https://fastgit.cc` | 通用代理 |
| 37 | 218ms | Ampcode | 0.08 MB/s | `https://ampcode.com` | 通用代理 |
| 38 | 218ms | Ghproxy | 1.94 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 39 | 220ms | Gh | 0.74 MB/s | `https://gh.halonice.com` | 通用代理 |
| 40 | 223ms | Sub | 0.13 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 41 | 224ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 42 | 227ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 43 | 228ms | Cursor | 0.47 MB/s | `https://cursor.com` | 通用代理 |
| 44 | 228ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 45 | 229ms | Ggg | 1.55 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 46 | 233ms | Ghproxy | 0.76 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 47 | 234ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 48 | 235ms | Kenyu | 1.65 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 49 | 236ms | GH-Proxy Org | 0.94 MB/s | `https://gh-proxy.org` | 通用代理 |
| 50 | 237ms | CrashMC CDN | 1.05 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 51 | 242ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 52 | 242ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 53 | 243ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 54 | 249ms | Twitter | 0.67 MB/s | `https://twitter.com` | 通用代理 |
| 55 | 252ms | Api | 0.09 MB/s | `https://api.solov.cc` | 通用代理 |
| 56 | 253ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 57 | 253ms | Nisar | 0.66 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 58 | 257ms | Gh | 1.93 MB/s | `https://gh.1k.ink` | 通用代理 |
| 59 | 271ms | Github | 0.71 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 60 | 288ms | Npee Down | 0.02 MB/s | `https://down.npee.cn` | 通用代理 |
| 61 | 289ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 62 | 291ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 63 | 313ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 64 | 316ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 65 | 323ms | Ednovas Mirror | 0.62 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 66 | 327ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 67 | 331ms | Gh | 0.67 MB/s | `https://gh.padao.fun` | 通用代理 |
| 68 | 339ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 69 | 344ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 70 | 346ms | 30006000 | 0.6 MB/s | `https://30006000.xyz` | 通用代理 |
| 71 | 346ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 72 | 356ms | GH Nxnow | 0.37 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 73 | 360ms | Gh | 0.96 MB/s | `https://gh.noki.icu` | 通用代理 |
| 74 | 368ms | Github | 1.52 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 75 | 374ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 76 | 378ms | Bailian | 0.07 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 77 | 382ms | Hk | 0.88 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 78 | 395ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 79 | 404ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 80 | 410ms | Getgit | 1.44 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 81 | 410ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 82 | 460ms | Aps | 0.05 MB/s | `https://aps.com` | 通用代理 |
| 83 | 471ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 84 | 477ms | Github | 1.27 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 85 | 480ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 86 | 482ms | Steamcommunity | 0.12 MB/s | `https://steamcommunity.com` | 通用代理 |
| 87 | 505ms | GHFast | 0.27 MB/s | `https://ghfast.top` | 通用代理 |
| 88 | 518ms | Aosmd | 0.14 MB/s | `https://aosmd.com` | 通用代理 |
| 89 | 523ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 90 | 554ms | GHProxy Net | 0.13 MB/s | `https://ghproxy.net` | 通用代理 |
| 91 | 563ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 92 | 564ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 93 | 567ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 94 | 586ms | Proxy | 0.63 MB/s | `https://proxy.vvvv.ee` | 通用代理 |
| 95 | 589ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 96 | 595ms | Github | 1.59 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 97 | 636ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 98 | 658ms | Fastfile | 0.99 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 99 | 659ms | Gh | 1.37 MB/s | `https://gh.dpik.top` | 通用代理 |
| 100 | 672ms | YYLX Git | 0.67 MB/s | `https://git.yylx.win` | 通用代理 |
| 101 | 693ms | Ghproxy | 0.21 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 102 | 694ms | Github | 0.28 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 103 | 735ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 104 | 738ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 105 | 790ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 106 | 801ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 107 | 811ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 108 | 824ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 109 | 844ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 110 | 878ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 111 | 883ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 112 | 893ms | Web | - | `https://web.4399.com` | 通用代理 |
| 113 | 898ms | GHFile Geekertao | 0.17 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 114 | 940ms | Mimo | 0.16 MB/s | `https://mimo.mi.com` | 通用代理 |
| 115 | 949ms | Gh | 0.92 MB/s | `https://gh.39.al` | 通用代理 |
| 116 | 1015ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 117 | 1137ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 118 | 1141ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 119 | 1151ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 120 | 1161ms | Git | 0.37 MB/s | `https://git.669966.xyz` | 通用代理 |
| 121 | 1204ms | Bseindia | 0.01 MB/s | `https://bseindia.com` | 通用代理 |
| 122 | 1227ms | Ghproxy | 0.24 MB/s | `https://ghproxy.cc` | 通用代理 |
| 123 | 1301ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 124 | 1324ms | Github | 0.16 MB/s | `https://github.chenc.dev` | 通用代理 |
| 125 | 1386ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 126 | 1590ms | Cf | 0.22 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 127 | 1613ms | G | 0.06 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 128 | 1639ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 129 | 1647ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 130 | 1726ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 131 | 1778ms | Ghproxy | 0.7 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 132 | 2022ms | Docs | 0.02 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 133 | 2373ms | Img | - | `https://img.ink` | 通用代理 |
| 134 | 3332ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 135 | 4018ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 136 | 7974ms | 5555 | 0.04 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 6 次 |
| GitClone (`gitclone-com`) | 1 次 |
| Gh (`gh-ddlc-top`) | 24 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Git (`git-tangbai-cc`) | 4 次 |
| Gitproxy (`gitproxy-click`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Gh (`gh-b52m-cn`) | 1 次 |
| Github (`github-dpik-top`) | 24 次 |
| Code (`code-leez-tech`) | 1 次 |
| Fastgpt (`fastgpt-leez-tech`) | 1 次 |
| Status (`status-leez-tech`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 141 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **148** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（46 个）。

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
