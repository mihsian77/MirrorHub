# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-29T04:36:27Z**，每 6 小时刷新一次。当前 ✅ **388** 在线 / ⚠️ **11** 不稳定 / ⚰️ **51** 已失效归档。

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
| 1 | 55ms | Microsoftedge | 1.31 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 67ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 3 | 70ms | Linkedin | 0.45 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 73ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 79ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 6 | 85ms | App | 0.27 MB/s | `https://app.netlify.com` | 通用代理 |
| 7 | 85ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 8 | 89ms | Godocs | 0.15 MB/s | `https://godocs.io` | 通用代理 |
| 9 | 93ms | Githubstatus | 2.88 MB/s | `https://githubstatus.com` | 通用代理 |
| 10 | 93ms | Lawyer-yu | 0.19 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 11 | 96ms | Deno | 0.44 MB/s | `https://deno.com` | 通用代理 |
| 12 | 96ms | X | 1.51 MB/s | `https://x.com` | 通用代理 |
| 13 | 102ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 14 | 102ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 15 | 103ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 16 | 103ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 17 | 106ms | Zebrunner | 1.82 MB/s | `https://zebrunner.com` | 通用代理 |
| 18 | 108ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 19 | 111ms | Goreportcard | 0.07 MB/s | `https://goreportcard.com` | 通用代理 |
| 20 | 113ms | Xjtu-nyxf-study-material | 0.17 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 21 | 117ms | Music-cli | 0.47 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 22 | 117ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 23 | 119ms | App | 0.06 MB/s | `https://app.codecov.io` | 通用代理 |
| 24 | 119ms | Img | - | `https://img.shields.io` | 通用代理 |
| 25 | 121ms | Opresume | 0.77 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 26 | 124ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 27 | 126ms | Opentakeoff | 0.1 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 28 | 128ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 29 | 129ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 30 | 132ms | Discord | 0.1 MB/s | `https://discord.gg` | 通用代理 |
| 31 | 132ms | Resume-5lv | 0.23 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 32 | 137ms | Components | 0.19 MB/s | `https://components.dereekb.com` | 通用代理 |
| 33 | 137ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 34 | 139ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 35 | 139ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 36 | 142ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 37 | 144ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 38 | 145ms | Nextup-resource | 0.08 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 39 | 146ms | Bolt2github | 0.1 MB/s | `https://bolt2github.com` | 通用代理 |
| 40 | 148ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 41 | 150ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 42 | 151ms | Kuroutoshikou | 1.19 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 43 | 151ms | Tms | 0.13 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 44 | 152ms | Kighelper-cloud | 0.1 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 45 | 153ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 46 | 153ms | Impeccable | 0.88 MB/s | `https://impeccable.style` | 通用代理 |
| 47 | 154ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 48 | 156ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 49 | 158ms | Opensunsama | 0.07 MB/s | `https://opensunsama.com` | 通用代理 |
| 50 | 159ms | Shiori-v1 | 0.04 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 51 | 163ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 52 | 163ms | App | 0.02 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 53 | 163ms | Dilo-d14 | 0.25 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 54 | 163ms | Ode | - | `https://ode.fun` | 通用代理 |
| 55 | 164ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 56 | 164ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 57 | 167ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 58 | 168ms | Github | 2.32 MB/s | `https://github.788787.xyz` | 通用代理 |
| 59 | 168ms | Vibesql | 0.14 MB/s | `https://vibesql.org` | 通用代理 |
| 60 | 169ms | Training | 0.23 MB/s | `https://training.ti.com` | 通用代理 |
| 61 | 170ms | Cbrowser | 1.71 MB/s | `https://cbrowser.ai` | 通用代理 |
| 62 | 171ms | Ai-trend-publish | 0.03 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 63 | 171ms | Cognitum | 0.19 MB/s | `https://cognitum.one` | 通用代理 |
| 64 | 171ms | Openpua | 0.33 MB/s | `https://openpua.ai` | 通用代理 |
| 65 | 172ms | Git | 1.47 MB/s | `https://git.820828.xyz` | 通用代理 |
| 66 | 173ms | Git | 2.47 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 67 | 175ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 68 | 178ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 69 | 178ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 70 | 179ms | Caiji | 0.07 MB/s | `https://caiji.cyou` | 通用代理 |
| 71 | 179ms | Gitea-mirror | 0.75 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 72 | 179ms | Glass | 0.23 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 73 | 181ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 74 | 181ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 75 | 183ms | GH-Proxy | 1.36 MB/s | `https://gh-proxy.com` | 通用代理 |
| 76 | 183ms | Thumb | 0.5 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 77 | 184ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 78 | 184ms | Ghproxy | 1.8 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 79 | 184ms | Play | 0.03 MB/s | `https://play.templatical.com` | 通用代理 |
| 80 | 185ms | Bestdori | 0.11 MB/s | `https://bestdori.com` | 通用代理 |
| 81 | 185ms | Github | 1.68 MB/s | `https://github.880824.xyz` | 通用代理 |
| 82 | 186ms | L4d2 | 0.14 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 83 | 186ms | Tokei | 0.64 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 84 | 187ms | Axios-http | 0.91 MB/s | `https://axios-http.com` | 通用代理 |
| 85 | 187ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 86 | 187ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 87 | 188ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 88 | 188ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 89 | 188ms | Github | 2.58 MB/s | `https://github.ihnic.com` | 通用代理 |
| 90 | 189ms | GH Monlor | 0.66 MB/s | `https://gh.monlor.com` | 通用代理 |
| 91 | 189ms | Gh | 2.01 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 92 | 191ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 93 | 193ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 94 | 193ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 95 | 194ms | Clypra | 0.08 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 96 | 195ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 97 | 198ms | Clayrune | 0.17 MB/s | `https://clayrune.io` | 通用代理 |
| 98 | 198ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 99 | 199ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 100 | 199ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 101 | 199ms | Themolt | 0.05 MB/s | `https://themolt.net` | 通用代理 |
| 102 | 200ms | Coreos | 6.79 MB/s | `https://coreos.com` | 通用代理 |
| 103 | 200ms | Gh | 1.49 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 104 | 200ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 105 | 200ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 106 | 201ms | Gsd | 0.46 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 107 | 204ms | Aiblackboxfc | 0.58 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 108 | 205ms | Cody | 0.17 MB/s | `https://cody.todyle.com` | 通用代理 |
| 109 | 206ms | Coffeecli | 0.11 MB/s | `https://coffeecli.com` | 通用代理 |
| 110 | 209ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 111 | 209ms | Radio-browser | 0.03 MB/s | `https://radio-browser.info` | 通用代理 |
| 112 | 210ms | Alas | 0.72 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 113 | 210ms | Cursor | 1.18 MB/s | `https://cursor.com` | 通用代理 |
| 114 | 211ms | Twitter | 1.09 MB/s | `https://twitter.com` | 通用代理 |
| 115 | 214ms | Ai-watch | 0.04 MB/s | `https://ai-watch.dev` | 通用代理 |
| 116 | 214ms | Ampcode | 0.15 MB/s | `https://ampcode.com` | 通用代理 |
| 117 | 215ms | Pidash | 0.02 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 118 | 216ms | Sub | 0.25 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 119 | 218ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 120 | 219ms | Ghproxy | 2.23 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 121 | 220ms | Wings | 0.04 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 122 | 224ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 123 | 227ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 124 | 230ms | Codeeraser | 0.08 MB/s | `https://codeeraser.dev` | 通用代理 |
| 125 | 235ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 126 | 238ms | Agentlimb | 0.21 MB/s | `https://agentlimb.com` | 通用代理 |
| 127 | 238ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 128 | 239ms | Polgarand | 0.07 MB/s | `https://polgarand.org` | 通用代理 |
| 129 | 240ms | GH-Proxy Org | 1.35 MB/s | `https://gh-proxy.org` | 通用代理 |
| 130 | 242ms | Ghproxy | 0.73 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 131 | 244ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 132 | 245ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 133 | 246ms | Aka | 1.02 MB/s | `https://aka.ms` | 通用代理 |
| 134 | 249ms | Aomedia | 0.45 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 135 | 250ms | Savannah | 0.08 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 136 | 252ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 137 | 253ms | Opencovibe | 0.3 MB/s | `https://opencovibe.com` | 通用代理 |
| 138 | 254ms | Cherryai | 0.06 MB/s | `https://cherryai.com` | 通用代理 |
| 139 | 255ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 140 | 255ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 141 | 258ms | Nisar | 0.88 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 142 | 260ms | Sina | - | `https://sina.dev` | 通用代理 |
| 143 | 260ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 144 | 260ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 145 | 261ms | Github | 0.49 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 146 | 266ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 147 | 267ms | Ggg | 2.01 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 148 | 267ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 149 | 268ms | Agoramarket | 0.02 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 150 | 268ms | Code | 0.95 MB/s | `https://code.claude.com` | 通用代理 |
| 151 | 268ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 152 | 270ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 153 | 272ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 154 | 274ms | Travis-ci | 0.33 MB/s | `https://travis-ci.org` | 通用代理 |
| 155 | 276ms | Youtu | 2.39 MB/s | `https://youtu.be` | 通用代理 |
| 156 | 281ms | Zuckerbot | 0.04 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 157 | 282ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 158 | 286ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 159 | 287ms | Visionmemorymcp | 0.22 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 160 | 288ms | Agenticcorporation | 0.07 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 161 | 290ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 162 | 291ms | CrashMC CDN | 0.66 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 163 | 291ms | Microcoreos | 0.33 MB/s | `https://microcoreos.com` | 通用代理 |
| 164 | 294ms | Bananaslides | 0.31 MB/s | `https://bananaslides.online` | 通用代理 |
| 165 | 300ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 166 | 302ms | Tiktok | 0.08 MB/s | `https://tiktok.com` | 通用代理 |
| 167 | 305ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 168 | 306ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 169 | 306ms | Sonarcloud | 0.37 MB/s | `https://sonarcloud.io` | 通用代理 |
| 170 | 307ms | Gh | 0.47 MB/s | `https://gh.padao.fun` | 通用代理 |
| 171 | 309ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 172 | 312ms | FastGit CC | 0.99 MB/s | `https://fastgit.cc` | 通用代理 |
| 173 | 313ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 174 | 314ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 175 | 314ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 176 | 315ms | Api | 0.07 MB/s | `https://api.solov.cc` | 通用代理 |
| 177 | 317ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 178 | 322ms | Turborepo-starter-kit-web | 0.09 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 179 | 323ms | Agent-room | 0.04 MB/s | `https://agent-room.com` | 通用代理 |
| 180 | 323ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 181 | 323ms | Steamcommunity | 0.15 MB/s | `https://steamcommunity.com` | 通用代理 |
| 182 | 325ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 183 | 325ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 184 | 329ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 185 | 330ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 186 | 337ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 187 | 337ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 188 | 337ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 189 | 339ms | B23 | - | `https://b23.tv` | 通用代理 |
| 190 | 346ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 191 | 347ms | Autonomi | 0.04 MB/s | `https://autonomi.dev` | 通用代理 |
| 192 | 348ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 193 | 348ms | Gpui | 0.25 MB/s | `https://gpui.rs` | 通用代理 |
| 194 | 349ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 195 | 354ms | Store | 1.46 MB/s | `https://store.steampowered.com` | 通用代理 |
| 196 | 357ms | 30006000 | - | `https://30006000.xyz` | 通用代理 |
| 197 | 360ms | Bailian | 0.03 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 198 | 360ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 199 | 365ms | Contrib | 0.28 MB/s | `https://contrib.rocks` | 通用代理 |
| 200 | 366ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 201 | 370ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 202 | 370ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 203 | 370ms | Claude | 0.37 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 204 | 373ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 205 | 382ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 206 | 385ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 207 | 387ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 208 | 390ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 209 | 391ms | Weaverse | 0.46 MB/s | `https://weaverse.io` | 通用代理 |
| 210 | 393ms | Im | 0.29 MB/s | `https://im.codes` | 通用代理 |
| 211 | 394ms | Serac | 0.09 MB/s | `https://serac.build` | 通用代理 |
| 212 | 402ms | GH Nxnow | 0.6 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 213 | 406ms | Msdn | 0.14 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 214 | 414ms | GHFast | 0.44 MB/s | `https://ghfast.top` | 通用代理 |
| 215 | 419ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 216 | 419ms | YYLX Git | 1.99 MB/s | `https://git.yylx.win` | 通用代理 |
| 217 | 420ms | Getgit | 1.78 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 218 | 422ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 219 | 424ms | Lecvdemarius | 0.11 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 220 | 426ms | Ednovas Mirror | 0.34 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 221 | 428ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 222 | 431ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 223 | 437ms | Safedocx | 0.23 MB/s | `https://safedocx.com` | 通用代理 |
| 224 | 437ms | V4 | 1.84 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 225 | 449ms | Memstack | 0.03 MB/s | `https://memstack.pro` | 通用代理 |
| 226 | 449ms | Tvv | 2.79 MB/s | `https://tvv.tw` | 通用代理 |
| 227 | 455ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 228 | 456ms | Bible-ai-explorer | 0.07 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 229 | 457ms | Ark | 0.46 MB/s | `https://ark.intel.com` | 通用代理 |
| 230 | 457ms | Gh | 0.77 MB/s | `https://gh.noki.icu` | 通用代理 |
| 231 | 465ms | Huly-mcp | 0.17 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 232 | 466ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 233 | 466ms | Gh | 2.04 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 234 | 473ms | Patchworkos | 0.37 MB/s | `https://patchworkos.com` | 通用代理 |
| 235 | 474ms | Aosmd | 0.42 MB/s | `https://aosmd.com` | 通用代理 |
| 236 | 475ms | Hk | 1.28 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 237 | 476ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 238 | 484ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 239 | 490ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 240 | 493ms | You | 0.07 MB/s | `https://you.piccalc.com` | 通用代理 |
| 241 | 499ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 242 | 500ms | Adult | 0.01 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 243 | 500ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 244 | 502ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 245 | 505ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 246 | 515ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 247 | 518ms | Gh | 2.03 MB/s | `https://gh.idayer.com` | 通用代理 |
| 248 | 521ms | Impro | 1.8 MB/s | `https://impro.social` | 通用代理 |
| 249 | 522ms | Lucky | 0.54 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 250 | 527ms | Wl | - | `https://wl.do` | 通用代理 |
| 251 | 530ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 252 | 536ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 253 | 536ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 254 | 541ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 255 | 546ms | 3d-set-visualizer | 0.06 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 256 | 549ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 257 | 554ms | Umami-mcp | 0.52 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 258 | 559ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 259 | 561ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 260 | 564ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 261 | 572ms | Agentkey | 0.29 MB/s | `https://agentkey.app` | 通用代理 |
| 262 | 574ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 263 | 576ms | Gp | 1.87 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 264 | 580ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 265 | 581ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 266 | 581ms | GHProxy Net | 0.03 MB/s | `https://ghproxy.net` | 通用代理 |
| 267 | 583ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 268 | 584ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 269 | 590ms | Clawbiz | 0.06 MB/s | `https://clawbiz.io` | 通用代理 |
| 270 | 592ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 271 | 594ms | Bseindia | 0.02 MB/s | `https://bseindia.com` | 通用代理 |
| 272 | 595ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 273 | 608ms | Gh | 1.98 MB/s | `https://gh.1k.ink` | 通用代理 |
| 274 | 617ms | Fastfile | 1.89 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 275 | 644ms | Github | 2.86 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 276 | 652ms | Agoracitizen | 0.03 MB/s | `https://agoracitizen.app` | 通用代理 |
| 277 | 653ms | Support | 1.13 MB/s | `https://support.apple.com` | 通用代理 |
| 278 | 657ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 279 | 662ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 280 | 664ms | Github | 0.32 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 281 | 676ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 282 | 684ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 283 | 686ms | Internhack | 0.04 MB/s | `https://internhack.xyz` | 通用代理 |
| 284 | 687ms | Github | 2.39 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 285 | 693ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 286 | 706ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 287 | 707ms | Onetwin | 0.01 MB/s | `https://onetwin.cn` | 通用代理 |
| 288 | 708ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 289 | 719ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 290 | 720ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 291 | 720ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 292 | 732ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 293 | 734ms | Wordpaper | 0.65 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 294 | 737ms | Aif | 0.05 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 295 | 742ms | GHFile Geekertao | 0.06 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 296 | 749ms | Docs | 0.29 MB/s | `https://docs.transifex.com` | 通用代理 |
| 297 | 751ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 298 | 757ms | Ghproxy | 0.26 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 299 | 763ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 300 | 766ms | Os | 0.12 MB/s | `https://os.ryo.lu` | 通用代理 |
| 301 | 767ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 302 | 790ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 303 | 790ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 304 | 795ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 305 | 796ms | Anh | 0.21 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 306 | 810ms | Dbgate | 0.23 MB/s | `https://dbgate.org` | 通用代理 |
| 307 | 830ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 308 | 832ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 309 | 844ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 310 | 846ms | Tools | 2.33 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 311 | 856ms | Ccgather | 0.05 MB/s | `https://ccgather.com` | 通用代理 |
| 312 | 868ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 313 | 877ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 314 | 915ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 315 | 922ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 316 | 922ms | Task | 0.02 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 317 | 931ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 318 | 931ms | Git | - | `https://git.tangbai.cc` | 通用代理 |
| 319 | 940ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 320 | 944ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 321 | 949ms | Web | - | `https://web.4399.com` | 通用代理 |
| 322 | 954ms | Ginlix | 0.74 MB/s | `https://ginlix.ai` | 通用代理 |
| 323 | 956ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 324 | 960ms | Yibiao | 0.11 MB/s | `https://yibiao.pro` | 通用代理 |
| 325 | 987ms | Mimo | 0.15 MB/s | `https://mimo.mi.com` | 通用代理 |
| 326 | 999ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 327 | 1008ms | Github | 1.9 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 328 | 1044ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 329 | 1045ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 330 | 1060ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 331 | 1061ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 332 | 1063ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 333 | 1064ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 334 | 1065ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 335 | 1083ms | Kenyu | 2.07 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 336 | 1111ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 337 | 1119ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 338 | 1140ms | V | - | `https://v.douyin.com` | 通用代理 |
| 339 | 1156ms | Dimagent | 0.17 MB/s | `https://dimagent.com` | 通用代理 |
| 340 | 1161ms | Your-domain | 0.04 MB/s | `https://your-domain.com` | 通用代理 |
| 341 | 1167ms | Github | 1.75 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 342 | 1197ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 343 | 1203ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 344 | 1211ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 345 | 1214ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 346 | 1232ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 347 | 1236ms | Atomcode | 0.05 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 348 | 1240ms | Cumora | 0.34 MB/s | `https://cumora.ai` | 通用代理 |
| 349 | 1257ms | Ghproxy | 0.24 MB/s | `https://ghproxy.cc` | 通用代理 |
| 350 | 1262ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 351 | 1264ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 352 | 1329ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 353 | 1342ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 354 | 1362ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 355 | 1375ms | Gh | - | `https://gh.39.al` | 通用代理 |
| 356 | 1392ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 357 | 1394ms | Github | - | `https://github.chenc.dev` | 通用代理 |
| 358 | 1406ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 359 | 1409ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 360 | 1416ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 361 | 1428ms | Cf | 0.24 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 362 | 1462ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 363 | 1469ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 364 | 1486ms | Cfkua | 2.03 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 365 | 1588ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 366 | 1595ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 367 | 1636ms | I-qps | 0.02 MB/s | `https://i-qps.net` | 通用代理 |
| 368 | 1640ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 369 | 1680ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 370 | 1687ms | Gh | 0.54 MB/s | `https://gh.dpik.top` | 通用代理 |
| 371 | 1712ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 372 | 1897ms | Git | 0.08 MB/s | `https://git.669966.xyz` | 通用代理 |
| 373 | 2028ms | G | - | `https://g.blfrp.cn` | 通用代理 |
| 374 | 2041ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 375 | 2150ms | Img | - | `https://img.ink` | 通用代理 |
| 376 | 2166ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 377 | 2235ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 378 | 2288ms | Gh | 0.09 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 379 | 2321ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 380 | 2438ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 381 | 2493ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 382 | 2535ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 383 | 2682ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 384 | 2710ms | Ghproxy | 0.05 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 385 | 3017ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 386 | 3156ms | Gh | 0.13 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 387 | 3180ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 388 | 3752ms | GHProxy MonkeyRay | - | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（11 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GH Zwnes (`gh-zwnes-xyz`) | 13 次 |
| Proxy (`proxy-yaoyaoling-net`) | 4 次 |
| Comfyit (`comfyit-cn`) | 1 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |
| 5555 (`5555-cab`) | 25 次 |
| Doxygen (`doxygen-org`) | 21 次 |
| Flashtype (`flashtype-com`) | 2 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 4 次 |
| Maplecode (`maplecode-art`) | 14 次 |
| Mobilevc (`mobilevc-top`) | 1 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 10 次 |

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
