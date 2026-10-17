# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-17T15:01:50Z**，每 6 小时刷新一次。当前 ✅ **124** 在线 / ⚠️ **5** 不稳定 / ⚰️ **46** 已失效归档。

## 核心特性

- **129 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 70ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 2 | 79ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 80ms | Microsoftedge | 0.35 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 4 | 84ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 5 | 85ms | Linkedin | 0.13 MB/s | `https://linkedin.com` | 通用代理 |
| 6 | 88ms | Githubstatus | 4.49 MB/s | `https://githubstatus.com` | 通用代理 |
| 7 | 103ms | App | 0.18 MB/s | `https://app.netlify.com` | 通用代理 |
| 8 | 104ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 9 | 117ms | Thumb | 5.11 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 10 | 127ms | Goreportcard | 0.04 MB/s | `https://goreportcard.com` | 通用代理 |
| 11 | 140ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 12 | 163ms | GH Monlor | - | `https://gh.monlor.com` | 通用代理 |
| 13 | 166ms | Training | 0.2 MB/s | `https://training.ti.com` | 通用代理 |
| 14 | 167ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 15 | 172ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 16 | 175ms | Github | 4.38 MB/s | `https://github.880824.xyz` | 通用代理 |
| 17 | 179ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 18 | 183ms | GH-Proxy | - | `https://gh-proxy.com` | 通用代理 |
| 19 | 184ms | Gp | 3.12 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 20 | 187ms | Github | 3.06 MB/s | `https://github.788787.xyz` | 通用代理 |
| 21 | 187ms | Nisar | 1.83 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 22 | 189ms | Gh | 1.45 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 23 | 191ms | Github | 4.25 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 24 | 191ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 25 | 195ms | Img | - | `https://img.shields.io` | 通用代理 |
| 26 | 198ms | Git | 2.42 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 27 | 200ms | Git | 3.06 MB/s | `https://git.820828.xyz` | 通用代理 |
| 28 | 205ms | Gh | 0.12 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 29 | 205ms | Ghproxy | 1.96 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 30 | 210ms | Axios-http | 1.62 MB/s | `https://axios-http.com` | 通用代理 |
| 31 | 210ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 32 | 216ms | Gh | 0.08 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 33 | 218ms | Sub | 0.2 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 34 | 219ms | Cursor | 0.59 MB/s | `https://cursor.com` | 通用代理 |
| 35 | 226ms | Ampcode | 0.16 MB/s | `https://ampcode.com` | 通用代理 |
| 36 | 229ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 37 | 233ms | Github | 1.41 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 38 | 235ms | Github | 4.53 MB/s | `https://github.ihnic.com` | 通用代理 |
| 39 | 236ms | Gh | 0.12 MB/s | `https://gh.halonice.com` | 通用代理 |
| 40 | 238ms | FastGit CC | - | `https://fastgit.cc` | 通用代理 |
| 41 | 247ms | Ghproxy | 0.34 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 42 | 247ms | Open | 0.03 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 43 | 259ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 44 | 260ms | Api | 0.13 MB/s | `https://api.solov.cc` | 通用代理 |
| 45 | 263ms | Aps | 0.08 MB/s | `https://aps.com` | 通用代理 |
| 46 | 265ms | Tvv | 6.07 MB/s | `https://tvv.tw` | 通用代理 |
| 47 | 267ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 48 | 272ms | Gh | 0.12 MB/s | `https://gh.1k.ink` | 通用代理 |
| 49 | 275ms | Gh | 0.22 MB/s | `https://gh.padao.fun` | 通用代理 |
| 50 | 279ms | GH-Proxy Org | - | `https://gh-proxy.org` | 通用代理 |
| 51 | 285ms | GH-Proxy YGXZ | 0.07 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 52 | 289ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 53 | 298ms | Bailian | 0.81 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 54 | 301ms | CrashMC CDN | - | `https://cdn.crashmc.com` | 通用代理 |
| 55 | 304ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 56 | 306ms | Npee Down | 0.03 MB/s | `https://down.npee.cn` | 通用代理 |
| 57 | 307ms | 30006000 | - | `https://30006000.xyz` | 通用代理 |
| 58 | 307ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 59 | 312ms | Kenyu | 2.86 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 60 | 315ms | GHFast | - | `https://ghfast.top` | 通用代理 |
| 61 | 326ms | Oem | - | `https://oem.re` | 通用代理 |
| 62 | 339ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 63 | 342ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 64 | 343ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 65 | 350ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 66 | 361ms | Github | 4.9 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 67 | 374ms | Hk | - | `https://hk.gh-proxy.com` | 通用代理 |
| 68 | 375ms | Gh | 0.52 MB/s | `https://gh.noki.icu` | 通用代理 |
| 69 | 383ms | Github | 3.37 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 70 | 401ms | Github | 3.77 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 71 | 402ms | Ednovas Mirror | 0.57 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 72 | 405ms | Ggg | 3.19 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 73 | 421ms | Msdn | 0.05 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 74 | 437ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 75 | 440ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 76 | 445ms | Getgit | - | `https://getgit.love8yun.eu.org` | 通用代理 |
| 77 | 446ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 78 | 489ms | YYLX Git | 1.16 MB/s | `https://git.yylx.win` | 通用代理 |
| 79 | 493ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 80 | 509ms | Ygdj7 | 0.05 MB/s | `https://ygdj7.com` | 通用代理 |
| 81 | 525ms | Proxy | 1.38 MB/s | `https://proxy.vvvv.ee` | 通用代理 |
| 82 | 535ms | Aosmd | 0.1 MB/s | `https://aosmd.com` | 通用代理 |
| 83 | 550ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 84 | 610ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 85 | 657ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 86 | 679ms | Ghproxy | 0.32 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 87 | 685ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 88 | 710ms | Github | 0.32 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 89 | 739ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 90 | 760ms | Fastfile | 1.58 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 91 | 763ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 92 | 772ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 93 | 788ms | GHFile Geekertao | - | `https://ghfile.geekertao.top` | 通用代理 |
| 94 | 838ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 95 | 847ms | Git | 0.26 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 96 | 860ms | Gh | - | `https://gh.39.al` | 通用代理 |
| 97 | 863ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 98 | 880ms | Mimo | 0.21 MB/s | `https://mimo.mi.com` | 通用代理 |
| 99 | 895ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 100 | 905ms | Your-domain | 0.08 MB/s | `https://your-domain.com` | 通用代理 |
| 101 | 913ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 102 | 976ms | Gh | 1.01 MB/s | `https://gh.dpik.top` | 通用代理 |
| 103 | 1039ms | Web | - | `https://web.4399.com` | 通用代理 |
| 104 | 1042ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 105 | 1079ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 106 | 1253ms | Github | 0.12 MB/s | `https://github.chenc.dev` | 通用代理 |
| 107 | 1313ms | Ghproxy | 0.29 MB/s | `https://ghproxy.cc` | 通用代理 |
| 108 | 1330ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 109 | 1354ms | SLink | 0.08 MB/s | `https://slink.ltd` | 通用代理 |
| 110 | 1429ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 111 | 1472ms | Cf | 0.08 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 112 | 1522ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 113 | 1580ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 114 | 1625ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 115 | 1883ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 116 | 2172ms | Img | - | `https://img.ink` | 通用代理 |
| 117 | 2223ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 118 | 2610ms | G | 0.22 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 119 | 2714ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 120 | 2877ms | Ghproxy | 0.04 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 121 | 3023ms | Gh | 0.09 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 122 | 3487ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 123 | 6417ms | Proxy | - | `https://proxy.yaoyaoling.net` | 通用代理 |
| 124 | 8675ms | 5555 | 0.07 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（5 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Gh (`gh-ddlc-top`) | 17 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Ghproxy (`ghproxy-imciel-com`) | 10 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Github (`github-dpik-top`) | 17 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 122 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **129** | |

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
