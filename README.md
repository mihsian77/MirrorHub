# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-23T11:05:51Z**，每 6 小时刷新一次。当前 ✅ **164** 在线 / ⚠️ **10** 不稳定 / ⚰️ **48** 已失效归档。

## 核心特性

- **174 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 55ms | Microsoftedge | 1.26 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 70ms | Deno | 0.52 MB/s | `https://deno.com` | 通用代理 |
| 3 | 71ms | Linkedin | 0.46 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 76ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 91ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 6 | 94ms | X | 1.72 MB/s | `https://x.com` | 通用代理 |
| 7 | 95ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 8 | 96ms | Gitea-mirror | 1.15 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 9 | 98ms | App | 0.22 MB/s | `https://app.netlify.com` | 通用代理 |
| 10 | 101ms | Resume-5lv | 0.28 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 11 | 109ms | Githubstatus | 4.09 MB/s | `https://githubstatus.com` | 通用代理 |
| 12 | 110ms | Crypto-funding-arbitrage | 0.09 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 13 | 115ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 14 | 117ms | Wordpaper | 0.65 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 15 | 121ms | Zebrunner | 2.06 MB/s | `https://zebrunner.com` | 通用代理 |
| 16 | 123ms | Thumb | 6.09 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 17 | 131ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 18 | 139ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 19 | 155ms | Goreportcard | 0.08 MB/s | `https://goreportcard.com` | 通用代理 |
| 20 | 155ms | Phabricator | 0.12 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 21 | 155ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 22 | 157ms | GH-Proxy | - | `https://gh-proxy.com` | 通用代理 |
| 23 | 165ms | Img | - | `https://img.shields.io` | 通用代理 |
| 24 | 167ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 25 | 176ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 26 | 187ms | Gh | - | `https://gh.996986.xyz` | 通用代理 |
| 27 | 188ms | Git | - | `https://git.820828.xyz` | 通用代理 |
| 28 | 189ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 29 | 192ms | Github | - | `https://github.880824.xyz` | 通用代理 |
| 30 | 195ms | Github | - | `https://github.zzrbk.xyz` | 通用代理 |
| 31 | 196ms | Sub | 0.25 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 32 | 197ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 33 | 199ms | GH Monlor | - | `https://gh.monlor.com` | 通用代理 |
| 34 | 199ms | Github | - | `https://github.788787.xyz` | 通用代理 |
| 35 | 199ms | Twitter | 1.07 MB/s | `https://twitter.com` | 通用代理 |
| 36 | 206ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 37 | 207ms | Gh | - | `https://gh.198962.xyz` | 通用代理 |
| 38 | 208ms | Ghproxy | - | `https://ghproxy.imciel.com` | 通用代理 |
| 39 | 209ms | Git | - | `https://git.951959483.xyz` | 通用代理 |
| 40 | 210ms | GH-Proxy Org | - | `https://gh-proxy.org` | 通用代理 |
| 41 | 211ms | Openttd | 0.06 MB/s | `https://openttd.org` | 通用代理 |
| 42 | 215ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 43 | 217ms | Axios-http | 1.23 MB/s | `https://axios-http.com` | 通用代理 |
| 44 | 217ms | Gp | - | `https://gp.871201.xyz` | 通用代理 |
| 45 | 219ms | Ampcode | 0.34 MB/s | `https://ampcode.com` | 通用代理 |
| 46 | 221ms | Coreos | 2.37 MB/s | `https://coreos.com` | 通用代理 |
| 47 | 222ms | Github | - | `https://github.ihnic.com` | 通用代理 |
| 48 | 225ms | Cursor | 0.87 MB/s | `https://cursor.com` | 通用代理 |
| 49 | 226ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 50 | 227ms | Doxygen | 0.06 MB/s | `https://doxygen.org` | 通用代理 |
| 51 | 228ms | Kuroutoshikou | 0.87 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 52 | 228ms | Radio-browser | 0.04 MB/s | `https://radio-browser.info` | 通用代理 |
| 53 | 230ms | Training | 0.26 MB/s | `https://training.ti.com` | 通用代理 |
| 54 | 232ms | Paypal | 0.05 MB/s | `https://paypal.com` | 通用代理 |
| 55 | 234ms | Ghproxy | - | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 56 | 235ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 57 | 249ms | Tvv | - | `https://tvv.tw` | 通用代理 |
| 58 | 254ms | Gh | - | `https://gh.1k.ink` | 通用代理 |
| 59 | 255ms | FastGit CC | - | `https://fastgit.cc` | 通用代理 |
| 60 | 258ms | Aomedia | 0.39 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 61 | 260ms | Contrib | 0.53 MB/s | `https://contrib.rocks` | 通用代理 |
| 62 | 260ms | Ghproxy | - | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 63 | 262ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 64 | 263ms | Support | 0.83 MB/s | `https://support.apple.com` | 通用代理 |
| 65 | 264ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 66 | 265ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 67 | 266ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 68 | 272ms | Nisar | 0.84 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 69 | 285ms | Github | - | `https://github.cnxiaobai.com` | 通用代理 |
| 70 | 291ms | Gh | - | `https://gh.padao.fun` | 通用代理 |
| 71 | 293ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 72 | 295ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 73 | 306ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 74 | 309ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 75 | 311ms | Code | 3.26 MB/s | `https://code.claude.com` | 通用代理 |
| 76 | 316ms | Kenyu | - | `https://kenyu.ggff.net` | 通用代理 |
| 77 | 317ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 78 | 321ms | CrashMC CDN | - | `https://cdn.crashmc.com` | 通用代理 |
| 79 | 326ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 80 | 327ms | Agoramarket | 0.55 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 81 | 335ms | Ggg | - | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 82 | 342ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 83 | 345ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 84 | 347ms | Bailian | 0.05 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 85 | 353ms | Api | 0.06 MB/s | `https://api.solov.cc` | 通用代理 |
| 86 | 354ms | Store | 1.16 MB/s | `https://store.steampowered.com` | 通用代理 |
| 87 | 355ms | 30006000 | - | `https://30006000.xyz` | 通用代理 |
| 88 | 359ms | Aps | 0.04 MB/s | `https://aps.com` | 通用代理 |
| 89 | 360ms | Steamcommunity | 0.15 MB/s | `https://steamcommunity.com` | 通用代理 |
| 90 | 367ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 91 | 371ms | Gh | - | `https://gh.noki.icu` | 通用代理 |
| 92 | 372ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 93 | 382ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 94 | 385ms | GHFast | - | `https://ghfast.top` | 通用代理 |
| 95 | 407ms | Github | - | `https://github.crdz.eu.org` | 通用代理 |
| 96 | 409ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 97 | 414ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 98 | 416ms | Github | - | `https://github.1ms.xx.kg` | 通用代理 |
| 99 | 419ms | Hk | - | `https://hk.gh-proxy.com` | 通用代理 |
| 100 | 427ms | Github | - | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 101 | 431ms | Getgit | - | `https://getgit.love8yun.eu.org` | 通用代理 |
| 102 | 433ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 103 | 435ms | Gh | - | `https://gh.39.al` | 通用代理 |
| 104 | 436ms | Msdn | 0.16 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 105 | 445ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 106 | 445ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 107 | 470ms | Aosmd | 0.25 MB/s | `https://aosmd.com` | 通用代理 |
| 108 | 471ms | Ark | 0.64 MB/s | `https://ark.intel.com` | 通用代理 |
| 109 | 494ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 110 | 499ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 111 | 510ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 112 | 518ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 113 | 519ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 114 | 521ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 115 | 532ms | Gh | - | `https://gh.llkk.cc` | 通用代理 |
| 116 | 546ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 117 | 562ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 118 | 586ms | YYLX Git | - | `https://git.yylx.win` | 通用代理 |
| 119 | 589ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 120 | 590ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 121 | 618ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 122 | 624ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 123 | 646ms | Github | 0.42 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 124 | 661ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 125 | 670ms | Docs | 0.28 MB/s | `https://docs.transifex.com` | 通用代理 |
| 126 | 716ms | GHFile Geekertao | - | `https://ghfile.geekertao.top` | 通用代理 |
| 127 | 723ms | Ghproxy | 0.22 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 128 | 762ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 129 | 773ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 130 | 775ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 131 | 798ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 132 | 802ms | Ednovas Mirror | - | `https://github.ednovas.xyz` | 通用代理 |
| 133 | 819ms | Gh | - | `https://gh.dpik.top` | 通用代理 |
| 134 | 824ms | Fastfile | 0.07 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 135 | 850ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 136 | 858ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 137 | 909ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 138 | 962ms | Mimo | 0.15 MB/s | `https://mimo.mi.com` | 通用代理 |
| 139 | 1045ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 140 | 1052ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 141 | 1075ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 142 | 1101ms | Web | - | `https://web.4399.com` | 通用代理 |
| 143 | 1121ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 144 | 1152ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 145 | 1205ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 146 | 1272ms | Ghproxy | 0.23 MB/s | `https://ghproxy.cc` | 通用代理 |
| 147 | 1280ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 148 | 1298ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 149 | 1304ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 150 | 1311ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 151 | 1451ms | Cf | - | `https://cf.ghproxy.cc` | 通用代理 |
| 152 | 1524ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 153 | 1599ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 154 | 1727ms | I-qps | 0.02 MB/s | `https://i-qps.net` | 通用代理 |
| 155 | 1736ms | Github | - | `https://github.chenc.dev` | 通用代理 |
| 156 | 1769ms | Git | - | `https://git.669966.xyz` | 通用代理 |
| 157 | 2102ms | G | - | `https://g.blfrp.cn` | 通用代理 |
| 158 | 2215ms | Img | - | `https://img.ink` | 通用代理 |
| 159 | 2274ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 160 | 3010ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 161 | 3365ms | Gh | - | `https://gh.b52m.cn` | 通用代理 |
| 162 | 3465ms | Wget | - | `https://wget.la` | 通用代理 |
| 163 | 3580ms | GHProxy MonkeyRay | - | `https://ghproxy.monkeyray.net` | 通用代理 |
| 164 | 4138ms | GitClone | - | `https://gitclone.com` | Clone 专用 |


### ⚠️ 不稳定节点（10 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Npee Down (`down-npee-cn`) | 14 次 |
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 21 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Gh (`gh-halonice-com`) | 13 次 |
| Ghproxy (`ghproxy-mirror-skybyte-me`) | 2 次 |
| Git (`git-tangbai-cc`) | 14 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Mirror (`mirror-houlang-cloud`) | 8 次 |
| Proxy (`proxy-vvvv-ee`) | 3 次 |
| 5555 (`5555-cab`) | 4 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 167 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **174** | |

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
