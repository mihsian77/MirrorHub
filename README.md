# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-25T15:39:56Z**，每 6 小时刷新一次。当前 ✅ **368** 在线 / ⚠️ **12** 不稳定 / ⚰️ **49** 已失效归档。

## 核心特性

- **380 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 43ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 2 | 60ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 3 | 60ms | Microsoftedge | 0.27 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 4 | 70ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 76ms | Linkedin | 0.27 MB/s | `https://linkedin.com` | 通用代理 |
| 6 | 81ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 7 | 84ms | Deno | 0.28 MB/s | `https://deno.com` | 通用代理 |
| 8 | 85ms | Dilo-d14 | 0.17 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 9 | 87ms | Huly-mcp | 0.17 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 10 | 88ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 11 | 88ms | Img | - | `https://img.shields.io` | 通用代理 |
| 12 | 88ms | Kighelper-cloud | 0.09 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 13 | 88ms | Opresume | 0.43 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 14 | 88ms | Wordpaper | 0.36 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 15 | 88ms | X | 0.8 MB/s | `https://x.com` | 通用代理 |
| 16 | 90ms | Tools | 1.44 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 17 | 90ms | Xjtu-nyxf-study-material | 0.13 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 18 | 92ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 19 | 93ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 20 | 95ms | Githubstatus | 0.96 MB/s | `https://githubstatus.com` | 通用代理 |
| 21 | 95ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 22 | 97ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 23 | 98ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 24 | 98ms | Gpui | 0.27 MB/s | `https://gpui.rs` | 通用代理 |
| 25 | 99ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 26 | 105ms | Impeccable | 0.91 MB/s | `https://impeccable.style` | 通用代理 |
| 27 | 108ms | Godocs | 0.05 MB/s | `https://godocs.io` | 通用代理 |
| 28 | 109ms | Crypto-funding-arbitrage | 0.08 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 29 | 109ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 30 | 110ms | Alas | 0.94 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 31 | 110ms | Freeport | 0.05 MB/s | `https://freeport.network` | 通用代理 |
| 32 | 111ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 33 | 111ms | Caw | 0.07 MB/s | `https://caw.rocks` | 通用代理 |
| 34 | 111ms | Impro | 1.89 MB/s | `https://impro.social` | 通用代理 |
| 35 | 114ms | App | 0.07 MB/s | `https://app.netlify.com` | 通用代理 |
| 36 | 116ms | Zebrunner | 1.09 MB/s | `https://zebrunner.com` | 通用代理 |
| 37 | 118ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 38 | 118ms | Serac | 0.09 MB/s | `https://serac.build` | 通用代理 |
| 39 | 119ms | Clayrune | 0.17 MB/s | `https://clayrune.io` | 通用代理 |
| 40 | 120ms | Anh | 0.22 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 41 | 120ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 42 | 120ms | L4d2 | 0.15 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 43 | 120ms | Opencovibe | 0.5 MB/s | `https://opencovibe.com` | 通用代理 |
| 44 | 121ms | Codeeraser | 0.12 MB/s | `https://codeeraser.dev` | 通用代理 |
| 45 | 121ms | Lawyer-yu | 0.05 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 46 | 121ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 47 | 121ms | Resume-5lv | 0.19 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 48 | 122ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 49 | 124ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 50 | 124ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 51 | 125ms | Agentlimb | 0.26 MB/s | `https://agentlimb.com` | 通用代理 |
| 52 | 126ms | Tokei | 0.56 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 53 | 128ms | Polgarand | 0.1 MB/s | `https://polgarand.org` | 通用代理 |
| 54 | 129ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 55 | 129ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 56 | 129ms | Thumb | 1.37 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 57 | 130ms | Chops | 0.04 MB/s | `https://chops.md` | 通用代理 |
| 58 | 130ms | Coffeecli | 0.09 MB/s | `https://coffeecli.com` | 通用代理 |
| 59 | 131ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 60 | 133ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 61 | 133ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 62 | 134ms | Gitea-mirror | 0.56 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 63 | 135ms | Discord | 0.07 MB/s | `https://discord.gg` | 通用代理 |
| 64 | 136ms | Bananaslides | 0.35 MB/s | `https://bananaslides.online` | 通用代理 |
| 65 | 136ms | Cognitum | 0.26 MB/s | `https://cognitum.one` | 通用代理 |
| 66 | 137ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 67 | 137ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 68 | 137ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 69 | 137ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 70 | 138ms | Vibesql | 0.13 MB/s | `https://vibesql.org` | 通用代理 |
| 71 | 139ms | Gh | 1.77 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 72 | 139ms | Glass | 0.21 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 73 | 143ms | Gh | 1.95 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 74 | 143ms | Github | 2.07 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 75 | 144ms | Github | 2.09 MB/s | `https://github.788787.xyz` | 通用代理 |
| 76 | 144ms | Gp | 2.23 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 77 | 144ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 78 | 145ms | Git | 2.34 MB/s | `https://git.820828.xyz` | 通用代理 |
| 79 | 145ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 80 | 146ms | Git | 2.09 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 81 | 147ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 82 | 148ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 83 | 148ms | Cody | 0.28 MB/s | `https://cody.todyle.com` | 通用代理 |
| 84 | 148ms | Openpua | 0.42 MB/s | `https://openpua.ai` | 通用代理 |
| 85 | 149ms | Ghproxy | 2.1 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 86 | 149ms | Play | 0.05 MB/s | `https://play.templatical.com` | 通用代理 |
| 87 | 149ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 88 | 150ms | Miaozitie | 0.07 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 89 | 154ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 90 | 155ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 91 | 162ms | GH Monlor | 0.77 MB/s | `https://gh.monlor.com` | 通用代理 |
| 92 | 162ms | GH-Proxy | 0.79 MB/s | `https://gh-proxy.com` | 通用代理 |
| 93 | 165ms | Bestdori | 0.09 MB/s | `https://bestdori.com` | 通用代理 |
| 94 | 165ms | Github | 2.02 MB/s | `https://github.880824.xyz` | 通用代理 |
| 95 | 165ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 96 | 166ms | Gh | 1.01 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 97 | 168ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 98 | 170ms | Tms | 0.1 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 99 | 175ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 100 | 176ms | Ghproxy | 1.9 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 101 | 177ms | Holyclaude | 0.14 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 102 | 177ms | Training | 0.19 MB/s | `https://training.ti.com` | 通用代理 |
| 103 | 177ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 104 | 178ms | Music-cli | 0.18 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 105 | 180ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 106 | 183ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 107 | 184ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 108 | 184ms | Github | 2.1 MB/s | `https://github.ihnic.com` | 通用代理 |
| 109 | 184ms | Opensunsama | 0.04 MB/s | `https://opensunsama.com` | 通用代理 |
| 110 | 184ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 111 | 185ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 112 | 185ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 113 | 186ms | Cbrowser | 0.9 MB/s | `https://cbrowser.ai` | 通用代理 |
| 114 | 187ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 115 | 188ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 116 | 190ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 117 | 191ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 118 | 191ms | Contrib | 0.3 MB/s | `https://contrib.rocks` | 通用代理 |
| 119 | 192ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 120 | 194ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 121 | 194ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 122 | 195ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 123 | 196ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 124 | 196ms | Twitter | 0.78 MB/s | `https://twitter.com` | 通用代理 |
| 125 | 197ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 126 | 198ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 127 | 198ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 128 | 199ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 129 | 204ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 130 | 208ms | Paypal | 0.02 MB/s | `https://paypal.com` | 通用代理 |
| 131 | 208ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 132 | 209ms | Ampcode | 0.27 MB/s | `https://ampcode.com` | 通用代理 |
| 133 | 209ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 134 | 209ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 135 | 210ms | Components | 0.1 MB/s | `https://components.dereekb.com` | 通用代理 |
| 136 | 212ms | Axios-http | 0.31 MB/s | `https://axios-http.com` | 通用代理 |
| 137 | 212ms | Microcoreos | 0.33 MB/s | `https://microcoreos.com` | 通用代理 |
| 138 | 212ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 139 | 213ms | Tvv | 2.27 MB/s | `https://tvv.tw` | 通用代理 |
| 140 | 214ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 141 | 216ms | Caiji | 0.12 MB/s | `https://caiji.cyou` | 通用代理 |
| 142 | 218ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 143 | 220ms | FastGit CC | 0.89 MB/s | `https://fastgit.cc` | 通用代理 |
| 144 | 222ms | Ginlix | 0.41 MB/s | `https://ginlix.ai` | 通用代理 |
| 145 | 222ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 146 | 224ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 147 | 224ms | Ode | - | `https://ode.fun` | 通用代理 |
| 148 | 227ms | Gh | 1.8 MB/s | `https://gh.1k.ink` | 通用代理 |
| 149 | 227ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 150 | 228ms | GH-Proxy Org | 0.97 MB/s | `https://gh-proxy.org` | 通用代理 |
| 151 | 228ms | Kenyu | 2.28 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 152 | 230ms | Cursor | 0.35 MB/s | `https://cursor.com` | 通用代理 |
| 153 | 230ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 154 | 231ms | CrashMC CDN | 1.0 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 155 | 232ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 156 | 233ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 157 | 234ms | Api | 0.1 MB/s | `https://api.solov.cc` | 通用代理 |
| 158 | 236ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 159 | 237ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 160 | 237ms | Visionmemorymcp | 0.24 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 161 | 239ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 162 | 241ms | Clypra | 0.04 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 163 | 244ms | Aka | 0.43 MB/s | `https://aka.ms` | 通用代理 |
| 164 | 246ms | Ghproxy | 0.89 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 165 | 246ms | Nisar | 0.94 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 166 | 251ms | Aiblackboxfc | 0.29 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 167 | 251ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 168 | 252ms | Sub | 0.08 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 169 | 253ms | Code | 1.09 MB/s | `https://code.claude.com` | 通用代理 |
| 170 | 254ms | Gsd | 0.11 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 171 | 255ms | Ggg | 2.33 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 172 | 255ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 173 | 260ms | Coreos | 1.5 MB/s | `https://coreos.com` | 通用代理 |
| 174 | 260ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 175 | 265ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 176 | 267ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 177 | 269ms | Agoramarket | 0.81 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 178 | 272ms | Worldofclaudecraft | 0.9 MB/s | `https://worldofclaudecraft.com` | 通用代理 |
| 179 | 274ms | Ai-watch | 0.01 MB/s | `https://ai-watch.dev` | 通用代理 |
| 180 | 274ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 181 | 276ms | Claude | 0.29 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 182 | 276ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 183 | 279ms | Flashtype | 0.14 MB/s | `https://flashtype.com` | 通用代理 |
| 184 | 279ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 185 | 279ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 186 | 282ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 187 | 286ms | Kuroutoshikou | 0.53 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 188 | 289ms | Gh | 0.75 MB/s | `https://gh.padao.fun` | 通用代理 |
| 189 | 289ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 190 | 290ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 191 | 292ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 192 | 298ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 193 | 298ms | Tiktok | 0.08 MB/s | `https://tiktok.com` | 通用代理 |
| 194 | 299ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 195 | 300ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 196 | 306ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 197 | 308ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 198 | 311ms | B23 | - | `https://b23.tv` | 通用代理 |
| 199 | 312ms | Youtu | 1.26 MB/s | `https://youtu.be` | 通用代理 |
| 200 | 314ms | Steamcommunity | 0.11 MB/s | `https://steamcommunity.com` | 通用代理 |
| 201 | 314ms | Weaverse | 0.38 MB/s | `https://weaverse.io` | 通用代理 |
| 202 | 316ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 203 | 317ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 204 | 318ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 205 | 318ms | You | 0.05 MB/s | `https://you.piccalc.com` | 通用代理 |
| 206 | 326ms | Github | 1.01 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 207 | 328ms | 30006000 | 0.8 MB/s | `https://30006000.xyz` | 通用代理 |
| 208 | 328ms | Aomedia | 0.22 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 209 | 328ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 210 | 332ms | Sonarcloud | 0.02 MB/s | `https://sonarcloud.io` | 通用代理 |
| 211 | 335ms | Agenticcorporation | 0.03 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 212 | 335ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 213 | 339ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 214 | 341ms | Ednovas Mirror | 0.57 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 215 | 342ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 216 | 343ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 217 | 343ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 218 | 356ms | Hk | 0.93 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 219 | 364ms | Agent-room | 0.01 MB/s | `https://agent-room.com` | 通用代理 |
| 220 | 365ms | Github | 2.17 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 221 | 366ms | Adult | 0.02 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 222 | 372ms | Store | 0.97 MB/s | `https://store.steampowered.com` | 通用代理 |
| 223 | 376ms | Bailian | 0.11 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 224 | 379ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 225 | 381ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 226 | 382ms | GHFast | 0.41 MB/s | `https://ghfast.top` | 通用代理 |
| 227 | 395ms | GH Nxnow | 0.4 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 228 | 398ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 229 | 403ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 230 | 404ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 231 | 405ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 232 | 408ms | Github | 2.14 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 233 | 409ms | Aps | 0.02 MB/s | `https://aps.com` | 通用代理 |
| 234 | 415ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 235 | 417ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 236 | 417ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 237 | 419ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 238 | 425ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 239 | 427ms | YYLX Git | 0.75 MB/s | `https://git.yylx.win` | 通用代理 |
| 240 | 429ms | Gh | 0.63 MB/s | `https://gh.noki.icu` | 通用代理 |
| 241 | 431ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 242 | 432ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 243 | 435ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 244 | 438ms | Github | 1.88 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 245 | 450ms | Bible-ai-explorer | 0.04 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 246 | 453ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 247 | 455ms | Getgit | 2.25 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 248 | 465ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 249 | 465ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 250 | 469ms | Ark | 0.55 MB/s | `https://ark.intel.com` | 通用代理 |
| 251 | 478ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 252 | 481ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 253 | 481ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 254 | 481ms | Wl | - | `https://wl.do` | 通用代理 |
| 255 | 485ms | Safedocx | 0.08 MB/s | `https://safedocx.com` | 通用代理 |
| 256 | 487ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 257 | 491ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 258 | 494ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 259 | 505ms | Lecvdemarius | 0.05 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 260 | 508ms | Easyboardgame | 0.01 MB/s | `https://easyboardgame.top` | 通用代理 |
| 261 | 509ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 262 | 512ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 263 | 516ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 264 | 516ms | Support | 0.11 MB/s | `https://support.apple.com` | 通用代理 |
| 265 | 519ms | Patchworkos | 0.27 MB/s | `https://patchworkos.com` | 通用代理 |
| 266 | 530ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 267 | 532ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 268 | 537ms | Readsync | 0.01 MB/s | `https://readsync.org` | 通用代理 |
| 269 | 537ms | Umami-mcp | 0.39 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 270 | 541ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 271 | 548ms | Agentkey | 0.42 MB/s | `https://agentkey.app` | 通用代理 |
| 272 | 549ms | Lucky | 0.45 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 273 | 556ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 274 | 556ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 275 | 558ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 276 | 559ms | Aosmd | 0.1 MB/s | `https://aosmd.com` | 通用代理 |
| 277 | 561ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 278 | 562ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 279 | 563ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 280 | 564ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 281 | 572ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 282 | 585ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 283 | 589ms | Gh | 0.71 MB/s | `https://gh.39.al` | 通用代理 |
| 284 | 609ms | Github | 0.42 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 285 | 615ms | Os | 0.03 MB/s | `https://os.ryo.lu` | 通用代理 |
| 286 | 629ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 287 | 643ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 288 | 644ms | Gh | 0.25 MB/s | `https://gh.dpik.top` | 通用代理 |
| 289 | 646ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 290 | 648ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 291 | 656ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 292 | 678ms | Clawbiz | 0.02 MB/s | `https://clawbiz.io` | 通用代理 |
| 293 | 679ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 294 | 683ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 295 | 685ms | Im | 0.13 MB/s | `https://im.codes` | 通用代理 |
| 296 | 690ms | Ghproxy | 0.27 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 297 | 706ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 298 | 713ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 299 | 718ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 300 | 725ms | Fastfile | 1.11 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 301 | 732ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 302 | 738ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 303 | 749ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 304 | 757ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 305 | 762ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 306 | 773ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 307 | 783ms | Git | 0.23 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 308 | 808ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 309 | 811ms | Aif | 0.03 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 310 | 814ms | Docs | 0.15 MB/s | `https://docs.transifex.com` | 通用代理 |
| 311 | 822ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 312 | 829ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 313 | 848ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 314 | 865ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 315 | 875ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 316 | 894ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 317 | 919ms | Yibiao | 0.13 MB/s | `https://yibiao.pro` | 通用代理 |
| 318 | 920ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 319 | 926ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 320 | 932ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 321 | 949ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 322 | 957ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 323 | 964ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 324 | 975ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 325 | 982ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 326 | 989ms | Kw-aigc | - | `https://kw-aigc.cn` | 通用代理 |
| 327 | 1035ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 328 | 1040ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 329 | 1043ms | Web | - | `https://web.4399.com` | 通用代理 |
| 330 | 1090ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 331 | 1092ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 332 | 1098ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 333 | 1120ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 334 | 1121ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 335 | 1122ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 336 | 1160ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 337 | 1162ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 338 | 1164ms | Atomcode | 0.05 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 339 | 1165ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 340 | 1177ms | Ghproxy | 0.28 MB/s | `https://ghproxy.cc` | 通用代理 |
| 341 | 1229ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 342 | 1230ms | V | - | `https://v.douyin.com` | 通用代理 |
| 343 | 1240ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 344 | 1242ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 345 | 1270ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 346 | 1295ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 347 | 1307ms | Github | 0.14 MB/s | `https://github.chenc.dev` | 通用代理 |
| 348 | 1325ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 349 | 1344ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 350 | 1366ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 351 | 1384ms | Git | 0.27 MB/s | `https://git.669966.xyz` | 通用代理 |
| 352 | 1407ms | Cf | 0.24 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 353 | 1620ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 354 | 1630ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 355 | 1675ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 356 | 1715ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 357 | 1862ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 358 | 1989ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 359 | 2113ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 360 | 2222ms | Img | - | `https://img.ink` | 通用代理 |
| 361 | 2331ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 362 | 2467ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 363 | 2933ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 364 | 2958ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 365 | 2959ms | Wget | - | `https://wget.la` | 通用代理 |
| 366 | 3252ms | G | 0.16 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 367 | 3482ms | Ghproxy | 0.04 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 368 | 4030ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHProxy Net (`ghproxy-net`) | 1 次 |
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 1 次 |
| Npee Down (`down-npee-cn`) | 23 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Gh (`gh-halonice-com`) | 22 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Gh (`gh-b52m-cn`) | 4 次 |
| 5555 (`5555-cab`) | 13 次 |
| Doxygen (`doxygen-org`) | 9 次 |
| Maplecode (`maplecode-art`) | 2 次 |
| Mobilevc (`mobilevc-top`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 373 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **380** | |

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
