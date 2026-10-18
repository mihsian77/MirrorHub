# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-18T10:28:24Z**，每 6 小时刷新一次。当前 ✅ **127** 在线 / ⚠️ **9** 不稳定 / ⚰️ **46** 已失效归档。

## 核心特性

- **136 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 65ms | Microsoftedge | 0.75 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 68ms | Linkedin | 0.46 MB/s | `https://linkedin.com` | 通用代理 |
| 3 | 69ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 4 | 72ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 87ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 6 | 90ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 7 | 94ms | Githubstatus | 3.55 MB/s | `https://githubstatus.com` | 通用代理 |
| 8 | 94ms | Radio-browser | 0.04 MB/s | `https://radio-browser.info` | 通用代理 |
| 9 | 96ms | App | 0.15 MB/s | `https://app.netlify.com` | 通用代理 |
| 10 | 116ms | Thumb | 5.44 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 11 | 136ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 12 | 137ms | Goreportcard | 0.07 MB/s | `https://goreportcard.com` | 通用代理 |
| 13 | 147ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 14 | 152ms | Github | 3.14 MB/s | `https://github.788787.xyz` | 通用代理 |
| 15 | 163ms | Training | 0.37 MB/s | `https://training.ti.com` | 通用代理 |
| 16 | 167ms | GH Monlor | 2.23 MB/s | `https://gh.monlor.com` | 通用代理 |
| 17 | 169ms | Github | 3.83 MB/s | `https://github.880824.xyz` | 通用代理 |
| 18 | 177ms | GH-Proxy | 2.44 MB/s | `https://gh-proxy.com` | 通用代理 |
| 19 | 179ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 20 | 181ms | Gh | 2.29 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 21 | 185ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 22 | 185ms | Git | 3.68 MB/s | `https://git.820828.xyz` | 通用代理 |
| 23 | 187ms | Git | 3.66 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 24 | 189ms | Gp | 3.74 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 25 | 192ms | Github | 3.15 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 26 | 196ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 27 | 198ms | Gh | 3.42 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 28 | 198ms | Github | 3.41 MB/s | `https://github.ihnic.com` | 通用代理 |
| 29 | 199ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 30 | 203ms | Gh | 3.46 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 31 | 203ms | Img | - | `https://img.shields.io` | 通用代理 |
| 32 | 206ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 33 | 216ms | Axios-http | 1.5 MB/s | `https://axios-http.com` | 通用代理 |
| 34 | 224ms | Cursor | 0.71 MB/s | `https://cursor.com` | 通用代理 |
| 35 | 226ms | Ampcode | 0.31 MB/s | `https://ampcode.com` | 通用代理 |
| 36 | 226ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 37 | 227ms | Ghproxy | 0.57 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 38 | 227ms | Sub | 0.33 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 39 | 230ms | Gh | 0.55 MB/s | `https://gh.halonice.com` | 通用代理 |
| 40 | 235ms | Ghproxy | 3.38 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 41 | 236ms | Nisar | 0.84 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 42 | 245ms | FastGit CC | 1.92 MB/s | `https://fastgit.cc` | 通用代理 |
| 43 | 245ms | Kenyu | 4.86 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 44 | 248ms | Tvv | 2.85 MB/s | `https://tvv.tw` | 通用代理 |
| 45 | 254ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 46 | 256ms | GH-Proxy Org | 1.9 MB/s | `https://gh-proxy.org` | 通用代理 |
| 47 | 256ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 48 | 264ms | Github | 0.49 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 49 | 269ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 50 | 269ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 51 | 272ms | Api | 0.08 MB/s | `https://api.solov.cc` | 通用代理 |
| 52 | 278ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 53 | 279ms | Gh | 3.88 MB/s | `https://gh.1k.ink` | 通用代理 |
| 54 | 279ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 55 | 289ms | CrashMC CDN | 2.95 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 56 | 293ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 57 | 301ms | Npee Down | 0.02 MB/s | `https://down.npee.cn` | 通用代理 |
| 58 | 305ms | Gh | 0.52 MB/s | `https://gh.padao.fun` | 通用代理 |
| 59 | 313ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 60 | 313ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 61 | 314ms | Oem | - | `https://oem.re` | 通用代理 |
| 62 | 317ms | GH Nxnow | 0.76 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 63 | 330ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 64 | 344ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 65 | 347ms | 30006000 | 0.41 MB/s | `https://30006000.xyz` | 通用代理 |
| 66 | 352ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 67 | 363ms | Gh | 0.73 MB/s | `https://gh.noki.icu` | 通用代理 |
| 68 | 373ms | Hk | 2.1 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 69 | 375ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 70 | 388ms | Ednovas Mirror | 0.56 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 71 | 388ms | Github | 3.62 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 72 | 401ms | Github | 3.73 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 73 | 401ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 74 | 422ms | Bailian | 0.04 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 75 | 429ms | Ggg | 3.15 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 76 | 450ms | GHProxy Net | 0.22 MB/s | `https://ghproxy.net` | 通用代理 |
| 77 | 454ms | Getgit | 3.2 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 78 | 465ms | Msdn | 0.11 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 79 | 492ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 80 | 515ms | Aosmd | 0.37 MB/s | `https://aosmd.com` | 通用代理 |
| 81 | 515ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 82 | 526ms | GHFast | 0.5 MB/s | `https://ghfast.top` | 通用代理 |
| 83 | 527ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 84 | 536ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 85 | 555ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 86 | 561ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 87 | 574ms | Github | 3.14 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 88 | 623ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 89 | 633ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 90 | 666ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 91 | 693ms | Ghproxy | 0.23 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 92 | 728ms | Fastfile | 2.27 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 93 | 756ms | Github | 0.32 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 94 | 757ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 95 | 758ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 96 | 767ms | YYLX Git | 0.46 MB/s | `https://git.yylx.win` | 通用代理 |
| 97 | 781ms | Git | - | `https://git.tangbai.cc` | 通用代理 |
| 98 | 786ms | GHFile Geekertao | 0.36 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 99 | 797ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 100 | 834ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 101 | 861ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 102 | 876ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 103 | 898ms | Gh | 0.57 MB/s | `https://gh.39.al` | 通用代理 |
| 104 | 914ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 105 | 935ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 106 | 943ms | Mimo | 0.15 MB/s | `https://mimo.mi.com` | 通用代理 |
| 107 | 979ms | Gh | 2.42 MB/s | `https://gh.dpik.top` | 通用代理 |
| 108 | 994ms | Web | - | `https://web.4399.com` | 通用代理 |
| 109 | 1089ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 110 | 1153ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 111 | 1264ms | Github | 0.13 MB/s | `https://github.chenc.dev` | 通用代理 |
| 112 | 1273ms | Ghproxy | 0.24 MB/s | `https://ghproxy.cc` | 通用代理 |
| 113 | 1290ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 114 | 1382ms | Cf | 0.25 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 115 | 1388ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 116 | 1456ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 117 | 1588ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 118 | 1650ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 119 | 1894ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 120 | 1953ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 121 | 2149ms | Img | - | `https://img.ink` | 通用代理 |
| 122 | 2151ms | G | 0.01 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 123 | 2459ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 124 | 2669ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 125 | 3184ms | Gh | 0.1 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 126 | 3560ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 127 | 8929ms | 5555 | 0.03 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（9 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 2 次 |
| Gh (`gh-ddlc-top`) | 20 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Ghproxy (`ghproxy-imciel-com`) | 13 次 |
| Ghproxy (`ghproxy-mirror-skybyte-me`) | 1 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Github (`github-dpik-top`) | 20 次 |
| Proxy (`proxy-vvvv-ee`) | 3 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 129 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **136** | |

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
