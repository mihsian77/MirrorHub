# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-09T04:43:33Z**，每 6 小时刷新一次。当前 ✅ **84** 在线 / ⚠️ **12** 不稳定 / ⚰️ **37** 已失效归档。

## 核心特性

- **96 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 77ms | Img | - | `https://img.shields.io` | 通用代理 |
| 2 | 83ms | Microsoftedge | 0.24 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 84ms | Githubstatus | 2.24 MB/s | `https://githubstatus.com` | 通用代理 |
| 4 | 128ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 5 | 135ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 6 | 138ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 7 | 172ms | Git | 1.59 MB/s | `https://git.820828.xyz` | 通用代理 |
| 8 | 174ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 9 | 174ms | Github | 1.23 MB/s | `https://github.788787.xyz` | 通用代理 |
| 10 | 175ms | Gp | 1.81 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 11 | 176ms | Github | 1.56 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 12 | 178ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 13 | 180ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 14 | 181ms | Gh | 2.03 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 15 | 187ms | Github | 1.99 MB/s | `https://github.880824.xyz` | 通用代理 |
| 16 | 194ms | GH-Proxy | 1.04 MB/s | `https://gh-proxy.com` | 通用代理 |
| 17 | 194ms | Git | 1.73 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 18 | 196ms | Gh | 1.45 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 19 | 204ms | Gh | 0.9 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 20 | 206ms | Tvv | 1.79 MB/s | `https://tvv.tw` | 通用代理 |
| 21 | 223ms | Ghproxy | 0.89 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 22 | 231ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 23 | 238ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 24 | 239ms | Ggg | 1.63 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 25 | 239ms | Gh | 0.36 MB/s | `https://gh.39.al` | 通用代理 |
| 26 | 247ms | GH Monlor | 1.44 MB/s | `https://gh.monlor.com` | 通用代理 |
| 27 | 250ms | Ghproxy | 2.75 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 28 | 253ms | Gh | 0.94 MB/s | `https://gh.idayer.com` | 通用代理 |
| 29 | 255ms | Github | 1.37 MB/s | `https://github.ihnic.com` | 通用代理 |
| 30 | 265ms | FastGit CC | 1.49 MB/s | `https://fastgit.cc` | 通用代理 |
| 31 | 273ms | Cursor | 0.4 MB/s | `https://cursor.com` | 通用代理 |
| 32 | 280ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 33 | 289ms | GH-Proxy Org | 1.18 MB/s | `https://gh-proxy.org` | 通用代理 |
| 34 | 293ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 35 | 300ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 36 | 313ms | Ghproxy | 1.6 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 37 | 321ms | Gh | 1.1 MB/s | `https://gh.padao.fun` | 通用代理 |
| 38 | 322ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 39 | 331ms | Npee Down | 0.05 MB/s | `https://down.npee.cn` | 通用代理 |
| 40 | 333ms | Gh | 1.06 MB/s | `https://gh.1k.ink` | 通用代理 |
| 41 | 357ms | Kenyu | 1.8 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 42 | 358ms | Hk | 1.41 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 43 | 361ms | Getgit | 1.94 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 44 | 363ms | Github | 1.48 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 45 | 364ms | CrashMC CDN | 1.05 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 46 | 372ms | GH-Proxy YGXZ | 0.03 MB/s | `https://gh-proxy.ygxz.in` | 通用代理 |
| 47 | 383ms | Github | 2.68 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 48 | 390ms | GH Nxnow | 0.73 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 49 | 402ms | 30006000 | 1.77 MB/s | `https://30006000.xyz` | 通用代理 |
| 50 | 406ms | GHFast | 0.9 MB/s | `https://ghfast.top` | 通用代理 |
| 51 | 420ms | Ednovas Mirror | 1.69 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 52 | 430ms | Gh | 0.53 MB/s | `https://gh.noki.icu` | 通用代理 |
| 53 | 467ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 54 | 475ms | GHProxy Net | 0.23 MB/s | `https://ghproxy.net` | 通用代理 |
| 55 | 510ms | YYLX Git | 2.27 MB/s | `https://git.yylx.win` | 通用代理 |
| 56 | 515ms | Github | 1.45 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 57 | 522ms | Github | 1.09 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 58 | 532ms | SLink | 0.06 MB/s | `https://slink.ltd` | 通用代理 |
| 59 | 566ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 60 | 568ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 61 | 611ms | Gh | 0.05 MB/s | `https://gh.halonice.com` | 通用代理 |
| 62 | 621ms | Github | 0.18 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 63 | 683ms | Git | 0.24 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 64 | 722ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 65 | 725ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 66 | 755ms | Ghproxy | 0.31 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 67 | 774ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 68 | 1006ms | Web | - | `https://web.4399.com` | 通用代理 |
| 69 | 1200ms | Git | 0.35 MB/s | `https://git.669966.xyz` | 通用代理 |
| 70 | 1209ms | Ghproxy | 0.34 MB/s | `https://ghproxy.cc` | 通用代理 |
| 71 | 1257ms | GHFile Geekertao | - | `https://ghfile.geekertao.top` | 通用代理 |
| 72 | 1272ms | Github | 0.16 MB/s | `https://github.chenc.dev` | 通用代理 |
| 73 | 1384ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 74 | 1385ms | Cf | 0.35 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 75 | 1390ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 76 | 1501ms | Ghproxy | 0.06 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 77 | 1562ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 78 | 2465ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 79 | 2517ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 80 | 2744ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 81 | 3132ms | G | 0.02 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 82 | 3799ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 83 | 5537ms | Proxy | 0.03 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 84 | 7921ms | GitClone | - | `https://gitclone.com` | Clone 专用 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Boki Mirror (`github-boki-moe`) | 14 次 |
| GHP Keleyaa (`ghp-keleyaa-com`) | 14 次 |
| GH Chjina (`gh-chjina-com`) | 14 次 |
| GHPXY Hwinzniej (`ghpxy-hwinzniej-top`) | 14 次 |
| GH ZWY (`gh-zwy-one`) | 10 次 |
| Lixxing Proxy (`github-proxy-lixxing-top`) | 14 次 |
| Gh (`gh-ddlc-top`) | 3 次 |
| ghproxy.homeboyc.cn (`ghproxy-homeboyc-cn`) | 10 次 |
| toolwa.com/github (`toolwa-com-github`) | 10 次 |
| github.akams.cn (`github-akams-cn`) | 10 次 |
| Gh (`gh-dpik-top`) | 1 次 |
| Gh (`gh-b52m-cn`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 89 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **96** | |

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
