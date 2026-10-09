# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-09T02:50:12Z**，每 6 小时刷新一次。当前 ✅ **80** 在线 / ⚠️ **12** 不稳定 / ⚰️ **37** 已失效归档。

## 核心特性

- **92 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 72ms | Microsoftedge | 0.47 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 84ms | Img | - | `https://img.shields.io` | 通用代理 |
| 3 | 135ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 4 | 143ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 5 | 153ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 6 | 170ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 7 | 172ms | Github | 1.54 MB/s | `https://github.788787.xyz` | 通用代理 |
| 8 | 175ms | Git | 1.33 MB/s | `https://git.820828.xyz` | 通用代理 |
| 9 | 178ms | Gh | 1.99 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 10 | 182ms | Github | 1.95 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 11 | 183ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 12 | 187ms | Gp | 1.65 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 13 | 194ms | Gh | 2.04 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 14 | 196ms | Git | 1.63 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 15 | 198ms | GH-Proxy | 1.19 MB/s | `https://gh-proxy.com` | 通用代理 |
| 16 | 198ms | Github | 1.79 MB/s | `https://github.880824.xyz` | 通用代理 |
| 17 | 209ms | Tvv | 1.89 MB/s | `https://tvv.tw` | 通用代理 |
| 18 | 217ms | Gh | 1.45 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 19 | 224ms | Ghproxy | 1.32 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 20 | 244ms | Ggg | 1.65 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 21 | 247ms | GH Monlor | 0.92 MB/s | `https://gh.monlor.com` | 通用代理 |
| 22 | 253ms | Gh | 0.68 MB/s | `https://gh.39.al` | 通用代理 |
| 23 | 262ms | Gh | 0.09 MB/s | `https://gh.halonice.com` | 通用代理 |
| 24 | 262ms | Gh | 1.54 MB/s | `https://gh.idayer.com` | 通用代理 |
| 25 | 264ms | Ghproxy | 1.73 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 26 | 276ms | Github | 1.4 MB/s | `https://github.ihnic.com` | 通用代理 |
| 27 | 277ms | GH-Proxy Org | 1.12 MB/s | `https://gh-proxy.org` | 通用代理 |
| 28 | 278ms | FastGit CC | 0.83 MB/s | `https://fastgit.cc` | 通用代理 |
| 29 | 294ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 30 | 307ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 31 | 314ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 32 | 328ms | Gh | 1.73 MB/s | `https://gh.1k.ink` | 通用代理 |
| 33 | 330ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 34 | 333ms | Github | 1.41 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 35 | 335ms | Npee Down | 0.02 MB/s | `https://down.npee.cn` | 通用代理 |
| 36 | 344ms | Ghproxy | 0.19 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 37 | 357ms | Gh | 0.53 MB/s | `https://gh.padao.fun` | 通用代理 |
| 38 | 378ms | GH-Proxy YGXZ | 0.02 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 39 | 381ms | CrashMC CDN | 0.89 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 40 | 382ms | Kenyu | 2.01 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 41 | 383ms | Getgit | 0.6 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 42 | 389ms | Github | 1.63 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 43 | 414ms | GH Nxnow | 0.33 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 44 | 423ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 45 | 428ms | GHFast | 0.27 MB/s | `https://ghfast.top` | 通用代理 |
| 46 | 444ms | Gh | 0.81 MB/s | `https://gh.noki.icu` | 通用代理 |
| 47 | 445ms | 30006000 | 0.5 MB/s | `https://30006000.xyz` | 通用代理 |
| 48 | 487ms | GHProxy Net | 0.27 MB/s | `https://ghproxy.net` | 通用代理 |
| 49 | 490ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 50 | 520ms | Your-domain | 0.03 MB/s | `https://your-domain.com` | 通用代理 |
| 51 | 531ms | YYLX Git | 0.69 MB/s | `https://git.yylx.win` | 通用代理 |
| 52 | 533ms | Github | 1.81 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 53 | 539ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 54 | 568ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 55 | 583ms | Github | 0.1 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 56 | 600ms | Github | 0.31 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 57 | 642ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 58 | 680ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 59 | 686ms | Git | 0.21 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 60 | 755ms | Ghproxy | 0.22 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 61 | 758ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 62 | 776ms | Web | - | `https://web.4399.com` | 通用代理 |
| 63 | 787ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 64 | 883ms | Ednovas Mirror | 0.48 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 65 | 1241ms | GHFile Geekertao | 0.21 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 66 | 1261ms | Ghproxy | 0.25 MB/s | `https://ghproxy.cc` | 通用代理 |
| 67 | 1270ms | Git | 0.28 MB/s | `https://git.669966.xyz` | 通用代理 |
| 68 | 1310ms | Github | 0.14 MB/s | `https://github.chenc.dev` | 通用代理 |
| 69 | 1364ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 70 | 1386ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 71 | 1391ms | Cf | 0.23 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 72 | 1409ms | Gh | 0.79 MB/s | `https://gh.dpik.top` | 通用代理 |
| 73 | 1517ms | Ghproxy | 0.15 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 74 | 1560ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 75 | 2280ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 76 | 2874ms | G | 0.15 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 77 | 3193ms | Gh | 0.06 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 78 | 3711ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 79 | 3770ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 80 | 5522ms | Proxy | - | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Boki Mirror (`github-boki-moe`) | 13 次 |
| GHP Keleyaa (`ghp-keleyaa-com`) | 13 次 |
| GH Chjina (`gh-chjina-com`) | 13 次 |
| GHPXY Hwinzniej (`ghpxy-hwinzniej-top`) | 13 次 |
| GH ZWY (`gh-zwy-one`) | 9 次 |
| Lixxing Proxy (`github-proxy-lixxing-top`) | 13 次 |
| GitClone (`gitclone-com`) | 2 次 |
| Gh (`gh-ddlc-top`) | 2 次 |
| ghproxy.homeboyc.cn (`ghproxy-homeboyc-cn`) | 9 次 |
| toolwa.com/github (`toolwa-com-github`) | 9 次 |
| github.akams.cn (`github-akams-cn`) | 9 次 |
| Gitproxy (`gitproxy-click`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 85 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **92** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（37 个）。

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
