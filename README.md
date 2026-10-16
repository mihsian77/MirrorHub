# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-16T03:17:19Z**，每 6 小时刷新一次。当前 ✅ **109** 在线 / ⚠️ **8** 不稳定 / ⚰️ **42** 已失效归档。

## 核心特性

- **117 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 50ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 2 | 79ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 84ms | Microsoftedge | 0.15 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 4 | 97ms | Githubstatus | 0.92 MB/s | `https://githubstatus.com` | 通用代理 |
| 5 | 97ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 6 | 106ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 7 | 119ms | Thumb | 1.03 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 8 | 139ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 9 | 155ms | Training | 0.11 MB/s | `https://training.ti.com` | 通用代理 |
| 10 | 159ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 11 | 169ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 12 | 173ms | GH-Proxy | 0.98 MB/s | `https://gh-proxy.com` | 通用代理 |
| 13 | 174ms | GH Monlor | 1.23 MB/s | `https://gh.monlor.com` | 通用代理 |
| 14 | 181ms | Github | 1.33 MB/s | `https://github.880824.xyz` | 通用代理 |
| 15 | 188ms | Axios-http | 0.28 MB/s | `https://axios-http.com` | 通用代理 |
| 16 | 198ms | Github | 1.29 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 17 | 203ms | Github | 1.11 MB/s | `https://github.788787.xyz` | 通用代理 |
| 18 | 204ms | Git | 1.32 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 19 | 210ms | Cursor | 0.52 MB/s | `https://cursor.com` | 通用代理 |
| 20 | 210ms | Gp | 1.61 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 21 | 216ms | Sub | 0.14 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 22 | 223ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 23 | 224ms | Ghproxy | 0.63 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 24 | 226ms | Tvv | 1.2 MB/s | `https://tvv.tw` | 通用代理 |
| 25 | 228ms | Gh | 1.21 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 26 | 229ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 27 | 231ms | Gh | 1.48 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 28 | 232ms | Git | 1.09 MB/s | `https://git.820828.xyz` | 通用代理 |
| 29 | 236ms | Gh | 1.35 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 30 | 237ms | Ampcode | 0.1 MB/s | `https://ampcode.com` | 通用代理 |
| 31 | 237ms | Gh | 1.55 MB/s | `https://gh.idayer.com` | 通用代理 |
| 32 | 240ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 33 | 243ms | Gh | 0.58 MB/s | `https://gh.halonice.com` | 通用代理 |
| 34 | 247ms | Gh | 0.73 MB/s | `https://gh.39.al` | 通用代理 |
| 35 | 253ms | Github | 0.74 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 36 | 254ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 37 | 254ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 38 | 255ms | Img | - | `https://img.shields.io` | 通用代理 |
| 39 | 262ms | Ghproxy | 1.04 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 40 | 262ms | Github | 1.4 MB/s | `https://github.ihnic.com` | 通用代理 |
| 41 | 266ms | Gh | 1.46 MB/s | `https://gh.1k.ink` | 通用代理 |
| 42 | 275ms | 30006000 | 0.65 MB/s | `https://30006000.xyz` | 通用代理 |
| 43 | 282ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 44 | 286ms | Api | 0.07 MB/s | `https://api.solov.cc` | 通用代理 |
| 45 | 286ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 46 | 289ms | FastGit CC | 0.99 MB/s | `https://fastgit.cc` | 通用代理 |
| 47 | 312ms | Hk | 0.99 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 48 | 315ms | Npee Down | 0.03 MB/s | `https://down.npee.cn` | 通用代理 |
| 49 | 322ms | Aps | 0.05 MB/s | `https://aps.com` | 通用代理 |
| 50 | 324ms | GH-Proxy YGXZ | 0.02 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 51 | 328ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 52 | 336ms | Gh | 0.53 MB/s | `https://gh.padao.fun` | 通用代理 |
| 53 | 352ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 54 | 353ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 55 | 356ms | CrashMC CDN | 0.84 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 56 | 360ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 57 | 366ms | Kenyu | 1.51 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 58 | 388ms | Github | 1.54 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 59 | 393ms | GH Nxnow | 0.69 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 60 | 395ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 61 | 408ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 62 | 415ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 63 | 417ms | GHProxy Net | 0.14 MB/s | `https://ghproxy.net` | 通用代理 |
| 64 | 428ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 65 | 460ms | Gh | 0.86 MB/s | `https://gh.noki.icu` | 通用代理 |
| 66 | 486ms | Aosmd | 0.17 MB/s | `https://aosmd.com` | 通用代理 |
| 67 | 504ms | Ygdj7 | 0.02 MB/s | `https://ygdj7.com` | 通用代理 |
| 68 | 546ms | Ednovas Mirror | - | `https://github.ednovas.xyz` | 通用代理 |
| 69 | 559ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 70 | 573ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 71 | 600ms | Github | 0.18 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 72 | 612ms | GH-Proxy Org | 0.89 MB/s | `https://gh-proxy.org` | 通用代理 |
| 73 | 615ms | Github | 1.26 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 74 | 627ms | Your-domain | 0.04 MB/s | `https://your-domain.com` | 通用代理 |
| 75 | 637ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 76 | 642ms | Ghproxy | 0.22 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 77 | 653ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 78 | 660ms | YYLX Git | - | `https://git.yylx.win` | 通用代理 |
| 79 | 679ms | Getgit | 1.39 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 80 | 707ms | GHFile Geekertao | 0.27 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 81 | 745ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 82 | 789ms | Fastfile | 0.67 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 83 | 808ms | GHFast | 0.55 MB/s | `https://ghfast.top` | 通用代理 |
| 84 | 812ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 85 | 822ms | Git | - | `https://git.tangbai.cc` | 通用代理 |
| 86 | 831ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 87 | 885ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 88 | 889ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 89 | 893ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 90 | 906ms | Github | 1.07 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 91 | 1022ms | Web | - | `https://web.4399.com` | 通用代理 |
| 92 | 1087ms | Ggg | 1.37 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 93 | 1215ms | Gh | 0.34 MB/s | `https://gh.dpik.top` | 通用代理 |
| 94 | 1234ms | Github | 0.15 MB/s | `https://github.chenc.dev` | 通用代理 |
| 95 | 1299ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 96 | 1347ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 97 | 1353ms | Ghproxy | 0.25 MB/s | `https://ghproxy.cc` | 通用代理 |
| 98 | 1585ms | Cf | 0.21 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 99 | 1729ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 100 | 1792ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 101 | 2017ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 102 | 2140ms | Img | - | `https://img.ink` | 通用代理 |
| 103 | 2474ms | Wget | 0.03 MB/s | `https://wget.la` | 通用代理 |
| 104 | 2614ms | G | 0.02 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 105 | 3075ms | Gh | 0.09 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 106 | 3127ms | Ghproxy | 0.06 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 107 | 3392ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 108 | 6185ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 109 | 9658ms | 5555 | 0.05 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（8 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GH ZWY (`gh-zwy-one`) | 24 次 |
| Gh (`gh-ddlc-top`) | 11 次 |
| ghproxy.homeboyc.cn (`ghproxy-homeboyc-cn`) | 24 次 |
| toolwa.com/github (`toolwa-com-github`) | 24 次 |
| github.akams.cn (`github-akams-cn`) | 24 次 |
| Ghproxy (`ghproxy-imciel-com`) | 4 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Github (`github-dpik-top`) | 11 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 110 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **117** | |

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
