# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-23T03:33:03Z**，每 6 小时刷新一次。当前 ✅ **160** 在线 / ⚠️ **12** 不稳定 / ⚰️ **48** 已失效归档。

## 核心特性

- **172 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 55ms | Microsoftedge | 1.42 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 70ms | Deno | 0.5 MB/s | `https://deno.com` | 通用代理 |
| 3 | 71ms | Linkedin | 0.51 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 75ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 92ms | Gitea-mirror | 0.89 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 6 | 93ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 7 | 94ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 8 | 98ms | X | 1.89 MB/s | `https://x.com` | 通用代理 |
| 9 | 101ms | App | 0.15 MB/s | `https://app.netlify.com` | 通用代理 |
| 10 | 106ms | Resume-5lv | 0.21 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 11 | 109ms | Githubstatus | 2.25 MB/s | `https://githubstatus.com` | 通用代理 |
| 12 | 114ms | Crypto-funding-arbitrage | 0.13 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 13 | 120ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 14 | 123ms | Wordpaper | 0.49 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 15 | 124ms | Thumb | 5.75 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 16 | 128ms | Zebrunner | 1.92 MB/s | `https://zebrunner.com` | 通用代理 |
| 17 | 133ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 18 | 138ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 19 | 155ms | Goreportcard | 0.06 MB/s | `https://goreportcard.com` | 通用代理 |
| 20 | 157ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 21 | 161ms | GH-Proxy | 1.63 MB/s | `https://gh-proxy.com` | 通用代理 |
| 22 | 182ms | Phabricator | 0.16 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 23 | 186ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 24 | 189ms | Img | - | `https://img.shields.io` | 通用代理 |
| 25 | 192ms | Gh | 2.75 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 26 | 192ms | Github | 1.8 MB/s | `https://github.880824.xyz` | 通用代理 |
| 27 | 192ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 28 | 196ms | Git | 2.73 MB/s | `https://git.820828.xyz` | 通用代理 |
| 29 | 198ms | Sub | 0.37 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 30 | 199ms | Twitter | 1.03 MB/s | `https://twitter.com` | 通用代理 |
| 31 | 200ms | GH Monlor | 1.59 MB/s | `https://gh.monlor.com` | 通用代理 |
| 32 | 202ms | Github | 2.88 MB/s | `https://github.788787.xyz` | 通用代理 |
| 33 | 204ms | Openttd | 0.02 MB/s | `https://openttd.org` | 通用代理 |
| 34 | 206ms | Github | 2.4 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 35 | 208ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 36 | 208ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 37 | 211ms | Axios-http | 1.55 MB/s | `https://axios-http.com` | 通用代理 |
| 38 | 213ms | Gh | 3.12 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 39 | 213ms | Ghproxy | 3.26 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 40 | 213ms | Git | 3.48 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 41 | 216ms | Ampcode | 0.26 MB/s | `https://ampcode.com` | 通用代理 |
| 42 | 218ms | Hopp | 0.05 MB/s | `https://hopp.sh` | 通用代理 |
| 43 | 218ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 44 | 221ms | Gp | 2.33 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 45 | 225ms | Cursor | 0.86 MB/s | `https://cursor.com` | 通用代理 |
| 46 | 226ms | GH-Proxy Org | 1.18 MB/s | `https://gh-proxy.org` | 通用代理 |
| 47 | 229ms | Github | 2.39 MB/s | `https://github.ihnic.com` | 通用代理 |
| 48 | 231ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 49 | 233ms | Coreos | 4.75 MB/s | `https://coreos.com` | 通用代理 |
| 50 | 234ms | Ghproxy | 2.35 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 51 | 234ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 52 | 238ms | Radio-browser | 0.06 MB/s | `https://radio-browser.info` | 通用代理 |
| 53 | 238ms | Tvv | 2.23 MB/s | `https://tvv.tw` | 通用代理 |
| 54 | 239ms | Training | 0.2 MB/s | `https://training.ti.com` | 通用代理 |
| 55 | 240ms | Kuroutoshikou | 1.18 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 56 | 242ms | Gh | 1.81 MB/s | `https://gh.idayer.com` | 通用代理 |
| 57 | 245ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 58 | 249ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 59 | 258ms | Gh | 2.28 MB/s | `https://gh.1k.ink` | 通用代理 |
| 60 | 260ms | FastGit CC | 1.36 MB/s | `https://fastgit.cc` | 通用代理 |
| 61 | 261ms | Aomedia | 0.42 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 62 | 265ms | Ghproxy | 0.58 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 63 | 265ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 64 | 266ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 65 | 268ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 66 | 273ms | Nisar | 0.85 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 67 | 275ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 68 | 280ms | Contrib | 0.42 MB/s | `https://contrib.rocks` | 通用代理 |
| 69 | 283ms | Github | 0.55 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 70 | 284ms | Gh | 0.54 MB/s | `https://gh.padao.fun` | 通用代理 |
| 71 | 311ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 72 | 313ms | Code | 2.21 MB/s | `https://code.claude.com` | 通用代理 |
| 73 | 314ms | Support | 0.48 MB/s | `https://support.apple.com` | 通用代理 |
| 74 | 316ms | Kenyu | 2.41 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 75 | 316ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 76 | 317ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 77 | 317ms | Ggg | 2.09 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 78 | 318ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 79 | 323ms | CrashMC CDN | 1.52 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 80 | 335ms | Agoramarket | 0.55 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 81 | 335ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 82 | 345ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 83 | 346ms | Api | 0.05 MB/s | `https://api.solov.cc` | 通用代理 |
| 84 | 355ms | Gh | 0.74 MB/s | `https://gh.noki.icu` | 通用代理 |
| 85 | 356ms | 30006000 | 0.42 MB/s | `https://30006000.xyz` | 通用代理 |
| 86 | 361ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 87 | 363ms | Bailian | 0.05 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 88 | 364ms | Steamcommunity | 0.13 MB/s | `https://steamcommunity.com` | 通用代理 |
| 89 | 364ms | Store | 1.63 MB/s | `https://store.steampowered.com` | 通用代理 |
| 90 | 376ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 91 | 382ms | Github | 2.82 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 92 | 384ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 93 | 389ms | GHFast | 0.2 MB/s | `https://ghfast.top` | 通用代理 |
| 94 | 391ms | Gh | 0.59 MB/s | `https://gh.39.al` | 通用代理 |
| 95 | 398ms | Aps | 0.07 MB/s | `https://aps.com` | 通用代理 |
| 96 | 398ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 97 | 399ms | Github | 2.83 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 98 | 411ms | Bseindia | 0.04 MB/s | `https://bseindia.com` | 通用代理 |
| 99 | 429ms | Msdn | 0.03 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 100 | 434ms | Getgit | 2.62 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 101 | 436ms | GH Nxnow | 0.6 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 102 | 436ms | GHProxy Net | 0.27 MB/s | `https://ghproxy.net` | 通用代理 |
| 103 | 442ms | Hk | 1.41 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 104 | 445ms | Ark | 0.44 MB/s | `https://ark.intel.com` | 通用代理 |
| 105 | 449ms | Github | 2.29 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 106 | 460ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 107 | 469ms | Aosmd | 0.35 MB/s | `https://aosmd.com` | 通用代理 |
| 108 | 495ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 109 | 507ms | Your-domain | 0.04 MB/s | `https://your-domain.com` | 通用代理 |
| 110 | 509ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 111 | 521ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 112 | 532ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 113 | 535ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 114 | 538ms | Gh | - | `https://gh.llkk.cc` | 通用代理 |
| 115 | 545ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 116 | 557ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 117 | 563ms | YYLX Git | 0.2 MB/s | `https://git.yylx.win` | 通用代理 |
| 118 | 590ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 119 | 592ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 120 | 608ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 121 | 647ms | Github | 0.34 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 122 | 656ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 123 | 662ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 124 | 678ms | Docs | 0.28 MB/s | `https://docs.transifex.com` | 通用代理 |
| 125 | 712ms | GHFile Geekertao | - | `https://ghfile.geekertao.top` | 通用代理 |
| 126 | 750ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 127 | 765ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 128 | 775ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 129 | 781ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 130 | 799ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 131 | 802ms | Ednovas Mirror | 0.44 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 132 | 835ms | Fastfile | 2.06 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 133 | 850ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 134 | 867ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 135 | 870ms | Gh | - | `https://gh.dpik.top` | 通用代理 |
| 136 | 880ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 137 | 967ms | Mimo | 0.15 MB/s | `https://mimo.mi.com` | 通用代理 |
| 138 | 1005ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 139 | 1046ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 140 | 1085ms | Web | - | `https://web.4399.com` | 通用代理 |
| 141 | 1124ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 142 | 1141ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 143 | 1214ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 144 | 1264ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 145 | 1290ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 146 | 1300ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 147 | 1311ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 148 | 1353ms | Ghproxy | 0.23 MB/s | `https://ghproxy.cc` | 通用代理 |
| 149 | 1451ms | Cf | 0.21 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 150 | 1592ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 151 | 1691ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 152 | 1704ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 153 | 1830ms | Github | 0.13 MB/s | `https://github.chenc.dev` | 通用代理 |
| 154 | 2138ms | Img | - | `https://img.ink` | 通用代理 |
| 155 | 2263ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 156 | 3002ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 157 | 3244ms | Gh | 0.07 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 158 | 3548ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 159 | 3993ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 160 | 4141ms | GitClone | - | `https://gitclone.com` | Clone 专用 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Npee Down (`down-npee-cn`) | 13 次 |
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 20 次 |
| G (`g-blfrp-cn`) | 1 次 |
| Gh (`gh-halonice-com`) | 12 次 |
| Ghproxy (`ghproxy-mirror-skybyte-me`) | 1 次 |
| Git (`git-669966-xyz`) | 2 次 |
| Git (`git-tangbai-cc`) | 13 次 |
| Proxy (`proxy-yaoyaoling-net`) | 1 次 |
| Mirror (`mirror-houlang-cloud`) | 7 次 |
| Proxy (`proxy-vvvv-ee`) | 2 次 |
| 5555 (`5555-cab`) | 3 次 |
| Status (`status-leez-tech`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 165 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **172** | |

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
