# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-29T12:26:07Z**，每 6 小时刷新一次。当前 ✅ **385** 在线 / ⚠️ **14** 不稳定 / ⚰️ **51** 已失效归档。

## 核心特性

- **399 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 55ms | Microsoftedge | 0.62 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 62ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 3 | 67ms | Linkedin | 0.12 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 75ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 78ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 6 | 82ms | App | 0.08 MB/s | `https://app.netlify.com` | 通用代理 |
| 7 | 85ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 8 | 89ms | Godocs | 0.05 MB/s | `https://godocs.io` | 通用代理 |
| 9 | 92ms | Lawyer-yu | 0.07 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 10 | 94ms | Githubstatus | 1.21 MB/s | `https://githubstatus.com` | 通用代理 |
| 11 | 96ms | Deno | 0.78 MB/s | `https://deno.com` | 通用代理 |
| 12 | 97ms | X | 1.22 MB/s | `https://x.com` | 通用代理 |
| 13 | 102ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 14 | 103ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 15 | 103ms | Zebrunner | 1.46 MB/s | `https://zebrunner.com` | 通用代理 |
| 16 | 104ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 17 | 105ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 18 | 107ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 19 | 112ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 20 | 115ms | Music-cli | 0.18 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 21 | 116ms | Xjtu-nyxf-study-material | 0.13 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 22 | 121ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 23 | 121ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 24 | 122ms | Img | - | `https://img.shields.io` | 通用代理 |
| 25 | 124ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 26 | 127ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 27 | 129ms | Discord | 0.07 MB/s | `https://discord.gg` | 通用代理 |
| 28 | 133ms | Resume-5lv | 0.19 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 29 | 133ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 30 | 135ms | Opresume | 0.39 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 31 | 135ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 32 | 136ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 33 | 137ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 34 | 140ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 35 | 141ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 36 | 143ms | Components | 0.11 MB/s | `https://components.dereekb.com` | 通用代理 |
| 37 | 143ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 38 | 144ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 39 | 146ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 40 | 146ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 41 | 147ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 42 | 149ms | Impeccable | 0.75 MB/s | `https://impeccable.style` | 通用代理 |
| 43 | 149ms | Kuroutoshikou | 0.58 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 44 | 152ms | Tms | 0.14 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 45 | 153ms | Kighelper-cloud | 0.06 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 46 | 153ms | Opensunsama | 0.05 MB/s | `https://opensunsama.com` | 通用代理 |
| 47 | 154ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 48 | 154ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 49 | 155ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 50 | 156ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 51 | 161ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 52 | 164ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 53 | 166ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 54 | 167ms | Ode | - | `https://ode.fun` | 通用代理 |
| 55 | 168ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 56 | 169ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 57 | 169ms | Dilo-d14 | 0.16 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 58 | 171ms | Openpua | 0.39 MB/s | `https://openpua.ai` | 通用代理 |
| 59 | 172ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 60 | 173ms | Git | 1.81 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 61 | 173ms | Vibesql | 0.08 MB/s | `https://vibesql.org` | 通用代理 |
| 62 | 174ms | Github | 1.99 MB/s | `https://github.788787.xyz` | 通用代理 |
| 63 | 174ms | Training | 0.16 MB/s | `https://training.ti.com` | 通用代理 |
| 64 | 175ms | Git | 3.04 MB/s | `https://git.820828.xyz` | 通用代理 |
| 65 | 177ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 66 | 177ms | Cognitum | 0.19 MB/s | `https://cognitum.one` | 通用代理 |
| 67 | 177ms | Play | 0.02 MB/s | `https://play.templatical.com` | 通用代理 |
| 68 | 177ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 69 | 178ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 70 | 179ms | Caiji | 0.09 MB/s | `https://caiji.cyou` | 通用代理 |
| 71 | 179ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 72 | 180ms | Cbrowser | 1.59 MB/s | `https://cbrowser.ai` | 通用代理 |
| 73 | 181ms | Axios-http | 0.23 MB/s | `https://axios-http.com` | 通用代理 |
| 74 | 181ms | Gitea-mirror | 0.6 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 75 | 182ms | Thumb | 1.16 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 76 | 183ms | Caw | 0.05 MB/s | `https://caw.rocks` | 通用代理 |
| 77 | 184ms | Crypto-funding-arbitrage | 0.05 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 78 | 185ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 79 | 185ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 80 | 186ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 81 | 186ms | Ghproxy | 2.86 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 82 | 186ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 83 | 187ms | Gh | 2.11 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 84 | 187ms | Github | 1.7 MB/s | `https://github.880824.xyz` | 通用代理 |
| 85 | 187ms | Glass | 0.19 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 86 | 187ms | Tokei | 0.32 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 87 | 189ms | L4d2 | 0.08 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 88 | 190ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 89 | 190ms | GH-Proxy | 0.72 MB/s | `https://gh-proxy.com` | 通用代理 |
| 90 | 190ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 91 | 191ms | GH Monlor | 0.64 MB/s | `https://gh.monlor.com` | 通用代理 |
| 92 | 192ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 93 | 194ms | Bestdori | 0.08 MB/s | `https://bestdori.com` | 通用代理 |
| 94 | 194ms | Clypra | 0.05 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 95 | 194ms | Github | 1.29 MB/s | `https://github.ihnic.com` | 通用代理 |
| 96 | 200ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 97 | 201ms | Gsd | 0.23 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 98 | 202ms | Gh | 1.33 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 99 | 202ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 100 | 205ms | Clayrune | 0.13 MB/s | `https://clayrune.io` | 通用代理 |
| 101 | 205ms | Cursor | 0.4 MB/s | `https://cursor.com` | 通用代理 |
| 102 | 205ms | Themolt | 0.04 MB/s | `https://themolt.net` | 通用代理 |
| 103 | 206ms | Aiblackboxfc | 0.21 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 104 | 206ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 105 | 207ms | Twitter | 0.78 MB/s | `https://twitter.com` | 通用代理 |
| 106 | 208ms | Coreos | 1.56 MB/s | `https://coreos.com` | 通用代理 |
| 107 | 209ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 108 | 210ms | Cody | 0.16 MB/s | `https://cody.todyle.com` | 通用代理 |
| 109 | 210ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 110 | 212ms | Ampcode | 0.19 MB/s | `https://ampcode.com` | 通用代理 |
| 111 | 213ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 112 | 214ms | Alas | 0.78 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 113 | 214ms | Ghproxy | 1.94 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 114 | 215ms | Sub | 0.13 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 115 | 217ms | Coffeecli | 0.09 MB/s | `https://coffeecli.com` | 通用代理 |
| 116 | 218ms | Miaozitie | 0.07 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 117 | 218ms | Polgarand | 0.06 MB/s | `https://polgarand.org` | 通用代理 |
| 118 | 220ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 119 | 221ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 120 | 223ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 121 | 224ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 122 | 227ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 123 | 227ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 124 | 228ms | Demo | 0.02 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 125 | 229ms | Codeeraser | 0.08 MB/s | `https://codeeraser.dev` | 通用代理 |
| 126 | 230ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 127 | 233ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 128 | 241ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 129 | 247ms | Cherryai | 0.04 MB/s | `https://cherryai.com` | 通用代理 |
| 130 | 248ms | GH-Proxy Org | 0.73 MB/s | `https://gh-proxy.org` | 通用代理 |
| 131 | 248ms | Ghproxy | 0.78 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 132 | 248ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 133 | 249ms | Agoramarket | 0.04 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 134 | 250ms | Agentlimb | 0.11 MB/s | `https://agentlimb.com` | 通用代理 |
| 135 | 253ms | Aomedia | 0.23 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 136 | 253ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 137 | 253ms | Savannah | 0.03 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 138 | 255ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 139 | 256ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 140 | 256ms | Sina | 0.84 MB/s | `https://sina.dev` | 通用代理 |
| 141 | 260ms | Github | 0.73 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 142 | 262ms | Ggg | 2.65 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 143 | 262ms | Opencovibe | 0.27 MB/s | `https://opencovibe.com` | 通用代理 |
| 144 | 266ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 145 | 267ms | Chops | 0.02 MB/s | `https://chops.md` | 通用代理 |
| 146 | 267ms | Travis-ci | 0.19 MB/s | `https://travis-ci.org` | 通用代理 |
| 147 | 269ms | Code | 1.22 MB/s | `https://code.claude.com` | 通用代理 |
| 148 | 269ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 149 | 271ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 150 | 274ms | Aka | 0.42 MB/s | `https://aka.ms` | 通用代理 |
| 151 | 274ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 152 | 274ms | Youtu | 1.23 MB/s | `https://youtu.be` | 通用代理 |
| 153 | 281ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 154 | 282ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 155 | 282ms | Visionmemorymcp | 0.23 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 156 | 284ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 157 | 284ms | Microcoreos | 0.28 MB/s | `https://microcoreos.com` | 通用代理 |
| 158 | 285ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 159 | 294ms | CrashMC CDN | 0.63 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 160 | 297ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 161 | 298ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 162 | 300ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 163 | 304ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 164 | 304ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 165 | 305ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 166 | 309ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 167 | 309ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 168 | 310ms | Bananaslides | 0.49 MB/s | `https://bananaslides.online` | 通用代理 |
| 169 | 312ms | Nisar | 0.76 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 170 | 312ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 171 | 313ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 172 | 313ms | Tiktok | 0.08 MB/s | `https://tiktok.com` | 通用代理 |
| 173 | 315ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 174 | 316ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 175 | 318ms | Steamcommunity | 0.13 MB/s | `https://steamcommunity.com` | 通用代理 |
| 176 | 318ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 177 | 319ms | FastGit CC | 0.91 MB/s | `https://fastgit.cc` | 通用代理 |
| 178 | 320ms | Api | 0.14 MB/s | `https://api.solov.cc` | 通用代理 |
| 179 | 325ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 180 | 325ms | Gh | 0.54 MB/s | `https://gh.padao.fun` | 通用代理 |
| 181 | 325ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 182 | 331ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 183 | 333ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 184 | 335ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 185 | 335ms | Sonarcloud | 0.12 MB/s | `https://sonarcloud.io` | 通用代理 |
| 186 | 337ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 187 | 344ms | B23 | - | `https://b23.tv` | 通用代理 |
| 188 | 348ms | Openttd | 0.04 MB/s | `https://openttd.org` | 通用代理 |
| 189 | 350ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 190 | 350ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 191 | 352ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 192 | 354ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 193 | 354ms | Gpui | 0.15 MB/s | `https://gpui.rs` | 通用代理 |
| 194 | 354ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 195 | 357ms | 30006000 | 0.68 MB/s | `https://30006000.xyz` | 通用代理 |
| 196 | 357ms | Store | 1.02 MB/s | `https://store.steampowered.com` | 通用代理 |
| 197 | 359ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 198 | 359ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 199 | 364ms | Claude | 0.39 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 200 | 366ms | Im | 0.48 MB/s | `https://im.codes` | 通用代理 |
| 201 | 368ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 202 | 370ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 203 | 372ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 204 | 375ms | Contrib | 0.23 MB/s | `https://contrib.rocks` | 通用代理 |
| 205 | 387ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 206 | 389ms | Bailian | 0.08 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 207 | 389ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 208 | 390ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 209 | 393ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 210 | 393ms | Serac | 0.05 MB/s | `https://serac.build` | 通用代理 |
| 211 | 397ms | Weaverse | 0.71 MB/s | `https://weaverse.io` | 通用代理 |
| 212 | 402ms | GH Nxnow | 0.53 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 213 | 407ms | GHFast | 0.47 MB/s | `https://ghfast.top` | 通用代理 |
| 214 | 413ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 215 | 413ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 216 | 417ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 217 | 420ms | Lecvdemarius | 0.05 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 218 | 421ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 219 | 422ms | Getgit | 2.21 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 220 | 429ms | Ednovas Mirror | 0.64 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 221 | 430ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 222 | 434ms | Tvv | 1.6 MB/s | `https://tvv.tw` | 通用代理 |
| 223 | 435ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 224 | 435ms | Ark | 0.49 MB/s | `https://ark.intel.com` | 通用代理 |
| 225 | 435ms | Safedocx | 0.12 MB/s | `https://safedocx.com` | 通用代理 |
| 226 | 436ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 227 | 441ms | V4 | 1.47 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 228 | 450ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 229 | 456ms | Bible-ai-explorer | 0.06 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 230 | 464ms | Huly-mcp | 0.15 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 231 | 467ms | Gh | 2.42 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 232 | 467ms | Hk | 0.82 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 233 | 470ms | YYLX Git | 0.38 MB/s | `https://git.yylx.win` | 通用代理 |
| 234 | 475ms | Aosmd | 0.14 MB/s | `https://aosmd.com` | 通用代理 |
| 235 | 475ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 236 | 476ms | Patchworkos | 0.31 MB/s | `https://patchworkos.com` | 通用代理 |
| 237 | 477ms | You | 0.26 MB/s | `https://you.piccalc.com` | 通用代理 |
| 238 | 478ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 239 | 481ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 240 | 484ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 241 | 487ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 242 | 496ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 243 | 500ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 244 | 504ms | Lucky | 0.45 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 245 | 504ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 246 | 509ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 247 | 515ms | Gh | 0.48 MB/s | `https://gh.noki.icu` | 通用代理 |
| 248 | 522ms | Impro | 1.4 MB/s | `https://impro.social` | 通用代理 |
| 249 | 528ms | Wl | - | `https://wl.do` | 通用代理 |
| 250 | 538ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 251 | 539ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 252 | 544ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 253 | 556ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 254 | 557ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 255 | 561ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 256 | 561ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 257 | 566ms | Umami-mcp | 0.92 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 258 | 579ms | Gp | 2.05 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 259 | 580ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 260 | 581ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 261 | 582ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 262 | 582ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 263 | 584ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 264 | 585ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 265 | 588ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 266 | 593ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 267 | 593ms | Fastfile | 2.11 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 268 | 596ms | Tsukuyomi | 0.09 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 269 | 597ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 270 | 601ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 271 | 606ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 272 | 607ms | Gh | 2.99 MB/s | `https://gh.1k.ink` | 通用代理 |
| 273 | 648ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 274 | 648ms | Github | 1.23 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 275 | 667ms | Github | 2.82 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 276 | 667ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 277 | 668ms | Github | 0.35 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 278 | 670ms | Agentkey | 0.13 MB/s | `https://agentkey.app` | 通用代理 |
| 279 | 671ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 280 | 671ms | Support | 0.1 MB/s | `https://support.apple.com` | 通用代理 |
| 281 | 675ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 282 | 683ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 283 | 698ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 284 | 704ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 285 | 705ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 286 | 705ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 287 | 708ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 288 | 720ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 289 | 734ms | Wordpaper | 0.45 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 290 | 740ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 291 | 744ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 292 | 748ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 293 | 750ms | Ghproxy | 0.25 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 294 | 754ms | Docs | 0.18 MB/s | `https://docs.transifex.com` | 通用代理 |
| 295 | 762ms | Os | 0.09 MB/s | `https://os.ryo.lu` | 通用代理 |
| 296 | 767ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 297 | 772ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 298 | 781ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 299 | 789ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 300 | 794ms | Anh | 0.14 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 301 | 805ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 302 | 816ms | Dbgate | 0.14 MB/s | `https://dbgate.org` | 通用代理 |
| 303 | 839ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 304 | 841ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 305 | 847ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 306 | 851ms | Tools | 1.47 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 307 | 869ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 308 | 876ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 309 | 891ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 310 | 906ms | Web | - | `https://web.4399.com` | 通用代理 |
| 311 | 920ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 312 | 921ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 313 | 924ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 314 | 928ms | Task | 0.02 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 315 | 930ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 316 | 932ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 317 | 933ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 318 | 939ms | Git | 0.2 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 319 | 945ms | Yibiao | 0.15 MB/s | `https://yibiao.pro` | 通用代理 |
| 320 | 958ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 321 | 962ms | Ginlix | 0.46 MB/s | `https://ginlix.ai` | 通用代理 |
| 322 | 980ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 323 | 986ms | Mimo | 0.17 MB/s | `https://mimo.mi.com` | 通用代理 |
| 324 | 1020ms | Github | 2.12 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 325 | 1023ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 326 | 1050ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 327 | 1060ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 328 | 1063ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 329 | 1068ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 330 | 1081ms | Cumora | 0.22 MB/s | `https://cumora.ai` | 通用代理 |
| 331 | 1095ms | Kenyu | 1.64 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 332 | 1098ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 333 | 1120ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 334 | 1132ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 335 | 1165ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 336 | 1172ms | V | - | `https://v.douyin.com` | 通用代理 |
| 337 | 1175ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 338 | 1178ms | Dimagent | 0.53 MB/s | `https://dimagent.com` | 通用代理 |
| 339 | 1180ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 340 | 1189ms | Github | 1.53 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 341 | 1215ms | Hevolve | 0.07 MB/s | `https://hevolve.ai` | 通用代理 |
| 342 | 1218ms | Ghproxy | 0.25 MB/s | `https://ghproxy.cc` | 通用代理 |
| 343 | 1223ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 344 | 1230ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 345 | 1236ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 346 | 1241ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 347 | 1267ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 348 | 1269ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 349 | 1324ms | Atomcode | 0.05 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 350 | 1343ms | Cfkua | 1.22 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 351 | 1344ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 352 | 1351ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 353 | 1354ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 354 | 1358ms | Github | 0.16 MB/s | `https://github.chenc.dev` | 通用代理 |
| 355 | 1412ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 356 | 1414ms | Cf | 0.29 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 357 | 1416ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 358 | 1421ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 359 | 1423ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 360 | 1429ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 361 | 1445ms | Gh | 0.5 MB/s | `https://gh.39.al` | 通用代理 |
| 362 | 1468ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 363 | 1573ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 364 | 1638ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 365 | 1640ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 366 | 1666ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 367 | 1714ms | Heycall-e | 0.1 MB/s | `https://heycall-e.com` | 通用代理 |
| 368 | 1739ms | Gh | 1.26 MB/s | `https://gh.dpik.top` | 通用代理 |
| 369 | 1747ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 370 | 1805ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 371 | 1886ms | Gh | 0.84 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 372 | 2000ms | G | 0.12 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 373 | 2040ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 374 | 2139ms | Img | - | `https://img.ink` | 通用代理 |
| 375 | 2172ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 376 | 2251ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 377 | 2253ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 378 | 2432ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 379 | 2441ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 380 | 2502ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 381 | 2503ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 382 | 3021ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 383 | 3095ms | Ghproxy | - | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 384 | 3140ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 385 | 3632ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（14 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 14 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 5 次 |
| Gh (`gh-b52m-cn`) | 1 次 |
| Proxy (`proxy-vvvv-ee`) | 2 次 |
| 5555 (`5555-cab`) | 26 次 |
| Doxygen (`doxygen-org`) | 22 次 |
| Flashtype (`flashtype-com`) | 3 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 5 次 |
| Maplecode (`maplecode-art`) | 15 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 11 次 |
| Adult (`adult-contents-fc2-com`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 392 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **399** | |

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
