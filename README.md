# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-26T22:23:29Z**，每 6 小时刷新一次。当前 ✅ **370** 在线 / ⚠️ **13** 不稳定 / ⚰️ **49** 已失效归档。

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
| 1 | 47ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 2 | 61ms | Microsoftedge | 0.63 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 66ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 4 | 67ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 75ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 6 | 81ms | Deno | 0.7 MB/s | `https://deno.com` | 通用代理 |
| 7 | 82ms | Linkedin | 0.23 MB/s | `https://linkedin.com` | 通用代理 |
| 8 | 88ms | Dilo-d14 | 0.12 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 9 | 88ms | Img | - | `https://img.shields.io` | 通用代理 |
| 10 | 89ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 11 | 90ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 12 | 92ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 13 | 92ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 14 | 94ms | Wordpaper | 0.31 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 15 | 94ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 16 | 95ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 17 | 95ms | Godocs | 0.08 MB/s | `https://godocs.io` | 通用代理 |
| 18 | 95ms | X | 0.94 MB/s | `https://x.com` | 通用代理 |
| 19 | 96ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 20 | 96ms | Kighelper-cloud | 0.08 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 21 | 98ms | Githubstatus | 1.0 MB/s | `https://githubstatus.com` | 通用代理 |
| 22 | 99ms | Crypto-funding-arbitrage | 0.08 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 23 | 100ms | Xjtu-nyxf-study-material | 0.09 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 24 | 105ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 25 | 109ms | Opresume | 0.42 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 26 | 110ms | Huly-mcp | 0.13 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 27 | 110ms | Lawyer-yu | 0.07 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 28 | 113ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 29 | 113ms | Resume-5lv | 0.16 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 30 | 113ms | Tools | 1.6 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 31 | 114ms | Impeccable | 1.11 MB/s | `https://impeccable.style` | 通用代理 |
| 32 | 115ms | App | 0.1 MB/s | `https://app.netlify.com` | 通用代理 |
| 33 | 115ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 34 | 116ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 35 | 120ms | Impro | 1.37 MB/s | `https://impro.social` | 通用代理 |
| 36 | 122ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 37 | 122ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 38 | 122ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 39 | 124ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 40 | 124ms | Zebrunner | 1.29 MB/s | `https://zebrunner.com` | 通用代理 |
| 41 | 127ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 42 | 128ms | Agentlimb | 0.15 MB/s | `https://agentlimb.com` | 通用代理 |
| 43 | 129ms | Thumb | 1.06 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 44 | 132ms | Gpui | 0.21 MB/s | `https://gpui.rs` | 通用代理 |
| 45 | 133ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 46 | 133ms | Clayrune | 0.1 MB/s | `https://clayrune.io` | 通用代理 |
| 47 | 133ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 48 | 133ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 49 | 134ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 50 | 135ms | Cognitum | 0.18 MB/s | `https://cognitum.one` | 通用代理 |
| 51 | 135ms | Gh | 1.26 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 52 | 135ms | Gp | 1.71 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 53 | 136ms | Discord | 0.06 MB/s | `https://discord.gg` | 通用代理 |
| 54 | 136ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 55 | 137ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 56 | 137ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 57 | 137ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 58 | 138ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 59 | 138ms | Github | 1.57 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 60 | 138ms | Vibesql | 0.07 MB/s | `https://vibesql.org` | 通用代理 |
| 61 | 139ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 62 | 139ms | Git | 1.23 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 63 | 141ms | Github | 1.61 MB/s | `https://github.788787.xyz` | 通用代理 |
| 64 | 142ms | Tokei | 0.46 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 65 | 143ms | Git | 1.36 MB/s | `https://git.820828.xyz` | 通用代理 |
| 66 | 144ms | Anh | 0.22 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 67 | 144ms | Gh | 1.71 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 68 | 145ms | Serac | 0.06 MB/s | `https://serac.build` | 通用代理 |
| 69 | 146ms | Demo | 0.02 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 70 | 146ms | L4d2 | 0.13 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 71 | 147ms | Coffeecli | 0.08 MB/s | `https://coffeecli.com` | 通用代理 |
| 72 | 148ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 73 | 148ms | Gitea-mirror | 0.71 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 74 | 149ms | Caw | 0.07 MB/s | `https://caw.rocks` | 通用代理 |
| 75 | 149ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 76 | 150ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 77 | 150ms | Github | 1.6 MB/s | `https://github.880824.xyz` | 通用代理 |
| 78 | 150ms | Opencovibe | 0.33 MB/s | `https://opencovibe.com` | 通用代理 |
| 79 | 150ms | Openpua | 0.51 MB/s | `https://openpua.ai` | 通用代理 |
| 80 | 151ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 81 | 151ms | GH-Proxy | 1.12 MB/s | `https://gh-proxy.com` | 通用代理 |
| 82 | 151ms | Glass | 0.18 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 83 | 152ms | Codeeraser | 0.09 MB/s | `https://codeeraser.dev` | 通用代理 |
| 84 | 152ms | Music-cli | 0.15 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 85 | 155ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 86 | 155ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 87 | 156ms | Alas | 0.54 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 88 | 156ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 89 | 157ms | Tms | 0.23 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 90 | 158ms | Ghproxy | 1.28 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 91 | 159ms | Miaozitie | 0.06 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 92 | 160ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 93 | 161ms | Bestdori | 0.09 MB/s | `https://bestdori.com` | 通用代理 |
| 94 | 163ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 95 | 165ms | Cody | 0.19 MB/s | `https://cody.todyle.com` | 通用代理 |
| 96 | 165ms | Gh | 0.99 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 97 | 165ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 98 | 167ms | Openttd | 0.03 MB/s | `https://openttd.org` | 通用代理 |
| 99 | 167ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 100 | 168ms | Cbrowser | 1.08 MB/s | `https://cbrowser.ai` | 通用代理 |
| 101 | 168ms | Contrib | 0.21 MB/s | `https://contrib.rocks` | 通用代理 |
| 102 | 168ms | Github | 1.8 MB/s | `https://github.ihnic.com` | 通用代理 |
| 103 | 168ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 104 | 169ms | GH Monlor | 0.96 MB/s | `https://gh.monlor.com` | 通用代理 |
| 105 | 172ms | Caiji | 0.08 MB/s | `https://caiji.cyou` | 通用代理 |
| 106 | 174ms | Polgarand | 0.05 MB/s | `https://polgarand.org` | 通用代理 |
| 107 | 175ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 108 | 176ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 109 | 178ms | Bananaslides | 0.35 MB/s | `https://bananaslides.online` | 通用代理 |
| 110 | 179ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 111 | 180ms | Holyclaude | 0.1 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 112 | 181ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 113 | 182ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 114 | 184ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 115 | 184ms | Opensunsama | 0.04 MB/s | `https://opensunsama.com` | 通用代理 |
| 116 | 185ms | Components | 0.07 MB/s | `https://components.dereekb.com` | 通用代理 |
| 117 | 185ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 118 | 186ms | Training | 0.13 MB/s | `https://training.ti.com` | 通用代理 |
| 119 | 187ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 120 | 187ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 121 | 188ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 122 | 188ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 123 | 188ms | Ghproxy | 1.58 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 124 | 189ms | Kuroutoshikou | 0.54 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 125 | 193ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 126 | 196ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 127 | 196ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 128 | 197ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 129 | 197ms | GH-Proxy Org | 0.66 MB/s | `https://gh-proxy.org` | 通用代理 |
| 130 | 198ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 131 | 200ms | Pidash | 0.04 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 132 | 201ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 133 | 202ms | Gsd | 0.23 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 134 | 204ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 135 | 204ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 136 | 204ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 137 | 205ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 138 | 208ms | Ode | - | `https://ode.fun` | 通用代理 |
| 139 | 211ms | Twitter | 0.49 MB/s | `https://twitter.com` | 通用代理 |
| 140 | 212ms | Ginlix | 0.43 MB/s | `https://ginlix.ai` | 通用代理 |
| 141 | 213ms | FastGit CC | 0.99 MB/s | `https://fastgit.cc` | 通用代理 |
| 142 | 214ms | CrashMC CDN | 0.62 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 143 | 214ms | Kenyu | 1.2 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 144 | 216ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 145 | 216ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 146 | 216ms | Tvv | 1.4 MB/s | `https://tvv.tw` | 通用代理 |
| 147 | 217ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 148 | 218ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 149 | 220ms | Ampcode | 0.19 MB/s | `https://ampcode.com` | 通用代理 |
| 150 | 222ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 151 | 222ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 152 | 224ms | Api | 0.09 MB/s | `https://api.solov.cc` | 通用代理 |
| 153 | 225ms | Gh | 1.41 MB/s | `https://gh.1k.ink` | 通用代理 |
| 154 | 227ms | Axios-http | 0.39 MB/s | `https://axios-http.com` | 通用代理 |
| 155 | 228ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 156 | 229ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 157 | 232ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 158 | 234ms | Cursor | 0.41 MB/s | `https://cursor.com` | 通用代理 |
| 159 | 234ms | Microcoreos | 0.25 MB/s | `https://microcoreos.com` | 通用代理 |
| 160 | 234ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 161 | 236ms | Aiblackboxfc | 0.27 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 162 | 236ms | Clypra | 0.05 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 163 | 237ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 164 | 239ms | Coreos | 1.83 MB/s | `https://coreos.com` | 通用代理 |
| 165 | 240ms | Ggg | 1.35 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 166 | 240ms | Ghproxy | 0.67 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 167 | 241ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 168 | 242ms | Aka | 0.44 MB/s | `https://aka.ms` | 通用代理 |
| 169 | 243ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 170 | 245ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 171 | 246ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 172 | 247ms | Nisar | 0.76 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 173 | 251ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 174 | 256ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 175 | 257ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 176 | 258ms | Sub | 0.13 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 177 | 261ms | Code | 1.5 MB/s | `https://code.claude.com` | 通用代理 |
| 178 | 262ms | Visionmemorymcp | 0.25 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 179 | 264ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 180 | 268ms | Agoramarket | 0.03 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 181 | 273ms | Github | 0.63 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 182 | 277ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 183 | 279ms | Tiktok | 0.14 MB/s | `https://tiktok.com` | 通用代理 |
| 184 | 281ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 185 | 289ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 186 | 290ms | Claude | 0.25 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 187 | 290ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 188 | 291ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 189 | 293ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 190 | 296ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 191 | 296ms | Youtu | 1.2 MB/s | `https://youtu.be` | 通用代理 |
| 192 | 297ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 193 | 299ms | Flashtype | - | `https://flashtype.com` | 通用代理 |
| 194 | 301ms | Gh | 0.51 MB/s | `https://gh.padao.fun` | 通用代理 |
| 195 | 305ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 196 | 307ms | Sonarcloud | 0.02 MB/s | `https://sonarcloud.io` | 通用代理 |
| 197 | 308ms | 30006000 | 0.66 MB/s | `https://30006000.xyz` | 通用代理 |
| 198 | 310ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 199 | 312ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 200 | 314ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 201 | 314ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 202 | 320ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 203 | 320ms | Weaverse | 0.52 MB/s | `https://weaverse.io` | 通用代理 |
| 204 | 321ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 205 | 323ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 206 | 323ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 207 | 323ms | Steamcommunity | 0.12 MB/s | `https://steamcommunity.com` | 通用代理 |
| 208 | 324ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 209 | 327ms | Aomedia | 0.24 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 210 | 330ms | B23 | - | `https://b23.tv` | 通用代理 |
| 211 | 332ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 212 | 338ms | GHFast | 0.62 MB/s | `https://ghfast.top` | 通用代理 |
| 213 | 339ms | Github | 1.2 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 214 | 341ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 215 | 350ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 216 | 351ms | Ednovas Mirror | 0.71 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 217 | 353ms | Store | 1.2 MB/s | `https://store.steampowered.com` | 通用代理 |
| 218 | 354ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 219 | 362ms | Github | 1.12 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 220 | 363ms | Sina | 0.81 MB/s | `https://sina.dev` | 通用代理 |
| 221 | 366ms | Bailian | 0.07 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 222 | 378ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 223 | 379ms | GH Nxnow | 0.81 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 224 | 379ms | Hk | 0.71 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 225 | 379ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 226 | 381ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 227 | 383ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 228 | 388ms | Getgit | 1.32 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 229 | 390ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 230 | 394ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 231 | 396ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 232 | 399ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 233 | 401ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 234 | 403ms | You | 0.13 MB/s | `https://you.piccalc.com` | 通用代理 |
| 235 | 406ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 236 | 406ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 237 | 411ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 238 | 413ms | Gh | 0.79 MB/s | `https://gh.noki.icu` | 通用代理 |
| 239 | 417ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 240 | 418ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 241 | 421ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 242 | 424ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 243 | 427ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 244 | 429ms | Github | 1.31 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 245 | 432ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 246 | 432ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 247 | 443ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 248 | 446ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 249 | 449ms | Bible-ai-explorer | 0.05 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 250 | 453ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 251 | 465ms | Safedocx | 0.1 MB/s | `https://safedocx.com` | 通用代理 |
| 252 | 468ms | Ark | 0.52 MB/s | `https://ark.intel.com` | 通用代理 |
| 253 | 470ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 254 | 477ms | Agentkey | 1.42 MB/s | `https://agentkey.app` | 通用代理 |
| 255 | 482ms | Lecvdemarius | 0.05 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 256 | 483ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 257 | 486ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 258 | 494ms | Patchworkos | 0.27 MB/s | `https://patchworkos.com` | 通用代理 |
| 259 | 495ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 260 | 498ms | Umami-mcp | 0.41 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 261 | 498ms | Wl | - | `https://wl.do` | 通用代理 |
| 262 | 499ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 263 | 502ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 264 | 509ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 265 | 514ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 266 | 528ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 267 | 532ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 268 | 541ms | Lucky | 0.42 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 269 | 542ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 270 | 549ms | Im | 0.63 MB/s | `https://im.codes` | 通用代理 |
| 271 | 554ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 272 | 558ms | Aosmd | 0.13 MB/s | `https://aosmd.com` | 通用代理 |
| 273 | 565ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 274 | 570ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 275 | 572ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 276 | 578ms | Github | 0.43 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 277 | 585ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 278 | 586ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 279 | 598ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 280 | 602ms | Support | 0.49 MB/s | `https://support.apple.com` | 通用代理 |
| 281 | 605ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 282 | 606ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 283 | 617ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 284 | 628ms | Gh | 0.82 MB/s | `https://gh.39.al` | 通用代理 |
| 285 | 658ms | Ghproxy | 0.23 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 286 | 663ms | Fastfile | 1.2 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 287 | 664ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 288 | 667ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 289 | 676ms | Os | 0.05 MB/s | `https://os.ryo.lu` | 通用代理 |
| 290 | 677ms | Clawbiz | 0.02 MB/s | `https://clawbiz.io` | 通用代理 |
| 291 | 692ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 292 | 695ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 293 | 700ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 294 | 716ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 295 | 719ms | Gh | 0.34 MB/s | `https://gh.dpik.top` | 通用代理 |
| 296 | 725ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 297 | 737ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 298 | 758ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 299 | 761ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 300 | 779ms | Aif | 0.02 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 301 | 780ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 302 | 781ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 303 | 785ms | Git | 0.2 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 304 | 795ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 305 | 796ms | Docs | 0.18 MB/s | `https://docs.transifex.com` | 通用代理 |
| 306 | 806ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 307 | 823ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 308 | 873ms | Ccgather | 0.07 MB/s | `https://ccgather.com` | 通用代理 |
| 309 | 876ms | Task | 0.01 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 310 | 886ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 311 | 891ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 312 | 893ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 313 | 913ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 314 | 916ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 315 | 919ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 316 | 929ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 317 | 953ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 318 | 969ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 319 | 979ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 320 | 981ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 321 | 996ms | Web | - | `https://web.4399.com` | 通用代理 |
| 322 | 1015ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 323 | 1017ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 324 | 1020ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 325 | 1036ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 326 | 1067ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 327 | 1075ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 328 | 1097ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 329 | 1111ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 330 | 1151ms | Your-domain | - | `https://your-domain.com` | 通用代理 |
| 331 | 1154ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 332 | 1162ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 333 | 1166ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 334 | 1169ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 335 | 1191ms | Ghproxy | 0.24 MB/s | `https://ghproxy.cc` | 通用代理 |
| 336 | 1191ms | V | - | `https://v.douyin.com` | 通用代理 |
| 337 | 1193ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 338 | 1203ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 339 | 1212ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 340 | 1230ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 341 | 1241ms | Git | 0.37 MB/s | `https://git.669966.xyz` | 通用代理 |
| 342 | 1244ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 343 | 1259ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 344 | 1275ms | GHProxy Net | 0.22 MB/s | `https://ghproxy.net` | 通用代理 |
| 345 | 1308ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 346 | 1330ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 347 | 1340ms | Github | 0.15 MB/s | `https://github.chenc.dev` | 通用代理 |
| 348 | 1348ms | Cf | 0.26 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 349 | 1349ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 350 | 1399ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 351 | 1473ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 352 | 1521ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 353 | 1578ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 354 | 1599ms | SLink | - | `https://slink.ltd` | 通用代理 |
| 355 | 1658ms | Heycall-e | 0.09 MB/s | `https://heycall-e.com` | 通用代理 |
| 356 | 1717ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 357 | 1938ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 358 | 2117ms | Img | - | `https://img.ink` | 通用代理 |
| 359 | 2261ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 360 | 2284ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 361 | 2299ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 362 | 2454ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 363 | 2645ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 364 | 2838ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 365 | 2980ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 366 | 3112ms | Ghproxy | 0.12 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 367 | 3273ms | Gh | 0.08 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 368 | 3349ms | G | 0.07 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 369 | 4306ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 370 | 6342ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（13 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| YYLX Git (`git-yylx-win`) | 2 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 5 次 |
| Npee Down (`down-npee-cn`) | 27 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Gh (`gh-halonice-com`) | 26 次 |
| Mirror (`mirror-houlang-cloud`) | 1 次 |
| 5555 (`5555-cab`) | 17 次 |
| Doxygen (`doxygen-org`) | 13 次 |
| Maplecode (`maplecode-art`) | 6 次 |
| Mobilevc (`mobilevc-top`) | 2 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 2 次 |
| Adult (`adult-contents-fc2-com`) | 1 次 |

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
