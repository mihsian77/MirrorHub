# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-19T22:02:59Z**，每 6 小时刷新一次。当前 ✅ **144** 在线 / ⚠️ **7** 不稳定 / ⚰️ **46** 已失效归档。

## 核心特性

- **151 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 64ms | Microsoftedge | 0.34 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 75ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 76ms | Linkedin | 0.13 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 78ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 5 | 89ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 6 | 96ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 7 | 98ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 8 | 104ms | Githubstatus | 5.33 MB/s | `https://githubstatus.com` | 通用代理 |
| 9 | 115ms | App | 0.09 MB/s | `https://app.netlify.com` | 通用代理 |
| 10 | 127ms | Thumb | 4.55 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 11 | 133ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 12 | 141ms | Git | 2.66 MB/s | `https://git.820828.xyz` | 通用代理 |
| 13 | 146ms | Git | 3.22 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 14 | 151ms | Github | 2.19 MB/s | `https://github.880824.xyz` | 通用代理 |
| 15 | 152ms | Github | 2.8 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 16 | 157ms | Gp | 2.55 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 17 | 157ms | Training | 0.27 MB/s | `https://training.ti.com` | 通用代理 |
| 18 | 158ms | Deno | 0.22 MB/s | `https://deno.com` | 通用代理 |
| 19 | 159ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 20 | 163ms | Github | 2.21 MB/s | `https://github.ihnic.com` | 通用代理 |
| 21 | 164ms | Ghproxy | 1.68 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 22 | 168ms | Tvv | 1.47 MB/s | `https://tvv.tw` | 通用代理 |
| 23 | 171ms | Github | 1.56 MB/s | `https://github.788787.xyz` | 通用代理 |
| 24 | 175ms | Gh | 1.84 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 25 | 177ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 26 | 177ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 27 | 182ms | Gh | 1.01 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 28 | 185ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 29 | 185ms | GH Monlor | 1.69 MB/s | `https://gh.monlor.com` | 通用代理 |
| 30 | 185ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 31 | 187ms | Gh | 2.22 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 32 | 192ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 33 | 195ms | GH-Proxy | 0.92 MB/s | `https://gh-proxy.com` | 通用代理 |
| 34 | 196ms | Twitter | 1.17 MB/s | `https://twitter.com` | 通用代理 |
| 35 | 199ms | Api | 0.15 MB/s | `https://api.solov.cc` | 通用代理 |
| 36 | 201ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 37 | 204ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 38 | 207ms | Gh | 1.03 MB/s | `https://gh.halonice.com` | 通用代理 |
| 39 | 207ms | Img | - | `https://img.shields.io` | 通用代理 |
| 40 | 210ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 41 | 211ms | Ghproxy | 2.33 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 42 | 216ms | FastGit CC | 1.1 MB/s | `https://fastgit.cc` | 通用代理 |
| 43 | 216ms | Hopp | 0.06 MB/s | `https://hopp.sh` | 通用代理 |
| 44 | 217ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 45 | 218ms | Axios-http | 0.39 MB/s | `https://axios-http.com` | 通用代理 |
| 46 | 218ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 47 | 219ms | Paypal | 0.02 MB/s | `https://paypal.com` | 通用代理 |
| 48 | 223ms | Ampcode | 0.2 MB/s | `https://ampcode.com` | 通用代理 |
| 49 | 223ms | Ggg | 2.43 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 50 | 223ms | Ghproxy | 1.99 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 51 | 223ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 52 | 229ms | Kenyu | 2.6 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 53 | 230ms | Cursor | 0.56 MB/s | `https://cursor.com` | 通用代理 |
| 54 | 231ms | Sub | 0.26 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 55 | 236ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 56 | 242ms | CrashMC CDN | 1.05 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 57 | 242ms | Nisar | 1.6 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 58 | 246ms | GH-Proxy Org | 0.84 MB/s | `https://gh-proxy.org` | 通用代理 |
| 59 | 250ms | Github | 1.67 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 60 | 251ms | Gh | 1.25 MB/s | `https://gh.1k.ink` | 通用代理 |
| 61 | 261ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 62 | 268ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 63 | 283ms | Open | 0.03 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 64 | 291ms | Aomedia | 0.11 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 65 | 299ms | Npee Down | 0.03 MB/s | `https://down.npee.cn` | 通用代理 |
| 66 | 306ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 67 | 306ms | Ednovas Mirror | 0.58 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 68 | 311ms | Gh | 2.98 MB/s | `https://gh.padao.fun` | 通用代理 |
| 69 | 312ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 70 | 315ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 71 | 315ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 72 | 319ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 73 | 321ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 74 | 324ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 75 | 335ms | 30006000 | 1.91 MB/s | `https://30006000.xyz` | 通用代理 |
| 76 | 341ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 77 | 341ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 78 | 349ms | Bailian | 0.85 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 79 | 351ms | Hk | 1.22 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 80 | 361ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 81 | 371ms | Gh | 0.43 MB/s | `https://gh.noki.icu` | 通用代理 |
| 82 | 375ms | Getgit | 1.76 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 83 | 389ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 84 | 394ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 85 | 397ms | Steamcommunity | 0.23 MB/s | `https://steamcommunity.com` | 通用代理 |
| 86 | 402ms | GH Nxnow | 0.32 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 87 | 425ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 88 | 430ms | Github | 3.18 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 89 | 467ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 90 | 469ms | Github | 1.96 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 91 | 477ms | Aps | 0.18 MB/s | `https://aps.com` | 通用代理 |
| 92 | 478ms | Msdn | 0.06 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 93 | 512ms | GHFast | 0.74 MB/s | `https://ghfast.top` | 通用代理 |
| 94 | 513ms | Ygdj7 | 0.05 MB/s | `https://ygdj7.com` | 通用代理 |
| 95 | 545ms | Aosmd | 0.12 MB/s | `https://aosmd.com` | 通用代理 |
| 96 | 552ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 97 | 552ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 98 | 573ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 99 | 573ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 100 | 583ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 101 | 585ms | Github | 2.06 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 102 | 626ms | YYLX Git | 0.68 MB/s | `https://git.yylx.win` | 通用代理 |
| 103 | 644ms | Gh | 0.5 MB/s | `https://gh.dpik.top` | 通用代理 |
| 104 | 644ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 105 | 648ms | Fastfile | 2.51 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 106 | 657ms | Ghproxy | 0.38 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 107 | 672ms | Github | 0.54 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 108 | 720ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 109 | 766ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 110 | 768ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 111 | 777ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 112 | 777ms | Git | - | `https://git.tangbai.cc` | 通用代理 |
| 113 | 779ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 114 | 818ms | Your-domain | 0.09 MB/s | `https://your-domain.com` | 通用代理 |
| 115 | 826ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 116 | 843ms | SLink | 0.09 MB/s | `https://slink.ltd` | 通用代理 |
| 117 | 845ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 118 | 845ms | Web | - | `https://web.4399.com` | 通用代理 |
| 119 | 907ms | Invent | 0.01 MB/s | `https://invent.kde.org` | 通用代理 |
| 120 | 928ms | Mimo | 0.2 MB/s | `https://mimo.mi.com` | 通用代理 |
| 121 | 930ms | Gh | 0.4 MB/s | `https://gh.39.al` | 通用代理 |
| 122 | 956ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 123 | 1152ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 124 | 1189ms | Ghproxy | 0.31 MB/s | `https://ghproxy.cc` | 通用代理 |
| 125 | 1209ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 126 | 1211ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 127 | 1249ms | Git | 0.09 MB/s | `https://git.669966.xyz` | 通用代理 |
| 128 | 1312ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 129 | 1321ms | Github | 0.17 MB/s | `https://github.chenc.dev` | 通用代理 |
| 130 | 1443ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 131 | 1564ms | Cf | 0.31 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 132 | 1567ms | G | 0.2 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 133 | 1608ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 134 | 1620ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 135 | 1639ms | Ghproxy | 1.31 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 136 | 1702ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 137 | 1962ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 138 | 2336ms | Img | - | `https://img.ink` | 通用代理 |
| 139 | 2632ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 140 | 3199ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 141 | 3860ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 142 | 4129ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 143 | 6189ms | Proxy | 0.04 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 144 | 7716ms | 5555 | 0.08 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（7 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHProxy Net (`ghproxy-net`) | 1 次 |
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 7 次 |
| Gh (`gh-ddlc-top`) | 25 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Gh (`gh-b52m-cn`) | 2 次 |
| Github (`github-dpik-top`) | 25 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 144 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **151** | |

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
