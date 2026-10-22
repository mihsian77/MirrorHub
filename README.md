# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-22T03:27:17Z**，每 6 小时刷新一次。当前 ✅ **156** 在线 / ⚠️ **13** 不稳定 / ⚰️ **48** 已失效归档。

## 核心特性

- **169 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 68ms | Microsoftedge | 0.37 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 80ms | Deno | 0.41 MB/s | `https://deno.com` | 通用代理 |
| 3 | 84ms | Linkedin | 0.13 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 85ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 98ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 6 | 109ms | App | 0.06 MB/s | `https://app.netlify.com` | 通用代理 |
| 7 | 115ms | X | 1.13 MB/s | `https://x.com` | 通用代理 |
| 8 | 118ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 9 | 119ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 10 | 119ms | Resume-5lv | 0.14 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 11 | 121ms | Githubstatus | 0.72 MB/s | `https://githubstatus.com` | 通用代理 |
| 12 | 138ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 13 | 140ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 14 | 141ms | Thumb | 0.72 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 15 | 145ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 16 | 149ms | Crypto-funding-arbitrage | 0.03 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 17 | 157ms | Wordpaper | 0.26 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 18 | 161ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 19 | 162ms | Zebrunner | 0.97 MB/s | `https://zebrunner.com` | 通用代理 |
| 20 | 168ms | GH-Proxy | 0.86 MB/s | `https://gh-proxy.com` | 通用代理 |
| 21 | 199ms | Git | 1.33 MB/s | `https://git.820828.xyz` | 通用代理 |
| 22 | 199ms | Github | 1.57 MB/s | `https://github.880824.xyz` | 通用代理 |
| 23 | 203ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 24 | 207ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 25 | 209ms | Tvv | 1.49 MB/s | `https://tvv.tw` | 通用代理 |
| 26 | 211ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 27 | 211ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 28 | 211ms | Training | 0.15 MB/s | `https://training.ti.com` | 通用代理 |
| 29 | 212ms | Twitter | 0.69 MB/s | `https://twitter.com` | 通用代理 |
| 30 | 215ms | Ghproxy | 1.48 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 31 | 216ms | Gh | 1.33 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 32 | 216ms | Github | 1.58 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 33 | 218ms | Git | 1.48 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 34 | 220ms | Github | 1.4 MB/s | `https://github.788787.xyz` | 通用代理 |
| 35 | 220ms | Openttd | 0.03 MB/s | `https://openttd.org` | 通用代理 |
| 36 | 221ms | Gh | 1.54 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 37 | 221ms | Img | - | `https://img.shields.io` | 通用代理 |
| 38 | 222ms | GH Monlor | 0.91 MB/s | `https://gh.monlor.com` | 通用代理 |
| 39 | 226ms | Ampcode | 0.22 MB/s | `https://ampcode.com` | 通用代理 |
| 40 | 227ms | Gh | 1.51 MB/s | `https://gh.1k.ink` | 通用代理 |
| 41 | 227ms | Github | 1.46 MB/s | `https://github.ihnic.com` | 通用代理 |
| 42 | 229ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 43 | 231ms | Ghproxy | 1.18 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 44 | 231ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 45 | 231ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 46 | 231ms | Sub | 0.13 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 47 | 234ms | Axios-http | 0.38 MB/s | `https://axios-http.com` | 通用代理 |
| 48 | 235ms | Gp | 1.28 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 49 | 236ms | Ghproxy | 0.85 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 50 | 242ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 51 | 244ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 52 | 244ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 53 | 246ms | Gh | 1.53 MB/s | `https://gh.idayer.com` | 通用代理 |
| 54 | 247ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 55 | 248ms | Cursor | 0.33 MB/s | `https://cursor.com` | 通用代理 |
| 56 | 249ms | GH-Proxy Org | 0.92 MB/s | `https://gh-proxy.org` | 通用代理 |
| 57 | 251ms | Github | 1.05 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 58 | 253ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 59 | 257ms | Agoramarket | 0.52 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 60 | 257ms | Gh | 0.92 MB/s | `https://gh.padao.fun` | 通用代理 |
| 61 | 263ms | Nisar | 0.84 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 62 | 265ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 63 | 274ms | FastGit CC | 0.95 MB/s | `https://fastgit.cc` | 通用代理 |
| 64 | 276ms | Coreos | 1.3 MB/s | `https://coreos.com` | 通用代理 |
| 65 | 292ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 66 | 293ms | Ggg | 1.26 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 67 | 294ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 68 | 303ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 69 | 303ms | Kenyu | 1.36 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 70 | 311ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 71 | 319ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 72 | 322ms | Bailian | 0.16 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 73 | 326ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 74 | 332ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 75 | 333ms | 30006000 | 0.56 MB/s | `https://30006000.xyz` | 通用代理 |
| 76 | 338ms | Code | 1.39 MB/s | `https://code.claude.com` | 通用代理 |
| 77 | 338ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 78 | 342ms | CrashMC CDN | 1.13 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 79 | 345ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 80 | 352ms | Api | 0.06 MB/s | `https://api.solov.cc` | 通用代理 |
| 81 | 358ms | Kuroutoshikou | 0.51 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 82 | 362ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 83 | 363ms | Gh | 0.65 MB/s | `https://gh.noki.icu` | 通用代理 |
| 84 | 364ms | Hk | 0.66 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 85 | 367ms | Steamcommunity | 0.1 MB/s | `https://steamcommunity.com` | 通用代理 |
| 86 | 371ms | GHFast | 0.75 MB/s | `https://ghfast.top` | 通用代理 |
| 87 | 371ms | Getgit | 1.5 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 88 | 385ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 89 | 385ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 90 | 388ms | Ark | 0.45 MB/s | `https://ark.intel.com` | 通用代理 |
| 91 | 388ms | Support | 0.41 MB/s | `https://support.apple.com` | 通用代理 |
| 92 | 391ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 93 | 405ms | Contrib | 0.2 MB/s | `https://contrib.rocks` | 通用代理 |
| 94 | 418ms | Store | 0.74 MB/s | `https://store.steampowered.com` | 通用代理 |
| 95 | 437ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 96 | 441ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 97 | 447ms | Aps | 0.04 MB/s | `https://aps.com` | 通用代理 |
| 98 | 454ms | Github | 1.33 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 99 | 458ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 100 | 473ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 101 | 478ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 102 | 489ms | SLink | 0.07 MB/s | `https://slink.ltd` | 通用代理 |
| 103 | 511ms | GH Nxnow | 0.3 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 104 | 513ms | YYLX Git | 0.41 MB/s | `https://git.yylx.win` | 通用代理 |
| 105 | 529ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 106 | 531ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 107 | 537ms | Github | 1.64 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 108 | 539ms | Aosmd | 0.15 MB/s | `https://aosmd.com` | 通用代理 |
| 109 | 552ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 110 | 565ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 111 | 565ms | Gh | 0.9 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 112 | 568ms | GHProxy Net | 0.23 MB/s | `https://ghproxy.net` | 通用代理 |
| 113 | 571ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 114 | 576ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 115 | 593ms | Github | 0.4 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 116 | 606ms | Github | 1.61 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 117 | 607ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 118 | 614ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 119 | 655ms | Ghproxy | 0.06 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 120 | 715ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 121 | 738ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 122 | 744ms | Fastfile | 0.96 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 123 | 749ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 124 | 751ms | Ghproxy | 0.34 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 125 | 772ms | GHFile Geekertao | 0.2 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 126 | 776ms | Docs | 0.16 MB/s | `https://docs.transifex.com` | 通用代理 |
| 127 | 809ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 128 | 810ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 129 | 820ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 130 | 829ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 131 | 863ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 132 | 886ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 133 | 899ms | Gh | 0.39 MB/s | `https://gh.dpik.top` | 通用代理 |
| 134 | 930ms | Mimo | 0.17 MB/s | `https://mimo.mi.com` | 通用代理 |
| 135 | 989ms | Web | - | `https://web.4399.com` | 通用代理 |
| 136 | 1085ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 137 | 1129ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 138 | 1133ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 139 | 1171ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 140 | 1233ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 141 | 1270ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 142 | 1304ms | Ghproxy | 0.27 MB/s | `https://ghproxy.cc` | 通用代理 |
| 143 | 1315ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 144 | 1339ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 145 | 1429ms | Cf | 0.23 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 146 | 1596ms | Github | 0.16 MB/s | `https://github.chenc.dev` | 通用代理 |
| 147 | 1708ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 148 | 1717ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 149 | 1870ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 150 | 2083ms | Img | - | `https://img.ink` | 通用代理 |
| 151 | 2221ms | G | 0.26 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 152 | 2444ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 153 | 2896ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 154 | 3259ms | Gh | 0.08 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 155 | 3741ms | Wget | - | `https://wget.la` | 通用代理 |
| 156 | 4000ms | GHProxy MonkeyRay | 0.05 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（13 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Ednovas Mirror (`github-ednovas-xyz`) | 1 次 |
| Npee Down (`down-npee-cn`) | 9 次 |
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 16 次 |
| GitClone (`gitclone-com`) | 8 次 |
| Gh (`gh-39-al`) | 3 次 |
| Gh (`gh-halonice-com`) | 8 次 |
| Git (`git-669966-xyz`) | 3 次 |
| Git (`git-tangbai-cc`) | 9 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Mirror (`mirror-houlang-cloud`) | 3 次 |
| 5555 (`5555-cab`) | 1 次 |
| Status (`status-leez-tech`) | 2 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 162 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **169** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（48 个）。

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
