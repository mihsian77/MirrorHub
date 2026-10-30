# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-30T04:34:51Z**，每 6 小时刷新一次。当前 ✅ **386** 在线 / ⚠️ **13** 不稳定 / ⚰️ **52** 已失效归档。

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
| 1 | 64ms | Microsoftedge | 0.64 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 69ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 3 | 74ms | Linkedin | 0.23 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 79ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 5 | 83ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 6 | 86ms | App | 0.09 MB/s | `https://app.netlify.com` | 通用代理 |
| 7 | 90ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 8 | 93ms | Githubstatus | 1.13 MB/s | `https://githubstatus.com` | 通用代理 |
| 9 | 95ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 10 | 100ms | Lawyer-yu | 0.08 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 11 | 101ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 12 | 101ms | X | 1.49 MB/s | `https://x.com` | 通用代理 |
| 13 | 102ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 14 | 102ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 15 | 104ms | Deno | 0.91 MB/s | `https://deno.com` | 通用代理 |
| 16 | 106ms | Zebrunner | 1.3 MB/s | `https://zebrunner.com` | 通用代理 |
| 17 | 111ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 18 | 113ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 19 | 115ms | Xjtu-nyxf-study-material | 0.21 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 20 | 122ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 21 | 122ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 22 | 123ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 23 | 123ms | Resume-5lv | 0.22 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 24 | 126ms | Music-cli | 0.19 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 25 | 127ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 26 | 130ms | Discord | 0.06 MB/s | `https://discord.gg` | 通用代理 |
| 27 | 132ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 28 | 134ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 29 | 137ms | Opresume | 0.62 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 30 | 141ms | Img | - | `https://img.shields.io` | 通用代理 |
| 31 | 142ms | Components | 0.09 MB/s | `https://components.dereekb.com` | 通用代理 |
| 32 | 147ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 33 | 149ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 34 | 149ms | Training | 0.15 MB/s | `https://training.ti.com` | 通用代理 |
| 35 | 151ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 36 | 151ms | Impeccable | 1.12 MB/s | `https://impeccable.style` | 通用代理 |
| 37 | 152ms | Osf | 0.04 MB/s | `https://osf.io` | 通用代理 |
| 38 | 153ms | Opensunsama | 0.05 MB/s | `https://opensunsama.com` | 通用代理 |
| 39 | 155ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 40 | 155ms | Kighelper-cloud | 0.1 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 41 | 156ms | Bolt2github | 0.04 MB/s | `https://bolt2github.com` | 通用代理 |
| 42 | 157ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 43 | 157ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 44 | 159ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 45 | 159ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 46 | 163ms | Tms | 0.15 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 47 | 164ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 48 | 164ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 49 | 165ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 50 | 165ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 51 | 166ms | Play | 0.06 MB/s | `https://play.templatical.com` | 通用代理 |
| 52 | 167ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 53 | 167ms | Git | 3.57 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 54 | 168ms | Git | 2.48 MB/s | `https://git.820828.xyz` | 通用代理 |
| 55 | 168ms | Gitea-mirror | 0.79 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 56 | 169ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 57 | 170ms | Ode | - | `https://ode.fun` | 通用代理 |
| 58 | 170ms | Vibesql | 0.14 MB/s | `https://vibesql.org` | 通用代理 |
| 59 | 171ms | Github | 3.25 MB/s | `https://github.788787.xyz` | 通用代理 |
| 60 | 172ms | Dilo-d14 | 0.22 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 61 | 172ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 62 | 175ms | L4d2 | 0.17 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 63 | 176ms | Openpua | 0.76 MB/s | `https://openpua.ai` | 通用代理 |
| 64 | 176ms | Tokei | 0.51 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 65 | 177ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 66 | 177ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 67 | 178ms | Caiji | 0.12 MB/s | `https://caiji.cyou` | 通用代理 |
| 68 | 179ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 69 | 179ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 70 | 180ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 71 | 181ms | Crypto-funding-arbitrage | 0.08 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 72 | 182ms | Ghproxy | 3.55 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 73 | 183ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 74 | 183ms | Github | 2.53 MB/s | `https://github.880824.xyz` | 通用代理 |
| 75 | 185ms | Bestdori | 0.09 MB/s | `https://bestdori.com` | 通用代理 |
| 76 | 185ms | Gh | 2.32 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 77 | 186ms | App | 0.05 MB/s | `https://app.opencastor.com` | 通用代理 |
| 78 | 186ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 79 | 186ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 80 | 187ms | Cognitum | 0.31 MB/s | `https://cognitum.one` | 通用代理 |
| 81 | 187ms | Glass | 0.24 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 82 | 188ms | Ai-trend-publish | 0.01 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 83 | 188ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 84 | 189ms | Clypra | 0.05 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 85 | 191ms | Cody | 0.25 MB/s | `https://cody.todyle.com` | 通用代理 |
| 86 | 192ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 87 | 193ms | Axios-http | 0.28 MB/s | `https://axios-http.com` | 通用代理 |
| 88 | 193ms | GH-Proxy | 1.19 MB/s | `https://gh-proxy.com` | 通用代理 |
| 89 | 194ms | Thumb | 1.11 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 90 | 195ms | Cbrowser | 2.44 MB/s | `https://cbrowser.ai` | 通用代理 |
| 91 | 195ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 92 | 195ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 93 | 199ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 94 | 200ms | GH Monlor | 1.33 MB/s | `https://gh.monlor.com` | 通用代理 |
| 95 | 202ms | Clayrune | 0.16 MB/s | `https://clayrune.io` | 通用代理 |
| 96 | 202ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 97 | 202ms | Twitter | 0.93 MB/s | `https://twitter.com` | 通用代理 |
| 98 | 203ms | Github | 2.89 MB/s | `https://github.ihnic.com` | 通用代理 |
| 99 | 204ms | Miaozitie | 0.11 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 100 | 206ms | Alas | 0.88 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 101 | 207ms | Codeeraser | 0.16 MB/s | `https://codeeraser.dev` | 通用代理 |
| 102 | 207ms | Hopp | 0.04 MB/s | `https://hopp.sh` | 通用代理 |
| 103 | 210ms | Aiblackboxfc | 0.35 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 104 | 210ms | Gh | 1.68 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 105 | 210ms | Ghproxy | 2.54 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 106 | 211ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 107 | 211ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 108 | 212ms | Pidash | 0.04 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 109 | 212ms | Polgarand | 0.09 MB/s | `https://polgarand.org` | 通用代理 |
| 110 | 212ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 111 | 215ms | Coffeecli | 0.15 MB/s | `https://coffeecli.com` | 通用代理 |
| 112 | 215ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 113 | 216ms | Ampcode | 0.17 MB/s | `https://ampcode.com` | 通用代理 |
| 114 | 218ms | Coreos | 1.73 MB/s | `https://coreos.com` | 通用代理 |
| 115 | 220ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 116 | 221ms | Agoramarket | 0.04 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 117 | 221ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 118 | 222ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 119 | 223ms | Cursor | 0.56 MB/s | `https://cursor.com` | 通用代理 |
| 120 | 224ms | Demo | 0.05 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 121 | 226ms | Sina | 0.68 MB/s | `https://sina.dev` | 通用代理 |
| 122 | 229ms | Cherryai | 0.07 MB/s | `https://cherryai.com` | 通用代理 |
| 123 | 230ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 124 | 231ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 125 | 233ms | Kuroutoshikou | 0.09 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 126 | 235ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 127 | 237ms | Ghproxy | 0.76 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 128 | 242ms | Sub | 0.13 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 129 | 243ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 130 | 243ms | Gsd | 0.23 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 131 | 243ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 132 | 248ms | Agentlimb | 0.27 MB/s | `https://agentlimb.com` | 通用代理 |
| 133 | 250ms | GH-Proxy Org | 1.22 MB/s | `https://gh-proxy.org` | 通用代理 |
| 134 | 250ms | Opencovibe | 0.42 MB/s | `https://opencovibe.com` | 通用代理 |
| 135 | 250ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 136 | 252ms | Github | 0.62 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 137 | 253ms | Ggg | 2.59 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 138 | 253ms | Savannah | 0.03 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 139 | 254ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 140 | 259ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 141 | 259ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 142 | 262ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 143 | 265ms | Microcoreos | 0.5 MB/s | `https://microcoreos.com` | 通用代理 |
| 144 | 269ms | Travis-ci | 0.18 MB/s | `https://travis-ci.org` | 通用代理 |
| 145 | 269ms | Visionmemorymcp | 0.24 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 146 | 270ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 147 | 273ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 148 | 274ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 149 | 275ms | Code | 1.04 MB/s | `https://code.claude.com` | 通用代理 |
| 150 | 278ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 151 | 279ms | Aka | 0.38 MB/s | `https://aka.ms` | 通用代理 |
| 152 | 279ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 153 | 280ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 154 | 280ms | Youtu | 1.29 MB/s | `https://youtu.be` | 通用代理 |
| 155 | 289ms | Bananaslides | 0.67 MB/s | `https://bananaslides.online` | 通用代理 |
| 156 | 290ms | CrashMC CDN | 1.33 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 157 | 291ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 158 | 295ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 159 | 295ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 160 | 296ms | Api | 0.08 MB/s | `https://api.solov.cc` | 通用代理 |
| 161 | 297ms | Nisar | 0.81 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 162 | 298ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 163 | 300ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 164 | 300ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 165 | 301ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 166 | 307ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 167 | 308ms | Gh | 0.6 MB/s | `https://gh.padao.fun` | 通用代理 |
| 168 | 308ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 169 | 309ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 170 | 309ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 171 | 313ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 172 | 316ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 173 | 317ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 174 | 317ms | Tiktok | 0.08 MB/s | `https://tiktok.com` | 通用代理 |
| 175 | 318ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 176 | 319ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 177 | 323ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 178 | 323ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 179 | 327ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 180 | 327ms | FastGit CC | 1.2 MB/s | `https://fastgit.cc` | 通用代理 |
| 181 | 328ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 182 | 331ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 183 | 336ms | Steamcommunity | 0.13 MB/s | `https://steamcommunity.com` | 通用代理 |
| 184 | 339ms | 30006000 | 0.75 MB/s | `https://30006000.xyz` | 通用代理 |
| 185 | 339ms | B23 | - | `https://b23.tv` | 通用代理 |
| 186 | 339ms | Claude | 0.39 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 187 | 340ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 188 | 342ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 189 | 347ms | Gpui | 0.23 MB/s | `https://gpui.rs` | 通用代理 |
| 190 | 348ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 191 | 348ms | Sonarcloud | 0.12 MB/s | `https://sonarcloud.io` | 通用代理 |
| 192 | 350ms | Openttd | 0.04 MB/s | `https://openttd.org` | 通用代理 |
| 193 | 360ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 194 | 365ms | Bailian | 0.08 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 195 | 366ms | Store | 1.03 MB/s | `https://store.steampowered.com` | 通用代理 |
| 196 | 368ms | Contrib | 0.52 MB/s | `https://contrib.rocks` | 通用代理 |
| 197 | 368ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 198 | 374ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 199 | 375ms | Serac | 0.07 MB/s | `https://serac.build` | 通用代理 |
| 200 | 376ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 201 | 379ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 202 | 381ms | Im | 1.45 MB/s | `https://im.codes` | 通用代理 |
| 203 | 382ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 204 | 389ms | Api | 0.04 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 205 | 394ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 206 | 396ms | Weaverse | 0.72 MB/s | `https://weaverse.io` | 通用代理 |
| 207 | 397ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 208 | 398ms | GHFast | 0.5 MB/s | `https://ghfast.top` | 通用代理 |
| 209 | 400ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 210 | 400ms | Oem | 0.04 MB/s | `https://oem.re` | 通用代理 |
| 211 | 403ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 212 | 416ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 213 | 420ms | Getgit | 2.96 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 214 | 422ms | V4 | 2.68 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 215 | 424ms | Hk | 0.78 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 216 | 425ms | Ednovas Mirror | 0.58 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 217 | 427ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 218 | 428ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 219 | 433ms | YYLX Git | 0.33 MB/s | `https://git.yylx.win` | 通用代理 |
| 220 | 435ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 221 | 436ms | You | 0.5 MB/s | `https://you.piccalc.com` | 通用代理 |
| 222 | 446ms | Ark | 0.7 MB/s | `https://ark.intel.com` | 通用代理 |
| 223 | 446ms | Lecvdemarius | 0.06 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 224 | 446ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 225 | 447ms | Tvv | 2.36 MB/s | `https://tvv.tw` | 通用代理 |
| 226 | 448ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 227 | 449ms | Huly-mcp | 0.21 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 228 | 454ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 229 | 457ms | Your-domain | 0.04 MB/s | `https://your-domain.com` | 通用代理 |
| 230 | 458ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 231 | 462ms | Gh | 3.42 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 232 | 463ms | Bible-ai-explorer | 0.05 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 233 | 463ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 234 | 463ms | Nyx | 0.04 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 235 | 464ms | Aps | 0.04 MB/s | `https://aps.com` | 通用代理 |
| 236 | 466ms | Safedocx | 0.11 MB/s | `https://safedocx.com` | 通用代理 |
| 237 | 481ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 238 | 488ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 239 | 490ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 240 | 491ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 241 | 496ms | Patchworkos | 0.32 MB/s | `https://patchworkos.com` | 通用代理 |
| 242 | 498ms | Lucky | 0.51 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 243 | 499ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 244 | 504ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 245 | 505ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 246 | 508ms | Wl | - | `https://wl.do` | 通用代理 |
| 247 | 510ms | Gh | 0.87 MB/s | `https://gh.noki.icu` | 通用代理 |
| 248 | 511ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 249 | 513ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 250 | 515ms | Aosmd | 0.18 MB/s | `https://aosmd.com` | 通用代理 |
| 251 | 523ms | Gh | 2.91 MB/s | `https://gh.idayer.com` | 通用代理 |
| 252 | 523ms | Impro | 1.8 MB/s | `https://impro.social` | 通用代理 |
| 253 | 541ms | Ygdj7 | 0.01 MB/s | `https://ygdj7.com` | 通用代理 |
| 254 | 548ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 255 | 552ms | Serverkit | 0.04 MB/s | `https://serverkit.ai` | 通用代理 |
| 256 | 554ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 257 | 556ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 258 | 560ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 259 | 565ms | Fastfile | 1.58 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 260 | 567ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 261 | 568ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 262 | 568ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 263 | 568ms | Tsukuyomi | 0.16 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 264 | 570ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 265 | 572ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 266 | 574ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 267 | 575ms | Gp | 3.21 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 268 | 578ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 269 | 602ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 270 | 615ms | Umami-mcp | 0.75 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 271 | 626ms | Gh | 3.15 MB/s | `https://gh.1k.ink` | 通用代理 |
| 272 | 634ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 273 | 643ms | Github | 3.29 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 274 | 658ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 275 | 660ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 276 | 664ms | Github | 2.65 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 277 | 675ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 278 | 675ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 279 | 679ms | Github | 0.41 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 280 | 680ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 281 | 685ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 282 | 686ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 283 | 693ms | Support | 0.35 MB/s | `https://support.apple.com` | 通用代理 |
| 284 | 694ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 285 | 694ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 286 | 703ms | Agentkey | 0.96 MB/s | `https://agentkey.app` | 通用代理 |
| 287 | 703ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 288 | 707ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 289 | 708ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 290 | 730ms | Wordpaper | 0.73 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 291 | 735ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 292 | 744ms | Os | 0.05 MB/s | `https://os.ryo.lu` | 通用代理 |
| 293 | 750ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 294 | 757ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 295 | 760ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 296 | 766ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 297 | 769ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 298 | 780ms | Anh | 0.27 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 299 | 790ms | Docs | 0.19 MB/s | `https://docs.transifex.com` | 通用代理 |
| 300 | 807ms | Ccgather | 0.04 MB/s | `https://ccgather.com` | 通用代理 |
| 301 | 808ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 302 | 815ms | Dbgate | 0.16 MB/s | `https://dbgate.org` | 通用代理 |
| 303 | 828ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 304 | 833ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 305 | 843ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 306 | 855ms | Tools | 1.96 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 307 | 856ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 308 | 859ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 309 | 867ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 310 | 870ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 311 | 872ms | Cumora | 0.32 MB/s | `https://cumora.ai` | 通用代理 |
| 312 | 878ms | GHFile Geekertao | 1.55 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 313 | 881ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 314 | 895ms | Git | 0.23 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 315 | 905ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 316 | 917ms | Yibiao | 0.14 MB/s | `https://yibiao.pro` | 通用代理 |
| 317 | 926ms | Task | 0.02 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 318 | 933ms | Web | - | `https://web.4399.com` | 通用代理 |
| 319 | 942ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 320 | 942ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 321 | 944ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 322 | 960ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 323 | 961ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 324 | 970ms | Ginlix | 0.58 MB/s | `https://ginlix.ai` | 通用代理 |
| 325 | 975ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 326 | 982ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 327 | 984ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 328 | 989ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 329 | 1002ms | Github | 1.43 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 330 | 1027ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 331 | 1075ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 332 | 1083ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 333 | 1088ms | Kenyu | 2.65 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 334 | 1092ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 335 | 1101ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 336 | 1107ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 337 | 1119ms | Cfkua | 1.79 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 338 | 1121ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 339 | 1122ms | Dimagent | 0.33 MB/s | `https://dimagent.com` | 通用代理 |
| 340 | 1127ms | V | - | `https://v.douyin.com` | 通用代理 |
| 341 | 1172ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 342 | 1177ms | Github | 2.41 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 343 | 1184ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 344 | 1185ms | Ghproxy | 0.26 MB/s | `https://ghproxy.cc` | 通用代理 |
| 345 | 1203ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 346 | 1227ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 347 | 1243ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 348 | 1244ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 349 | 1245ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 350 | 1253ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 351 | 1276ms | Atomcode | 0.09 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 352 | 1306ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 353 | 1307ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 354 | 1326ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 355 | 1331ms | Github | 0.16 MB/s | `https://github.chenc.dev` | 通用代理 |
| 356 | 1373ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 357 | 1399ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 358 | 1402ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 359 | 1416ms | Cf | 0.29 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 360 | 1425ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 361 | 1429ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 362 | 1430ms | Gh | 0.58 MB/s | `https://gh.39.al` | 通用代理 |
| 363 | 1442ms | Gh | 0.89 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 364 | 1447ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 365 | 1545ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 366 | 1617ms | Gh | 0.68 MB/s | `https://gh.dpik.top` | 通用代理 |
| 367 | 1650ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 368 | 1661ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 369 | 1694ms | Heycall-e | 0.12 MB/s | `https://heycall-e.com` | 通用代理 |
| 370 | 1747ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 371 | 1806ms | Git | 0.3 MB/s | `https://git.669966.xyz` | 通用代理 |
| 372 | 1818ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 373 | 1860ms | G | 0.07 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 374 | 1935ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 375 | 2073ms | Img | - | `https://img.ink` | 通用代理 |
| 376 | 2153ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 377 | 2156ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 378 | 2169ms | Provider | - | `https://provider.com` | 通用代理 |
| 379 | 2351ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 380 | 2396ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 381 | 2465ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 382 | 2727ms | Ghproxy | 0.05 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 383 | 2767ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 384 | 3049ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 385 | 3180ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 386 | 3528ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（13 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHProxy Net (`ghproxy-net`) | 1 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 16 次 |
| Proxy (`proxy-yaoyaoling-net`) | 1 次 |
| Gh (`gh-b52m-cn`) | 3 次 |
| Proxy (`proxy-vvvv-ee`) | 4 次 |
| Nssurge (`nssurge-com`) | 2 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 2 次 |
| Doxygen (`doxygen-org`) | 24 次 |
| Flashtype (`flashtype-com`) | 1 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 7 次 |
| Maplecode (`maplecode-art`) | 17 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 13 次 |
| Adult (`adult-contents-fc2-com`) | 3 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 392 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **399** | |

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
