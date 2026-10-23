# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-23T21:03:30Z**，每 6 小时刷新一次。当前 ✅ **169** 在线 / ⚠️ **8** 不稳定 / ⚰️ **48** 已失效归档。

## 核心特性

- **177 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 54ms | Microsoftedge | 0.65 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 72ms | Deno | 0.6 MB/s | `https://deno.com` | 通用代理 |
| 3 | 72ms | Linkedin | 0.16 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 78ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 86ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 6 | 92ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 7 | 97ms | X | 1.01 MB/s | `https://x.com` | 通用代理 |
| 8 | 98ms | App | 0.09 MB/s | `https://app.netlify.com` | 通用代理 |
| 9 | 100ms | Githubstatus | 1.04 MB/s | `https://githubstatus.com` | 通用代理 |
| 10 | 101ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 11 | 118ms | Wordpaper | 0.2 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 12 | 123ms | Thumb | 1.04 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 13 | 124ms | Zebrunner | 1.13 MB/s | `https://zebrunner.com` | 通用代理 |
| 14 | 126ms | Crypto-funding-arbitrage | 0.05 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 15 | 133ms | Resume-5lv | 0.11 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 16 | 134ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 17 | 137ms | Gitea-mirror | 0.49 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 18 | 138ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 19 | 139ms | Img | - | `https://img.shields.io` | 通用代理 |
| 20 | 147ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 21 | 149ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 22 | 155ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 23 | 161ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 24 | 172ms | GH-Proxy | 0.81 MB/s | `https://gh-proxy.com` | 通用代理 |
| 25 | 175ms | Phabricator | 0.06 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 26 | 186ms | Gh | 0.76 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 27 | 192ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 28 | 192ms | Git | 0.63 MB/s | `https://git.820828.xyz` | 通用代理 |
| 29 | 193ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 30 | 194ms | Github | 0.82 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 31 | 195ms | Github | 0.97 MB/s | `https://github.788787.xyz` | 通用代理 |
| 32 | 200ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 33 | 202ms | Twitter | 0.59 MB/s | `https://twitter.com` | 通用代理 |
| 34 | 205ms | GH Monlor | - | `https://gh.monlor.com` | 通用代理 |
| 35 | 205ms | Ghproxy | 0.84 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 36 | 206ms | Github | 1.03 MB/s | `https://github.880824.xyz` | 通用代理 |
| 37 | 207ms | Gh | 0.74 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 38 | 207ms | Sub | 0.12 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 39 | 209ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 40 | 209ms | Git | 0.96 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 41 | 212ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 42 | 213ms | Ampcode | 0.18 MB/s | `https://ampcode.com` | 通用代理 |
| 43 | 214ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 44 | 214ms | Openttd | 0.03 MB/s | `https://openttd.org` | 通用代理 |
| 45 | 218ms | Gp | 0.9 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 46 | 219ms | Cursor | 0.44 MB/s | `https://cursor.com` | 通用代理 |
| 47 | 224ms | Axios-http | 0.35 MB/s | `https://axios-http.com` | 通用代理 |
| 48 | 225ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 49 | 225ms | Training | 0.13 MB/s | `https://training.ti.com` | 通用代理 |
| 50 | 227ms | GH-Proxy Org | 0.82 MB/s | `https://gh-proxy.org` | 通用代理 |
| 51 | 227ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 52 | 228ms | Github | 0.76 MB/s | `https://github.ihnic.com` | 通用代理 |
| 53 | 228ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 54 | 231ms | Paypal | 0.02 MB/s | `https://paypal.com` | 通用代理 |
| 55 | 234ms | Gh | 1.05 MB/s | `https://gh.1k.ink` | 通用代理 |
| 56 | 237ms | App | 0.03 MB/s | `https://app.codecov.io` | 通用代理 |
| 57 | 248ms | Coreos | 1.17 MB/s | `https://coreos.com` | 通用代理 |
| 58 | 248ms | Ghproxy | 0.98 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 59 | 252ms | Tvv | 0.42 MB/s | `https://tvv.tw` | 通用代理 |
| 60 | 259ms | Ghproxy | 0.71 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 61 | 260ms | Aomedia | 0.23 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 62 | 261ms | Support | 0.37 MB/s | `https://support.apple.com` | 通用代理 |
| 63 | 263ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 64 | 263ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 65 | 265ms | FastGit CC | 0.81 MB/s | `https://fastgit.cc` | 通用代理 |
| 66 | 270ms | Contrib | 0.14 MB/s | `https://contrib.rocks` | 通用代理 |
| 67 | 270ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 68 | 274ms | Nisar | 0.75 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 69 | 287ms | Code | 1.75 MB/s | `https://code.claude.com` | 通用代理 |
| 70 | 287ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 71 | 291ms | Gh | 0.52 MB/s | `https://gh.padao.fun` | 通用代理 |
| 72 | 296ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 73 | 304ms | Ggg | 1.19 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 74 | 304ms | Kuroutoshikou | 0.74 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 75 | 305ms | Kenyu | 0.67 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 76 | 309ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 77 | 311ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 78 | 314ms | Github | 0.69 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 79 | 326ms | Agoramarket | 0.27 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 80 | 330ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 81 | 333ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 82 | 334ms | CrashMC CDN | 0.59 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 83 | 340ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 84 | 342ms | Steamcommunity | 0.08 MB/s | `https://steamcommunity.com` | 通用代理 |
| 85 | 345ms | Api | 0.07 MB/s | `https://api.solov.cc` | 通用代理 |
| 86 | 354ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 87 | 359ms | Oem | 0.01 MB/s | `https://oem.re` | 通用代理 |
| 88 | 364ms | 30006000 | 0.67 MB/s | `https://30006000.xyz` | 通用代理 |
| 89 | 369ms | Gh | 0.6 MB/s | `https://gh.noki.icu` | 通用代理 |
| 90 | 370ms | Bailian | 0.06 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 91 | 372ms | Store | 0.79 MB/s | `https://store.steampowered.com` | 通用代理 |
| 92 | 381ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 93 | 384ms | Github | 0.81 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 94 | 385ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 95 | 403ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 96 | 403ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 97 | 404ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 98 | 408ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 99 | 411ms | Github | 0.91 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 100 | 418ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 101 | 420ms | Tiktok | 0.11 MB/s | `https://tiktok.com` | 通用代理 |
| 102 | 424ms | Msdn | 0.01 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 103 | 432ms | Hk | - | `https://hk.gh-proxy.com` | 通用代理 |
| 104 | 436ms | GHFast | 0.5 MB/s | `https://ghfast.top` | 通用代理 |
| 105 | 440ms | Github | 1.03 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 106 | 445ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 107 | 447ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 108 | 451ms | Getgit | 1.11 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 109 | 455ms | GHProxy Net | 0.34 MB/s | `https://ghproxy.net` | 通用代理 |
| 110 | 459ms | Gh | 0.58 MB/s | `https://gh.39.al` | 通用代理 |
| 111 | 479ms | Ark | 0.37 MB/s | `https://ark.intel.com` | 通用代理 |
| 112 | 492ms | Aosmd | 0.11 MB/s | `https://aosmd.com` | 通用代理 |
| 113 | 506ms | Proxy | 0.96 MB/s | `https://proxy.vvvv.ee` | 通用代理 |
| 114 | 518ms | YYLX Git | 0.4 MB/s | `https://git.yylx.win` | 通用代理 |
| 115 | 522ms | Gh | 1.05 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 116 | 527ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 117 | 533ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 118 | 536ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 119 | 545ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 120 | 546ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 121 | 557ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 122 | 590ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 123 | 596ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 124 | 611ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 125 | 620ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 126 | 636ms | Ednovas Mirror | 0.33 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 127 | 648ms | Github | 0.36 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 128 | 659ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 129 | 687ms | Gh | 0.71 MB/s | `https://gh.dpik.top` | 通用代理 |
| 130 | 701ms | Docs | 0.18 MB/s | `https://docs.transifex.com` | 通用代理 |
| 131 | 716ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 132 | 731ms | Ghproxy | 0.2 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 133 | 762ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 134 | 774ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 135 | 779ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 136 | 790ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 137 | 849ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 138 | 868ms | Fastfile | 0.66 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 139 | 877ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 140 | 881ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 141 | 963ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 142 | 1004ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 143 | 1016ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 144 | 1049ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 145 | 1049ms | Web | - | `https://web.4399.com` | 通用代理 |
| 146 | 1142ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 147 | 1152ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 148 | 1175ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 149 | 1177ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 150 | 1238ms | Ghproxy | 0.21 MB/s | `https://ghproxy.cc` | 通用代理 |
| 151 | 1261ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 152 | 1295ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 153 | 1324ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 154 | 1455ms | Cf | 0.24 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 155 | 1669ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 156 | 1680ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 157 | 1698ms | Git | 0.2 MB/s | `https://git.669966.xyz` | 通用代理 |
| 158 | 1713ms | Github | 0.15 MB/s | `https://github.chenc.dev` | 通用代理 |
| 159 | 1726ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 160 | 2020ms | Ghproxy | 0.15 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 161 | 2164ms | G | 0.17 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 162 | 2264ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 163 | 2296ms | Img | - | `https://img.ink` | 通用代理 |
| 164 | 3000ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 165 | 3220ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 166 | 3428ms | Gh | - | `https://gh.b52m.cn` | 通用代理 |
| 167 | 3459ms | Wget | - | `https://wget.la` | 通用代理 |
| 168 | 3772ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 169 | 6166ms | Proxy | 0.03 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（8 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| Npee Down (`down-npee-cn`) | 16 次 |
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 23 次 |
| Gh (`gh-idayer-com`) | 3 次 |
| Gh (`gh-halonice-com`) | 15 次 |
| Git (`git-tangbai-cc`) | 16 次 |
| 5555 (`5555-cab`) | 6 次 |
| Doxygen (`doxygen-org`) | 2 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 170 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **177** | |

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
