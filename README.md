# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-28T04:18:29Z**，每 6 小时刷新一次。当前 ✅ **377** 在线 / ⚠️ **19** 不稳定 / ⚰️ **51** 已失效归档。

## 核心特性

- **396 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 58ms | Microsoftedge | 0.86 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 62ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 3 | 67ms | Linkedin | 0.51 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 73ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 78ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 6 | 79ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 7 | 80ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 8 | 81ms | Deno | 0.42 MB/s | `https://deno.com` | 通用代理 |
| 9 | 86ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 10 | 86ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 11 | 90ms | App | 0.11 MB/s | `https://app.netlify.com` | 通用代理 |
| 12 | 91ms | Godocs | 0.18 MB/s | `https://godocs.io` | 通用代理 |
| 13 | 99ms | X | 0.57 MB/s | `https://x.com` | 通用代理 |
| 14 | 100ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 15 | 100ms | Lawyer-yu | 0.22 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 16 | 103ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 17 | 105ms | Githubstatus | 1.69 MB/s | `https://githubstatus.com` | 通用代理 |
| 18 | 112ms | Xjtu-nyxf-study-material | - | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 19 | 115ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 20 | 117ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 21 | 118ms | App | 0.01 MB/s | `https://app.codecov.io` | 通用代理 |
| 22 | 119ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 23 | 120ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 24 | 121ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 25 | 121ms | Goreportcard | 0.07 MB/s | `https://goreportcard.com` | 通用代理 |
| 26 | 121ms | Music-cli | 0.51 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 27 | 126ms | Cognitum | - | `https://cognitum.one` | 通用代理 |
| 28 | 129ms | Zebrunner | 2.59 MB/s | `https://zebrunner.com` | 通用代理 |
| 29 | 130ms | Opentakeoff | 0.09 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 30 | 130ms | Resume-5lv | 0.01 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 31 | 132ms | Thumb | 0.48 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 32 | 135ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 33 | 136ms | Caiji | 0.09 MB/s | `https://caiji.cyou` | 通用代理 |
| 34 | 136ms | Osf | 0.05 MB/s | `https://osf.io` | 通用代理 |
| 35 | 138ms | App | 0.01 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 36 | 138ms | Discord | 0.14 MB/s | `https://discord.gg` | 通用代理 |
| 37 | 140ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 38 | 141ms | Tms | 0.14 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 39 | 142ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 40 | 143ms | Kighelper-cloud | - | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 41 | 144ms | Impeccable | 1.49 MB/s | `https://impeccable.style` | 通用代理 |
| 42 | 145ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 43 | 147ms | Components | 0.18 MB/s | `https://components.dereekb.com` | 通用代理 |
| 44 | 148ms | Vibesql | 0.01 MB/s | `https://vibesql.org` | 通用代理 |
| 45 | 149ms | App | - | `https://app.opencastor.com` | 通用代理 |
| 46 | 150ms | Git | - | `https://git.820828.xyz` | 通用代理 |
| 47 | 150ms | Git | 0.05 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 48 | 151ms | Freeport | - | `https://freeport.network` | 通用代理 |
| 49 | 152ms | Github | 3.29 MB/s | `https://github.880824.xyz` | 通用代理 |
| 50 | 153ms | Gitea-mirror | - | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 51 | 153ms | Github | 3.05 MB/s | `https://github.788787.xyz` | 通用代理 |
| 52 | 154ms | Dilo-d14 | 0.01 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 53 | 155ms | Bolt2github | 0.11 MB/s | `https://bolt2github.com` | 通用代理 |
| 54 | 155ms | Cbrowser | 0.06 MB/s | `https://cbrowser.ai` | 通用代理 |
| 55 | 156ms | Tokei | 0.45 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 56 | 159ms | Glass | 0.08 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 57 | 160ms | Miaozitie | - | `https://miaozitie.80wdb.com` | 通用代理 |
| 58 | 161ms | Openpua | 0.82 MB/s | `https://openpua.ai` | 通用代理 |
| 59 | 161ms | Play | 0.02 MB/s | `https://play.templatical.com` | 通用代理 |
| 60 | 162ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 61 | 162ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 62 | 162ms | Nextup-resource | 0.04 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 63 | 162ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 64 | 163ms | Clayrune | 0.02 MB/s | `https://clayrune.io` | 通用代理 |
| 65 | 163ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 66 | 164ms | Bestdori | 0.06 MB/s | `https://bestdori.com` | 通用代理 |
| 67 | 164ms | GH-Proxy | 0.74 MB/s | `https://gh-proxy.com` | 通用代理 |
| 68 | 164ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 69 | 165ms | L4d2 | - | `https://l4d2.laoyutang.cn` | 通用代理 |
| 70 | 166ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 71 | 168ms | Gh | 3.05 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 72 | 169ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 73 | 170ms | Hopp | 0.05 MB/s | `https://hopp.sh` | 通用代理 |
| 74 | 170ms | Kuroutoshikou | 1.64 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 75 | 170ms | Shiori-v1 | 0.07 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 76 | 171ms | Cody | 0.01 MB/s | `https://cody.todyle.com` | 通用代理 |
| 77 | 172ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 78 | 172ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 79 | 173ms | Coffeecli | - | `https://coffeecli.com` | 通用代理 |
| 80 | 173ms | Demo | 0.03 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 81 | 173ms | Gh | 3.1 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 82 | 174ms | Github | 0.01 MB/s | `https://github.ihnic.com` | 通用代理 |
| 83 | 174ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 84 | 174ms | Opensunsama | 0.08 MB/s | `https://opensunsama.com` | 通用代理 |
| 85 | 178ms | Alas | 0.02 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 86 | 179ms | Cherryai | 0.1 MB/s | `https://cherryai.com` | 通用代理 |
| 87 | 179ms | GH Monlor | 0.44 MB/s | `https://gh.monlor.com` | 通用代理 |
| 88 | 179ms | Training | 0.21 MB/s | `https://training.ti.com` | 通用代理 |
| 89 | 180ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 90 | 181ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 91 | 181ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 92 | 181ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 93 | 182ms | Ghproxy | 3.8 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 94 | 182ms | Gsd | 0.34 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 95 | 183ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 96 | 183ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 97 | 184ms | Crypto-funding-arbitrage | - | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 98 | 185ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 99 | 186ms | Ai-trend-publish | 0.03 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 100 | 191ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 101 | 192ms | Ode | - | `https://ode.fun` | 通用代理 |
| 102 | 194ms | GH-Proxy Org | 1.05 MB/s | `https://gh-proxy.org` | 通用代理 |
| 103 | 197ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 104 | 199ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 105 | 201ms | Aiblackboxfc | 0.4 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 106 | 201ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 107 | 202ms | Codeeraser | 0.08 MB/s | `https://codeeraser.dev` | 通用代理 |
| 108 | 203ms | Polgarand | - | `https://polgarand.org` | 通用代理 |
| 109 | 204ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 110 | 205ms | Agentlimb | - | `https://agentlimb.com` | 通用代理 |
| 111 | 206ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 112 | 209ms | Ghproxy | 2.84 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 113 | 210ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 114 | 210ms | Cursor | 0.58 MB/s | `https://cursor.com` | 通用代理 |
| 115 | 213ms | Clypra | 0.08 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 116 | 215ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 117 | 216ms | Axios-http | 1.32 MB/s | `https://axios-http.com` | 通用代理 |
| 118 | 216ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 119 | 217ms | Themolt | 0.07 MB/s | `https://themolt.net` | 通用代理 |
| 120 | 218ms | Savannah | 0.07 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 121 | 220ms | Bananaslides | 0.01 MB/s | `https://bananaslides.online` | 通用代理 |
| 122 | 220ms | Travis-ci | 0.09 MB/s | `https://travis-ci.org` | 通用代理 |
| 123 | 223ms | Coreos | 5.79 MB/s | `https://coreos.com` | 通用代理 |
| 124 | 225ms | Opencovibe | 0.02 MB/s | `https://opencovibe.com` | 通用代理 |
| 125 | 225ms | Twitter | 0.51 MB/s | `https://twitter.com` | 通用代理 |
| 126 | 228ms | Ghproxy | 0.55 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 127 | 228ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 128 | 229ms | Ampcode | 0.37 MB/s | `https://ampcode.com` | 通用代理 |
| 129 | 230ms | Ggg | 3.08 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 130 | 233ms | Chops | - | `https://chops.md` | 通用代理 |
| 131 | 236ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 132 | 236ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 133 | 237ms | Microcoreos | 0.02 MB/s | `https://microcoreos.com` | 通用代理 |
| 134 | 238ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 135 | 239ms | Aka | 0.97 MB/s | `https://aka.ms` | 通用代理 |
| 136 | 242ms | Sub | 0.36 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 137 | 242ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 138 | 243ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 139 | 243ms | Code | 0.67 MB/s | `https://code.claude.com` | 通用代理 |
| 140 | 244ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 141 | 246ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 142 | 247ms | Agoramarket | 0.05 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 143 | 250ms | CrashMC CDN | - | `https://cdn.crashmc.com` | 通用代理 |
| 144 | 252ms | Aomedia | 0.42 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 145 | 252ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 146 | 253ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 147 | 255ms | Wings | 0.04 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 148 | 256ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 149 | 262ms | Github | 0.48 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 150 | 263ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 151 | 265ms | Nisar | 0.87 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 152 | 267ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 153 | 271ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 154 | 273ms | Flashtype | - | `https://flashtype.com` | 通用代理 |
| 155 | 275ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 156 | 276ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 157 | 279ms | Api | 0.01 MB/s | `https://api.solov.cc` | 通用代理 |
| 158 | 280ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 159 | 281ms | Visionmemorymcp | 0.2 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 160 | 283ms | Youtu | 2.48 MB/s | `https://youtu.be` | 通用代理 |
| 161 | 284ms | Contrib | 0.03 MB/s | `https://contrib.rocks` | 通用代理 |
| 162 | 285ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 163 | 290ms | Sina | 0.57 MB/s | `https://sina.dev` | 通用代理 |
| 164 | 292ms | Tiktok | 0.35 MB/s | `https://tiktok.com` | 通用代理 |
| 165 | 293ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 166 | 293ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 167 | 299ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 168 | 300ms | FastGit CC | - | `https://fastgit.cc` | 通用代理 |
| 169 | 301ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 170 | 301ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 171 | 303ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 172 | 304ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 173 | 307ms | Agenticcorporation | 0.08 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 174 | 309ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 175 | 312ms | Claude | 0.07 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 176 | 314ms | Openttd | - | `https://openttd.org` | 通用代理 |
| 177 | 319ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 178 | 321ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 179 | 321ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 180 | 321ms | Gpui | 0.02 MB/s | `https://gpui.rs` | 通用代理 |
| 181 | 323ms | Sonarcloud | 0.02 MB/s | `https://sonarcloud.io` | 通用代理 |
| 182 | 324ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 183 | 324ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 184 | 325ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 185 | 327ms | Gh | 0.43 MB/s | `https://gh.padao.fun` | 通用代理 |
| 186 | 329ms | Radio-browser | 0.05 MB/s | `https://radio-browser.info` | 通用代理 |
| 187 | 333ms | 30006000 | 0.46 MB/s | `https://30006000.xyz` | 通用代理 |
| 188 | 334ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 189 | 338ms | Oem | 0.01 MB/s | `https://oem.re` | 通用代理 |
| 190 | 343ms | B23 | - | `https://b23.tv` | 通用代理 |
| 191 | 344ms | Agent-room | 0.04 MB/s | `https://agent-room.com` | 通用代理 |
| 192 | 345ms | Steamcommunity | 0.13 MB/s | `https://steamcommunity.com` | 通用代理 |
| 193 | 350ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 194 | 355ms | Store | 0.94 MB/s | `https://store.steampowered.com` | 通用代理 |
| 195 | 355ms | Turborepo-starter-kit-web | 0.11 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 196 | 356ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 197 | 356ms | Weaverse | 0.42 MB/s | `https://weaverse.io` | 通用代理 |
| 198 | 357ms | Bailian | 0.05 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 199 | 360ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 200 | 362ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 201 | 368ms | Serac | 0.03 MB/s | `https://serac.build` | 通用代理 |
| 202 | 377ms | App | 0.02 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 203 | 379ms | Gh | 0.78 MB/s | `https://gh.noki.icu` | 通用代理 |
| 204 | 382ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 205 | 384ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 206 | 387ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 207 | 390ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 208 | 397ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 209 | 403ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 210 | 403ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 211 | 404ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 212 | 411ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 213 | 412ms | Ednovas Mirror | 0.58 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 214 | 420ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 215 | 421ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 216 | 425ms | V4 | 0.11 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 217 | 429ms | Api | - | `https://api.everyapi.ai` | 通用代理 |
| 218 | 438ms | Gh | 2.76 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 219 | 443ms | YYLX Git | 0.21 MB/s | `https://git.yylx.win` | 通用代理 |
| 220 | 445ms | Msdn | 0.06 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 221 | 446ms | Memstack | 0.03 MB/s | `https://memstack.pro` | 通用代理 |
| 222 | 449ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 223 | 450ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 224 | 455ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 225 | 456ms | Lecvdemarius | 0.11 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 226 | 456ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 227 | 457ms | Bible-ai-explorer | 0.06 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 228 | 459ms | Aps | 0.06 MB/s | `https://aps.com` | 通用代理 |
| 229 | 460ms | Agentkey | 0.6 MB/s | `https://agentkey.app` | 通用代理 |
| 230 | 461ms | Huly-mcp | - | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 231 | 463ms | GHFast | 0.38 MB/s | `https://ghfast.top` | 通用代理 |
| 232 | 463ms | Tvv | - | `https://tvv.tw` | 通用代理 |
| 233 | 478ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 234 | 480ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 235 | 481ms | Patchworkos | 0.38 MB/s | `https://patchworkos.com` | 通用代理 |
| 236 | 481ms | Safedocx | 0.16 MB/s | `https://safedocx.com` | 通用代理 |
| 237 | 482ms | Im | 0.98 MB/s | `https://im.codes` | 通用代理 |
| 238 | 484ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 239 | 485ms | Adult | 0.01 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 240 | 485ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 241 | 486ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 242 | 488ms | Impro | 0.13 MB/s | `https://impro.social` | 通用代理 |
| 243 | 489ms | Ark | 0.33 MB/s | `https://ark.intel.com` | 通用代理 |
| 244 | 489ms | Hk | 0.96 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 245 | 501ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 246 | 507ms | Aosmd | 0.31 MB/s | `https://aosmd.com` | 通用代理 |
| 247 | 514ms | Wl | - | `https://wl.do` | 通用代理 |
| 248 | 522ms | Gh | 0.07 MB/s | `https://gh.idayer.com` | 通用代理 |
| 249 | 526ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 250 | 529ms | Lucky | 0.42 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 251 | 537ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 252 | 539ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 253 | 545ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 254 | 547ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 255 | 548ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 256 | 552ms | Gh | 2.92 MB/s | `https://gh.1k.ink` | 通用代理 |
| 257 | 557ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 258 | 561ms | Gp | 3.74 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 259 | 579ms | Ygdj7 | 0.01 MB/s | `https://ygdj7.com` | 通用代理 |
| 260 | 580ms | 3d-set-visualizer | 0.05 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 261 | 580ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 262 | 588ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 263 | 589ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 264 | 589ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 265 | 597ms | Fastfile | 0.01 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 266 | 618ms | Github | - | `https://github.zzrbk.xyz` | 通用代理 |
| 267 | 618ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 268 | 632ms | Clawbiz | 0.04 MB/s | `https://clawbiz.io` | 通用代理 |
| 269 | 635ms | Github | 0.35 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 270 | 639ms | Support | 0.51 MB/s | `https://support.apple.com` | 通用代理 |
| 271 | 644ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 272 | 654ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 273 | 658ms | Agoracitizen | 0.03 MB/s | `https://agoracitizen.app` | 通用代理 |
| 274 | 666ms | Github | 0.14 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 275 | 673ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 276 | 680ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 277 | 682ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 278 | 684ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 279 | 688ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 280 | 699ms | Congressmcp | - | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 281 | 711ms | Hubp | - | `https://hubp.org` | 通用代理 |
| 282 | 714ms | Os | 0.06 MB/s | `https://os.ryo.lu` | 通用代理 |
| 283 | 716ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 284 | 731ms | Wordpaper | - | `https://wordpaper.pages.dev` | 通用代理 |
| 285 | 735ms | Onetwin | 0.01 MB/s | `https://onetwin.cn` | 通用代理 |
| 286 | 744ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 287 | 745ms | Aif | 0.05 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 288 | 747ms | Docs | 0.27 MB/s | `https://docs.transifex.com` | 通用代理 |
| 289 | 752ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 290 | 759ms | Ghproxy | 0.23 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 291 | 760ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 292 | 764ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 293 | 766ms | Anh | 0.02 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 294 | 777ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 295 | 796ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 296 | 808ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 297 | 823ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 298 | 835ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 299 | 835ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 300 | 845ms | Git | 0.09 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 301 | 856ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 302 | 861ms | Tools | - | `https://tools.realtime-ai.chat` | 通用代理 |
| 303 | 862ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 304 | 880ms | Dbgate | 0.21 MB/s | `https://dbgate.org` | 通用代理 |
| 305 | 900ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 306 | 903ms | Ginlix | 0.04 MB/s | `https://ginlix.ai` | 通用代理 |
| 307 | 907ms | Github | 0.12 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 308 | 907ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 309 | 925ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 310 | 928ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 311 | 943ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 312 | 949ms | Dimagent | 0.13 MB/s | `https://dimagent.com` | 通用代理 |
| 313 | 955ms | Web | - | `https://web.4399.com` | 通用代理 |
| 314 | 962ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 315 | 967ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 316 | 970ms | Mimo | 0.14 MB/s | `https://mimo.mi.com` | 通用代理 |
| 317 | 982ms | Yibiao | 0.1 MB/s | `https://yibiao.pro` | 通用代理 |
| 318 | 1009ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 319 | 1028ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 320 | 1030ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 321 | 1034ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 322 | 1045ms | Kenyu | 1.47 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 323 | 1061ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 324 | 1068ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 325 | 1070ms | GHProxy Net | 0.08 MB/s | `https://ghproxy.net` | 通用代理 |
| 326 | 1093ms | V | 0.05 MB/s | `https://v.douyin.com` | 通用代理 |
| 327 | 1128ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 328 | 1133ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 329 | 1149ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 330 | 1166ms | Your-domain | 0.04 MB/s | `https://your-domain.com` | 通用代理 |
| 331 | 1168ms | Github | - | `https://github.crdz.eu.org` | 通用代理 |
| 332 | 1186ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 333 | 1192ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 334 | 1192ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 335 | 1208ms | Hevolve | 0.07 MB/s | `https://hevolve.ai` | 通用代理 |
| 336 | 1215ms | Gh | - | `https://gh.dpik.top` | 通用代理 |
| 337 | 1242ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 338 | 1243ms | Ghproxy | 0.12 MB/s | `https://ghproxy.cc` | 通用代理 |
| 339 | 1245ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 340 | 1265ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 341 | 1277ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 342 | 1292ms | Gh | 0.35 MB/s | `https://gh.39.al` | 通用代理 |
| 343 | 1299ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 344 | 1315ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 345 | 1347ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 346 | 1360ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 347 | 1361ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 348 | 1367ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 349 | 1374ms | Github | 0.12 MB/s | `https://github.chenc.dev` | 通用代理 |
| 350 | 1377ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 351 | 1405ms | Cf | 0.23 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 352 | 1465ms | Bks | - | `https://bks.indevs.in` | 通用代理 |
| 353 | 1482ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 354 | 1494ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 355 | 1520ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 356 | 1565ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 357 | 1667ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 358 | 1697ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 359 | 1708ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 360 | 1824ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 361 | 1902ms | Git | 0.11 MB/s | `https://git.669966.xyz` | 通用代理 |
| 362 | 2110ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 363 | 2143ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 364 | 2144ms | Provider | - | `https://provider.com` | 通用代理 |
| 365 | 2153ms | Img | - | `https://img.ink` | 通用代理 |
| 366 | 2286ms | Cumora | 0.02 MB/s | `https://cumora.ai` | 通用代理 |
| 367 | 2396ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 368 | 2486ms | Gh | - | `https://gh.223456.xyz` | 通用代理 |
| 369 | 2518ms | Cfkua | - | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 370 | 2557ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 371 | 2699ms | Wget | - | `https://wget.la` | 通用代理 |
| 372 | 2715ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 373 | 2817ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 374 | 3083ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 375 | 3159ms | Gh | - | `https://gh.b52m.cn` | 通用代理 |
| 376 | 3196ms | G | 0.18 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 377 | 4010ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（19 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 4 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 10 次 |
| GitClone (`gitclone-com`) | 5 次 |
| Getgit (`getgit-love8yun-eu-org`) | 1 次 |
| Ghproxy (`ghproxy-mirror-skybyte-me`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 1 次 |
| Img (`img-shields-io`) | 1 次 |
| Proxy (`proxy-vvvv-ee`) | 5 次 |
| 5555 (`5555-cab`) | 22 次 |
| Doxygen (`doxygen-org`) | 18 次 |
| Caw (`caw-rocks`) | 1 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 1 次 |
| Maplecode (`maplecode-art`) | 11 次 |
| Opresume (`opresume-pages-dev`) | 1 次 |
| Pew (`pew-md`) | 1 次 |
| Umami-mcp (`umami-mcp-macawls-dev`) | 1 次 |
| You (`you-piccalc-com`) | 1 次 |
| Electronforge (`electronforge-io`) | 1 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 7 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 389 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **396** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（51 个）。

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
