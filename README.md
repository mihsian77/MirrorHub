# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-26T03:25:30Z**，每 6 小时刷新一次。当前 ✅ **371** 在线 / ⚠️ **11** 不稳定 / ⚰️ **49** 已失效归档。

## 核心特性

- **382 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 45ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 2 | 61ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 3 | 64ms | Microsoftedge | 0.6 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 4 | 70ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 80ms | Deno | 0.92 MB/s | `https://deno.com` | 通用代理 |
| 6 | 83ms | Linkedin | 0.18 MB/s | `https://linkedin.com` | 通用代理 |
| 7 | 86ms | Dilo-d14 | 0.19 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 8 | 88ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 9 | 90ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 10 | 91ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 11 | 92ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 12 | 92ms | Huly-mcp | 0.17 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 13 | 92ms | Img | - | `https://img.shields.io` | 通用代理 |
| 14 | 92ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 15 | 94ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 16 | 96ms | Wordpaper | 0.29 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 17 | 96ms | X | 1.25 MB/s | `https://x.com` | 通用代理 |
| 18 | 98ms | Kighelper-cloud | 0.08 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 19 | 98ms | Xjtu-nyxf-study-material | 0.13 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 20 | 100ms | Opresume | 0.56 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 21 | 101ms | Githubstatus | 0.86 MB/s | `https://githubstatus.com` | 通用代理 |
| 22 | 101ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 23 | 102ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 24 | 103ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 25 | 109ms | Gpui | 0.17 MB/s | `https://gpui.rs` | 通用代理 |
| 26 | 112ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 27 | 112ms | Tools | 1.71 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 28 | 113ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 29 | 114ms | Impeccable | 1.1 MB/s | `https://impeccable.style` | 通用代理 |
| 30 | 117ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 31 | 117ms | Lawyer-yu | 0.07 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 32 | 119ms | Impro | 1.54 MB/s | `https://impro.social` | 通用代理 |
| 33 | 119ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 34 | 120ms | App | 0.13 MB/s | `https://app.netlify.com` | 通用代理 |
| 35 | 120ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 36 | 123ms | Serac | 0.06 MB/s | `https://serac.build` | 通用代理 |
| 37 | 124ms | Freeport | 0.02 MB/s | `https://freeport.network` | 通用代理 |
| 38 | 124ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 39 | 127ms | Agentlimb | 0.19 MB/s | `https://agentlimb.com` | 通用代理 |
| 40 | 127ms | Zebrunner | 1.02 MB/s | `https://zebrunner.com` | 通用代理 |
| 41 | 128ms | Clayrune | 0.12 MB/s | `https://clayrune.io` | 通用代理 |
| 42 | 128ms | L4d2 | 0.13 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 43 | 129ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 44 | 129ms | Codeeraser | 0.12 MB/s | `https://codeeraser.dev` | 通用代理 |
| 45 | 131ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 46 | 131ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 47 | 131ms | Tokei | 0.47 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 48 | 132ms | Anh | 0.2 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 49 | 132ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 50 | 132ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 51 | 132ms | Resume-5lv | 0.16 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 52 | 133ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 53 | 134ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 54 | 134ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 55 | 135ms | Cognitum | 0.16 MB/s | `https://cognitum.one` | 通用代理 |
| 56 | 136ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 57 | 136ms | Discord | 0.09 MB/s | `https://discord.gg` | 通用代理 |
| 58 | 138ms | Coffeecli | 0.1 MB/s | `https://coffeecli.com` | 通用代理 |
| 59 | 138ms | Demo | 0.03 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 60 | 138ms | Opencovibe | 0.28 MB/s | `https://opencovibe.com` | 通用代理 |
| 61 | 138ms | Vibesql | 0.12 MB/s | `https://vibesql.org` | 通用代理 |
| 62 | 138ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 63 | 139ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 64 | 142ms | Gitea-mirror | 0.64 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 65 | 142ms | Thumb | 1.0 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 66 | 143ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 67 | 145ms | Cody | 0.18 MB/s | `https://cody.todyle.com` | 通用代理 |
| 68 | 146ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 69 | 146ms | Gp | 2.71 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 70 | 147ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 71 | 147ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 72 | 148ms | Gh | 2.03 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 73 | 148ms | Github | 2.13 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 74 | 149ms | Miaozitie | 0.07 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 75 | 150ms | Git | 2.4 MB/s | `https://git.820828.xyz` | 通用代理 |
| 76 | 151ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 77 | 151ms | Bananaslides | 0.36 MB/s | `https://bananaslides.online` | 通用代理 |
| 78 | 151ms | Git | 2.65 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 79 | 151ms | Glass | 0.15 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 80 | 152ms | Alas | 0.77 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 81 | 152ms | Github | 2.54 MB/s | `https://github.788787.xyz` | 通用代理 |
| 82 | 152ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 83 | 155ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 84 | 156ms | Bestdori | 0.07 MB/s | `https://bestdori.com` | 通用代理 |
| 85 | 156ms | Gh | 3.06 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 86 | 156ms | Openpua | 0.48 MB/s | `https://openpua.ai` | 通用代理 |
| 87 | 157ms | Osf | 0.03 MB/s | `https://osf.io` | 通用代理 |
| 88 | 159ms | Play | 0.05 MB/s | `https://play.templatical.com` | 通用代理 |
| 89 | 161ms | Tms | 0.14 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 90 | 163ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 91 | 163ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 92 | 164ms | Music-cli | 0.18 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 93 | 165ms | GH-Proxy | 1.03 MB/s | `https://gh-proxy.com` | 通用代理 |
| 94 | 166ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 95 | 167ms | Polgarand | 0.06 MB/s | `https://polgarand.org` | 通用代理 |
| 96 | 168ms | Cbrowser | 1.56 MB/s | `https://cbrowser.ai` | 通用代理 |
| 97 | 170ms | Github | 2.43 MB/s | `https://github.880824.xyz` | 通用代理 |
| 98 | 171ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 99 | 171ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 100 | 173ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 101 | 175ms | Training | 0.13 MB/s | `https://training.ti.com` | 通用代理 |
| 102 | 177ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 103 | 178ms | Gh | 1.3 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 104 | 179ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 105 | 180ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 106 | 180ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 107 | 181ms | Caiji | 0.11 MB/s | `https://caiji.cyou` | 通用代理 |
| 108 | 182ms | Ghproxy | 2.3 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 109 | 183ms | GH Monlor | 1.11 MB/s | `https://gh.monlor.com` | 通用代理 |
| 110 | 184ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 111 | 185ms | Opensunsama | 0.04 MB/s | `https://opensunsama.com` | 通用代理 |
| 112 | 186ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 113 | 187ms | Contrib | 0.41 MB/s | `https://contrib.rocks` | 通用代理 |
| 114 | 187ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 115 | 187ms | Holyclaude | 0.12 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 116 | 188ms | Github | 2.05 MB/s | `https://github.ihnic.com` | 通用代理 |
| 117 | 189ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 118 | 189ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 119 | 190ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 120 | 191ms | Pidash | 0.04 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 121 | 191ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 122 | 193ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 123 | 193ms | Ghproxy | 2.58 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 124 | 195ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 125 | 196ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 126 | 196ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 127 | 198ms | Components | 0.09 MB/s | `https://components.dereekb.com` | 通用代理 |
| 128 | 198ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 129 | 199ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 130 | 201ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 131 | 202ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 132 | 203ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 133 | 205ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 134 | 205ms | Worldofclaudecraft | 1.42 MB/s | `https://worldofclaudecraft.com` | 通用代理 |
| 135 | 207ms | Ode | - | `https://ode.fun` | 通用代理 |
| 136 | 208ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 137 | 211ms | Twitter | 0.85 MB/s | `https://twitter.com` | 通用代理 |
| 138 | 214ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 139 | 214ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 140 | 216ms | Ginlix | 0.54 MB/s | `https://ginlix.ai` | 通用代理 |
| 141 | 220ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 142 | 221ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 143 | 221ms | Microcoreos | 0.32 MB/s | `https://microcoreos.com` | 通用代理 |
| 144 | 223ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 145 | 224ms | Kenyu | 2.18 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 146 | 225ms | Gsd | 0.24 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 147 | 227ms | GH-Proxy Org | 1.13 MB/s | `https://gh-proxy.org` | 通用代理 |
| 148 | 227ms | Gh | 2.45 MB/s | `https://gh.idayer.com` | 通用代理 |
| 149 | 228ms | Ampcode | 0.21 MB/s | `https://ampcode.com` | 通用代理 |
| 150 | 229ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 151 | 229ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 152 | 230ms | Gh | 2.17 MB/s | `https://gh.1k.ink` | 通用代理 |
| 153 | 230ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 154 | 231ms | Api | 0.14 MB/s | `https://api.solov.cc` | 通用代理 |
| 155 | 231ms | FastGit CC | 1.12 MB/s | `https://fastgit.cc` | 通用代理 |
| 156 | 232ms | Tvv | 1.69 MB/s | `https://tvv.tw` | 通用代理 |
| 157 | 236ms | Aka | 0.64 MB/s | `https://aka.ms` | 通用代理 |
| 158 | 237ms | Clypra | 0.04 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 159 | 238ms | Aiblackboxfc | 0.29 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 160 | 238ms | Ggg | 2.51 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 161 | 239ms | Ghproxy | 0.7 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 162 | 240ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 163 | 242ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 164 | 242ms | Axios-http | 0.3 MB/s | `https://axios-http.com` | 通用代理 |
| 165 | 242ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 166 | 243ms | Cursor | 0.41 MB/s | `https://cursor.com` | 通用代理 |
| 167 | 245ms | CrashMC CDN | 1.09 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 168 | 246ms | Nisar | 0.74 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 169 | 247ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 170 | 249ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 171 | 253ms | Visionmemorymcp | 0.23 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 172 | 257ms | Ai-watch | 0.01 MB/s | `https://ai-watch.dev` | 通用代理 |
| 173 | 258ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 174 | 258ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 175 | 260ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 176 | 263ms | Code | 1.49 MB/s | `https://code.claude.com` | 通用代理 |
| 177 | 263ms | Coreos | 1.63 MB/s | `https://coreos.com` | 通用代理 |
| 178 | 267ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 179 | 267ms | Sub | 0.11 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 180 | 269ms | Claude | 0.38 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 181 | 269ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 182 | 274ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 183 | 275ms | Agoramarket | 0.76 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 184 | 280ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 185 | 280ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 186 | 282ms | Tiktok | 0.16 MB/s | `https://tiktok.com` | 通用代理 |
| 187 | 285ms | Kuroutoshikou | 0.55 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 188 | 285ms | Sonarcloud | 0.11 MB/s | `https://sonarcloud.io` | 通用代理 |
| 189 | 288ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 190 | 290ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 191 | 297ms | Youtu | 1.25 MB/s | `https://youtu.be` | 通用代理 |
| 192 | 298ms | Gh | 0.61 MB/s | `https://gh.padao.fun` | 通用代理 |
| 193 | 302ms | Weaverse | 0.48 MB/s | `https://weaverse.io` | 通用代理 |
| 194 | 303ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 195 | 303ms | Github | 0.57 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 196 | 307ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 197 | 308ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 198 | 309ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 199 | 310ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 200 | 311ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 201 | 318ms | 30006000 | 0.61 MB/s | `https://30006000.xyz` | 通用代理 |
| 202 | 318ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 203 | 320ms | B23 | - | `https://b23.tv` | 通用代理 |
| 204 | 320ms | You | 0.08 MB/s | `https://you.piccalc.com` | 通用代理 |
| 205 | 324ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 206 | 325ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 207 | 326ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 208 | 330ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 209 | 335ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 210 | 335ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 211 | 336ms | Steamcommunity | 0.12 MB/s | `https://steamcommunity.com` | 通用代理 |
| 212 | 339ms | Aomedia | 0.22 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 213 | 347ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 214 | 351ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 215 | 353ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 216 | 355ms | Ednovas Mirror | 0.75 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 217 | 355ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 218 | 358ms | Bailian | 0.1 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 219 | 362ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 220 | 369ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 221 | 372ms | Github | 2.85 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 222 | 378ms | GH Nxnow | 0.78 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 223 | 379ms | Hk | 0.56 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 224 | 382ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 225 | 383ms | GHFast | 0.45 MB/s | `https://ghfast.top` | 通用代理 |
| 226 | 384ms | Turborepo-starter-kit-web | 0.06 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 227 | 386ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 228 | 387ms | Github | 1.75 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 229 | 390ms | Store | 0.82 MB/s | `https://store.steampowered.com` | 通用代理 |
| 230 | 405ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 231 | 405ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 232 | 406ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 233 | 407ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 234 | 408ms | Gh | 0.83 MB/s | `https://gh.noki.icu` | 通用代理 |
| 235 | 409ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 236 | 410ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 237 | 414ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 238 | 414ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 239 | 419ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 240 | 422ms | Aps | 0.06 MB/s | `https://aps.com` | 通用代理 |
| 241 | 429ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 242 | 430ms | Getgit | 1.94 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 243 | 432ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 244 | 442ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 245 | 452ms | Bible-ai-explorer | 0.04 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 246 | 455ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 247 | 459ms | Github | 1.78 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 248 | 460ms | YYLX Git | 0.42 MB/s | `https://git.yylx.win` | 通用代理 |
| 249 | 463ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 250 | 471ms | Agentkey | 0.38 MB/s | `https://agentkey.app` | 通用代理 |
| 251 | 471ms | Safedocx | 0.12 MB/s | `https://safedocx.com` | 通用代理 |
| 252 | 475ms | Ark | 0.39 MB/s | `https://ark.intel.com` | 通用代理 |
| 253 | 475ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 254 | 481ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 255 | 489ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 256 | 489ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 257 | 491ms | Wl | - | `https://wl.do` | 通用代理 |
| 258 | 498ms | Lecvdemarius | 0.06 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 259 | 499ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 260 | 502ms | Patchworkos | 0.28 MB/s | `https://patchworkos.com` | 通用代理 |
| 261 | 504ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 262 | 510ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 263 | 510ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 264 | 512ms | Umami-mcp | 0.41 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 265 | 520ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 266 | 521ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 267 | 524ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 268 | 525ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 269 | 530ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 270 | 535ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 271 | 537ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 272 | 551ms | Lucky | 0.27 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 273 | 556ms | Nyx | 0.06 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 274 | 566ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 275 | 567ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 276 | 576ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 277 | 581ms | Aosmd | 0.21 MB/s | `https://aosmd.com` | 通用代理 |
| 278 | 587ms | Github | 0.29 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 279 | 594ms | Gh | 0.64 MB/s | `https://gh.39.al` | 通用代理 |
| 280 | 596ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 281 | 600ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 282 | 603ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 283 | 620ms | Support | 0.11 MB/s | `https://support.apple.com` | 通用代理 |
| 284 | 626ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 285 | 628ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 286 | 632ms | Os | 0.05 MB/s | `https://os.ryo.lu` | 通用代理 |
| 287 | 642ms | Im | 0.21 MB/s | `https://im.codes` | 通用代理 |
| 288 | 652ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 289 | 655ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 290 | 659ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 291 | 661ms | Gh | 0.39 MB/s | `https://gh.dpik.top` | 通用代理 |
| 292 | 662ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 293 | 682ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 294 | 705ms | Tsukuyomi | 0.07 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 295 | 708ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 296 | 717ms | GHFile Geekertao | 0.93 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 297 | 718ms | Fastfile | 1.31 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 298 | 719ms | Ghproxy | 0.25 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 299 | 722ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 300 | 725ms | Luna | 0.01 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 301 | 727ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 302 | 728ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 303 | 760ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 304 | 773ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 305 | 789ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 306 | 790ms | Task | 0.01 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 307 | 792ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 308 | 797ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 309 | 807ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 310 | 809ms | Git | 0.2 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 311 | 812ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 312 | 833ms | Docs | 0.2 MB/s | `https://docs.transifex.com` | 通用代理 |
| 313 | 835ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 314 | 837ms | Ccgather | 0.05 MB/s | `https://ccgather.com` | 通用代理 |
| 315 | 845ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 316 | 869ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 317 | 879ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 318 | 893ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 319 | 912ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 320 | 923ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 321 | 934ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 322 | 941ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 323 | 952ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 324 | 967ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 325 | 985ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 326 | 999ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 327 | 1000ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 328 | 1008ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 329 | 1017ms | Web | - | `https://web.4399.com` | 通用代理 |
| 330 | 1024ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 331 | 1068ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 332 | 1081ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 333 | 1119ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 334 | 1132ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 335 | 1137ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 336 | 1137ms | V | 0.07 MB/s | `https://v.douyin.com` | 通用代理 |
| 337 | 1145ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 338 | 1150ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 339 | 1177ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 340 | 1181ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 341 | 1198ms | Ghproxy | 0.23 MB/s | `https://ghproxy.cc` | 通用代理 |
| 342 | 1216ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 343 | 1220ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 344 | 1225ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 345 | 1226ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 346 | 1263ms | GHProxy Net | 0.06 MB/s | `https://ghproxy.net` | 通用代理 |
| 347 | 1313ms | Git | 0.42 MB/s | `https://git.669966.xyz` | 通用代理 |
| 348 | 1314ms | Github | 0.12 MB/s | `https://github.chenc.dev` | 通用代理 |
| 349 | 1317ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 350 | 1319ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 351 | 1336ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 352 | 1366ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 353 | 1371ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 354 | 1388ms | Cf | 0.23 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 355 | 1459ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 356 | 1585ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 357 | 1640ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 358 | 1669ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 359 | 1729ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 360 | 1957ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 361 | 1994ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 362 | 2131ms | Img | - | `https://img.ink` | 通用代理 |
| 363 | 2254ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 364 | 2351ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 365 | 2439ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 366 | 2658ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 367 | 2901ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 368 | 2929ms | Wget | - | `https://wget.la` | 通用代理 |
| 369 | 3098ms | Ghproxy | 0.12 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 370 | 3322ms | G | 0.09 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 371 | 4459ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（11 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GH Zwnes (`gh-zwnes-xyz`) | 3 次 |
| Npee Down (`down-npee-cn`) | 25 次 |
| Gh (`gh-halonice-com`) | 24 次 |
| Proxy (`proxy-yaoyaoling-net`) | 4 次 |
| Gh (`gh-b52m-cn`) | 1 次 |
| Proxy (`proxy-vvvv-ee`) | 2 次 |
| 5555 (`5555-cab`) | 15 次 |
| Doxygen (`doxygen-org`) | 11 次 |
| Flashtype (`flashtype-com`) | 2 次 |
| Maplecode (`maplecode-art`) | 4 次 |
| Adult (`adult-contents-fc2-com`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 375 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **382** | |

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
