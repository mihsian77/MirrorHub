# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-25T20:28:13Z**，每 6 小时刷新一次。当前 ✅ **366** 在线 / ⚠️ **15** 不稳定 / ⚰️ **49** 已失效归档。

## 核心特性

- **381 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 44ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 2 | 57ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 3 | 61ms | Microsoftedge | 1.39 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 4 | 71ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 76ms | Linkedin | 0.44 MB/s | `https://linkedin.com` | 通用代理 |
| 6 | 82ms | Deno | 0.53 MB/s | `https://deno.com` | 通用代理 |
| 7 | 82ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 8 | 86ms | Dilo-d14 | 0.24 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 9 | 88ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 10 | 88ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 11 | 88ms | Huly-mcp | 0.16 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 12 | 89ms | Img | - | `https://img.shields.io` | 通用代理 |
| 13 | 90ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 14 | 90ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 15 | 90ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 16 | 91ms | Opresume | 0.21 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 17 | 91ms | X | 1.31 MB/s | `https://x.com` | 通用代理 |
| 18 | 92ms | Wordpaper | 0.36 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 19 | 95ms | Githubstatus | 2.48 MB/s | `https://githubstatus.com` | 通用代理 |
| 20 | 98ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 21 | 98ms | Kighelper-cloud | 0.11 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 22 | 98ms | Xjtu-nyxf-study-material | 0.22 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 23 | 99ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 24 | 100ms | Godocs | 0.15 MB/s | `https://godocs.io` | 通用代理 |
| 25 | 100ms | Gpui | 0.27 MB/s | `https://gpui.rs` | 通用代理 |
| 26 | 105ms | Impeccable | 1.36 MB/s | `https://impeccable.style` | 通用代理 |
| 27 | 108ms | Crypto-funding-arbitrage | 0.1 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 28 | 110ms | Impro | 2.21 MB/s | `https://impro.social` | 通用代理 |
| 29 | 111ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 30 | 112ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 31 | 113ms | App | 0.25 MB/s | `https://app.netlify.com` | 通用代理 |
| 32 | 113ms | Lawyer-yu | 0.2 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 33 | 113ms | Tools | 2.92 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 34 | 114ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 35 | 116ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 36 | 118ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 37 | 119ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 38 | 120ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 39 | 120ms | Serac | 0.06 MB/s | `https://serac.build` | 通用代理 |
| 40 | 121ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 41 | 121ms | Opencovibe | 0.24 MB/s | `https://opencovibe.com` | 通用代理 |
| 42 | 121ms | Zebrunner | 1.97 MB/s | `https://zebrunner.com` | 通用代理 |
| 43 | 122ms | Anh | 0.21 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 44 | 123ms | Agentlimb | 0.22 MB/s | `https://agentlimb.com` | 通用代理 |
| 45 | 124ms | Clayrune | 0.12 MB/s | `https://clayrune.io` | 通用代理 |
| 46 | 126ms | Codeeraser | 0.15 MB/s | `https://codeeraser.dev` | 通用代理 |
| 47 | 126ms | L4d2 | 0.15 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 48 | 126ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 49 | 126ms | Resume-5lv | 0.18 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 50 | 128ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 51 | 128ms | Caw | 0.05 MB/s | `https://caw.rocks` | 通用代理 |
| 52 | 128ms | Discord | 0.12 MB/s | `https://discord.gg` | 通用代理 |
| 53 | 129ms | Thumb | 6.18 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 54 | 129ms | Tokei | 0.4 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 55 | 130ms | App | 0.07 MB/s | `https://app.codecov.io` | 通用代理 |
| 56 | 130ms | Coffeecli | 0.12 MB/s | `https://coffeecli.com` | 通用代理 |
| 57 | 130ms | Polgarand | 0.1 MB/s | `https://polgarand.org` | 通用代理 |
| 58 | 130ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 59 | 131ms | Demo | 0.05 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 60 | 131ms | Opentakeoff | 0.09 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 61 | 132ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 62 | 132ms | Cognitum | 0.21 MB/s | `https://cognitum.one` | 通用代理 |
| 63 | 133ms | Chops | 0.02 MB/s | `https://chops.md` | 通用代理 |
| 64 | 133ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 65 | 133ms | Vibesql | 0.14 MB/s | `https://vibesql.org` | 通用代理 |
| 66 | 138ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 67 | 139ms | Alas | 1.04 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 68 | 139ms | Gh | 2.13 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 69 | 139ms | Gitea-mirror | 1.05 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 70 | 139ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 71 | 140ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 72 | 140ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 73 | 142ms | Git | 2.58 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 74 | 143ms | Github | 1.65 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 75 | 144ms | Cody | 0.2 MB/s | `https://cody.todyle.com` | 通用代理 |
| 76 | 144ms | Git | 2.06 MB/s | `https://git.820828.xyz` | 通用代理 |
| 77 | 144ms | Hopp | 0.05 MB/s | `https://hopp.sh` | 通用代理 |
| 78 | 144ms | Miaozitie | 0.09 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 79 | 145ms | Github | 0.96 MB/s | `https://github.788787.xyz` | 通用代理 |
| 80 | 145ms | Gp | 2.34 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 81 | 146ms | Glass | 0.23 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 82 | 147ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 83 | 149ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 84 | 149ms | Gh | 2.61 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 85 | 153ms | Bananaslides | 0.28 MB/s | `https://bananaslides.online` | 通用代理 |
| 86 | 153ms | Nextup-resource | 0.07 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 87 | 153ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 88 | 154ms | Openpua | 0.39 MB/s | `https://openpua.ai` | 通用代理 |
| 89 | 154ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 90 | 157ms | Bestdori | 0.11 MB/s | `https://bestdori.com` | 通用代理 |
| 91 | 159ms | GH-Proxy | 1.47 MB/s | `https://gh-proxy.com` | 通用代理 |
| 92 | 159ms | Shiori-v1 | 0.05 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 93 | 161ms | Tms | 0.18 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 94 | 163ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 95 | 164ms | Github | 2.56 MB/s | `https://github.880824.xyz` | 通用代理 |
| 96 | 165ms | Music-cli | 0.54 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 97 | 166ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 98 | 167ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 99 | 168ms | GH Monlor | 1.79 MB/s | `https://gh.monlor.com` | 通用代理 |
| 100 | 169ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 101 | 170ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 102 | 170ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 103 | 171ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 104 | 171ms | Gh | 2.55 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 105 | 173ms | Training | 0.29 MB/s | `https://training.ti.com` | 通用代理 |
| 106 | 174ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 107 | 174ms | Opensunsama | 0.07 MB/s | `https://opensunsama.com` | 通用代理 |
| 108 | 176ms | Ghproxy | 2.59 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 109 | 177ms | Cbrowser | 1.98 MB/s | `https://cbrowser.ai` | 通用代理 |
| 110 | 177ms | Holyclaude | 0.15 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 111 | 180ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 112 | 180ms | Ai-trend-publish | 0.05 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 113 | 181ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 114 | 182ms | Worldofclaudecraft | 2.57 MB/s | `https://worldofclaudecraft.com` | 通用代理 |
| 115 | 183ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 116 | 184ms | Github | 2.76 MB/s | `https://github.ihnic.com` | 通用代理 |
| 117 | 184ms | Openttd | 0.07 MB/s | `https://openttd.org` | 通用代理 |
| 118 | 185ms | Bolt2github | 0.08 MB/s | `https://bolt2github.com` | 通用代理 |
| 119 | 185ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 120 | 187ms | Contrib | 0.33 MB/s | `https://contrib.rocks` | 通用代理 |
| 121 | 188ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 122 | 192ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 123 | 192ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 124 | 193ms | Ghproxy | 2.75 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 125 | 194ms | Caiji | 0.09 MB/s | `https://caiji.cyou` | 通用代理 |
| 126 | 194ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 127 | 194ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 128 | 195ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 129 | 197ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 130 | 199ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 131 | 200ms | Components | 0.14 MB/s | `https://components.dereekb.com` | 通用代理 |
| 132 | 200ms | Twitter | 0.85 MB/s | `https://twitter.com` | 通用代理 |
| 133 | 201ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 134 | 202ms | Congressmcp | 0.05 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 135 | 204ms | Ode | - | `https://ode.fun` | 通用代理 |
| 136 | 208ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 137 | 208ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 138 | 209ms | Ginlix | 0.98 MB/s | `https://ginlix.ai` | 通用代理 |
| 139 | 209ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 140 | 209ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 141 | 209ms | Phabricator | 0.13 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 142 | 209ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 143 | 215ms | Ampcode | 0.35 MB/s | `https://ampcode.com` | 通用代理 |
| 144 | 217ms | Microcoreos | 0.39 MB/s | `https://microcoreos.com` | 通用代理 |
| 145 | 220ms | GH-Proxy Org | 1.46 MB/s | `https://gh-proxy.org` | 通用代理 |
| 146 | 222ms | Gh | 3.06 MB/s | `https://gh.1k.ink` | 通用代理 |
| 147 | 223ms | Themolt | 0.07 MB/s | `https://themolt.net` | 通用代理 |
| 148 | 225ms | Axios-http | 1.09 MB/s | `https://axios-http.com` | 通用代理 |
| 149 | 225ms | FastGit CC | 1.58 MB/s | `https://fastgit.cc` | 通用代理 |
| 150 | 227ms | Kenyu | 3.0 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 151 | 227ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 152 | 228ms | Cursor | 0.72 MB/s | `https://cursor.com` | 通用代理 |
| 153 | 229ms | Clypra | 0.14 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 154 | 229ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 155 | 229ms | Tvv | 2.13 MB/s | `https://tvv.tw` | 通用代理 |
| 156 | 231ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 157 | 233ms | Api | 0.07 MB/s | `https://api.solov.cc` | 通用代理 |
| 158 | 234ms | CrashMC CDN | 2.19 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 159 | 236ms | Aka | 0.43 MB/s | `https://aka.ms` | 通用代理 |
| 160 | 237ms | Gsd | 0.3 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 161 | 237ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 162 | 240ms | Aiblackboxfc | 0.25 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 163 | 240ms | Ghproxy | - | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 164 | 240ms | Visionmemorymcp | 0.2 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 165 | 242ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 166 | 242ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 167 | 245ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 168 | 246ms | Nisar | 0.74 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 169 | 249ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 170 | 250ms | Ggg | 3.18 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 171 | 251ms | Ai-watch | 0.05 MB/s | `https://ai-watch.dev` | 通用代理 |
| 172 | 251ms | Coreos | 3.82 MB/s | `https://coreos.com` | 通用代理 |
| 173 | 251ms | Sub | 0.34 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 174 | 255ms | Code | 0.78 MB/s | `https://code.claude.com` | 通用代理 |
| 175 | 260ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 176 | 263ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 177 | 265ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 178 | 266ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 179 | 268ms | Agoramarket | 0.61 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 180 | 268ms | Claude | 0.28 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 181 | 272ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 182 | 277ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 183 | 282ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 184 | 282ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 185 | 283ms | Tiktok | 0.25 MB/s | `https://tiktok.com` | 通用代理 |
| 186 | 284ms | Kuroutoshikou | 1.74 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 187 | 284ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 188 | 286ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 189 | 287ms | Youtu | 2.36 MB/s | `https://youtu.be` | 通用代理 |
| 190 | 291ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 191 | 295ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 192 | 296ms | Gh | - | `https://gh.padao.fun` | 通用代理 |
| 193 | 303ms | Weaverse | 0.78 MB/s | `https://weaverse.io` | 通用代理 |
| 194 | 308ms | Github | - | `https://github.cnxiaobai.com` | 通用代理 |
| 195 | 310ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 196 | 310ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 197 | 311ms | Agenticcorporation | 0.08 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 198 | 311ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 199 | 314ms | Steamcommunity | 0.18 MB/s | `https://steamcommunity.com` | 通用代理 |
| 200 | 316ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 201 | 318ms | Radio-browser | 0.01 MB/s | `https://radio-browser.info` | 通用代理 |
| 202 | 319ms | B23 | - | `https://b23.tv` | 通用代理 |
| 203 | 319ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 204 | 321ms | 30006000 | - | `https://30006000.xyz` | 通用代理 |
| 205 | 326ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 206 | 329ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 207 | 331ms | Aomedia | 0.42 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 208 | 335ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 209 | 337ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 210 | 339ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 211 | 341ms | Sonarcloud | 0.02 MB/s | `https://sonarcloud.io` | 通用代理 |
| 212 | 342ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 213 | 343ms | You | 0.06 MB/s | `https://you.piccalc.com` | 通用代理 |
| 214 | 348ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 215 | 350ms | Ednovas Mirror | - | `https://github.ednovas.xyz` | 通用代理 |
| 216 | 366ms | Hk | 0.47 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 217 | 367ms | Github | 1.75 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 218 | 370ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 219 | 373ms | Bailian | 0.04 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 220 | 374ms | Turborepo-starter-kit-web | 0.13 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 221 | 376ms | GHFast | - | `https://ghfast.top` | 通用代理 |
| 222 | 379ms | Store | 1.11 MB/s | `https://store.steampowered.com` | 通用代理 |
| 223 | 384ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 224 | 387ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 225 | 400ms | App | 0.02 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 226 | 406ms | Bseindia | 0.05 MB/s | `https://bseindia.com` | 通用代理 |
| 227 | 406ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 228 | 407ms | GH Nxnow | 0.65 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 229 | 408ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 230 | 412ms | Github | 2.68 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 231 | 414ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 232 | 415ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 233 | 417ms | YYLX Git | - | `https://git.yylx.win` | 通用代理 |
| 234 | 423ms | Aps | 0.02 MB/s | `https://aps.com` | 通用代理 |
| 235 | 426ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 236 | 429ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 237 | 429ms | Gh | 0.66 MB/s | `https://gh.noki.icu` | 通用代理 |
| 238 | 431ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 239 | 433ms | Getgit | 2.63 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 240 | 436ms | Bible-ai-explorer | 0.1 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 241 | 442ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 242 | 444ms | Adult | 0.01 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 243 | 448ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 244 | 449ms | Github | 3.43 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 245 | 468ms | Safedocx | 0.17 MB/s | `https://safedocx.com` | 通用代理 |
| 246 | 474ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 247 | 476ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 248 | 480ms | Ark | 0.51 MB/s | `https://ark.intel.com` | 通用代理 |
| 249 | 480ms | Msdn | 0.1 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 250 | 482ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 251 | 483ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 252 | 489ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 253 | 490ms | Lecvdemarius | 0.12 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 254 | 494ms | Wl | - | `https://wl.do` | 通用代理 |
| 255 | 496ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 256 | 501ms | Patchworkos | 0.37 MB/s | `https://patchworkos.com` | 通用代理 |
| 257 | 506ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 258 | 516ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 259 | 517ms | Agentkey | 0.4 MB/s | `https://agentkey.app` | 通用代理 |
| 260 | 518ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 261 | 523ms | Memstack | 0.04 MB/s | `https://memstack.pro` | 通用代理 |
| 262 | 524ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 263 | 526ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 264 | 527ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 265 | 528ms | Umami-mcp | 0.54 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 266 | 538ms | Lucky | 0.47 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 267 | 540ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 268 | 541ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 269 | 542ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 270 | 544ms | Support | 0.17 MB/s | `https://support.apple.com` | 通用代理 |
| 271 | 557ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 272 | 561ms | Aosmd | 0.33 MB/s | `https://aosmd.com` | 通用代理 |
| 273 | 564ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 274 | 570ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 275 | 572ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 276 | 573ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 277 | 585ms | Gh | - | `https://gh.39.al` | 通用代理 |
| 278 | 586ms | 3d-set-visualizer | 0.05 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 279 | 590ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 280 | 595ms | Github | - | `https://github.xxlab.tech` | 通用代理 |
| 281 | 600ms | Task | 0.01 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 282 | 618ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 283 | 648ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 284 | 648ms | Clawbiz | 0.05 MB/s | `https://clawbiz.io` | 通用代理 |
| 285 | 649ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 286 | 650ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 287 | 652ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 288 | 661ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 289 | 661ms | Im | 0.43 MB/s | `https://im.codes` | 通用代理 |
| 290 | 671ms | Gh | 0.43 MB/s | `https://gh.dpik.top` | 通用代理 |
| 291 | 679ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 292 | 694ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 293 | 709ms | Agoracitizen | 0.03 MB/s | `https://agoracitizen.app` | 通用代理 |
| 294 | 709ms | Fastfile | 1.13 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 295 | 712ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 296 | 720ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 297 | 723ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 298 | 739ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 299 | 757ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 300 | 772ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 301 | 779ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 302 | 789ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 303 | 793ms | Git | - | `https://git.tangbai.cc` | 通用代理 |
| 304 | 794ms | Aif | 0.02 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 305 | 810ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 306 | 812ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 307 | 817ms | Docs | 0.3 MB/s | `https://docs.transifex.com` | 通用代理 |
| 308 | 830ms | Ccgather | 0.05 MB/s | `https://ccgather.com` | 通用代理 |
| 309 | 830ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 310 | 848ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 311 | 876ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 312 | 899ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 313 | 910ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 314 | 921ms | Mimo | 0.14 MB/s | `https://mimo.mi.com` | 通用代理 |
| 315 | 929ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 316 | 935ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 317 | 949ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 318 | 968ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 319 | 971ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 320 | 976ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 321 | 986ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 322 | 996ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 323 | 1015ms | Web | - | `https://web.4399.com` | 通用代理 |
| 324 | 1028ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 325 | 1066ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 326 | 1073ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 327 | 1091ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 328 | 1098ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 329 | 1136ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 330 | 1155ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 331 | 1155ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 332 | 1164ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 333 | 1164ms | Ghproxy | - | `https://ghproxy.cc` | 通用代理 |
| 334 | 1170ms | V | - | `https://v.douyin.com` | 通用代理 |
| 335 | 1177ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 336 | 1181ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 337 | 1193ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 338 | 1218ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 339 | 1218ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 340 | 1240ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 341 | 1256ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 342 | 1291ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 343 | 1312ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 344 | 1328ms | Github | - | `https://github.chenc.dev` | 通用代理 |
| 345 | 1329ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 346 | 1383ms | Cf | - | `https://cf.ghproxy.cc` | 通用代理 |
| 347 | 1392ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 348 | 1411ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 349 | 1508ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 350 | 1605ms | I-qps | 0.02 MB/s | `https://i-qps.net` | 通用代理 |
| 351 | 1624ms | Heycall-e | 0.12 MB/s | `https://heycall-e.com` | 通用代理 |
| 352 | 1674ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 353 | 1714ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 354 | 1967ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 355 | 2005ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 356 | 2136ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 357 | 2207ms | Img | - | `https://img.ink` | 通用代理 |
| 358 | 2301ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 359 | 2462ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 360 | 2916ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 361 | 2921ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 362 | 2935ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 363 | 3164ms | Gh | - | `https://gh.b52m.cn` | 通用代理 |
| 364 | 3269ms | G | - | `https://g.blfrp.cn` | 通用代理 |
| 365 | 3513ms | Ghproxy | - | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 366 | 4485ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（15 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 2 次 |
| Npee Down (`down-npee-cn`) | 24 次 |
| Gh (`gh-idayer-com`) | 3 次 |
| Gh (`gh-halonice-com`) | 23 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 3 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |
| 5555 (`5555-cab`) | 14 次 |
| Code (`code-leez-tech`) | 1 次 |
| Fastgpt (`fastgpt-leez-tech`) | 1 次 |
| Doxygen (`doxygen-org`) | 10 次 |
| Dreamgraph (`dreamgraph-nofs-ai`) | 1 次 |
| Flashtype (`flashtype-com`) | 1 次 |
| Maplecode (`maplecode-art`) | 3 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 374 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **381** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（49 个）。

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
