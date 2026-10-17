# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-17T03:08:16Z**，每 6 小时刷新一次。当前 ✅ **119** 在线 / ⚠️ **7** 不稳定 / ⚰️ **46** 已失效归档。

## 核心特性

- **126 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 49ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 2 | 64ms | Linkedin | 0.13 MB/s | `https://linkedin.com` | 通用代理 |
| 3 | 77ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 4 | 83ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 5 | 85ms | Microsoftedge | 0.62 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 6 | 89ms | App | 0.1 MB/s | `https://app.netlify.com` | 通用代理 |
| 7 | 97ms | Githubstatus | 0.85 MB/s | `https://githubstatus.com` | 通用代理 |
| 8 | 100ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 9 | 118ms | Thumb | 1.02 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 10 | 123ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 11 | 143ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 12 | 149ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 13 | 161ms | GH-Proxy | 1.09 MB/s | `https://gh-proxy.com` | 通用代理 |
| 14 | 162ms | Training | 0.14 MB/s | `https://training.ti.com` | 通用代理 |
| 15 | 167ms | GH Monlor | 0.83 MB/s | `https://gh.monlor.com` | 通用代理 |
| 16 | 174ms | Img | - | `https://img.shields.io` | 通用代理 |
| 17 | 180ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 18 | 186ms | Github | 1.56 MB/s | `https://github.880824.xyz` | 通用代理 |
| 19 | 189ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 20 | 189ms | Github | 1.69 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 21 | 193ms | Gp | 1.71 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 22 | 199ms | Github | 1.66 MB/s | `https://github.788787.xyz` | 通用代理 |
| 23 | 201ms | Git | 1.48 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 24 | 201ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 25 | 205ms | Gh | 1.57 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 26 | 208ms | Axios-http | 0.39 MB/s | `https://axios-http.com` | 通用代理 |
| 27 | 212ms | Gh | 1.45 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 28 | 213ms | Cursor | 0.42 MB/s | `https://cursor.com` | 通用代理 |
| 29 | 215ms | Ghproxy | - | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 30 | 221ms | Sub | 0.15 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 31 | 222ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 32 | 223ms | Gh | 1.62 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 33 | 224ms | Git | 1.23 MB/s | `https://git.820828.xyz` | 通用代理 |
| 34 | 232ms | Gh | - | `https://gh.halonice.com` | 通用代理 |
| 35 | 239ms | Ampcode | 0.17 MB/s | `https://ampcode.com` | 通用代理 |
| 36 | 247ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 37 | 250ms | Github | - | `https://github.cnxiaobai.com` | 通用代理 |
| 38 | 251ms | Gh | 1.34 MB/s | `https://gh.1k.ink` | 通用代理 |
| 39 | 252ms | FastGit CC | 1.2 MB/s | `https://fastgit.cc` | 通用代理 |
| 40 | 252ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 41 | 254ms | Open | 0.01 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 42 | 255ms | Ghproxy | 1.27 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 43 | 255ms | Github | 1.17 MB/s | `https://github.ihnic.com` | 通用代理 |
| 44 | 259ms | Nisar | 0.72 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 45 | 260ms | Gh | 1.51 MB/s | `https://gh.idayer.com` | 通用代理 |
| 46 | 266ms | Tvv | 1.35 MB/s | `https://tvv.tw` | 通用代理 |
| 47 | 293ms | GH-Proxy Org | 1.19 MB/s | `https://gh-proxy.org` | 通用代理 |
| 48 | 304ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 49 | 305ms | Npee Down | 0.02 MB/s | `https://down.npee.cn` | 通用代理 |
| 50 | 315ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 51 | 316ms | GH-Proxy YGXZ | 0.02 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 52 | 320ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 53 | 322ms | 30006000 | - | `https://30006000.xyz` | 通用代理 |
| 54 | 322ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 55 | 323ms | GH Nxnow | 0.77 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 56 | 325ms | Api | 0.12 MB/s | `https://api.solov.cc` | 通用代理 |
| 57 | 329ms | Gh | - | `https://gh.padao.fun` | 通用代理 |
| 58 | 330ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 59 | 335ms | CrashMC CDN | 1.12 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 60 | 339ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 61 | 341ms | Kenyu | 1.3 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 62 | 344ms | Oem | - | `https://oem.re` | 通用代理 |
| 63 | 351ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 64 | 362ms | Hk | - | `https://hk.gh-proxy.com` | 通用代理 |
| 65 | 374ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 66 | 382ms | Gh | 0.85 MB/s | `https://gh.noki.icu` | 通用代理 |
| 67 | 384ms | Github | 1.36 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 68 | 406ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 69 | 411ms | Github | 1.43 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 70 | 411ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 71 | 420ms | Ggg | 1.47 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 72 | 423ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 73 | 424ms | Bailian | 0.06 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 74 | 426ms | Getgit | 1.28 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 75 | 435ms | Gh | - | `https://gh.39.al` | 通用代理 |
| 76 | 438ms | Ednovas Mirror | - | `https://github.ednovas.xyz` | 通用代理 |
| 77 | 445ms | Github | 1.47 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 78 | 496ms | Aosmd | 0.2 MB/s | `https://aosmd.com` | 通用代理 |
| 79 | 511ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 80 | 525ms | Ygdj7 | 0.05 MB/s | `https://ygdj7.com` | 通用代理 |
| 81 | 548ms | YYLX Git | - | `https://git.yylx.win` | 通用代理 |
| 82 | 548ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 83 | 563ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 84 | 568ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 85 | 580ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 86 | 647ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 87 | 694ms | Ghproxy | 0.21 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 88 | 737ms | Github | 0.07 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 89 | 738ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 90 | 754ms | GHFast | - | `https://ghfast.top` | 通用代理 |
| 91 | 769ms | GHFile Geekertao | 0.34 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 92 | 784ms | Fastfile | 0.82 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 93 | 810ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 94 | 831ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 95 | 834ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 96 | 867ms | Git | - | `https://git.tangbai.cc` | 通用代理 |
| 97 | 936ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 98 | 955ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 99 | 999ms | Gh | 0.75 MB/s | `https://gh.dpik.top` | 通用代理 |
| 100 | 1010ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 101 | 1055ms | Web | - | `https://web.4399.com` | 通用代理 |
| 102 | 1063ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 103 | 1194ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 104 | 1280ms | Github | - | `https://github.chenc.dev` | 通用代理 |
| 105 | 1299ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 106 | 1344ms | Ghproxy | 0.07 MB/s | `https://ghproxy.cc` | 通用代理 |
| 107 | 1355ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 108 | 1431ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 109 | 1530ms | Cf | - | `https://cf.ghproxy.cc` | 通用代理 |
| 110 | 1623ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 111 | 1820ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 112 | 1886ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 113 | 1953ms | Img | - | `https://img.ink` | 通用代理 |
| 114 | 2202ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 115 | 2452ms | Ghproxy | 0.1 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 116 | 2712ms | G | - | `https://g.blfrp.cn` | 通用代理 |
| 117 | 2979ms | Gh | 0.11 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 118 | 6187ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 119 | 8626ms | 5555 | 0.03 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（7 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHProxy MonkeyRay (`ghproxy-monkeyray-net`) | 1 次 |
| GitClone (`gitclone-com`) | 4 次 |
| Gh (`gh-ddlc-top`) | 15 次 |
| Ghproxy (`ghproxy-imciel-com`) | 8 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Github (`github-dpik-top`) | 15 次 |
| Proxy (`proxy-vvvv-ee`) | 2 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 119 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **126** | |

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
