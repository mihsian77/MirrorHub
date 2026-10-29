# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-29T22:33:15Z**，每 6 小时刷新一次。当前 ✅ **384** 在线 / ⚠️ **16** 不稳定 / ⚰️ **51** 已失效归档。

## 核心特性

- **400 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 64ms | Microsoftedge | 0.19 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 70ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 3 | 75ms | Linkedin | 0.14 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 82ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 5 | 83ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 6 | 90ms | App | 0.09 MB/s | `https://app.netlify.com` | 通用代理 |
| 7 | 90ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 8 | 95ms | Godocs | 0.06 MB/s | `https://godocs.io` | 通用代理 |
| 9 | 98ms | Githubstatus | 2.47 MB/s | `https://githubstatus.com` | 通用代理 |
| 10 | 101ms | Lawyer-yu | 0.06 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 11 | 104ms | X | 1.23 MB/s | `https://x.com` | 通用代理 |
| 12 | 106ms | Deno | 0.2 MB/s | `https://deno.com` | 通用代理 |
| 13 | 106ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 14 | 106ms | Zebrunner | 3.14 MB/s | `https://zebrunner.com` | 通用代理 |
| 15 | 107ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 16 | 109ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 17 | 112ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 18 | 113ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 19 | 119ms | Xjtu-nyxf-study-material | 0.13 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 20 | 122ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 21 | 127ms | Music-cli | 0.15 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 22 | 128ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 23 | 129ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 24 | 130ms | Opresume | 0.54 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 25 | 131ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 26 | 134ms | Resume-5lv | 0.18 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 27 | 135ms | Discord | 0.06 MB/s | `https://discord.gg` | 通用代理 |
| 28 | 136ms | Opentakeoff | 0.03 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 29 | 136ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 30 | 142ms | Img | - | `https://img.shields.io` | 通用代理 |
| 31 | 144ms | Components | 0.1 MB/s | `https://components.dereekb.com` | 通用代理 |
| 32 | 147ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 33 | 148ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 34 | 151ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 35 | 152ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 36 | 153ms | Kuroutoshikou | 0.87 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 37 | 153ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 38 | 154ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 39 | 155ms | Impeccable | 0.95 MB/s | `https://impeccable.style` | 通用代理 |
| 40 | 156ms | Opensunsama | 0.11 MB/s | `https://opensunsama.com` | 通用代理 |
| 41 | 157ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 42 | 157ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 43 | 159ms | Kighelper-cloud | 0.09 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 44 | 159ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 45 | 161ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 46 | 161ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 47 | 162ms | Tms | 0.1 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 48 | 163ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 49 | 163ms | Training | 0.3 MB/s | `https://training.ti.com` | 通用代理 |
| 50 | 166ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 51 | 167ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 52 | 168ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 53 | 172ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 54 | 173ms | Git | 2.09 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 55 | 174ms | Git | 1.89 MB/s | `https://git.820828.xyz` | 通用代理 |
| 56 | 174ms | Gitea-mirror | 0.67 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 57 | 174ms | Vibesql | 0.06 MB/s | `https://vibesql.org` | 通用代理 |
| 58 | 174ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 59 | 176ms | Dilo-d14 | 0.17 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 60 | 176ms | Play | 0.03 MB/s | `https://play.templatical.com` | 通用代理 |
| 61 | 177ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 62 | 177ms | Github | 2.01 MB/s | `https://github.788787.xyz` | 通用代理 |
| 63 | 178ms | Openpua | 0.45 MB/s | `https://openpua.ai` | 通用代理 |
| 64 | 179ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 65 | 179ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 66 | 181ms | Ode | - | `https://ode.fun` | 通用代理 |
| 67 | 182ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 68 | 182ms | Cognitum | 0.17 MB/s | `https://cognitum.one` | 通用代理 |
| 69 | 182ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 70 | 183ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 71 | 184ms | Caiji | 0.06 MB/s | `https://caiji.cyou` | 通用代理 |
| 72 | 184ms | Crypto-funding-arbitrage | 0.06 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 73 | 185ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 74 | 186ms | Ghproxy | 0.61 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 75 | 187ms | L4d2 | 0.12 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 76 | 188ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 77 | 189ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 78 | 189ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 79 | 189ms | Tokei | 0.41 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 80 | 190ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 81 | 191ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 82 | 191ms | Glass | 0.25 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 83 | 192ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 84 | 192ms | Github | 2.33 MB/s | `https://github.880824.xyz` | 通用代理 |
| 85 | 192ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 86 | 193ms | Bestdori | 0.11 MB/s | `https://bestdori.com` | 通用代理 |
| 87 | 193ms | Gh | 2.54 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 88 | 194ms | GH-Proxy | 1.12 MB/s | `https://gh-proxy.com` | 通用代理 |
| 89 | 195ms | Clypra | 0.08 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 90 | 195ms | Thumb | 1.03 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 91 | 197ms | Axios-http | 0.29 MB/s | `https://axios-http.com` | 通用代理 |
| 92 | 198ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 93 | 202ms | Cbrowser | 0.55 MB/s | `https://cbrowser.ai` | 通用代理 |
| 94 | 204ms | GH Monlor | 1.12 MB/s | `https://gh.monlor.com` | 通用代理 |
| 95 | 205ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 96 | 205ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 97 | 205ms | Polgarand | 0.07 MB/s | `https://polgarand.org` | 通用代理 |
| 98 | 207ms | Cody | 0.19 MB/s | `https://cody.todyle.com` | 通用代理 |
| 99 | 208ms | Clayrune | 0.14 MB/s | `https://clayrune.io` | 通用代理 |
| 100 | 210ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 101 | 210ms | Twitter | 0.94 MB/s | `https://twitter.com` | 通用代理 |
| 102 | 212ms | Alas | 0.96 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 103 | 212ms | Pidash | 0.04 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 104 | 213ms | Aiblackboxfc | 0.31 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 105 | 213ms | Github | 1.81 MB/s | `https://github.ihnic.com` | 通用代理 |
| 106 | 213ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 107 | 214ms | Coffeecli | 0.11 MB/s | `https://coffeecli.com` | 通用代理 |
| 108 | 214ms | Gh | 1.28 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 109 | 216ms | Ghproxy | 2.21 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 110 | 218ms | Miaozitie | 0.07 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 111 | 219ms | Ampcode | 0.26 MB/s | `https://ampcode.com` | 通用代理 |
| 112 | 219ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 113 | 220ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 114 | 221ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 115 | 222ms | Codeeraser | 0.1 MB/s | `https://codeeraser.dev` | 通用代理 |
| 116 | 222ms | Coreos | 1.98 MB/s | `https://coreos.com` | 通用代理 |
| 117 | 224ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 118 | 225ms | Cursor | 0.43 MB/s | `https://cursor.com` | 通用代理 |
| 119 | 227ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 120 | 227ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 121 | 228ms | Sina | 3.17 MB/s | `https://sina.dev` | 通用代理 |
| 122 | 230ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 123 | 233ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 124 | 235ms | Demo | 0.03 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 125 | 235ms | Ghproxy | 1.4 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 126 | 236ms | Agoramarket | 0.07 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 127 | 241ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 128 | 242ms | Sub | 0.13 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 129 | 244ms | Cherryai | 0.05 MB/s | `https://cherryai.com` | 通用代理 |
| 130 | 245ms | Gsd | 0.08 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 131 | 248ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 132 | 251ms | Phabricator | 0.03 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 133 | 252ms | Github | 2.44 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 134 | 253ms | Agentlimb | 0.2 MB/s | `https://agentlimb.com` | 通用代理 |
| 135 | 253ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 136 | 258ms | GH-Proxy Org | 0.97 MB/s | `https://gh-proxy.org` | 通用代理 |
| 137 | 259ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 138 | 259ms | Savannah | 0.03 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 139 | 262ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 140 | 265ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 141 | 267ms | Opencovibe | 0.37 MB/s | `https://opencovibe.com` | 通用代理 |
| 142 | 268ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 143 | 269ms | Code | 1.38 MB/s | `https://code.claude.com` | 通用代理 |
| 144 | 269ms | Ggg | 0.22 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 145 | 269ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 146 | 272ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 147 | 273ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 148 | 273ms | Travis-ci | 0.16 MB/s | `https://travis-ci.org` | 通用代理 |
| 149 | 273ms | Visionmemorymcp | 0.26 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 150 | 279ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 151 | 282ms | Aka | 0.68 MB/s | `https://aka.ms` | 通用代理 |
| 152 | 283ms | Microcoreos | 0.24 MB/s | `https://microcoreos.com` | 通用代理 |
| 153 | 289ms | Flashtype | - | `https://flashtype.com` | 通用代理 |
| 154 | 290ms | Youtu | 1.36 MB/s | `https://youtu.be` | 通用代理 |
| 155 | 291ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 156 | 293ms | Bananaslides | 0.83 MB/s | `https://bananaslides.online` | 通用代理 |
| 157 | 295ms | CrashMC CDN | - | `https://cdn.crashmc.com` | 通用代理 |
| 158 | 296ms | Api | 0.19 MB/s | `https://api.solov.cc` | 通用代理 |
| 159 | 298ms | Nisar | 1.69 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 160 | 301ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 161 | 302ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 162 | 303ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 163 | 303ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 164 | 305ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 165 | 305ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 166 | 305ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 167 | 307ms | Agenticcorporation | 0.03 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 168 | 307ms | Gh | 1.41 MB/s | `https://gh.padao.fun` | 通用代理 |
| 169 | 307ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 170 | 309ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 171 | 310ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 172 | 316ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 173 | 323ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 174 | 327ms | Tiktok | 0.12 MB/s | `https://tiktok.com` | 通用代理 |
| 175 | 328ms | FastGit CC | 1.73 MB/s | `https://fastgit.cc` | 通用代理 |
| 176 | 330ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 177 | 333ms | Turborepo-starter-kit-web | 0.07 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 178 | 336ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 179 | 336ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 180 | 336ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 181 | 338ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 182 | 338ms | Sonarcloud | 0.1 MB/s | `https://sonarcloud.io` | 通用代理 |
| 183 | 342ms | B23 | - | `https://b23.tv` | 通用代理 |
| 184 | 342ms | Steamcommunity | 0.12 MB/s | `https://steamcommunity.com` | 通用代理 |
| 185 | 342ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 186 | 343ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 187 | 344ms | 30006000 | 1.51 MB/s | `https://30006000.xyz` | 通用代理 |
| 188 | 346ms | Bailian | 0.11 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 189 | 348ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 190 | 349ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 191 | 350ms | Gpui | 0.21 MB/s | `https://gpui.rs` | 通用代理 |
| 192 | 357ms | Openttd | 0.04 MB/s | `https://openttd.org` | 通用代理 |
| 193 | 359ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 194 | 363ms | Store | 1.09 MB/s | `https://store.steampowered.com` | 通用代理 |
| 195 | 364ms | Claude | 0.29 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 196 | 365ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 197 | 367ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 198 | 368ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 199 | 372ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 200 | 379ms | Im | 0.32 MB/s | `https://im.codes` | 通用代理 |
| 201 | 381ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 202 | 384ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 203 | 385ms | Contrib | 0.26 MB/s | `https://contrib.rocks` | 通用代理 |
| 204 | 386ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 205 | 389ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 206 | 391ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 207 | 393ms | GHFast | 0.92 MB/s | `https://ghfast.top` | 通用代理 |
| 208 | 393ms | Serac | 0.07 MB/s | `https://serac.build` | 通用代理 |
| 209 | 395ms | Weaverse | 0.6 MB/s | `https://weaverse.io` | 通用代理 |
| 210 | 396ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 211 | 400ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 212 | 403ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 213 | 407ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 214 | 422ms | Getgit | 2.21 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 215 | 423ms | Ednovas Mirror | 1.7 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 216 | 432ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 217 | 434ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 218 | 436ms | Lecvdemarius | 0.05 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 219 | 443ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 220 | 444ms | V4 | 2.33 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 221 | 445ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 222 | 446ms | Tvv | 2.5 MB/s | `https://tvv.tw` | 通用代理 |
| 223 | 452ms | Msdn | 0.03 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 224 | 454ms | Hk | 1.49 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 225 | 460ms | Ark | 0.48 MB/s | `https://ark.intel.com` | 通用代理 |
| 226 | 460ms | Bible-ai-explorer | 0.07 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 227 | 461ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 228 | 461ms | Safedocx | 0.11 MB/s | `https://safedocx.com` | 通用代理 |
| 229 | 462ms | YYLX Git | 0.14 MB/s | `https://git.yylx.win` | 通用代理 |
| 230 | 464ms | Huly-mcp | 0.15 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 231 | 469ms | Gh | 2.0 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 232 | 470ms | Aps | 0.12 MB/s | `https://aps.com` | 通用代理 |
| 233 | 478ms | You | 0.29 MB/s | `https://you.piccalc.com` | 通用代理 |
| 234 | 481ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 235 | 491ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 236 | 494ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 237 | 494ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 238 | 497ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 239 | 499ms | Patchworkos | 0.25 MB/s | `https://patchworkos.com` | 通用代理 |
| 240 | 501ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 241 | 504ms | Lucky | 0.55 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 242 | 509ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 243 | 511ms | Wl | - | `https://wl.do` | 通用代理 |
| 244 | 522ms | Aosmd | 0.14 MB/s | `https://aosmd.com` | 通用代理 |
| 245 | 523ms | Impro | 1.27 MB/s | `https://impro.social` | 通用代理 |
| 246 | 524ms | Gh | 0.45 MB/s | `https://gh.noki.icu` | 通用代理 |
| 247 | 524ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 248 | 532ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 249 | 542ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 250 | 544ms | Ygdj7 | 0.05 MB/s | `https://ygdj7.com` | 通用代理 |
| 251 | 548ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 252 | 556ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 253 | 558ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 254 | 569ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 255 | 570ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 256 | 574ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 257 | 575ms | Easyboardgame | 0.01 MB/s | `https://easyboardgame.top` | 通用代理 |
| 258 | 576ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 259 | 578ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 260 | 578ms | Gp | 2.3 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 261 | 578ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 262 | 580ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 263 | 591ms | Clawbiz | 0.02 MB/s | `https://clawbiz.io` | 通用代理 |
| 264 | 599ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 265 | 603ms | Fastfile | 1.49 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 266 | 605ms | Umami-mcp | 0.32 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 267 | 608ms | GHProxy Net | 0.15 MB/s | `https://ghproxy.net` | 通用代理 |
| 268 | 617ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 269 | 635ms | Gh | 2.01 MB/s | `https://gh.1k.ink` | 通用代理 |
| 270 | 646ms | Github | 2.09 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 271 | 660ms | Tracely-studio | 0.05 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 272 | 663ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 273 | 666ms | Github | 0.29 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 274 | 672ms | Github | 2.31 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 275 | 673ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 276 | 681ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 277 | 682ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 278 | 686ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 279 | 694ms | Support | 0.13 MB/s | `https://support.apple.com` | 通用代理 |
| 280 | 702ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 281 | 704ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 282 | 706ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 283 | 708ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 284 | 714ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 285 | 720ms | Agentkey | 0.19 MB/s | `https://agentkey.app` | 通用代理 |
| 286 | 720ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 287 | 733ms | Wordpaper | 0.42 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 288 | 744ms | Os | 0.03 MB/s | `https://os.ryo.lu` | 通用代理 |
| 289 | 748ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 290 | 750ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 291 | 766ms | Ghproxy | 0.33 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 292 | 768ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 293 | 769ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 294 | 778ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 295 | 786ms | Docs | 0.15 MB/s | `https://docs.transifex.com` | 通用代理 |
| 296 | 796ms | Anh | 0.25 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 297 | 808ms | Ccgather | 0.08 MB/s | `https://ccgather.com` | 通用代理 |
| 298 | 811ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 299 | 812ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 300 | 815ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 301 | 820ms | Dbgate | 0.11 MB/s | `https://dbgate.org` | 通用代理 |
| 302 | 827ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 303 | 832ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 304 | 857ms | Tools | 2.05 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 305 | 865ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 306 | 871ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 307 | 882ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 308 | 901ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 309 | 903ms | Git | 0.27 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 310 | 913ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 311 | 926ms | Task | 0.02 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 312 | 927ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 313 | 933ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 314 | 934ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 315 | 934ms | Yibiao | 0.13 MB/s | `https://yibiao.pro` | 通用代理 |
| 316 | 940ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 317 | 940ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 318 | 954ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 319 | 963ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 320 | 965ms | Cumora | 0.34 MB/s | `https://cumora.ai` | 通用代理 |
| 321 | 966ms | Web | - | `https://web.4399.com` | 通用代理 |
| 322 | 970ms | Ginlix | 0.29 MB/s | `https://ginlix.ai` | 通用代理 |
| 323 | 979ms | Mimo | 0.19 MB/s | `https://mimo.mi.com` | 通用代理 |
| 324 | 998ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 325 | 1022ms | Github | 2.61 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 326 | 1063ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 327 | 1071ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 328 | 1091ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 329 | 1094ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 330 | 1096ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 331 | 1101ms | Kenyu | 2.36 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 332 | 1113ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 333 | 1134ms | Dimagent | 0.4 MB/s | `https://dimagent.com` | 通用代理 |
| 334 | 1136ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 335 | 1142ms | Your-domain | 0.11 MB/s | `https://your-domain.com` | 通用代理 |
| 336 | 1154ms | V | - | `https://v.douyin.com` | 通用代理 |
| 337 | 1169ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 338 | 1186ms | Ghproxy | 0.36 MB/s | `https://ghproxy.cc` | 通用代理 |
| 339 | 1192ms | Github | 1.82 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 340 | 1202ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 341 | 1222ms | Cfkua | 1.3 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 342 | 1226ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 343 | 1240ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 344 | 1245ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 345 | 1255ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 346 | 1287ms | Atomcode | 0.07 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 347 | 1288ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 348 | 1291ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 349 | 1330ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 350 | 1330ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 351 | 1362ms | Github | 0.19 MB/s | `https://github.chenc.dev` | 通用代理 |
| 352 | 1369ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 353 | 1394ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 354 | 1401ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 355 | 1413ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 356 | 1414ms | Cf | 0.39 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 357 | 1416ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 358 | 1431ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 359 | 1433ms | Gh | 1.23 MB/s | `https://gh.39.al` | 通用代理 |
| 360 | 1445ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 361 | 1565ms | SLink | 0.06 MB/s | `https://slink.ltd` | 通用代理 |
| 362 | 1599ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 363 | 1636ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 364 | 1640ms | Gh | 0.56 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 365 | 1650ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 366 | 1667ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 367 | 1713ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 368 | 1731ms | Gh | 1.84 MB/s | `https://gh.dpik.top` | 通用代理 |
| 369 | 1814ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 370 | 1982ms | G | 0.26 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 371 | 2066ms | Img | - | `https://img.ink` | 通用代理 |
| 372 | 2069ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 373 | 2159ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 374 | 2163ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 375 | 2333ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 376 | 2422ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 377 | 2440ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 378 | 2459ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 379 | 2550ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 380 | 3086ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 381 | 3097ms | Ghproxy | 0.13 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 382 | 3316ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 383 | 3630ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 384 | 6328ms | Proxy | 0.04 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（16 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 15 次 |
| GH Nxnow (`gh-nxnow-top`) | 1 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Git (`git-669966-xyz`) | 2 次 |
| Gh (`gh-b52m-cn`) | 2 次 |
| Proxy (`proxy-vvvv-ee`) | 3 次 |
| 5555 (`5555-cab`) | 27 次 |
| Nssurge (`nssurge-com`) | 1 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 1 次 |
| Doxygen (`doxygen-org`) | 23 次 |
| Dreamgraph (`dreamgraph-nofs-ai`) | 1 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 6 次 |
| Maplecode (`maplecode-art`) | 16 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 12 次 |
| Adult (`adult-contents-fc2-com`) | 2 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 393 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **400** | |

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
