# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-17T20:13:43Z**，每 6 小时刷新一次。当前 ✅ **119** 在线 / ⚠️ **10** 不稳定 / ⚰️ **46** 已失效归档。

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
| 1 | 79ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 2 | 80ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 3 | 81ms | Linkedin | 0.24 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 81ms | Microsoftedge | 0.6 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 5 | 90ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 6 | 102ms | Githubstatus | 0.83 MB/s | `https://githubstatus.com` | 通用代理 |
| 7 | 107ms | App | 0.11 MB/s | `https://app.netlify.com` | 通用代理 |
| 8 | 110ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 9 | 129ms | Thumb | 1.07 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 10 | 141ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 11 | 173ms | Training | 0.13 MB/s | `https://training.ti.com` | 通用代理 |
| 12 | 176ms | GH Monlor | 0.82 MB/s | `https://gh.monlor.com` | 通用代理 |
| 13 | 179ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 14 | 180ms | Github | 1.48 MB/s | `https://github.880824.xyz` | 通用代理 |
| 15 | 184ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 16 | 187ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 17 | 191ms | GH-Proxy | 0.95 MB/s | `https://gh-proxy.com` | 通用代理 |
| 18 | 192ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 19 | 192ms | Gp | 1.61 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 20 | 195ms | Gh | 1.42 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 21 | 198ms | Github | 1.73 MB/s | `https://github.788787.xyz` | 通用代理 |
| 22 | 199ms | Github | 1.51 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 23 | 205ms | Git | 1.79 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 24 | 206ms | Ghproxy | 0.74 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 25 | 207ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 26 | 208ms | Git | 1.66 MB/s | `https://git.820828.xyz` | 通用代理 |
| 27 | 210ms | Nisar | 0.38 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 28 | 215ms | Img | - | `https://img.shields.io` | 通用代理 |
| 29 | 216ms | Gh | 1.4 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 30 | 223ms | Gh | 1.45 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 31 | 223ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 32 | 225ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 33 | 228ms | Github | 0.72 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 34 | 229ms | Gh | 0.85 MB/s | `https://gh.halonice.com` | 通用代理 |
| 35 | 231ms | Axios-http | 0.32 MB/s | `https://axios-http.com` | 通用代理 |
| 36 | 231ms | Github | 1.59 MB/s | `https://github.ihnic.com` | 通用代理 |
| 37 | 235ms | Cursor | 0.47 MB/s | `https://cursor.com` | 通用代理 |
| 38 | 238ms | Sub | 0.14 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 39 | 239ms | Ampcode | 0.2 MB/s | `https://ampcode.com` | 通用代理 |
| 40 | 246ms | Ghproxy | 1.48 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 41 | 250ms | FastGit CC | 1.0 MB/s | `https://fastgit.cc` | 通用代理 |
| 42 | 251ms | Api | 0.1 MB/s | `https://api.solov.cc` | 通用代理 |
| 43 | 252ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 44 | 257ms | Tvv | 1.44 MB/s | `https://tvv.tw` | 通用代理 |
| 45 | 268ms | Aps | 0.04 MB/s | `https://aps.com` | 通用代理 |
| 46 | 277ms | GH-Proxy Org | 0.93 MB/s | `https://gh-proxy.org` | 通用代理 |
| 47 | 277ms | Gh | 1.48 MB/s | `https://gh.1k.ink` | 通用代理 |
| 48 | 278ms | Gh | 0.64 MB/s | `https://gh.padao.fun` | 通用代理 |
| 49 | 279ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 50 | 282ms | GH-Proxy YGXZ | 0.03 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 51 | 284ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 52 | 286ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 53 | 292ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 54 | 294ms | 30006000 | 0.63 MB/s | `https://30006000.xyz` | 通用代理 |
| 55 | 304ms | CrashMC CDN | 1.07 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 56 | 313ms | Npee Down | 0.03 MB/s | `https://down.npee.cn` | 通用代理 |
| 57 | 315ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 58 | 317ms | Kenyu | 1.49 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 59 | 320ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 60 | 322ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 61 | 324ms | GHFast | 0.52 MB/s | `https://ghfast.top` | 通用代理 |
| 62 | 329ms | Oem | - | `https://oem.re` | 通用代理 |
| 63 | 332ms | Bailian | 0.07 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 64 | 349ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 65 | 354ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 66 | 379ms | Gh | 0.8 MB/s | `https://gh.noki.icu` | 通用代理 |
| 67 | 389ms | Hk | 0.56 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 68 | 403ms | Github | 1.24 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 69 | 411ms | Github | 1.68 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 70 | 414ms | Ednovas Mirror | 0.7 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 71 | 416ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 72 | 418ms | Ggg | 1.47 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 73 | 419ms | Github | 1.3 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 74 | 457ms | Getgit | 1.18 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 75 | 463ms | GHProxy Net | 0.32 MB/s | `https://ghproxy.net` | 通用代理 |
| 76 | 494ms | YYLX Git | 0.76 MB/s | `https://git.yylx.win` | 通用代理 |
| 77 | 495ms | Msdn | 0.03 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 78 | 495ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 79 | 503ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 80 | 549ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 81 | 558ms | Aosmd | 0.13 MB/s | `https://aosmd.com` | 通用代理 |
| 82 | 560ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 83 | 645ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 84 | 655ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 85 | 684ms | Ghproxy | 0.22 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 86 | 701ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 87 | 715ms | Github | 0.28 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 88 | 737ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 89 | 774ms | Git | 0.21 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 90 | 775ms | Fastfile | 1.05 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 91 | 785ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 92 | 839ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 93 | 849ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 94 | 859ms | Gh | 0.8 MB/s | `https://gh.39.al` | 通用代理 |
| 95 | 862ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 96 | 869ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 97 | 890ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 98 | 899ms | Mimo | 0.16 MB/s | `https://mimo.mi.com` | 通用代理 |
| 99 | 985ms | Gh | 0.26 MB/s | `https://gh.dpik.top` | 通用代理 |
| 100 | 1043ms | Web | - | `https://web.4399.com` | 通用代理 |
| 101 | 1064ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 102 | 1156ms | Git | 0.28 MB/s | `https://git.669966.xyz` | 通用代理 |
| 103 | 1236ms | Github | 0.14 MB/s | `https://github.chenc.dev` | 通用代理 |
| 104 | 1321ms | Ghproxy | 0.2 MB/s | `https://ghproxy.cc` | 通用代理 |
| 105 | 1357ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 106 | 1422ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 107 | 1491ms | Cf | 0.21 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 108 | 1534ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 109 | 1537ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 110 | 1566ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 111 | 1632ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 112 | 1891ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 113 | 2128ms | Img | - | `https://img.ink` | 通用代理 |
| 114 | 2533ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 115 | 2624ms | G | 0.07 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 116 | 2865ms | Ghproxy | 0.15 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 117 | 3671ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 118 | 6322ms | Proxy | - | `https://proxy.yaoyaoling.net` | 通用代理 |
| 119 | 8711ms | 5555 | 0.06 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（10 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| GH Nxnow (`gh-nxnow-top`) | 1 次 |
| GitClone (`gitclone-com`) | 1 次 |
| Gh (`gh-ddlc-top`) | 18 次 |
| Gh (`gh-idayer-com`) | 3 次 |
| Ghproxy (`ghproxy-imciel-com`) | 11 次 |
| Gh (`gh-b52m-cn`) | 1 次 |
| Comfyit (`comfyit-cn`) | 1 次 |
| Github (`github-dpik-top`) | 18 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |

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
