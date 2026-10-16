# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-16T16:09:55Z**，每 6 小时刷新一次。当前 ✅ **109** 在线 / ⚠️ **10** 不稳定 / ⚰️ **42** 已失效归档。

## 核心特性

- **119 个节点**，4 大分类，全部经过测速验证
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
| 2 | 77ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 87ms | Microsoftedge | 0.61 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 4 | 101ms | Githubstatus | 1.14 MB/s | `https://githubstatus.com` | 通用代理 |
| 5 | 119ms | Thumb | 1.07 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 6 | 125ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 7 | 141ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 8 | 156ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 9 | 162ms | Training | 0.12 MB/s | `https://training.ti.com` | 通用代理 |
| 10 | 168ms | GH Monlor | 0.77 MB/s | `https://gh.monlor.com` | 通用代理 |
| 11 | 170ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 12 | 170ms | Github | 1.36 MB/s | `https://github.880824.xyz` | 通用代理 |
| 13 | 177ms | GH-Proxy | 1.01 MB/s | `https://gh-proxy.com` | 通用代理 |
| 14 | 182ms | Github | 1.34 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 15 | 184ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 16 | 184ms | Img | - | `https://img.shields.io` | 通用代理 |
| 17 | 190ms | Github | 1.31 MB/s | `https://github.788787.xyz` | 通用代理 |
| 18 | 190ms | Gp | 1.31 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 19 | 190ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 20 | 192ms | Git | 1.37 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 21 | 204ms | Gh | 1.18 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 22 | 210ms | Gh | 1.16 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 23 | 210ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 24 | 212ms | Gh | 1.33 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 25 | 214ms | Cursor | 0.44 MB/s | `https://cursor.com` | 通用代理 |
| 26 | 216ms | Ghproxy | 0.76 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 27 | 218ms | Axios-http | 0.32 MB/s | `https://axios-http.com` | 通用代理 |
| 28 | 219ms | Git | 1.4 MB/s | `https://git.820828.xyz` | 通用代理 |
| 29 | 224ms | Gh | 0.71 MB/s | `https://gh.halonice.com` | 通用代理 |
| 30 | 230ms | Sub | 0.14 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 31 | 231ms | Api | 0.11 MB/s | `https://api.solov.cc` | 通用代理 |
| 32 | 232ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 33 | 237ms | Ampcode | 0.17 MB/s | `https://ampcode.com` | 通用代理 |
| 34 | 241ms | Github | 1.4 MB/s | `https://github.ihnic.com` | 通用代理 |
| 35 | 244ms | Oem | - | `https://oem.re` | 通用代理 |
| 36 | 246ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 37 | 248ms | Ghproxy | 1.34 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 38 | 251ms | Gh | 0.51 MB/s | `https://gh.39.al` | 通用代理 |
| 39 | 251ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 40 | 253ms | FastGit CC | 0.85 MB/s | `https://fastgit.cc` | 通用代理 |
| 41 | 254ms | Github | 0.54 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 42 | 256ms | Gh | 1.33 MB/s | `https://gh.1k.ink` | 通用代理 |
| 43 | 259ms | Tvv | 1.36 MB/s | `https://tvv.tw` | 通用代理 |
| 44 | 267ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 45 | 292ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 46 | 294ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 47 | 297ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 48 | 306ms | 30006000 | 0.71 MB/s | `https://30006000.xyz` | 通用代理 |
| 49 | 306ms | Npee Down | 0.03 MB/s | `https://down.npee.cn` | 通用代理 |
| 50 | 311ms | GH-Proxy YGXZ | 0.02 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 51 | 322ms | Hk | 0.42 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 52 | 323ms | CrashMC CDN | 0.92 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 53 | 334ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 54 | 336ms | Gh | 0.48 MB/s | `https://gh.padao.fun` | 通用代理 |
| 55 | 355ms | Kenyu | 1.45 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 56 | 357ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 57 | 366ms | GH Nxnow | 0.68 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 58 | 372ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 59 | 372ms | Proxy | 1.27 MB/s | `https://proxy.vvvv.ee` | 通用代理 |
| 60 | 391ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 61 | 401ms | Github | 1.22 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 62 | 406ms | GHProxy Net | 0.18 MB/s | `https://ghproxy.net` | 通用代理 |
| 63 | 425ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 64 | 437ms | Msdn | 0.03 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 65 | 439ms | Ednovas Mirror | 0.58 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 66 | 456ms | Gh | 0.75 MB/s | `https://gh.noki.icu` | 通用代理 |
| 67 | 496ms | Aosmd | 0.16 MB/s | `https://aosmd.com` | 通用代理 |
| 68 | 510ms | Ygdj7 | - | `https://ygdj7.com` | 通用代理 |
| 69 | 511ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 70 | 566ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 71 | 589ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 72 | 596ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 73 | 613ms | GH-Proxy Org | 0.88 MB/s | `https://gh-proxy.org` | 通用代理 |
| 74 | 615ms | Github | 1.31 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 75 | 630ms | Ghproxy | 0.22 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 76 | 664ms | Your-domain | 0.01 MB/s | `https://your-domain.com` | 通用代理 |
| 77 | 683ms | YYLX Git | 0.53 MB/s | `https://git.yylx.win` | 通用代理 |
| 78 | 700ms | GHFile Geekertao | 0.33 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 79 | 723ms | Github | 0.3 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 80 | 729ms | Getgit | 1.33 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 81 | 745ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 82 | 753ms | GHFast | 0.57 MB/s | `https://ghfast.top` | 通用代理 |
| 83 | 779ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 84 | 786ms | Fastfile | 1.31 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 85 | 812ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 86 | 814ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 87 | 845ms | Git | 0.15 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 88 | 858ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 89 | 924ms | Github | 1.6 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 90 | 968ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 91 | 1034ms | Web | - | `https://web.4399.com` | 通用代理 |
| 92 | 1120ms | Ggg | 1.46 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 93 | 1251ms | Gh | 0.2 MB/s | `https://gh.dpik.top` | 通用代理 |
| 94 | 1272ms | Github | 0.11 MB/s | `https://github.chenc.dev` | 通用代理 |
| 95 | 1298ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 96 | 1315ms | Ghproxy | 0.22 MB/s | `https://ghproxy.cc` | 通用代理 |
| 97 | 1323ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 98 | 1390ms | SLink | - | `https://slink.ltd` | 通用代理 |
| 99 | 1511ms | Cf | 0.25 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 100 | 1811ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 101 | 2045ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 102 | 2110ms | Img | - | `https://img.ink` | 通用代理 |
| 103 | 2205ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 104 | 2618ms | G | 0.14 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 105 | 2784ms | Ghproxy | 0.06 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 106 | 2950ms | Gh | 0.09 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 107 | 3389ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 108 | 6186ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 109 | 9672ms | 5555 | 0.03 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（10 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GH ZWY (`gh-zwy-one`) | 26 次 |
| GitClone (`gitclone-com`) | 2 次 |
| Gh (`gh-ddlc-top`) | 13 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| ghproxy.homeboyc.cn (`ghproxy-homeboyc-cn`) | 26 次 |
| toolwa.com/github (`toolwa-com-github`) | 26 次 |
| github.akams.cn (`github-akams-cn`) | 26 次 |
| Ghproxy (`ghproxy-imciel-com`) | 6 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Github (`github-dpik-top`) | 13 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 112 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **119** | |

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
