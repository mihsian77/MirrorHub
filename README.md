# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-26T12:22:34Z**，每 6 小时刷新一次。当前 ✅ **367** 在线 / ⚠️ **16** 不稳定 / ⚰️ **49** 已失效归档。

## 核心特性

- **383 个节点**，4 大分类，全部经过测速验证
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
| 2 | 60ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 3 | 60ms | Microsoftedge | 0.17 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 4 | 69ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 78ms | Linkedin | 0.51 MB/s | `https://linkedin.com` | 通用代理 |
| 6 | 80ms | Deno | 0.55 MB/s | `https://deno.com` | 通用代理 |
| 7 | 82ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 8 | 84ms | Dilo-d14 | 0.13 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 9 | 87ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 10 | 87ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 11 | 88ms | Img | - | `https://img.shields.io` | 通用代理 |
| 12 | 88ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 13 | 88ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 14 | 90ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 15 | 92ms | Osf | 0.08 MB/s | `https://osf.io` | 通用代理 |
| 16 | 92ms | X | 0.93 MB/s | `https://x.com` | 通用代理 |
| 17 | 94ms | Githubstatus | 2.4 MB/s | `https://githubstatus.com` | 通用代理 |
| 18 | 94ms | Huly-mcp | 0.06 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 19 | 94ms | Kighelper-cloud | 0.1 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 20 | 95ms | Godocs | 0.1 MB/s | `https://godocs.io` | 通用代理 |
| 21 | 95ms | Wordpaper | 0.33 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 22 | 96ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 23 | 97ms | Opresume | 0.56 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 24 | 97ms | Xjtu-nyxf-study-material | 0.21 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 25 | 99ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 26 | 104ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 27 | 105ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 28 | 106ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 29 | 110ms | Lawyer-yu | 0.22 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 30 | 111ms | Tools | 2.93 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 31 | 112ms | Impeccable | 0.99 MB/s | `https://impeccable.style` | 通用代理 |
| 32 | 113ms | App | 0.22 MB/s | `https://app.netlify.com` | 通用代理 |
| 33 | 118ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 34 | 118ms | Impro | 2.24 MB/s | `https://impro.social` | 通用代理 |
| 35 | 119ms | Zebrunner | 3.45 MB/s | `https://zebrunner.com` | 通用代理 |
| 36 | 120ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 37 | 121ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 38 | 121ms | Gpui | 0.23 MB/s | `https://gpui.rs` | 通用代理 |
| 39 | 122ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 40 | 122ms | Resume-5lv | 0.25 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 41 | 124ms | App | 0.06 MB/s | `https://app.codecov.io` | 通用代理 |
| 42 | 125ms | Serac | 0.07 MB/s | `https://serac.build` | 通用代理 |
| 43 | 126ms | Agentlimb | 0.25 MB/s | `https://agentlimb.com` | 通用代理 |
| 44 | 128ms | Opentakeoff | 0.12 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 45 | 129ms | Clayrune | 0.18 MB/s | `https://clayrune.io` | 通用代理 |
| 46 | 129ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 47 | 129ms | Thumb | 6.23 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 48 | 130ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 49 | 130ms | Anh | 0.2 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 50 | 132ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 51 | 132ms | Discord | 0.13 MB/s | `https://discord.gg` | 通用代理 |
| 52 | 132ms | L4d2 | 0.17 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 53 | 134ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 54 | 134ms | Tokei | 0.47 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 55 | 134ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 56 | 135ms | Caw | 0.07 MB/s | `https://caw.rocks` | 通用代理 |
| 57 | 135ms | Cognitum | 0.18 MB/s | `https://cognitum.one` | 通用代理 |
| 58 | 136ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 59 | 136ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 60 | 136ms | Opencovibe | 0.37 MB/s | `https://opencovibe.com` | 通用代理 |
| 61 | 137ms | Vibesql | 0.13 MB/s | `https://vibesql.org` | 通用代理 |
| 62 | 138ms | Codeeraser | 0.11 MB/s | `https://codeeraser.dev` | 通用代理 |
| 63 | 138ms | Gh | 1.78 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 64 | 138ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 65 | 139ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 66 | 139ms | Goreportcard | 0.05 MB/s | `https://goreportcard.com` | 通用代理 |
| 67 | 141ms | Github | 2.79 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 68 | 141ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 69 | 143ms | Coffeecli | 0.12 MB/s | `https://coffeecli.com` | 通用代理 |
| 70 | 143ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 71 | 145ms | Gh | 3.14 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 72 | 145ms | Gitea-mirror | 0.94 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 73 | 146ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 74 | 147ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 75 | 147ms | Git | 2.68 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 76 | 147ms | Gp | 2.29 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 77 | 148ms | Git | 2.61 MB/s | `https://git.820828.xyz` | 通用代理 |
| 78 | 148ms | Github | 2.59 MB/s | `https://github.788787.xyz` | 通用代理 |
| 79 | 148ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 80 | 150ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 81 | 150ms | Miaozitie | 0.09 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 82 | 151ms | Cody | 0.26 MB/s | `https://cody.todyle.com` | 通用代理 |
| 83 | 151ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 84 | 152ms | Alas | 0.82 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 85 | 152ms | Glass | 0.21 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 86 | 152ms | Music-cli | 0.3 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 87 | 152ms | Openpua | 0.51 MB/s | `https://openpua.ai` | 通用代理 |
| 88 | 153ms | Bestdori | 0.1 MB/s | `https://bestdori.com` | 通用代理 |
| 89 | 153ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 90 | 153ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 91 | 154ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 92 | 154ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 93 | 155ms | GH-Proxy | 2.09 MB/s | `https://gh-proxy.com` | 通用代理 |
| 94 | 157ms | Tms | 0.15 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 95 | 158ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 96 | 160ms | Shiori-v1 | 0.05 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 97 | 161ms | Cbrowser | 1.96 MB/s | `https://cbrowser.ai` | 通用代理 |
| 98 | 166ms | Bananaslides | 0.32 MB/s | `https://bananaslides.online` | 通用代理 |
| 99 | 166ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 100 | 167ms | Gh | 2.02 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 101 | 167ms | Github | 2.43 MB/s | `https://github.880824.xyz` | 通用代理 |
| 102 | 170ms | Ghproxy | 1.67 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 103 | 172ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 104 | 174ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 105 | 174ms | Contrib | 0.52 MB/s | `https://contrib.rocks` | 通用代理 |
| 106 | 174ms | Openttd | 0.06 MB/s | `https://openttd.org` | 通用代理 |
| 107 | 175ms | Bolt2github | 0.13 MB/s | `https://bolt2github.com` | 通用代理 |
| 108 | 175ms | Caiji | 0.08 MB/s | `https://caiji.cyou` | 通用代理 |
| 109 | 175ms | Training | 0.23 MB/s | `https://training.ti.com` | 通用代理 |
| 110 | 176ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 111 | 176ms | Opensunsama | 0.08 MB/s | `https://opensunsama.com` | 通用代理 |
| 112 | 178ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 113 | 178ms | GH Monlor | 1.89 MB/s | `https://gh.monlor.com` | 通用代理 |
| 114 | 179ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 115 | 179ms | Polgarand | 0.03 MB/s | `https://polgarand.org` | 通用代理 |
| 116 | 182ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 117 | 183ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 118 | 183ms | Holyclaude | 0.18 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 119 | 186ms | Ai-trend-publish | 0.05 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 120 | 186ms | Kuroutoshikou | 0.99 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 121 | 187ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 122 | 187ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 123 | 187ms | Github | 2.07 MB/s | `https://github.ihnic.com` | 通用代理 |
| 124 | 188ms | Components | 0.14 MB/s | `https://components.dereekb.com` | 通用代理 |
| 125 | 188ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 126 | 191ms | Congressmcp | 0.04 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 127 | 192ms | Ghproxy | 2.72 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 128 | 194ms | Ode | - | `https://ode.fun` | 通用代理 |
| 129 | 196ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 130 | 197ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 131 | 198ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 132 | 199ms | Pidash | 0.02 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 133 | 202ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 134 | 204ms | GH-Proxy Org | 1.3 MB/s | `https://gh-proxy.org` | 通用代理 |
| 135 | 205ms | Twitter | 0.98 MB/s | `https://twitter.com` | 通用代理 |
| 136 | 206ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 137 | 206ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 138 | 206ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 139 | 207ms | Ginlix | 0.77 MB/s | `https://ginlix.ai` | 通用代理 |
| 140 | 209ms | Gsd | 0.47 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 141 | 209ms | Themolt | 0.05 MB/s | `https://themolt.net` | 通用代理 |
| 142 | 210ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 143 | 213ms | Phabricator | 0.13 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 144 | 216ms | Kenyu | 2.18 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 145 | 217ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 146 | 219ms | Ampcode | 0.24 MB/s | `https://ampcode.com` | 通用代理 |
| 147 | 219ms | FastGit CC | 1.1 MB/s | `https://fastgit.cc` | 通用代理 |
| 148 | 220ms | Microcoreos | 0.39 MB/s | `https://microcoreos.com` | 通用代理 |
| 149 | 222ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 150 | 222ms | Tvv | 1.59 MB/s | `https://tvv.tw` | 通用代理 |
| 151 | 222ms | Wings | 0.04 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 152 | 224ms | Gh | 2.53 MB/s | `https://gh.1k.ink` | 通用代理 |
| 153 | 224ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 154 | 227ms | Axios-http | 1.3 MB/s | `https://axios-http.com` | 通用代理 |
| 155 | 227ms | CrashMC CDN | 2.47 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 156 | 228ms | Cursor | 0.95 MB/s | `https://cursor.com` | 通用代理 |
| 157 | 229ms | Clypra | 0.09 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 158 | 230ms | Aka | 1.04 MB/s | `https://aka.ms` | 通用代理 |
| 159 | 230ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 160 | 233ms | Aiblackboxfc | 0.42 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 161 | 233ms | Ggg | 2.67 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 162 | 233ms | Zuckerbot | 0.05 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 163 | 235ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 164 | 236ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 165 | 238ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 166 | 239ms | Coreos | 5.36 MB/s | `https://coreos.com` | 通用代理 |
| 167 | 240ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 168 | 242ms | Ghproxy | 0.58 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 169 | 243ms | Api | 0.05 MB/s | `https://api.solov.cc` | 通用代理 |
| 170 | 243ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 171 | 248ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 172 | 249ms | Nisar | 0.86 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 173 | 255ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 174 | 257ms | Visionmemorymcp | 0.22 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 175 | 258ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 176 | 259ms | Sub | 0.45 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 177 | 261ms | Code | 1.94 MB/s | `https://code.claude.com` | 通用代理 |
| 178 | 262ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 179 | 265ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 180 | 272ms | Agoramarket | 0.58 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 181 | 272ms | Claude | 0.34 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 182 | 272ms | Tiktok | 0.3 MB/s | `https://tiktok.com` | 通用代理 |
| 183 | 277ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 184 | 279ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 185 | 282ms | Youtu | 2.5 MB/s | `https://youtu.be` | 通用代理 |
| 186 | 285ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 187 | 285ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 188 | 294ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 189 | 297ms | Sonarcloud | 0.02 MB/s | `https://sonarcloud.io` | 通用代理 |
| 190 | 299ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 191 | 299ms | Gh | 0.46 MB/s | `https://gh.padao.fun` | 通用代理 |
| 192 | 300ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 193 | 300ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 194 | 304ms | Agenticcorporation | 0.06 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 195 | 305ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 196 | 308ms | Github | 0.57 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 197 | 310ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 198 | 312ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 199 | 312ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 200 | 314ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 201 | 316ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 202 | 316ms | Weaverse | 0.79 MB/s | `https://weaverse.io` | 通用代理 |
| 203 | 320ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 204 | 320ms | Radio-browser | 0.05 MB/s | `https://radio-browser.info` | 通用代理 |
| 205 | 320ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 206 | 321ms | 30006000 | 0.38 MB/s | `https://30006000.xyz` | 通用代理 |
| 207 | 321ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 208 | 324ms | B23 | - | `https://b23.tv` | 通用代理 |
| 209 | 325ms | Steamcommunity | 0.16 MB/s | `https://steamcommunity.com` | 通用代理 |
| 210 | 328ms | Aomedia | 0.32 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 211 | 339ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 212 | 343ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 213 | 344ms | Github | 1.7 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 214 | 345ms | GHFast | 0.48 MB/s | `https://ghfast.top` | 通用代理 |
| 215 | 346ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 216 | 357ms | Ednovas Mirror | 0.4 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 217 | 357ms | Hk | 1.44 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 218 | 365ms | Bailian | 0.04 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 219 | 367ms | Autonomi | 0.03 MB/s | `https://autonomi.dev` | 通用代理 |
| 220 | 367ms | Store | 1.77 MB/s | `https://store.steampowered.com` | 通用代理 |
| 221 | 369ms | Turborepo-starter-kit-web | 0.14 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 222 | 370ms | You | 0.06 MB/s | `https://you.piccalc.com` | 通用代理 |
| 223 | 373ms | Github | 2.78 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 224 | 381ms | GH Nxnow | 0.67 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 225 | 382ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 226 | 383ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 227 | 383ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 228 | 391ms | Getgit | 2.39 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 229 | 393ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 230 | 394ms | App | 0.02 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 231 | 396ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 232 | 398ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 233 | 400ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 234 | 400ms | Gh | 0.44 MB/s | `https://gh.noki.icu` | 通用代理 |
| 235 | 401ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 236 | 407ms | Bseindia | - | `https://bseindia.com` | 通用代理 |
| 237 | 408ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 238 | 419ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 239 | 424ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 240 | 425ms | Aps | 0.02 MB/s | `https://aps.com` | 通用代理 |
| 241 | 425ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 242 | 429ms | Github | 3.15 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 243 | 433ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 244 | 437ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 245 | 442ms | Bible-ai-explorer | 0.12 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 246 | 444ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 247 | 448ms | Adult | 0.01 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 248 | 455ms | Readsync | 0.04 MB/s | `https://readsync.org` | 通用代理 |
| 249 | 458ms | Ark | 0.53 MB/s | `https://ark.intel.com` | 通用代理 |
| 250 | 458ms | Safedocx | 0.21 MB/s | `https://safedocx.com` | 通用代理 |
| 251 | 467ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 252 | 468ms | Agentkey | 0.5 MB/s | `https://agentkey.app` | 通用代理 |
| 253 | 482ms | Msdn | 0.15 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 254 | 488ms | Lecvdemarius | 0.11 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 255 | 489ms | Patchworkos | 0.36 MB/s | `https://patchworkos.com` | 通用代理 |
| 256 | 492ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 257 | 497ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 258 | 498ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 259 | 498ms | Wl | - | `https://wl.do` | 通用代理 |
| 260 | 501ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 261 | 501ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 262 | 505ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 263 | 506ms | Memstack | 0.04 MB/s | `https://memstack.pro` | 通用代理 |
| 264 | 510ms | Umami-mcp | 0.49 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 265 | 512ms | Sina | 0.45 MB/s | `https://sina.dev` | 通用代理 |
| 266 | 524ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 267 | 527ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 268 | 535ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 269 | 542ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 270 | 543ms | Lucky | 0.47 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 271 | 552ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 272 | 555ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 273 | 562ms | Aosmd | 0.26 MB/s | `https://aosmd.com` | 通用代理 |
| 274 | 570ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 275 | 571ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 276 | 573ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 277 | 575ms | Github | 0.17 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 278 | 576ms | 3d-set-visualizer | 0.06 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 279 | 583ms | Gh | 0.48 MB/s | `https://gh.39.al` | 通用代理 |
| 280 | 587ms | Internhack | 0.04 MB/s | `https://internhack.xyz` | 通用代理 |
| 281 | 593ms | Im | 0.69 MB/s | `https://im.codes` | 通用代理 |
| 282 | 601ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 283 | 602ms | Support | 1.33 MB/s | `https://support.apple.com` | 通用代理 |
| 284 | 618ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 285 | 638ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 286 | 643ms | Tsukuyomi | 0.14 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 287 | 646ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 288 | 647ms | Clawbiz | 0.07 MB/s | `https://clawbiz.io` | 通用代理 |
| 289 | 654ms | Gh | 0.4 MB/s | `https://gh.dpik.top` | 通用代理 |
| 290 | 657ms | Fastfile | 1.62 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 291 | 666ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 292 | 666ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 293 | 674ms | Os | 0.03 MB/s | `https://os.ryo.lu` | 通用代理 |
| 294 | 686ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 295 | 687ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 296 | 693ms | Agoracitizen | 0.03 MB/s | `https://agoracitizen.app` | 通用代理 |
| 297 | 701ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 298 | 711ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 299 | 715ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 300 | 735ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 301 | 736ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 302 | 758ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 303 | 776ms | Aif | 0.05 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 304 | 795ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 305 | 799ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 306 | 800ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 307 | 802ms | Docs | 0.29 MB/s | `https://docs.transifex.com` | 通用代理 |
| 308 | 803ms | Git | 0.19 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 309 | 810ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 310 | 814ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 311 | 848ms | Task | 0.01 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 312 | 864ms | Ccgather | 0.04 MB/s | `https://ccgather.com` | 通用代理 |
| 313 | 880ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 314 | 891ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 315 | 895ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 316 | 928ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 317 | 933ms | Mimo | 0.16 MB/s | `https://mimo.mi.com` | 通用代理 |
| 318 | 940ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 319 | 950ms | Yibiao | 0.11 MB/s | `https://yibiao.pro` | 通用代理 |
| 320 | 966ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 321 | 974ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 322 | 975ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 323 | 987ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 324 | 998ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 325 | 1003ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 326 | 1013ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 327 | 1016ms | Web | - | `https://web.4399.com` | 通用代理 |
| 328 | 1020ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 329 | 1059ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 330 | 1080ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 331 | 1097ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 332 | 1116ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 333 | 1141ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 334 | 1160ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 335 | 1162ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 336 | 1164ms | V | - | `https://v.douyin.com` | 通用代理 |
| 337 | 1173ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 338 | 1192ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 339 | 1194ms | Ghproxy | 0.23 MB/s | `https://ghproxy.cc` | 通用代理 |
| 340 | 1204ms | Atomcode | 0.03 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 341 | 1212ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 342 | 1222ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 343 | 1225ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 344 | 1289ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 345 | 1302ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 346 | 1313ms | Github | 0.12 MB/s | `https://github.chenc.dev` | 通用代理 |
| 347 | 1348ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 348 | 1370ms | Cf | 0.24 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 349 | 1406ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 350 | 1426ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 351 | 1509ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 352 | 1590ms | I-qps | 0.02 MB/s | `https://i-qps.net` | 通用代理 |
| 353 | 1636ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 354 | 1714ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 355 | 1989ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 356 | 2054ms | Img | - | `https://img.ink` | 通用代理 |
| 357 | 2217ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 358 | 2250ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 359 | 2353ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 360 | 2444ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 361 | 2453ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 362 | 2868ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 363 | 2928ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 364 | 3072ms | Ghproxy | 0.19 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 365 | 3315ms | Gh | 0.08 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 366 | 3361ms | G | 0.02 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 367 | 4309ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（16 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHProxy Net (`ghproxy-net`) | 1 次 |
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| YYLX Git (`git-yylx-win`) | 1 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 4 次 |
| Npee Down (`down-npee-cn`) | 26 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Gh (`gh-halonice-com`) | 25 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 5 次 |
| Proxy (`proxy-vvvv-ee`) | 3 次 |
| 5555 (`5555-cab`) | 16 次 |
| Doxygen (`doxygen-org`) | 12 次 |
| Flashtype (`flashtype-com`) | 3 次 |
| Maplecode (`maplecode-art`) | 5 次 |
| Mobilevc (`mobilevc-top`) | 1 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 376 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **383** | |

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
