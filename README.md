# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-30T22:01:55Z**，每 6 小时刷新一次。当前 ✅ **386** 在线 / ⚠️ **19** 不稳定 / ⚰️ **52** 已失效归档。

## 核心特性

- **405 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 64ms | Microsoftedge | 0.2 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 70ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 3 | 77ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 4 | 81ms | Githubstatus | 5.64 MB/s | `https://githubstatus.com` | 通用代理 |
| 5 | 81ms | Linkedin | 0.13 MB/s | `https://linkedin.com` | 通用代理 |
| 6 | 83ms | App | 0.12 MB/s | `https://app.netlify.com` | 通用代理 |
| 7 | 83ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 8 | 89ms | Godocs | 0.06 MB/s | `https://godocs.io` | 通用代理 |
| 9 | 94ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 10 | 95ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 11 | 98ms | Lawyer-yu | 0.06 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 12 | 99ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 13 | 99ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 14 | 100ms | X | 1.5 MB/s | `https://x.com` | 通用代理 |
| 15 | 100ms | Zebrunner | 1.58 MB/s | `https://zebrunner.com` | 通用代理 |
| 16 | 102ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 17 | 110ms | Xjtu-nyxf-study-material | 0.26 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 18 | 111ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 19 | 115ms | Resume-5lv | 0.32 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 20 | 116ms | Deno | 0.21 MB/s | `https://deno.com` | 通用代理 |
| 21 | 119ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 22 | 120ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 23 | 120ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 24 | 121ms | Opresume | 0.48 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 25 | 126ms | Opentakeoff | 0.05 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 26 | 127ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 27 | 127ms | Music-cli | 0.29 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 28 | 127ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 29 | 131ms | Discord | 0.09 MB/s | `https://discord.gg` | 通用代理 |
| 30 | 139ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 31 | 140ms | Img | - | `https://img.shields.io` | 通用代理 |
| 32 | 141ms | Components | 0.11 MB/s | `https://components.dereekb.com` | 通用代理 |
| 33 | 141ms | Training | 0.23 MB/s | `https://training.ti.com` | 通用代理 |
| 34 | 146ms | Opensunsama | 0.09 MB/s | `https://opensunsama.com` | 通用代理 |
| 35 | 148ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 36 | 148ms | Impeccable | 0.94 MB/s | `https://impeccable.style` | 通用代理 |
| 37 | 149ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 38 | 150ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 39 | 151ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 40 | 151ms | Bolt2github | 0.04 MB/s | `https://bolt2github.com` | 通用代理 |
| 41 | 153ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 42 | 153ms | Osf | 0.01 MB/s | `https://osf.io` | 通用代理 |
| 43 | 155ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 44 | 156ms | Kighelper-cloud | 0.16 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 45 | 156ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 46 | 158ms | Caw | 0.11 MB/s | `https://caw.rocks` | 通用代理 |
| 47 | 159ms | Git | 2.81 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 48 | 160ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 49 | 161ms | Play | 0.07 MB/s | `https://play.templatical.com` | 通用代理 |
| 50 | 162ms | Shiori-v1 | 0.08 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 51 | 164ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 52 | 164ms | Git | 3.05 MB/s | `https://git.820828.xyz` | 通用代理 |
| 53 | 164ms | Github | 2.83 MB/s | `https://github.788787.xyz` | 通用代理 |
| 54 | 165ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 55 | 166ms | Ode | - | `https://ode.fun` | 通用代理 |
| 56 | 167ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 57 | 169ms | Ghproxy | 3.65 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 58 | 170ms | Tokei | 0.56 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 59 | 171ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 60 | 171ms | Gitea-mirror | 0.92 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 61 | 172ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 62 | 172ms | Docs | 0.05 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 63 | 174ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 64 | 175ms | Caiji | - | `https://caiji.cyou` | 通用代理 |
| 65 | 175ms | Crypto-funding-arbitrage | 0.09 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 66 | 175ms | Openpua | 0.91 MB/s | `https://openpua.ai` | 通用代理 |
| 67 | 175ms | Tms | 0.1 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 68 | 175ms | Vibesql | 0.17 MB/s | `https://vibesql.org` | 通用代理 |
| 69 | 176ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 70 | 177ms | Ai-trend-publish | 0.03 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 71 | 177ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 72 | 178ms | Gh | 3.95 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 73 | 178ms | Github | 3.44 MB/s | `https://github.880824.xyz` | 通用代理 |
| 74 | 179ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 75 | 181ms | Bestdori | 0.15 MB/s | `https://bestdori.com` | 通用代理 |
| 76 | 181ms | L4d2 | 0.19 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 77 | 181ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 78 | 181ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 79 | 182ms | Dilo-d14 | 0.29 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 80 | 182ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 81 | 184ms | Clypra | 0.08 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 82 | 185ms | Axios-http | 0.48 MB/s | `https://axios-http.com` | 通用代理 |
| 83 | 185ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 84 | 185ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 85 | 186ms | Cody | 0.41 MB/s | `https://cody.todyle.com` | 通用代理 |
| 86 | 186ms | Freeport | 0.06 MB/s | `https://freeport.network` | 通用代理 |
| 87 | 186ms | Glass | 0.35 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 88 | 187ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 89 | 188ms | Ghproxy | 2.6 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 90 | 189ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 91 | 191ms | GH Monlor | 1.52 MB/s | `https://gh.monlor.com` | 通用代理 |
| 92 | 192ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 93 | 192ms | GH-Proxy | 1.45 MB/s | `https://gh-proxy.com` | 通用代理 |
| 94 | 192ms | Radio-browser | 0.06 MB/s | `https://radio-browser.info` | 通用代理 |
| 95 | 194ms | Twitter | 1.03 MB/s | `https://twitter.com` | 通用代理 |
| 96 | 196ms | Github | 2.36 MB/s | `https://github.ihnic.com` | 通用代理 |
| 97 | 199ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 98 | 201ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 99 | 202ms | Hopp | 0.08 MB/s | `https://hopp.sh` | 通用代理 |
| 100 | 204ms | Alas | 1.35 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 101 | 204ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 102 | 205ms | Cherryai | 0.08 MB/s | `https://cherryai.com` | 通用代理 |
| 103 | 205ms | Clayrune | 0.18 MB/s | `https://clayrune.io` | 通用代理 |
| 104 | 205ms | Codeeraser | 0.13 MB/s | `https://codeeraser.dev` | 通用代理 |
| 105 | 205ms | Cognitum | 0.13 MB/s | `https://cognitum.one` | 通用代理 |
| 106 | 205ms | Polgarand | 0.12 MB/s | `https://polgarand.org` | 通用代理 |
| 107 | 206ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 108 | 207ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 109 | 209ms | Pidash | 0.07 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 110 | 210ms | Coffeecli | 0.14 MB/s | `https://coffeecli.com` | 通用代理 |
| 111 | 210ms | Demo | 0.05 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 112 | 213ms | Thumb | 4.82 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 113 | 215ms | Sub | 0.17 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 114 | 216ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 115 | 217ms | Cbrowser | 0.62 MB/s | `https://cbrowser.ai` | 通用代理 |
| 116 | 219ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 117 | 220ms | Agoramarket | 0.11 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 118 | 220ms | Cursor | 0.5 MB/s | `https://cursor.com` | 通用代理 |
| 119 | 220ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 120 | 221ms | Aiblackboxfc | 0.31 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 121 | 221ms | Ghproxy | 1.55 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 122 | 222ms | Sina | 3.09 MB/s | `https://sina.dev` | 通用代理 |
| 123 | 224ms | Ampcode | 0.21 MB/s | `https://ampcode.com` | 通用代理 |
| 124 | 224ms | Coreos | 1.66 MB/s | `https://coreos.com` | 通用代理 |
| 125 | 224ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 126 | 224ms | Themolt | 0.02 MB/s | `https://themolt.net` | 通用代理 |
| 127 | 229ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 128 | 229ms | Ggg | 2.89 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 129 | 242ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 130 | 245ms | GH-Proxy Org | 0.98 MB/s | `https://gh-proxy.org` | 通用代理 |
| 131 | 245ms | Wings | 0.04 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 132 | 246ms | Agentlimb | 0.18 MB/s | `https://agentlimb.com` | 通用代理 |
| 133 | 251ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 134 | 252ms | Opencovibe | 0.32 MB/s | `https://opencovibe.com` | 通用代理 |
| 135 | 253ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 136 | 255ms | Github | 3.1 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 137 | 255ms | Open | 0.03 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 138 | 256ms | GHFast | 1.25 MB/s | `https://ghfast.top` | 通用代理 |
| 139 | 257ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 140 | 259ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 141 | 263ms | Savannah | 0.02 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 142 | 263ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 143 | 265ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 144 | 265ms | Microcoreos | 0.55 MB/s | `https://microcoreos.com` | 通用代理 |
| 145 | 266ms | Api | 0.23 MB/s | `https://api.solov.cc` | 通用代理 |
| 146 | 266ms | Visionmemorymcp | 0.47 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 147 | 268ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 148 | 271ms | Code | 2.56 MB/s | `https://code.claude.com` | 通用代理 |
| 149 | 273ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 150 | 273ms | Travis-ci | 0.13 MB/s | `https://travis-ci.org` | 通用代理 |
| 151 | 275ms | Aka | 0.22 MB/s | `https://aka.ms` | 通用代理 |
| 152 | 276ms | Gsd | 0.06 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 153 | 277ms | Youtu | 1.15 MB/s | `https://youtu.be` | 通用代理 |
| 154 | 278ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 155 | 283ms | Bananaslides | 0.87 MB/s | `https://bananaslides.online` | 通用代理 |
| 156 | 284ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 157 | 285ms | CrashMC CDN | 1.51 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 158 | 286ms | Gh | 2.7 MB/s | `https://gh.padao.fun` | 通用代理 |
| 159 | 286ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 160 | 288ms | Nisar | 1.64 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 161 | 289ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 162 | 291ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 163 | 294ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 164 | 294ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 165 | 294ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 166 | 296ms | Agenticcorporation | 0.03 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 167 | 298ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 168 | 298ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 169 | 302ms | FastGit CC | 1.68 MB/s | `https://fastgit.cc` | 通用代理 |
| 170 | 304ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 171 | 305ms | Tiktok | 0.12 MB/s | `https://tiktok.com` | 通用代理 |
| 172 | 305ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 173 | 310ms | Kuroutoshikou | 4.57 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 174 | 317ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 175 | 319ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 176 | 320ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 177 | 321ms | Data | 0.02 MB/s | `https://data.openecon.ai` | 通用代理 |
| 178 | 322ms | Turborepo-starter-kit-web | 0.14 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 179 | 323ms | B23 | - | `https://b23.tv` | 通用代理 |
| 180 | 327ms | Steamcommunity | 0.14 MB/s | `https://steamcommunity.com` | 通用代理 |
| 181 | 328ms | 30006000 | 1.86 MB/s | `https://30006000.xyz` | 通用代理 |
| 182 | 330ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 183 | 332ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 184 | 333ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 185 | 336ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 186 | 336ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 187 | 341ms | Autonomi | 0.04 MB/s | `https://autonomi.dev` | 通用代理 |
| 188 | 341ms | Claude | 0.43 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 189 | 344ms | Gpui | 0.2 MB/s | `https://gpui.rs` | 通用代理 |
| 190 | 345ms | Im | 0.76 MB/s | `https://im.codes` | 通用代理 |
| 191 | 347ms | Agent-room | 0.04 MB/s | `https://agent-room.com` | 通用代理 |
| 192 | 349ms | Openttd | 0.06 MB/s | `https://openttd.org` | 通用代理 |
| 193 | 349ms | Store | 2.9 MB/s | `https://store.steampowered.com` | 通用代理 |
| 194 | 355ms | Bailian | 0.24 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 195 | 357ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 196 | 363ms | Sonarcloud | 0.08 MB/s | `https://sonarcloud.io` | 通用代理 |
| 197 | 371ms | Serac | 0.12 MB/s | `https://serac.build` | 通用代理 |
| 198 | 376ms | Oem | 0.01 MB/s | `https://oem.re` | 通用代理 |
| 199 | 381ms | Contrib | 0.31 MB/s | `https://contrib.rocks` | 通用代理 |
| 200 | 382ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 201 | 386ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 202 | 388ms | Ednovas Mirror | 1.61 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 203 | 394ms | V4 | 4.95 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 204 | 395ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 205 | 395ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 206 | 396ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 207 | 397ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 208 | 400ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 209 | 402ms | Getgit | 3.09 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 210 | 406ms | Hk | 1.65 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 211 | 408ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 212 | 412ms | Codeflying | 0.01 MB/s | `https://codeflying.app` | 通用代理 |
| 213 | 416ms | YYLX Git | 0.38 MB/s | `https://git.yylx.win` | 通用代理 |
| 214 | 422ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 215 | 425ms | Msdn | 0.07 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 216 | 428ms | Weaverse | 0.58 MB/s | `https://weaverse.io` | 通用代理 |
| 217 | 432ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 218 | 436ms | Bible-ai-explorer | 0.11 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 219 | 436ms | Tvv | 4.57 MB/s | `https://tvv.tw` | 通用代理 |
| 220 | 438ms | Lecvdemarius | 0.07 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 221 | 441ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 222 | 444ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 223 | 444ms | Your-domain | 0.09 MB/s | `https://your-domain.com` | 通用代理 |
| 224 | 445ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 225 | 445ms | Huly-mcp | 0.21 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 226 | 447ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 227 | 448ms | Safedocx | 0.14 MB/s | `https://safedocx.com` | 通用代理 |
| 228 | 453ms | Aps | 0.18 MB/s | `https://aps.com` | 通用代理 |
| 229 | 455ms | Gh | 3.87 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 230 | 467ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 231 | 471ms | Nyx | 0.06 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 232 | 474ms | Ark | 0.91 MB/s | `https://ark.intel.com` | 通用代理 |
| 233 | 474ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 234 | 482ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 235 | 488ms | Lucky | 0.46 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 236 | 490ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 237 | 493ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 238 | 494ms | Api | - | `https://api.river.ai` | 通用代理 |
| 239 | 499ms | SLink | 0.1 MB/s | `https://slink.ltd` | 通用代理 |
| 240 | 499ms | Wl | - | `https://wl.do` | 通用代理 |
| 241 | 501ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 242 | 508ms | Patchworkos | 0.25 MB/s | `https://patchworkos.com` | 通用代理 |
| 243 | 509ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 244 | 520ms | Impro | 2.05 MB/s | `https://impro.social` | 通用代理 |
| 245 | 522ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 246 | 525ms | 3d-set-visualizer | 0.06 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 247 | 525ms | Aosmd | 0.12 MB/s | `https://aosmd.com` | 通用代理 |
| 248 | 525ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 249 | 528ms | Ygdj7 | 0.05 MB/s | `https://ygdj7.com` | 通用代理 |
| 250 | 532ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 251 | 533ms | Gh | 0.57 MB/s | `https://gh.noki.icu` | 通用代理 |
| 252 | 534ms | Serverkit | 0.05 MB/s | `https://serverkit.ai` | 通用代理 |
| 253 | 539ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 254 | 540ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 255 | 546ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 256 | 556ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 257 | 559ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 258 | 561ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 259 | 564ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 260 | 566ms | You | 0.07 MB/s | `https://you.piccalc.com` | 通用代理 |
| 261 | 567ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 262 | 572ms | Gp | 3.9 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 263 | 573ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 264 | 574ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 265 | 578ms | Clawbiz | 0.06 MB/s | `https://clawbiz.io` | 通用代理 |
| 266 | 592ms | Fastfile | 0.96 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 267 | 595ms | Tracely-studio | 0.05 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 268 | 606ms | Bseindia | - | `https://bseindia.com` | 通用代理 |
| 269 | 611ms | Gh | 4.07 MB/s | `https://gh.1k.ink` | 通用代理 |
| 270 | 631ms | Github | 2.61 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 271 | 637ms | Umami-mcp | 0.32 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 272 | 645ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 273 | 645ms | Tsukuyomi | 0.1 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 274 | 648ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 275 | 649ms | Agentkey | 1.4 MB/s | `https://agentkey.app` | 通用代理 |
| 276 | 656ms | Github | 0.37 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 277 | 666ms | Github | 3.55 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 278 | 674ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 279 | 677ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 280 | 686ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 281 | 690ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 282 | 701ms | Support | 0.14 MB/s | `https://support.apple.com` | 通用代理 |
| 283 | 703ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 284 | 708ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 285 | 717ms | Internhack | 0.08 MB/s | `https://internhack.xyz` | 通用代理 |
| 286 | 717ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 287 | 724ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 288 | 727ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 289 | 732ms | Wordpaper | 0.91 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 290 | 733ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 291 | 737ms | Cumora | 0.41 MB/s | `https://cumora.ai` | 通用代理 |
| 292 | 740ms | Ghproxy | 0.37 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 293 | 755ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 294 | 764ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 295 | 768ms | Code | 0.01 MB/s | `https://code.videolan.org` | 通用代理 |
| 296 | 772ms | Ccgather | 0.07 MB/s | `https://ccgather.com` | 通用代理 |
| 297 | 779ms | Anh | 0.22 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 298 | 785ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 299 | 801ms | Dbgate | 0.13 MB/s | `https://dbgate.org` | 通用代理 |
| 300 | 806ms | Docs | 0.14 MB/s | `https://docs.transifex.com` | 通用代理 |
| 301 | 816ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 302 | 825ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 303 | 837ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 304 | 844ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 305 | 850ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 306 | 851ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 307 | 853ms | Tools | 3.35 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 308 | 853ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 309 | 858ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 310 | 859ms | Invent | 0.01 MB/s | `https://invent.kde.org` | 通用代理 |
| 311 | 868ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 312 | 894ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 313 | 902ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 314 | 902ms | Yibiao | 0.15 MB/s | `https://yibiao.pro` | 通用代理 |
| 315 | 905ms | Web | - | `https://web.4399.com` | 通用代理 |
| 316 | 913ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 317 | 921ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 318 | 926ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 319 | 933ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 320 | 936ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 321 | 965ms | Mimo | 0.21 MB/s | `https://mimo.mi.com` | 通用代理 |
| 322 | 966ms | Cfkua | 3.24 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 323 | 974ms | Ginlix | 0.44 MB/s | `https://ginlix.ai` | 通用代理 |
| 324 | 985ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 325 | 999ms | Github | 3.3 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 326 | 1006ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 327 | 1018ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 328 | 1028ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 329 | 1039ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 330 | 1053ms | Honeymeta | 0.02 MB/s | `https://honeymeta.com` | 通用代理 |
| 331 | 1053ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 332 | 1063ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 333 | 1079ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 334 | 1089ms | Kenyu | 2.7 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 335 | 1108ms | V | - | `https://v.douyin.com` | 通用代理 |
| 336 | 1117ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 337 | 1119ms | Dimagent | 0.15 MB/s | `https://dimagent.com` | 通用代理 |
| 338 | 1154ms | Ghproxy | 0.41 MB/s | `https://ghproxy.cc` | 通用代理 |
| 339 | 1160ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 340 | 1163ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 341 | 1171ms | Github | 3.95 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 342 | 1173ms | GHProxy Net | 0.24 MB/s | `https://ghproxy.net` | 通用代理 |
| 343 | 1178ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 344 | 1183ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 345 | 1189ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 346 | 1195ms | Gh | 0.61 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 347 | 1214ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 348 | 1221ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 349 | 1227ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 350 | 1244ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 351 | 1266ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 352 | 1269ms | Atomcode | 0.08 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 353 | 1287ms | Github | 0.19 MB/s | `https://github.chenc.dev` | 通用代理 |
| 354 | 1307ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 355 | 1319ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 356 | 1342ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 357 | 1367ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 358 | 1376ms | Cf | 0.31 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 359 | 1386ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 360 | 1406ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 361 | 1408ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 362 | 1413ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 363 | 1448ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 364 | 1500ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 365 | 1606ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 366 | 1682ms | Heycall-e | 0.12 MB/s | `https://heycall-e.com` | 通用代理 |
| 367 | 1823ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 368 | 1839ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 369 | 1871ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 370 | 1938ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 371 | 2079ms | Img | - | `https://img.ink` | 通用代理 |
| 372 | 2211ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 373 | 2229ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 374 | 2272ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 375 | 2289ms | Upyun | 0.01 MB/s | `https://upyun.com` | 通用代理 |
| 376 | 2293ms | Wget | 0.19 MB/s | `https://wget.la` | 通用代理 |
| 377 | 2316ms | Gh | 0.58 MB/s | `https://gh.dpik.top` | 通用代理 |
| 378 | 2316ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 379 | 2379ms | G | 0.27 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 380 | 2635ms | Ghproxy | 0.26 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 381 | 2662ms | Tcl | 0.01 MB/s | `https://tcl.tk` | 通用代理 |
| 382 | 2899ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 383 | 3025ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 384 | 3046ms | Git | - | `https://git.net2o.de` | 通用代理 |
| 385 | 3480ms | GHProxy MonkeyRay | 0.09 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 386 | 6285ms | Proxy | 0.04 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（19 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 18 次 |
| Gh (`gh-llkk-cc`) | 2 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Gh (`gh-39-al`) | 1 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Git (`git-tangbai-cc`) | 1 次 |
| Gh (`gh-b52m-cn`) | 5 次 |
| Proxy (`proxy-vvvv-ee`) | 6 次 |
| Nssurge (`nssurge-com`) | 4 次 |
| Fastgpt (`fastgpt-leez-tech`) | 1 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 4 次 |
| Doxygen (`doxygen-org`) | 26 次 |
| Demo (`demo-mcphub-app`) | 1 次 |
| Flashtype (`flashtype-com`) | 1 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 9 次 |
| Maplecode (`maplecode-art`) | 19 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 15 次 |
| Adult (`adult-contents-fc2-com`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 398 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **405** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（52 个）。

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
