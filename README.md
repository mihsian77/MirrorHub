# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-31T11:48:03Z**，每 6 小时刷新一次。当前 ✅ **390** 在线 / ⚠️ **17** 不稳定 / ⚰️ **53** 已失效归档。

## 核心特性

- **407 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 73ms | Microsoftedge | 0.2 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 78ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 3 | 81ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 4 | 82ms | Githubstatus | 2.45 MB/s | `https://githubstatus.com` | 通用代理 |
| 5 | 84ms | Linkedin | 0.14 MB/s | `https://linkedin.com` | 通用代理 |
| 6 | 84ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 7 | 92ms | Megacrit | 0.37 MB/s | `https://megacrit.com` | 通用代理 |
| 8 | 94ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 9 | 95ms | Godocs | 0.06 MB/s | `https://godocs.io` | 通用代理 |
| 10 | 95ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 11 | 95ms | X | 1.29 MB/s | `https://x.com` | 通用代理 |
| 12 | 97ms | Zebrunner | 2.14 MB/s | `https://zebrunner.com` | 通用代理 |
| 13 | 98ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 14 | 99ms | Openchamber | 0.85 MB/s | `https://openchamber.dev` | 通用代理 |
| 15 | 99ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 16 | 99ms | Xjtu-nyxf-study-material | 0.21 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 17 | 100ms | App | 0.06 MB/s | `https://app.netlify.com` | 通用代理 |
| 18 | 101ms | Resume-5lv | 0.21 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 19 | 110ms | Lawyer-yu | 0.07 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 20 | 111ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 21 | 112ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 22 | 113ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 23 | 113ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 24 | 117ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 25 | 119ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 26 | 121ms | Opresume | 0.73 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 27 | 122ms | Deno | 0.2 MB/s | `https://deno.com` | 通用代理 |
| 28 | 122ms | Impeccable | 1.15 MB/s | `https://impeccable.style` | 通用代理 |
| 29 | 126ms | App | 0.02 MB/s | `https://app.codecov.io` | 通用代理 |
| 30 | 132ms | Components | 0.09 MB/s | `https://components.dereekb.com` | 通用代理 |
| 31 | 136ms | Opentakeoff | 0.03 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 32 | 136ms | Training | 0.39 MB/s | `https://training.ti.com` | 通用代理 |
| 33 | 137ms | Music-cli | 0.16 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 34 | 142ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 35 | 143ms | Discord | 0.07 MB/s | `https://discord.gg` | 通用代理 |
| 36 | 144ms | Opensunsama | 0.08 MB/s | `https://opensunsama.com` | 通用代理 |
| 37 | 145ms | Kighelper-cloud | 0.11 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 38 | 146ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 39 | 147ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 40 | 147ms | Git | 3.05 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 41 | 148ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 42 | 152ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 43 | 153ms | Img | - | `https://img.shields.io` | 通用代理 |
| 44 | 154ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 45 | 156ms | Ghproxy | 3.16 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 46 | 156ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 47 | 157ms | Git | 2.51 MB/s | `https://git.820828.xyz` | 通用代理 |
| 48 | 159ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 49 | 161ms | Play | 0.05 MB/s | `https://play.templatical.com` | 通用代理 |
| 50 | 163ms | Gitea-mirror | 1.04 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 51 | 164ms | Gh | 2.7 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 52 | 164ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 53 | 165ms | Crypto-funding-arbitrage | 0.1 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 54 | 166ms | Github | 2.84 MB/s | `https://github.788787.xyz` | 通用代理 |
| 55 | 166ms | Vibesql | 0.17 MB/s | `https://vibesql.org` | 通用代理 |
| 56 | 167ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 57 | 168ms | Caiji | - | `https://caiji.cyou` | 通用代理 |
| 58 | 168ms | Caw | 0.07 MB/s | `https://caw.rocks` | 通用代理 |
| 59 | 168ms | Glass | 0.29 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 60 | 169ms | Cody | 0.29 MB/s | `https://cody.todyle.com` | 通用代理 |
| 61 | 169ms | Openpua | 0.61 MB/s | `https://openpua.ai` | 通用代理 |
| 62 | 170ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 63 | 170ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 64 | 171ms | Codeeraser | 0.14 MB/s | `https://codeeraser.dev` | 通用代理 |
| 65 | 173ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 66 | 173ms | Dilo-d14 | 0.22 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 67 | 174ms | GH-Proxy | 1.34 MB/s | `https://gh-proxy.com` | 通用代理 |
| 68 | 175ms | Github | 2.66 MB/s | `https://github.880824.xyz` | 通用代理 |
| 69 | 175ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 70 | 176ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 71 | 176ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 72 | 176ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 73 | 176ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 74 | 177ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 75 | 178ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 76 | 178ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 77 | 178ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 78 | 178ms | Freeport | 0.05 MB/s | `https://freeport.network` | 通用代理 |
| 79 | 179ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 80 | 179ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 81 | 179ms | L4d2 | 0.16 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 82 | 179ms | Tokei | 0.65 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 83 | 184ms | Bestdori | 0.13 MB/s | `https://bestdori.com` | 通用代理 |
| 84 | 184ms | Clayrune | 0.21 MB/s | `https://clayrune.io` | 通用代理 |
| 85 | 184ms | GH Monlor | 1.17 MB/s | `https://gh.monlor.com` | 通用代理 |
| 86 | 185ms | Polgarand | 0.11 MB/s | `https://polgarand.org` | 通用代理 |
| 87 | 185ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 88 | 186ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 89 | 186ms | Ode | - | `https://ode.fun` | 通用代理 |
| 90 | 186ms | Twitter | 0.8 MB/s | `https://twitter.com` | 通用代理 |
| 91 | 187ms | Clypra | 0.03 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 92 | 188ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 93 | 188ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 94 | 192ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 95 | 193ms | Alas | 1.02 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 96 | 193ms | Miaozitie | 0.11 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 97 | 193ms | Tms | 0.09 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 98 | 194ms | Axios-http | 0.24 MB/s | `https://axios-http.com` | 通用代理 |
| 99 | 195ms | Github | 2.71 MB/s | `https://github.ihnic.com` | 通用代理 |
| 100 | 195ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 101 | 197ms | Ghproxy | 2.75 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 102 | 198ms | Pidash | 0.04 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 103 | 198ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 104 | 198ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 105 | 199ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 106 | 200ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 107 | 201ms | Aiblackboxfc | 0.35 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 108 | 202ms | Coffeecli | 0.14 MB/s | `https://coffeecli.com` | 通用代理 |
| 109 | 203ms | Sina | 1.97 MB/s | `https://sina.dev` | 通用代理 |
| 110 | 204ms | Cherryai | 0.07 MB/s | `https://cherryai.com` | 通用代理 |
| 111 | 204ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 112 | 205ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 113 | 205ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 114 | 209ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 115 | 209ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 116 | 213ms | Agoramarket | 0.11 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 117 | 213ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 118 | 214ms | Ampcode | 0.28 MB/s | `https://ampcode.com` | 通用代理 |
| 119 | 215ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 120 | 215ms | Cognitum | 0.17 MB/s | `https://cognitum.one` | 通用代理 |
| 121 | 217ms | Ggg | 3.17 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 122 | 219ms | Coreos | 1.89 MB/s | `https://coreos.com` | 通用代理 |
| 123 | 223ms | Agentlimb | 0.29 MB/s | `https://agentlimb.com` | 通用代理 |
| 124 | 223ms | Cbrowser | 0.9 MB/s | `https://cbrowser.ai` | 通用代理 |
| 125 | 224ms | GH-Proxy Org | 0.94 MB/s | `https://gh-proxy.org` | 通用代理 |
| 126 | 224ms | Ghproxy | 2.23 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 127 | 233ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 128 | 233ms | Thumb | 1.0 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 129 | 234ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 130 | 235ms | Docs | 0.09 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 131 | 235ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 132 | 240ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 133 | 242ms | Themolt | 0.02 MB/s | `https://themolt.net` | 通用代理 |
| 134 | 244ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 135 | 245ms | Github | 1.37 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 136 | 245ms | Opencovibe | 0.51 MB/s | `https://opencovibe.com` | 通用代理 |
| 137 | 246ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 138 | 246ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 139 | 249ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 140 | 249ms | Microcoreos | 0.43 MB/s | `https://microcoreos.com` | 通用代理 |
| 141 | 257ms | CrashMC CDN | 0.88 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 142 | 257ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 143 | 258ms | Api | 0.27 MB/s | `https://api.solov.cc` | 通用代理 |
| 144 | 258ms | Cursor | 0.29 MB/s | `https://cursor.com` | 通用代理 |
| 145 | 258ms | Visionmemorymcp | 0.16 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 146 | 260ms | Youtu | 1.37 MB/s | `https://youtu.be` | 通用代理 |
| 147 | 265ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 148 | 267ms | Kuroutoshikou | 0.99 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 149 | 268ms | Code | 1.55 MB/s | `https://code.claude.com` | 通用代理 |
| 150 | 269ms | Open | 0.03 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 151 | 271ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 152 | 274ms | Aka | 0.77 MB/s | `https://aka.ms` | 通用代理 |
| 153 | 274ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 154 | 275ms | Bananaslides | 1.14 MB/s | `https://bananaslides.online` | 通用代理 |
| 155 | 275ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 156 | 275ms | Savannah | 0.02 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 157 | 279ms | Gh | 1.47 MB/s | `https://gh.padao.fun` | 通用代理 |
| 158 | 283ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 159 | 284ms | Travis-ci | 0.13 MB/s | `https://travis-ci.org` | 通用代理 |
| 160 | 287ms | Nisar | 1.68 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 161 | 289ms | FastGit CC | 3.13 MB/s | `https://fastgit.cc` | 通用代理 |
| 162 | 289ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 163 | 290ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 164 | 293ms | Gsd | 0.13 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 165 | 295ms | Phabricator | 0.03 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 166 | 296ms | Agenticcorporation | 0.03 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 167 | 296ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 168 | 298ms | Tiktok | 0.11 MB/s | `https://tiktok.com` | 通用代理 |
| 169 | 299ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 170 | 300ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 171 | 301ms | Openttd | 0.07 MB/s | `https://openttd.org` | 通用代理 |
| 172 | 306ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 173 | 310ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 174 | 310ms | Steamcommunity | 0.14 MB/s | `https://steamcommunity.com` | 通用代理 |
| 175 | 312ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 176 | 316ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 177 | 317ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 178 | 318ms | B23 | - | `https://b23.tv` | 通用代理 |
| 179 | 318ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 180 | 323ms | 30006000 | 1.27 MB/s | `https://30006000.xyz` | 通用代理 |
| 181 | 324ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 182 | 324ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 183 | 327ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 184 | 328ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 185 | 330ms | Store | 1.25 MB/s | `https://store.steampowered.com` | 通用代理 |
| 186 | 331ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 187 | 332ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 188 | 333ms | Claude | 0.36 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 189 | 333ms | Turborepo-starter-kit-web | 0.07 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 190 | 338ms | Getgit | 3.05 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 191 | 345ms | Gpui | 0.29 MB/s | `https://gpui.rs` | 通用代理 |
| 192 | 353ms | Ednovas Mirror | 1.4 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 193 | 355ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 194 | 356ms | Im | 1.05 MB/s | `https://im.codes` | 通用代理 |
| 195 | 356ms | Sonarcloud | 0.1 MB/s | `https://sonarcloud.io` | 通用代理 |
| 196 | 357ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 197 | 364ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 198 | 364ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 199 | 365ms | Serac | 0.11 MB/s | `https://serac.build` | 通用代理 |
| 200 | 366ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 201 | 370ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 202 | 372ms | Hk | 1.6 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 203 | 376ms | Contrib | 0.26 MB/s | `https://contrib.rocks` | 通用代理 |
| 204 | 381ms | Oem | 0.04 MB/s | `https://oem.re` | 通用代理 |
| 205 | 382ms | V4 | 2.7 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 206 | 388ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 207 | 393ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 208 | 406ms | Bailian | 0.1 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 209 | 408ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 210 | 409ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 211 | 412ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 212 | 412ms | Msdn | 0.05 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 213 | 412ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 214 | 416ms | Codeflying | 0.01 MB/s | `https://codeflying.app` | 通用代理 |
| 215 | 420ms | Tvv | 3.21 MB/s | `https://tvv.tw` | 通用代理 |
| 216 | 420ms | Weaverse | 0.64 MB/s | `https://weaverse.io` | 通用代理 |
| 217 | 421ms | Aps | 0.05 MB/s | `https://aps.com` | 通用代理 |
| 218 | 421ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 219 | 422ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 220 | 424ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 221 | 424ms | Huly-mcp | 0.21 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 222 | 431ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 223 | 432ms | Bible-ai-explorer | 0.08 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 224 | 437ms | YYLX Git | 0.77 MB/s | `https://git.yylx.win` | 通用代理 |
| 225 | 438ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 226 | 440ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 227 | 446ms | GH Nxnow | 0.56 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 228 | 447ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 229 | 447ms | Your-domain | 0.09 MB/s | `https://your-domain.com` | 通用代理 |
| 230 | 451ms | Gh | 2.77 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 231 | 462ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 232 | 468ms | Safedocx | 0.11 MB/s | `https://safedocx.com` | 通用代理 |
| 233 | 471ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 234 | 473ms | Lucky | 0.51 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 235 | 474ms | Lecvdemarius | 0.06 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 236 | 475ms | Ark | 1.26 MB/s | `https://ark.intel.com` | 通用代理 |
| 237 | 487ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 238 | 488ms | Wl | - | `https://wl.do` | 通用代理 |
| 239 | 489ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 240 | 489ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 241 | 493ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 242 | 496ms | Proxy | 3.13 MB/s | `https://proxy.vvvv.ee` | 通用代理 |
| 243 | 496ms | SLink | 0.06 MB/s | `https://slink.ltd` | 通用代理 |
| 244 | 497ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 245 | 499ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 246 | 500ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 247 | 518ms | Patchworkos | 0.27 MB/s | `https://patchworkos.com` | 通用代理 |
| 248 | 519ms | Serverkit | 0.05 MB/s | `https://serverkit.ai` | 通用代理 |
| 249 | 520ms | Impro | 2.35 MB/s | `https://impro.social` | 通用代理 |
| 250 | 531ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 251 | 533ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 252 | 534ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 253 | 543ms | Api | - | `https://api.river.ai` | 通用代理 |
| 254 | 547ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 255 | 551ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 256 | 559ms | Aosmd | 0.12 MB/s | `https://aosmd.com` | 通用代理 |
| 257 | 563ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 258 | 564ms | Easyboardgame | 0.02 MB/s | `https://easyboardgame.top` | 通用代理 |
| 259 | 566ms | Gp | 2.73 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 260 | 566ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 261 | 568ms | Gh | 0.48 MB/s | `https://gh.noki.icu` | 通用代理 |
| 262 | 569ms | You | 0.94 MB/s | `https://you.piccalc.com` | 通用代理 |
| 263 | 577ms | Tracely-studio | 0.04 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 264 | 594ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 265 | 596ms | Agentkey | 1.47 MB/s | `https://agentkey.app` | 通用代理 |
| 266 | 598ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 267 | 601ms | Fastfile | 1.89 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 268 | 601ms | Memstack | 0.01 MB/s | `https://memstack.pro` | 通用代理 |
| 269 | 608ms | Gh | 3.09 MB/s | `https://gh.1k.ink` | 通用代理 |
| 270 | 609ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 271 | 625ms | Github | 2.9 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 272 | 635ms | Github | 0.39 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 273 | 638ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 274 | 642ms | Tsukuyomi | 0.11 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 275 | 644ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 276 | 645ms | Github | 3.35 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 277 | 651ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 278 | 659ms | Bseindia | 0.01 MB/s | `https://bseindia.com` | 通用代理 |
| 279 | 664ms | Umami-mcp | 0.64 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 280 | 675ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 281 | 678ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 282 | 679ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 283 | 683ms | Os | 0.09 MB/s | `https://os.ryo.lu` | 通用代理 |
| 284 | 688ms | Support | 0.11 MB/s | `https://support.apple.com` | 通用代理 |
| 285 | 693ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 286 | 696ms | Ghproxy | 0.34 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 287 | 705ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 288 | 708ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 289 | 708ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 290 | 719ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 291 | 720ms | Wordpaper | 0.71 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 292 | 734ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 293 | 734ms | Cumora | 0.44 MB/s | `https://cumora.ai` | 通用代理 |
| 294 | 736ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 295 | 742ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 296 | 754ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 297 | 764ms | Anh | 0.28 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 298 | 766ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 299 | 787ms | Internhack | 0.04 MB/s | `https://internhack.xyz` | 通用代理 |
| 300 | 800ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 301 | 801ms | Aif | 0.05 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 302 | 806ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 303 | 825ms | Dbgate | 0.13 MB/s | `https://dbgate.org` | 通用代理 |
| 304 | 825ms | Docs | 0.15 MB/s | `https://docs.transifex.com` | 通用代理 |
| 305 | 828ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 306 | 831ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 307 | 840ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 308 | 843ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 309 | 848ms | Tools | 2.29 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 310 | 860ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 311 | 867ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 312 | 868ms | Code | 0.01 MB/s | `https://code.videolan.org` | 通用代理 |
| 313 | 874ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 314 | 876ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 315 | 886ms | Cfkua | 2.09 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 316 | 896ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 317 | 904ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 318 | 904ms | Yibiao | 0.14 MB/s | `https://yibiao.pro` | 通用代理 |
| 319 | 920ms | Task | 0.02 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 320 | 930ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 321 | 940ms | Mimo | 0.19 MB/s | `https://mimo.mi.com` | 通用代理 |
| 322 | 953ms | Github | 3.16 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 323 | 955ms | GHFile Geekertao | 0.42 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 324 | 957ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 325 | 958ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 326 | 973ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 327 | 980ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 328 | 985ms | Ginlix | 0.56 MB/s | `https://ginlix.ai` | 通用代理 |
| 329 | 1007ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 330 | 1026ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 331 | 1035ms | Web | - | `https://web.4399.com` | 通用代理 |
| 332 | 1044ms | Gh | 0.56 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 333 | 1052ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 334 | 1060ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 335 | 1061ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 336 | 1065ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 337 | 1076ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 338 | 1087ms | Kenyu | 2.73 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 339 | 1123ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 340 | 1134ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 341 | 1141ms | Dimagent | 0.28 MB/s | `https://dimagent.com` | 通用代理 |
| 342 | 1147ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 343 | 1165ms | Github | 3.16 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 344 | 1170ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 345 | 1178ms | Hevolve | 0.09 MB/s | `https://hevolve.ai` | 通用代理 |
| 346 | 1183ms | V | 0.06 MB/s | `https://v.douyin.com` | 通用代理 |
| 347 | 1189ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 348 | 1194ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 349 | 1202ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 350 | 1215ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 351 | 1217ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 352 | 1223ms | Github | 0.18 MB/s | `https://github.chenc.dev` | 通用代理 |
| 353 | 1248ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 354 | 1270ms | Atomcode | 0.07 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 355 | 1290ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 356 | 1291ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 357 | 1311ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 358 | 1330ms | Gh | 0.39 MB/s | `https://gh.39.al` | 通用代理 |
| 359 | 1387ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 360 | 1407ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 361 | 1409ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 362 | 1422ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 363 | 1425ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 364 | 1456ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 365 | 1520ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 366 | 1544ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 367 | 1621ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 368 | 1673ms | Heycall-e | 0.12 MB/s | `https://heycall-e.com` | 通用代理 |
| 369 | 1762ms | Free | 0.72 MB/s | `https://free.cn.eu.org` | 通用代理 |
| 370 | 1784ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 371 | 1790ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 372 | 1824ms | Git | 0.14 MB/s | `https://git.669966.xyz` | 通用代理 |
| 373 | 1932ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 374 | 1985ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 375 | 2026ms | G | 0.02 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 376 | 2054ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 377 | 2110ms | Wget | 0.15 MB/s | `https://wget.la` | 通用代理 |
| 378 | 2119ms | Img | - | `https://img.ink` | 通用代理 |
| 379 | 2168ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 380 | 2207ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 381 | 2275ms | Gh | 0.71 MB/s | `https://gh.dpik.top` | 通用代理 |
| 382 | 2369ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 383 | 2402ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 384 | 2614ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 385 | 2755ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 386 | 3003ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 387 | 3041ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 388 | 3169ms | Ghproxy | 0.03 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 389 | 3554ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 390 | 3820ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |


### ⚠️ 不稳定节点（17 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFast (`ghfast-top`) | 1 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 20 次 |
| Gh (`gh-llkk-cc`) | 4 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Cf (`cf-ghproxy-cc`) | 1 次 |
| Ghproxy (`ghproxy-cc`) | 1 次 |
| Git (`git-tangbai-cc`) | 3 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Gh (`gh-b52m-cn`) | 7 次 |
| Sub (`sub-ikar-eu-org`) | 2 次 |
| Nssurge (`nssurge-com`) | 6 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 6 次 |
| Flashtype (`flashtype-com`) | 1 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 11 次 |
| Maplecode (`maplecode-art`) | 21 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 17 次 |
| Adult (`adult-contents-fc2-com`) | 3 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 400 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **407** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（53 个）。

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
