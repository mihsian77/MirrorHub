# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-28T22:18:42Z**，每 6 小时刷新一次。当前 ✅ **386** 在线 / ⚠️ **13** 不稳定 / ⚰️ **51** 已失效归档。

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
| 1 | 56ms | Microsoftedge | 1.15 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 68ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 3 | 69ms | Linkedin | 0.44 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 73ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 79ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 6 | 84ms | App | 0.16 MB/s | `https://app.netlify.com` | 通用代理 |
| 7 | 85ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 8 | 89ms | Godocs | 0.18 MB/s | `https://godocs.io` | 通用代理 |
| 9 | 93ms | Githubstatus | 1.52 MB/s | `https://githubstatus.com` | 通用代理 |
| 10 | 94ms | Deno | 0.59 MB/s | `https://deno.com` | 通用代理 |
| 11 | 94ms | Lawyer-yu | 0.21 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 12 | 97ms | X | 1.28 MB/s | `https://x.com` | 通用代理 |
| 13 | 100ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 14 | 101ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 15 | 103ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 16 | 103ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 17 | 105ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 18 | 107ms | Zebrunner | 2.87 MB/s | `https://zebrunner.com` | 通用代理 |
| 19 | 110ms | Music-cli | 0.56 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 20 | 112ms | Goreportcard | 0.07 MB/s | `https://goreportcard.com` | 通用代理 |
| 21 | 114ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 22 | 116ms | Xjtu-nyxf-study-material | 0.15 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 23 | 117ms | App | 0.06 MB/s | `https://app.codecov.io` | 通用代理 |
| 24 | 120ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 25 | 121ms | Opresume | 0.44 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 26 | 122ms | Img | - | `https://img.shields.io` | 通用代理 |
| 27 | 124ms | Opentakeoff | 0.1 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 28 | 126ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 29 | 130ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 30 | 132ms | Discord | 0.11 MB/s | `https://discord.gg` | 通用代理 |
| 31 | 135ms | Resume-5lv | 0.15 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 32 | 137ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 33 | 138ms | Osf | 0.08 MB/s | `https://osf.io` | 通用代理 |
| 34 | 139ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 35 | 141ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 36 | 141ms | Components | 0.15 MB/s | `https://components.dereekb.com` | 通用代理 |
| 37 | 145ms | Bolt2github | 0.05 MB/s | `https://bolt2github.com` | 通用代理 |
| 38 | 145ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 39 | 146ms | Nextup-resource | 0.05 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 40 | 146ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 41 | 148ms | Tms | 0.15 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 42 | 150ms | Kighelper-cloud | 0.1 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 43 | 151ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 44 | 151ms | Shiori-v1 | 0.04 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 45 | 152ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 46 | 153ms | Impeccable | 0.21 MB/s | `https://impeccable.style` | 通用代理 |
| 47 | 153ms | Thumb | 0.5 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 48 | 156ms | Opensunsama | 0.08 MB/s | `https://opensunsama.com` | 通用代理 |
| 49 | 157ms | Kuroutoshikou | 1.78 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 50 | 157ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 51 | 158ms | App | 0.02 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 52 | 159ms | Ai-trend-publish | 0.05 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 53 | 159ms | Dilo-d14 | 0.25 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 54 | 159ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 55 | 160ms | Ode | - | `https://ode.fun` | 通用代理 |
| 56 | 161ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 57 | 162ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 58 | 162ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 59 | 165ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 60 | 167ms | Cognitum | 0.05 MB/s | `https://cognitum.one` | 通用代理 |
| 61 | 167ms | Vibesql | 0.05 MB/s | `https://vibesql.org` | 通用代理 |
| 62 | 168ms | Cbrowser | 0.45 MB/s | `https://cbrowser.ai` | 通用代理 |
| 63 | 168ms | Training | 0.26 MB/s | `https://training.ti.com` | 通用代理 |
| 64 | 169ms | Git | 0.42 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 65 | 169ms | Github | - | `https://github.788787.xyz` | 通用代理 |
| 66 | 172ms | Git | 0.37 MB/s | `https://git.820828.xyz` | 通用代理 |
| 67 | 173ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 68 | 174ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 69 | 177ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 70 | 177ms | Caiji | 0.02 MB/s | `https://caiji.cyou` | 通用代理 |
| 71 | 178ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 72 | 178ms | Openpua | 0.12 MB/s | `https://openpua.ai` | 通用代理 |
| 73 | 179ms | Github | 0.45 MB/s | `https://github.880824.xyz` | 通用代理 |
| 74 | 180ms | Gitea-mirror | 0.21 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 75 | 181ms | Crypto-funding-arbitrage | 0.09 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 76 | 181ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 77 | 183ms | Bestdori | 0.02 MB/s | `https://bestdori.com` | 通用代理 |
| 78 | 183ms | Freeport | 0.01 MB/s | `https://freeport.network` | 通用代理 |
| 79 | 183ms | GH-Proxy | - | `https://gh-proxy.com` | 通用代理 |
| 80 | 183ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 81 | 185ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 82 | 186ms | Glass | 0.08 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 83 | 188ms | Github | 0.38 MB/s | `https://github.ihnic.com` | 通用代理 |
| 84 | 188ms | Play | 0.01 MB/s | `https://play.templatical.com` | 通用代理 |
| 85 | 189ms | Tokei | 0.12 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 86 | 190ms | GH Monlor | - | `https://gh.monlor.com` | 通用代理 |
| 87 | 191ms | App | 0.01 MB/s | `https://app.opencastor.com` | 通用代理 |
| 88 | 191ms | Hopp | 0.01 MB/s | `https://hopp.sh` | 通用代理 |
| 89 | 192ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 90 | 192ms | Gh | 0.35 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 91 | 192ms | L4d2 | 0.04 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 92 | 192ms | Miaozitie | 0.02 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 93 | 195ms | Caw | 0.02 MB/s | `https://caw.rocks` | 通用代理 |
| 94 | 195ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 95 | 196ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 96 | 197ms | Themolt | 0.05 MB/s | `https://themolt.net` | 通用代理 |
| 97 | 198ms | Axios-http | 1.1 MB/s | `https://axios-http.com` | 通用代理 |
| 98 | 199ms | Clypra | 0.23 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 99 | 200ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 100 | 200ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 101 | 200ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 102 | 201ms | Clayrune | 0.06 MB/s | `https://clayrune.io` | 通用代理 |
| 103 | 202ms | Gh | - | `https://gh.llkk.cc` | 通用代理 |
| 104 | 203ms | Coreos | 2.5 MB/s | `https://coreos.com` | 通用代理 |
| 105 | 204ms | Cody | 0.08 MB/s | `https://cody.todyle.com` | 通用代理 |
| 106 | 204ms | Coffeecli | 0.05 MB/s | `https://coffeecli.com` | 通用代理 |
| 107 | 204ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 108 | 205ms | Gsd | 0.51 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 109 | 206ms | Ai-watch | 0.04 MB/s | `https://ai-watch.dev` | 通用代理 |
| 110 | 209ms | Cursor | 1.1 MB/s | `https://cursor.com` | 通用代理 |
| 111 | 209ms | Twitter | 0.94 MB/s | `https://twitter.com` | 通用代理 |
| 112 | 210ms | Aiblackboxfc | 0.32 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 113 | 213ms | Ghproxy | 0.39 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 114 | 214ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 115 | 216ms | Sub | 0.37 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 116 | 219ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 117 | 220ms | Ampcode | 0.38 MB/s | `https://ampcode.com` | 通用代理 |
| 118 | 221ms | Wings | 0.04 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 119 | 222ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 120 | 224ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 121 | 226ms | Demo | 0.01 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 122 | 226ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 123 | 227ms | Ghproxy | 0.64 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 124 | 228ms | Alas | 0.14 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 125 | 229ms | GH-Proxy Org | - | `https://gh-proxy.org` | 通用代理 |
| 126 | 230ms | Ghproxy | 0.44 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 127 | 233ms | Codeeraser | 0.04 MB/s | `https://codeeraser.dev` | 通用代理 |
| 128 | 233ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 129 | 235ms | Agentlimb | 0.08 MB/s | `https://agentlimb.com` | 通用代理 |
| 130 | 238ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 131 | 241ms | Aka | 0.94 MB/s | `https://aka.ms` | 通用代理 |
| 132 | 241ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 133 | 242ms | Polgarand | 0.03 MB/s | `https://polgarand.org` | 通用代理 |
| 134 | 245ms | Ggg | 0.28 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 135 | 249ms | Opencovibe | 0.12 MB/s | `https://opencovibe.com` | 通用代理 |
| 136 | 250ms | Aomedia | 0.34 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 137 | 253ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 138 | 255ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 139 | 256ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 140 | 257ms | Nisar | 0.89 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 141 | 258ms | Github | 0.58 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 142 | 259ms | Code | 1.21 MB/s | `https://code.claude.com` | 通用代理 |
| 143 | 261ms | Savannah | 0.08 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 144 | 263ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 145 | 266ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 146 | 266ms | Sina | 0.69 MB/s | `https://sina.dev` | 通用代理 |
| 147 | 267ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 148 | 269ms | Chops | 0.01 MB/s | `https://chops.md` | 通用代理 |
| 149 | 270ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 150 | 271ms | Tiktok | 0.23 MB/s | `https://tiktok.com` | 通用代理 |
| 151 | 273ms | Youtu | 2.07 MB/s | `https://youtu.be` | 通用代理 |
| 152 | 274ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 153 | 278ms | Cherryai | 0.01 MB/s | `https://cherryai.com` | 通用代理 |
| 154 | 281ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 155 | 282ms | Agoramarket | 0.01 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 156 | 283ms | Visionmemorymcp | 0.22 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 157 | 285ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 158 | 286ms | Agenticcorporation | 0.07 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 159 | 287ms | Bananaslides | 0.09 MB/s | `https://bananaslides.online` | 通用代理 |
| 160 | 291ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 161 | 292ms | CrashMC CDN | 0.17 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 162 | 293ms | Travis-ci | 0.12 MB/s | `https://travis-ci.org` | 通用代理 |
| 163 | 297ms | Microcoreos | 0.09 MB/s | `https://microcoreos.com` | 通用代理 |
| 164 | 299ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 165 | 299ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 166 | 306ms | Radio-browser | 0.05 MB/s | `https://radio-browser.info` | 通用代理 |
| 167 | 312ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 168 | 313ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 169 | 314ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 170 | 316ms | Gh | 0.49 MB/s | `https://gh.padao.fun` | 通用代理 |
| 171 | 317ms | FastGit CC | 0.35 MB/s | `https://fastgit.cc` | 通用代理 |
| 172 | 317ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 173 | 318ms | Agent-room | 0.04 MB/s | `https://agent-room.com` | 通用代理 |
| 174 | 318ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 175 | 319ms | 30006000 | - | `https://30006000.xyz` | 通用代理 |
| 176 | 319ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 177 | 320ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 178 | 321ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 179 | 321ms | Turborepo-starter-kit-web | 0.12 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 180 | 322ms | Api | 0.02 MB/s | `https://api.solov.cc` | 通用代理 |
| 181 | 322ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 182 | 324ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 183 | 325ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 184 | 327ms | Steamcommunity | 0.17 MB/s | `https://steamcommunity.com` | 通用代理 |
| 185 | 329ms | Sonarcloud | 0.71 MB/s | `https://sonarcloud.io` | 通用代理 |
| 186 | 330ms | Im | 0.13 MB/s | `https://im.codes` | 通用代理 |
| 187 | 331ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 188 | 332ms | Contrib | 0.07 MB/s | `https://contrib.rocks` | 通用代理 |
| 189 | 336ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 190 | 338ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 191 | 339ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 192 | 339ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 193 | 342ms | Bailian | 0.04 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 194 | 343ms | Openttd | 0.02 MB/s | `https://openttd.org` | 通用代理 |
| 195 | 344ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 196 | 345ms | B23 | - | `https://b23.tv` | 通用代理 |
| 197 | 346ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 198 | 349ms | Gpui | 0.07 MB/s | `https://gpui.rs` | 通用代理 |
| 199 | 352ms | Autonomi | 0.03 MB/s | `https://autonomi.dev` | 通用代理 |
| 200 | 353ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 201 | 357ms | Store | 0.91 MB/s | `https://store.steampowered.com` | 通用代理 |
| 202 | 363ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 203 | 368ms | App | 0.02 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 204 | 368ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 205 | 371ms | Claude | 0.07 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 206 | 386ms | Weaverse | 0.32 MB/s | `https://weaverse.io` | 通用代理 |
| 207 | 388ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 208 | 391ms | Oem | 0.01 MB/s | `https://oem.re` | 通用代理 |
| 209 | 392ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 210 | 395ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 211 | 395ms | Serac | 0.03 MB/s | `https://serac.build` | 通用代理 |
| 212 | 401ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 213 | 411ms | Msdn | 0.1 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 214 | 413ms | GHFast | - | `https://ghfast.top` | 通用代理 |
| 215 | 420ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 216 | 420ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 217 | 424ms | YYLX Git | 0.21 MB/s | `https://git.yylx.win` | 通用代理 |
| 218 | 430ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 219 | 432ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 220 | 433ms | Bible-ai-explorer | 0.1 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 221 | 434ms | Lecvdemarius | 0.13 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 222 | 437ms | Ednovas Mirror | 0.19 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 223 | 438ms | Aps | 0.04 MB/s | `https://aps.com` | 通用代理 |
| 224 | 443ms | Memstack | 0.03 MB/s | `https://memstack.pro` | 通用代理 |
| 225 | 444ms | Safedocx | 0.18 MB/s | `https://safedocx.com` | 通用代理 |
| 226 | 448ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 227 | 452ms | V4 | - | `https://v4.gh-proxy.org` | 通用代理 |
| 228 | 453ms | Ark | 0.55 MB/s | `https://ark.intel.com` | 通用代理 |
| 229 | 455ms | Getgit | 0.23 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 230 | 458ms | Bseindia | 0.05 MB/s | `https://bseindia.com` | 通用代理 |
| 231 | 459ms | Gh | 0.86 MB/s | `https://gh.noki.icu` | 通用代理 |
| 232 | 460ms | Gh | 0.28 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 233 | 463ms | Huly-mcp | 0.16 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 234 | 464ms | Tvv | 0.42 MB/s | `https://tvv.tw` | 通用代理 |
| 235 | 465ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 236 | 470ms | Patchworkos | 0.39 MB/s | `https://patchworkos.com` | 通用代理 |
| 237 | 471ms | Aosmd | 0.31 MB/s | `https://aosmd.com` | 通用代理 |
| 238 | 474ms | You | 0.05 MB/s | `https://you.piccalc.com` | 通用代理 |
| 239 | 486ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 240 | 496ms | Hk | - | `https://hk.gh-proxy.com` | 通用代理 |
| 241 | 496ms | Proxy | 0.31 MB/s | `https://proxy.vvvv.ee` | 通用代理 |
| 242 | 500ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 243 | 500ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 244 | 502ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 245 | 506ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 246 | 507ms | Adult | 0.01 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 247 | 508ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 248 | 521ms | Impro | 0.34 MB/s | `https://impro.social` | 通用代理 |
| 249 | 523ms | Lucky | 0.55 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 250 | 528ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 251 | 529ms | Wl | - | `https://wl.do` | 通用代理 |
| 252 | 531ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 253 | 541ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 254 | 543ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 255 | 544ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 256 | 546ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 257 | 547ms | 3d-set-visualizer | 0.06 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 258 | 551ms | Agentkey | 0.11 MB/s | `https://agentkey.app` | 通用代理 |
| 259 | 552ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 260 | 553ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 261 | 559ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 262 | 559ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 263 | 560ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 264 | 564ms | Umami-mcp | 0.58 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 265 | 576ms | Easyboardgame | 0.01 MB/s | `https://easyboardgame.top` | 通用代理 |
| 266 | 578ms | Gp | 0.43 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 267 | 579ms | Serverkit | 0.01 MB/s | `https://serverkit.ai` | 通用代理 |
| 268 | 580ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 269 | 581ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 270 | 591ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 271 | 596ms | Clawbiz | 0.05 MB/s | `https://clawbiz.io` | 通用代理 |
| 272 | 600ms | Gh | 0.4 MB/s | `https://gh.1k.ink` | 通用代理 |
| 273 | 603ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 274 | 611ms | Fastfile | 0.34 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 275 | 640ms | Github | 0.33 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 276 | 643ms | Github | 0.45 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 277 | 660ms | Agoracitizen | 0.03 MB/s | `https://agoracitizen.app` | 通用代理 |
| 278 | 662ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 279 | 669ms | Internhack | 0.05 MB/s | `https://internhack.xyz` | 通用代理 |
| 280 | 674ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 281 | 681ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 282 | 682ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 283 | 683ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 284 | 683ms | Github | 0.41 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 285 | 689ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 286 | 689ms | Support | 0.12 MB/s | `https://support.apple.com` | 通用代理 |
| 287 | 695ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 288 | 695ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 289 | 712ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 290 | 715ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 291 | 723ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 292 | 733ms | Wordpaper | 0.42 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 293 | 739ms | Aif | 0.01 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 294 | 746ms | Docs | 0.29 MB/s | `https://docs.transifex.com` | 通用代理 |
| 295 | 753ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 296 | 756ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 297 | 758ms | Congressmcp | 0.01 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 298 | 765ms | Ghproxy | 0.25 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 299 | 765ms | Os | 0.06 MB/s | `https://os.ryo.lu` | 通用代理 |
| 300 | 766ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 301 | 789ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 302 | 794ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 303 | 797ms | Anh | 0.07 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 304 | 811ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 305 | 832ms | Dbgate | 0.25 MB/s | `https://dbgate.org` | 通用代理 |
| 306 | 834ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 307 | 835ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 308 | 842ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 309 | 856ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 310 | 862ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 311 | 863ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 312 | 865ms | Tools | 1.39 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 313 | 892ms | Git | 0.16 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 314 | 902ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 315 | 915ms | Web | - | `https://web.4399.com` | 通用代理 |
| 316 | 919ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 317 | 934ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 318 | 934ms | Github | 0.42 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 319 | 936ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 320 | 937ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 321 | 950ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 322 | 951ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 323 | 952ms | Ginlix | 0.15 MB/s | `https://ginlix.ai` | 通用代理 |
| 324 | 956ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 325 | 960ms | Yibiao | 0.14 MB/s | `https://yibiao.pro` | 通用代理 |
| 326 | 978ms | Mimo | 0.16 MB/s | `https://mimo.mi.com` | 通用代理 |
| 327 | 1038ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 328 | 1043ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 329 | 1053ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 330 | 1058ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 331 | 1059ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 332 | 1061ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 333 | 1079ms | Kenyu | 0.44 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 334 | 1097ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 335 | 1122ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 336 | 1132ms | V | - | `https://v.douyin.com` | 通用代理 |
| 337 | 1135ms | Dimagent | 0.11 MB/s | `https://dimagent.com` | 通用代理 |
| 338 | 1135ms | Github | 0.45 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 339 | 1151ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 340 | 1191ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 341 | 1193ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 342 | 1196ms | Gh | - | `https://gh.223456.xyz` | 通用代理 |
| 343 | 1209ms | Gh | - | `https://gh.dpik.top` | 通用代理 |
| 344 | 1215ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 345 | 1224ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 346 | 1225ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 347 | 1233ms | Atomcode | 0.07 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 348 | 1250ms | Ghproxy | 0.19 MB/s | `https://ghproxy.cc` | 通用代理 |
| 349 | 1261ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 350 | 1263ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 351 | 1281ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 352 | 1295ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 353 | 1308ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 354 | 1326ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 355 | 1327ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 356 | 1333ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 357 | 1336ms | Gh | 0.67 MB/s | `https://gh.39.al` | 通用代理 |
| 358 | 1337ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 359 | 1375ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 360 | 1381ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 361 | 1392ms | Github | 0.15 MB/s | `https://github.chenc.dev` | 通用代理 |
| 362 | 1421ms | Cf | 0.18 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 363 | 1456ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 364 | 1468ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 365 | 1468ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 366 | 1469ms | Cumora | 0.08 MB/s | `https://cumora.ai` | 通用代理 |
| 367 | 1488ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 368 | 1571ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 369 | 1642ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 370 | 1656ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 371 | 1705ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 372 | 1749ms | Cfkua | 0.41 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 373 | 2093ms | Img | - | `https://img.ink` | 通用代理 |
| 374 | 2098ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 375 | 2136ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 376 | 2147ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 377 | 2427ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 378 | 2574ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 379 | 2582ms | G | 0.18 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 380 | 2604ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 381 | 2697ms | Ghproxy | 0.12 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 382 | 2732ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 383 | 2975ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 384 | 3183ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 385 | 3186ms | Gh | - | `https://gh.b52m.cn` | 通用代理 |
| 386 | 4089ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（13 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 6 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 12 次 |
| GitClone (`gitclone-com`) | 7 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 3 次 |
| 5555 (`5555-cab`) | 24 次 |
| Doxygen (`doxygen-org`) | 20 次 |
| App (`app-happy-next-com`) | 1 次 |
| Flashtype (`flashtype-com`) | 1 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 3 次 |
| Maplecode (`maplecode-art`) | 13 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 9 次 |

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
