# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-27T21:54:41Z**，每 6 小时刷新一次。当前 ✅ **383** 在线 / ⚠️ **12** 不稳定 / ⚰️ **51** 已失效归档。

## 核心特性

- **395 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 57ms | Microsoftedge | 0.56 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 57ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 3 | 69ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 4 | 71ms | Linkedin | 0.18 MB/s | `https://linkedin.com` | 通用代理 |
| 5 | 77ms | Deno | 0.39 MB/s | `https://deno.com` | 通用代理 |
| 6 | 79ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 7 | 82ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 8 | 83ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 9 | 86ms | Img | - | `https://img.shields.io` | 通用代理 |
| 10 | 87ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 11 | 88ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 12 | 95ms | App | 0.09 MB/s | `https://app.netlify.com` | 通用代理 |
| 13 | 99ms | X | 1.07 MB/s | `https://x.com` | 通用代理 |
| 14 | 100ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 15 | 101ms | Dilo-d14 | 0.11 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 16 | 101ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 17 | 102ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 18 | 104ms | Kighelper-cloud | 0.06 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 19 | 104ms | Lawyer-yu | 0.07 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 20 | 105ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 21 | 106ms | Githubstatus | 0.83 MB/s | `https://githubstatus.com` | 通用代理 |
| 22 | 108ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 23 | 110ms | Crypto-funding-arbitrage | 0.05 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 24 | 111ms | Wordpaper | 0.41 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 25 | 113ms | Opresume | 0.35 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 26 | 113ms | Xjtu-nyxf-study-material | 0.11 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 27 | 115ms | Thumb | 1.07 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 28 | 116ms | Tools | 1.5 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 29 | 117ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 30 | 124ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 31 | 126ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 32 | 126ms | Cognitum | 0.15 MB/s | `https://cognitum.one` | 通用代理 |
| 33 | 126ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 34 | 127ms | Impro | 1.39 MB/s | `https://impro.social` | 通用代理 |
| 35 | 129ms | Music-cli | 0.18 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 36 | 130ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 37 | 130ms | Zebrunner | 0.99 MB/s | `https://zebrunner.com` | 通用代理 |
| 38 | 131ms | Opentakeoff | 0.05 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 39 | 131ms | Resume-5lv | 0.12 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 40 | 134ms | Tms | 0.14 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 41 | 135ms | Huly-mcp | 0.13 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 42 | 136ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 43 | 138ms | Impeccable | 0.74 MB/s | `https://impeccable.style` | 通用代理 |
| 44 | 142ms | Gpui | 0.21 MB/s | `https://gpui.rs` | 通用代理 |
| 45 | 143ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 46 | 144ms | Components | 0.08 MB/s | `https://components.dereekb.com` | 通用代理 |
| 47 | 144ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 48 | 144ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 49 | 145ms | Gp | 1.42 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 50 | 145ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 51 | 147ms | Bestdori | 0.09 MB/s | `https://bestdori.com` | 通用代理 |
| 52 | 147ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 53 | 147ms | Discord | 0.09 MB/s | `https://discord.gg` | 通用代理 |
| 54 | 147ms | Tokei | 0.53 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 55 | 148ms | App | 0.02 MB/s | `https://app.opencastor.com` | 通用代理 |
| 56 | 148ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 57 | 148ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 58 | 149ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 59 | 149ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 60 | 150ms | Gh | 1.38 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 61 | 150ms | Github | 1.27 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 62 | 151ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 63 | 151ms | Vibesql | 0.13 MB/s | `https://vibesql.org` | 通用代理 |
| 64 | 152ms | Serac | 0.09 MB/s | `https://serac.build` | 通用代理 |
| 65 | 153ms | Github | 1.45 MB/s | `https://github.880824.xyz` | 通用代理 |
| 66 | 153ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 67 | 153ms | Openpua | 0.5 MB/s | `https://openpua.ai` | 通用代理 |
| 68 | 154ms | Git | 1.42 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 69 | 154ms | Github | 1.47 MB/s | `https://github.788787.xyz` | 通用代理 |
| 70 | 154ms | L4d2 | 0.18 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 71 | 155ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 72 | 155ms | Git | 1.29 MB/s | `https://git.820828.xyz` | 通用代理 |
| 73 | 156ms | Agentlimb | 0.2 MB/s | `https://agentlimb.com` | 通用代理 |
| 74 | 157ms | Gitea-mirror | 0.6 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 75 | 158ms | Cumora | 0.35 MB/s | `https://cumora.ai` | 通用代理 |
| 76 | 158ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 77 | 159ms | Cbrowser | 1.19 MB/s | `https://cbrowser.ai` | 通用代理 |
| 78 | 160ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 79 | 161ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 80 | 161ms | Glass | 0.21 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 81 | 162ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 82 | 162ms | Clayrune | 0.14 MB/s | `https://clayrune.io` | 通用代理 |
| 83 | 162ms | GH-Proxy | 1.02 MB/s | `https://gh-proxy.com` | 通用代理 |
| 84 | 163ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 85 | 164ms | Contrib | 0.23 MB/s | `https://contrib.rocks` | 通用代理 |
| 86 | 165ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 87 | 166ms | Caiji | 0.08 MB/s | `https://caiji.cyou` | 通用代理 |
| 88 | 166ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 89 | 166ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 90 | 166ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 91 | 168ms | Anh | 0.25 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 92 | 168ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 93 | 168ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 94 | 169ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 95 | 169ms | Demo | 0.02 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 96 | 169ms | Opencovibe | 0.41 MB/s | `https://opencovibe.com` | 通用代理 |
| 97 | 169ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 98 | 170ms | Coffeecli | 0.12 MB/s | `https://coffeecli.com` | 通用代理 |
| 99 | 170ms | Gh | 1.02 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 100 | 170ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 101 | 171ms | Holyclaude | 0.17 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 102 | 171ms | Play | 0.03 MB/s | `https://play.templatical.com` | 通用代理 |
| 103 | 172ms | Training | 0.15 MB/s | `https://training.ti.com` | 通用代理 |
| 104 | 173ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 105 | 173ms | Gh | 1.4 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 106 | 174ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 107 | 174ms | Gsd | 0.16 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 108 | 174ms | Kuroutoshikou | 0.76 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 109 | 176ms | Gh | 1.2 MB/s | `https://gh.1k.ink` | 通用代理 |
| 110 | 177ms | Cody | 0.24 MB/s | `https://cody.todyle.com` | 通用代理 |
| 111 | 177ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 112 | 177ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 113 | 179ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 114 | 179ms | Alas | 0.36 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 115 | 180ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 116 | 180ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 117 | 180ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 118 | 180ms | Opensunsama | 0.05 MB/s | `https://opensunsama.com` | 通用代理 |
| 119 | 181ms | GH Monlor | 0.95 MB/s | `https://gh.monlor.com` | 通用代理 |
| 120 | 181ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 121 | 182ms | Github | 1.29 MB/s | `https://github.ihnic.com` | 通用代理 |
| 122 | 183ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 123 | 183ms | Ghproxy | 1.02 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 124 | 184ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 125 | 187ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 126 | 188ms | Codeeraser | 0.13 MB/s | `https://codeeraser.dev` | 通用代理 |
| 127 | 188ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 128 | 189ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 129 | 195ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 130 | 195ms | Bananaslides | 0.3 MB/s | `https://bananaslides.online` | 通用代理 |
| 131 | 198ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 132 | 198ms | Ode | - | `https://ode.fun` | 通用代理 |
| 133 | 202ms | Cherryai | 0.04 MB/s | `https://cherryai.com` | 通用代理 |
| 134 | 202ms | GH-Proxy Org | 0.94 MB/s | `https://gh-proxy.org` | 通用代理 |
| 135 | 205ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 136 | 206ms | Ginlix | 0.47 MB/s | `https://ginlix.ai` | 通用代理 |
| 137 | 206ms | Polgarand | 0.05 MB/s | `https://polgarand.org` | 通用代理 |
| 138 | 207ms | Aiblackboxfc | 0.26 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 139 | 210ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 140 | 212ms | Ghproxy | 1.49 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 141 | 213ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 142 | 214ms | Clypra | 0.06 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 143 | 216ms | Openttd | 0.03 MB/s | `https://openttd.org` | 通用代理 |
| 144 | 217ms | Cursor | 0.43 MB/s | `https://cursor.com` | 通用代理 |
| 145 | 220ms | Themolt | 0.04 MB/s | `https://themolt.net` | 通用代理 |
| 146 | 221ms | Kenyu | 1.41 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 147 | 222ms | Twitter | 0.71 MB/s | `https://twitter.com` | 通用代理 |
| 148 | 222ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 149 | 223ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 150 | 223ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 151 | 225ms | Axios-http | 0.37 MB/s | `https://axios-http.com` | 通用代理 |
| 152 | 225ms | Coreos | 1.37 MB/s | `https://coreos.com` | 通用代理 |
| 153 | 225ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 154 | 228ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 155 | 232ms | Ghproxy | 0.72 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 156 | 232ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 157 | 236ms | Ampcode | 0.24 MB/s | `https://ampcode.com` | 通用代理 |
| 158 | 236ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 159 | 241ms | Aka | 0.52 MB/s | `https://aka.ms` | 通用代理 |
| 160 | 243ms | Microcoreos | 0.31 MB/s | `https://microcoreos.com` | 通用代理 |
| 161 | 245ms | Tvv | 1.29 MB/s | `https://tvv.tw` | 通用代理 |
| 162 | 246ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 163 | 247ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 164 | 247ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 165 | 249ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 166 | 250ms | Sub | 0.13 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 167 | 250ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 168 | 251ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 169 | 252ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 170 | 253ms | Agoramarket | 0.05 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 171 | 253ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 172 | 254ms | Aomedia | 0.25 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 173 | 254ms | Ggg | 1.38 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 174 | 256ms | Code | 0.85 MB/s | `https://code.claude.com` | 通用代理 |
| 175 | 256ms | Travis-ci | 0.16 MB/s | `https://travis-ci.org` | 通用代理 |
| 176 | 257ms | Api | 0.12 MB/s | `https://api.solov.cc` | 通用代理 |
| 177 | 257ms | CrashMC CDN | 0.75 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 178 | 260ms | Savannah | 0.04 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 179 | 261ms | Nisar | 0.77 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 180 | 269ms | FastGit CC | 0.89 MB/s | `https://fastgit.cc` | 通用代理 |
| 181 | 269ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 182 | 271ms | Github | 0.66 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 183 | 274ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 184 | 275ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 185 | 277ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 186 | 277ms | Visionmemorymcp | 0.21 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 187 | 285ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 188 | 285ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 189 | 285ms | Youtu | 1.11 MB/s | `https://youtu.be` | 通用代理 |
| 190 | 289ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 191 | 296ms | Tiktok | 0.1 MB/s | `https://tiktok.com` | 通用代理 |
| 192 | 297ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 193 | 300ms | Flashtype | - | `https://flashtype.com` | 通用代理 |
| 194 | 301ms | Sina | 0.44 MB/s | `https://sina.dev` | 通用代理 |
| 195 | 303ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 196 | 307ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 197 | 309ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 198 | 311ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 199 | 317ms | 30006000 | 0.61 MB/s | `https://30006000.xyz` | 通用代理 |
| 200 | 317ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 201 | 317ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 202 | 319ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 203 | 320ms | Claude | 0.21 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 204 | 321ms | Gh | 0.56 MB/s | `https://gh.padao.fun` | 通用代理 |
| 205 | 329ms | Agenticcorporation | 0.03 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 206 | 330ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 207 | 330ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 208 | 333ms | Weaverse | 0.57 MB/s | `https://weaverse.io` | 通用代理 |
| 209 | 336ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 210 | 336ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 211 | 337ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 212 | 337ms | Sonarcloud | 0.02 MB/s | `https://sonarcloud.io` | 通用代理 |
| 213 | 337ms | Steamcommunity | 0.06 MB/s | `https://steamcommunity.com` | 通用代理 |
| 214 | 340ms | B23 | - | `https://b23.tv` | 通用代理 |
| 215 | 340ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 216 | 341ms | Github | 1.36 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 217 | 349ms | Store | 0.65 MB/s | `https://store.steampowered.com` | 通用代理 |
| 218 | 352ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 219 | 359ms | Gh | 0.71 MB/s | `https://gh.noki.icu` | 通用代理 |
| 220 | 361ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 221 | 362ms | Turborepo-starter-kit-web | 0.03 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 222 | 364ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 223 | 366ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 224 | 367ms | Bailian | 0.07 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 225 | 367ms | Github | 1.38 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 226 | 371ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 227 | 372ms | You | 0.24 MB/s | `https://you.piccalc.com` | 通用代理 |
| 228 | 382ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 229 | 385ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 230 | 386ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 231 | 388ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 232 | 388ms | GH Nxnow | 0.29 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 233 | 389ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 234 | 397ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 235 | 398ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 236 | 403ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 237 | 405ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 238 | 406ms | Getgit | 1.4 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 239 | 409ms | Ednovas Mirror | 0.73 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 240 | 410ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 241 | 416ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 242 | 416ms | V4 | 1.29 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 243 | 423ms | Hk | 0.63 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 244 | 424ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 245 | 429ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 246 | 433ms | YYLX Git | 1.0 MB/s | `https://git.yylx.win` | 通用代理 |
| 247 | 440ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 248 | 443ms | Agentkey | 0.62 MB/s | `https://agentkey.app` | 通用代理 |
| 249 | 443ms | Aps | 0.04 MB/s | `https://aps.com` | 通用代理 |
| 250 | 448ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 251 | 449ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 252 | 451ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 253 | 451ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 254 | 452ms | Ark | 0.41 MB/s | `https://ark.intel.com` | 通用代理 |
| 255 | 454ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 256 | 459ms | Lecvdemarius | 0.06 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 257 | 461ms | Github | 1.45 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 258 | 461ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 259 | 462ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 260 | 464ms | Bible-ai-explorer | 0.05 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 261 | 466ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 262 | 478ms | Safedocx | 0.1 MB/s | `https://safedocx.com` | 通用代理 |
| 263 | 478ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 264 | 482ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 265 | 487ms | Patchworkos | 0.29 MB/s | `https://patchworkos.com` | 通用代理 |
| 266 | 488ms | GHFast | 0.67 MB/s | `https://ghfast.top` | 通用代理 |
| 267 | 496ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 268 | 512ms | Umami-mcp | 0.84 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 269 | 515ms | Wl | - | `https://wl.do` | 通用代理 |
| 270 | 524ms | Aosmd | 0.13 MB/s | `https://aosmd.com` | 通用代理 |
| 271 | 530ms | Tsukuyomi | 0.09 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 272 | 532ms | Lucky | 0.41 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 273 | 534ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 274 | 542ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 275 | 544ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 276 | 548ms | Im | 0.95 MB/s | `https://im.codes` | 通用代理 |
| 277 | 549ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 278 | 550ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 279 | 560ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 280 | 561ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 281 | 575ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 282 | 583ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 283 | 585ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 284 | 593ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 285 | 593ms | Gh | 0.32 MB/s | `https://gh.dpik.top` | 通用代理 |
| 286 | 598ms | Support | 0.12 MB/s | `https://support.apple.com` | 通用代理 |
| 287 | 614ms | Fastfile | 1.23 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 288 | 634ms | Clawbiz | 0.02 MB/s | `https://clawbiz.io` | 通用代理 |
| 289 | 634ms | Github | 0.24 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 290 | 650ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 291 | 662ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 292 | 668ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 293 | 673ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 294 | 673ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 295 | 678ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 296 | 682ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 297 | 692ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 298 | 696ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 299 | 720ms | Cfkua | 0.75 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 300 | 727ms | Os | 0.09 MB/s | `https://os.ryo.lu` | 通用代理 |
| 301 | 730ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 302 | 734ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 303 | 747ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 304 | 750ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 305 | 758ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 306 | 760ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 307 | 762ms | Docs | 0.18 MB/s | `https://docs.transifex.com` | 通用代理 |
| 308 | 767ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 309 | 769ms | Gh | 0.47 MB/s | `https://gh.39.al` | 通用代理 |
| 310 | 771ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 311 | 778ms | Tracely-studio | 0.01 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 312 | 814ms | Git | 0.16 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 313 | 819ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 314 | 821ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 315 | 830ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 316 | 842ms | Dimagent | 0.68 MB/s | `https://dimagent.com` | 通用代理 |
| 317 | 868ms | Ccgather | 0.05 MB/s | `https://ccgather.com` | 通用代理 |
| 318 | 876ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 319 | 876ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 320 | 903ms | GHProxy Net | 0.22 MB/s | `https://ghproxy.net` | 通用代理 |
| 321 | 913ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 322 | 918ms | Task | 0.02 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 323 | 931ms | Dbgate | 0.15 MB/s | `https://dbgate.org` | 通用代理 |
| 324 | 934ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 325 | 952ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 326 | 958ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 327 | 972ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 328 | 977ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 329 | 977ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 330 | 980ms | Web | - | `https://web.4399.com` | 通用代理 |
| 331 | 992ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 332 | 1003ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 333 | 1005ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 334 | 1027ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 335 | 1028ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 336 | 1069ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 337 | 1081ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 338 | 1114ms | V | - | `https://v.douyin.com` | 通用代理 |
| 339 | 1120ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 340 | 1138ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 341 | 1140ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 342 | 1167ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 343 | 1170ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 344 | 1174ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 345 | 1176ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 346 | 1212ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 347 | 1220ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 348 | 1225ms | Ghproxy | 0.24 MB/s | `https://ghproxy.cc` | 通用代理 |
| 349 | 1227ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 350 | 1230ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 351 | 1234ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 352 | 1234ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 353 | 1325ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 354 | 1330ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 355 | 1332ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 356 | 1336ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 357 | 1357ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 358 | 1358ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 359 | 1359ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 360 | 1375ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 361 | 1413ms | Cf | 0.24 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 362 | 1416ms | Git | 0.1 MB/s | `https://git.669966.xyz` | 通用代理 |
| 363 | 1431ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 364 | 1491ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 365 | 1575ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 366 | 1620ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 367 | 1677ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 368 | 1707ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 369 | 1732ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 370 | 2139ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 371 | 2150ms | Img | - | `https://img.ink` | 通用代理 |
| 372 | 2279ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 373 | 2321ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 374 | 2356ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 375 | 2513ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 376 | 2763ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 377 | 2890ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 378 | 3035ms | Gh | 0.19 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 379 | 3053ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 380 | 3166ms | Ghproxy | 0.12 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 381 | 3240ms | G | 0.16 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 382 | 4015ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 383 | 6331ms | Proxy | 0.04 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 3 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 9 次 |
| GitClone (`gitclone-com`) | 4 次 |
| Gh (`gh-idayer-com`) | 3 次 |
| Github (`github-chenc-dev`) | 1 次 |
| Proxy (`proxy-vvvv-ee`) | 4 次 |
| 5555 (`5555-cab`) | 21 次 |
| Fastgpt (`fastgpt-leez-tech`) | 1 次 |
| Doxygen (`doxygen-org`) | 17 次 |
| Maplecode (`maplecode-art`) | 10 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 6 次 |
| Adult (`adult-contents-fc2-com`) | 2 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 388 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **395** | |

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
