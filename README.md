# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-27T17:35:25Z**，每 6 小时刷新一次。当前 ✅ **383** 在线 / ⚠️ **12** 不稳定 / ⚰️ **51** 已失效归档。

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
| 1 | 55ms | Microsoftedge | 0.35 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 56ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 3 | 67ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 4 | 72ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 5 | 73ms | Deno | 0.23 MB/s | `https://deno.com` | 通用代理 |
| 6 | 73ms | Linkedin | 0.16 MB/s | `https://linkedin.com` | 通用代理 |
| 7 | 80ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 8 | 81ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 9 | 81ms | Img | - | `https://img.shields.io` | 通用代理 |
| 10 | 84ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 11 | 86ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 12 | 93ms | X | 1.54 MB/s | `https://x.com` | 通用代理 |
| 13 | 94ms | App | 0.12 MB/s | `https://app.netlify.com` | 通用代理 |
| 14 | 95ms | Dilo-d14 | 0.05 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 15 | 95ms | Githubstatus | 4.17 MB/s | `https://githubstatus.com` | 通用代理 |
| 16 | 97ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 17 | 97ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 18 | 100ms | Godocs | 0.06 MB/s | `https://godocs.io` | 通用代理 |
| 19 | 100ms | Lawyer-yu | 0.07 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 20 | 101ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 21 | 101ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 22 | 105ms | Crypto-funding-arbitrage | 0.06 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 23 | 106ms | Kighelper-cloud | 0.05 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 24 | 106ms | Xjtu-nyxf-study-material | 0.14 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 25 | 108ms | Wordpaper | 0.55 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 26 | 112ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 27 | 112ms | Opresume | 0.2 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 28 | 115ms | Thumb | 4.43 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 29 | 115ms | Tools | 1.87 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 30 | 117ms | App | 0.01 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 31 | 121ms | Goreportcard | 0.04 MB/s | `https://goreportcard.com` | 通用代理 |
| 32 | 121ms | Zebrunner | 1.86 MB/s | `https://zebrunner.com` | 通用代理 |
| 33 | 122ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 34 | 123ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 35 | 123ms | Impro | 1.3 MB/s | `https://impro.social` | 通用代理 |
| 36 | 126ms | Cognitum | 0.1 MB/s | `https://cognitum.one` | 通用代理 |
| 37 | 126ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 38 | 127ms | Music-cli | 0.28 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 39 | 127ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 40 | 128ms | Huly-mcp | 0.1 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 41 | 129ms | Resume-5lv | 0.08 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 42 | 130ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 43 | 135ms | Tms | 0.08 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 44 | 135ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 45 | 135ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 46 | 136ms | Discord | 0.07 MB/s | `https://discord.gg` | 通用代理 |
| 47 | 136ms | Impeccable | 0.71 MB/s | `https://impeccable.style` | 通用代理 |
| 48 | 137ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 49 | 138ms | Clayrune | 0.09 MB/s | `https://clayrune.io` | 通用代理 |
| 50 | 138ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 51 | 138ms | Gp | 0.74 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 52 | 139ms | Agentlimb | 0.15 MB/s | `https://agentlimb.com` | 通用代理 |
| 53 | 141ms | Gh | 1.45 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 54 | 141ms | Vibesql | 0.05 MB/s | `https://vibesql.org` | 通用代理 |
| 55 | 142ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 56 | 142ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 57 | 142ms | Freeport | 0.02 MB/s | `https://freeport.network` | 通用代理 |
| 58 | 142ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 59 | 143ms | Github | 1.8 MB/s | `https://github.788787.xyz` | 通用代理 |
| 60 | 143ms | Github | 2.24 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 61 | 143ms | Gpui | 0.18 MB/s | `https://gpui.rs` | 通用代理 |
| 62 | 144ms | Github | 1.33 MB/s | `https://github.880824.xyz` | 通用代理 |
| 63 | 144ms | Hopp | 0.05 MB/s | `https://hopp.sh` | 通用代理 |
| 64 | 145ms | App | 0.02 MB/s | `https://app.opencastor.com` | 通用代理 |
| 65 | 145ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 66 | 145ms | Git | 2.71 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 67 | 147ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 68 | 147ms | Git | 1.4 MB/s | `https://git.820828.xyz` | 通用代理 |
| 69 | 147ms | Tokei | 0.33 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 70 | 150ms | Bestdori | 0.11 MB/s | `https://bestdori.com` | 通用代理 |
| 71 | 152ms | Components | 0.09 MB/s | `https://components.dereekb.com` | 通用代理 |
| 72 | 153ms | GH-Proxy | 0.64 MB/s | `https://gh-proxy.com` | 通用代理 |
| 73 | 153ms | L4d2 | 0.05 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 74 | 155ms | Serac | 0.06 MB/s | `https://serac.build` | 通用代理 |
| 75 | 156ms | Cbrowser | 0.83 MB/s | `https://cbrowser.ai` | 通用代理 |
| 76 | 156ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 77 | 156ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 78 | 157ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 79 | 158ms | Gitea-mirror | 0.54 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 80 | 158ms | Openpua | 0.24 MB/s | `https://openpua.ai` | 通用代理 |
| 81 | 159ms | Anh | 0.1 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 82 | 159ms | Contrib | 0.25 MB/s | `https://contrib.rocks` | 通用代理 |
| 83 | 159ms | Nextup-resource | 0.08 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 84 | 160ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 85 | 160ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 86 | 161ms | Gh | 1.06 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 87 | 161ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 88 | 162ms | Caw | 0.03 MB/s | `https://caw.rocks` | 通用代理 |
| 89 | 162ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 90 | 163ms | Glass | 0.09 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 91 | 164ms | Demo | 0.03 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 92 | 164ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 93 | 165ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 94 | 165ms | Miaozitie | 0.04 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 95 | 165ms | Shiori-v1 | 0.09 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 96 | 166ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 97 | 166ms | Gh | 1.31 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 98 | 167ms | Bolt2github | 0.04 MB/s | `https://bolt2github.com` | 通用代理 |
| 99 | 168ms | Opencovibe | 0.27 MB/s | `https://opencovibe.com` | 通用代理 |
| 100 | 169ms | Caiji | 0.06 MB/s | `https://caiji.cyou` | 通用代理 |
| 101 | 169ms | Coffeecli | 0.09 MB/s | `https://coffeecli.com` | 通用代理 |
| 102 | 170ms | Cody | 0.1 MB/s | `https://cody.todyle.com` | 通用代理 |
| 103 | 170ms | Kuroutoshikou | 0.13 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 104 | 170ms | Training | 0.21 MB/s | `https://training.ti.com` | 通用代理 |
| 105 | 170ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 106 | 171ms | Alas | 0.94 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 107 | 172ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 108 | 172ms | Gsd | 0.09 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 109 | 172ms | Play | 0.03 MB/s | `https://play.templatical.com` | 通用代理 |
| 110 | 173ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 111 | 173ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 112 | 174ms | Chops | 0.01 MB/s | `https://chops.md` | 通用代理 |
| 113 | 175ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 114 | 175ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 115 | 175ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 116 | 176ms | Github | 1.62 MB/s | `https://github.ihnic.com` | 通用代理 |
| 117 | 176ms | Holyclaude | 0.07 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 118 | 177ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 119 | 177ms | Ghproxy | 2.28 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 120 | 178ms | GH Monlor | 1.31 MB/s | `https://gh.monlor.com` | 通用代理 |
| 121 | 179ms | Gh | 1.61 MB/s | `https://gh.1k.ink` | 通用代理 |
| 122 | 179ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 123 | 181ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 124 | 183ms | Ai-trend-publish | 0.04 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 125 | 183ms | Codeeraser | 0.06 MB/s | `https://codeeraser.dev` | 通用代理 |
| 126 | 185ms | Opensunsama | 0.09 MB/s | `https://opensunsama.com` | 通用代理 |
| 127 | 187ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 128 | 188ms | Aiblackboxfc | 0.23 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 129 | 190ms | Cumora | 0.25 MB/s | `https://cumora.ai` | 通用代理 |
| 130 | 192ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 131 | 199ms | GH-Proxy Org | 1.62 MB/s | `https://gh-proxy.org` | 通用代理 |
| 132 | 199ms | Ginlix | 0.38 MB/s | `https://ginlix.ai` | 通用代理 |
| 133 | 199ms | Ode | - | `https://ode.fun` | 通用代理 |
| 134 | 201ms | Cherryai | 0.04 MB/s | `https://cherryai.com` | 通用代理 |
| 135 | 203ms | Openttd | 0.04 MB/s | `https://openttd.org` | 通用代理 |
| 136 | 203ms | Polgarand | 0.05 MB/s | `https://polgarand.org` | 通用代理 |
| 137 | 204ms | Bananaslides | 0.3 MB/s | `https://bananaslides.online` | 通用代理 |
| 138 | 204ms | Clypra | 0.06 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 139 | 204ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 140 | 204ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 141 | 207ms | Ghproxy | 2.71 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 142 | 208ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 143 | 212ms | Pidash | 0.06 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 144 | 214ms | Kenyu | 1.54 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 145 | 214ms | Twitter | 0.88 MB/s | `https://twitter.com` | 通用代理 |
| 146 | 216ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 147 | 216ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 148 | 216ms | Coreos | 1.41 MB/s | `https://coreos.com` | 通用代理 |
| 149 | 216ms | Cursor | 0.73 MB/s | `https://cursor.com` | 通用代理 |
| 150 | 216ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 151 | 218ms | Axios-http | 0.66 MB/s | `https://axios-http.com` | 通用代理 |
| 152 | 218ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 153 | 222ms | CrashMC CDN | 1.11 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 154 | 224ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 155 | 225ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 156 | 226ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 157 | 227ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 158 | 229ms | Aka | 0.71 MB/s | `https://aka.ms` | 通用代理 |
| 159 | 229ms | Ampcode | 0.16 MB/s | `https://ampcode.com` | 通用代理 |
| 160 | 230ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 161 | 240ms | Tvv | 2.86 MB/s | `https://tvv.tw` | 通用代理 |
| 162 | 241ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 163 | 241ms | Ggg | 1.66 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 164 | 242ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 165 | 242ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 166 | 243ms | Ghproxy | 2.29 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 167 | 243ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 168 | 245ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 169 | 247ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 170 | 249ms | Aomedia | 0.13 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 171 | 250ms | Savannah | 0.02 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 172 | 250ms | Travis-ci | 0.13 MB/s | `https://travis-ci.org` | 通用代理 |
| 173 | 250ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 174 | 252ms | Code | 1.56 MB/s | `https://code.claude.com` | 通用代理 |
| 175 | 253ms | Microcoreos | 0.26 MB/s | `https://microcoreos.com` | 通用代理 |
| 176 | 256ms | Nisar | 1.84 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 177 | 261ms | Api | 0.18 MB/s | `https://api.solov.cc` | 通用代理 |
| 178 | 261ms | Sub | 0.26 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 179 | 266ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 180 | 267ms | Agoramarket | 0.04 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 181 | 269ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 182 | 269ms | Tiktok | 0.11 MB/s | `https://tiktok.com` | 通用代理 |
| 183 | 271ms | Visionmemorymcp | 0.35 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 184 | 272ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 185 | 273ms | FastGit CC | 1.23 MB/s | `https://fastgit.cc` | 通用代理 |
| 186 | 273ms | Sina | 2.38 MB/s | `https://sina.dev` | 通用代理 |
| 187 | 274ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 188 | 275ms | Github | 1.61 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 189 | 281ms | Open | 0.03 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 190 | 284ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 191 | 284ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 192 | 292ms | Youtu | 0.84 MB/s | `https://youtu.be` | 通用代理 |
| 193 | 298ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 194 | 300ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 195 | 301ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 196 | 307ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 197 | 311ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 198 | 314ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 199 | 314ms | Steamcommunity | 0.19 MB/s | `https://steamcommunity.com` | 通用代理 |
| 200 | 314ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 201 | 318ms | 30006000 | 1.97 MB/s | `https://30006000.xyz` | 通用代理 |
| 202 | 318ms | Claude | 0.31 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 203 | 319ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 204 | 322ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 205 | 323ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 206 | 323ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 207 | 324ms | Gh | 1.82 MB/s | `https://gh.padao.fun` | 通用代理 |
| 208 | 325ms | Weaverse | 0.72 MB/s | `https://weaverse.io` | 通用代理 |
| 209 | 329ms | Github | 1.14 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 210 | 331ms | Agent-room | 0.05 MB/s | `https://agent-room.com` | 通用代理 |
| 211 | 332ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 212 | 333ms | Radio-browser | 0.03 MB/s | `https://radio-browser.info` | 通用代理 |
| 213 | 334ms | Sonarcloud | 0.01 MB/s | `https://sonarcloud.io` | 通用代理 |
| 214 | 334ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 215 | 334ms | Store | 1.5 MB/s | `https://store.steampowered.com` | 通用代理 |
| 216 | 341ms | B23 | - | `https://b23.tv` | 通用代理 |
| 217 | 342ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 218 | 343ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 219 | 352ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 220 | 356ms | Turborepo-starter-kit-web | 0.09 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 221 | 359ms | Github | 1.6 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 222 | 359ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 223 | 361ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 224 | 362ms | Bailian | 0.24 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 225 | 367ms | You | 0.05 MB/s | `https://you.piccalc.com` | 通用代理 |
| 226 | 372ms | Autonomi | 0.03 MB/s | `https://autonomi.dev` | 通用代理 |
| 227 | 374ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 228 | 375ms | Gh | 0.48 MB/s | `https://gh.noki.icu` | 通用代理 |
| 229 | 378ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 230 | 379ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 231 | 389ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 232 | 390ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 233 | 392ms | Ednovas Mirror | 0.79 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 234 | 393ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 235 | 401ms | Hk | 1.32 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 236 | 403ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 237 | 409ms | Codeflying | 0.01 MB/s | `https://codeflying.app` | 通用代理 |
| 238 | 410ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 239 | 411ms | Getgit | 1.8 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 240 | 418ms | Readsync | 0.04 MB/s | `https://readsync.org` | 通用代理 |
| 241 | 420ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 242 | 421ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 243 | 428ms | Agentkey | 0.15 MB/s | `https://agentkey.app` | 通用代理 |
| 244 | 429ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 245 | 429ms | YYLX Git | 0.54 MB/s | `https://git.yylx.win` | 通用代理 |
| 246 | 441ms | Aps | 0.05 MB/s | `https://aps.com` | 通用代理 |
| 247 | 441ms | Github | 1.59 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 248 | 442ms | Bseindia | - | `https://bseindia.com` | 通用代理 |
| 249 | 447ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 250 | 449ms | Memstack | 0.04 MB/s | `https://memstack.pro` | 通用代理 |
| 251 | 449ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 252 | 450ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 253 | 450ms | Bible-ai-explorer | 0.13 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 254 | 450ms | Msdn | 0.05 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 255 | 453ms | Ark | 0.97 MB/s | `https://ark.intel.com` | 通用代理 |
| 256 | 456ms | Lecvdemarius | 0.07 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 257 | 460ms | Safedocx | 0.17 MB/s | `https://safedocx.com` | 通用代理 |
| 258 | 465ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 259 | 465ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 260 | 480ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 261 | 482ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 262 | 483ms | Patchworkos | 0.24 MB/s | `https://patchworkos.com` | 通用代理 |
| 263 | 489ms | GHFast | 1.74 MB/s | `https://ghfast.top` | 通用代理 |
| 264 | 492ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 265 | 506ms | Umami-mcp | 0.32 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 266 | 507ms | Aosmd | 0.11 MB/s | `https://aosmd.com` | 通用代理 |
| 267 | 516ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 268 | 518ms | Wl | - | `https://wl.do` | 通用代理 |
| 269 | 524ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 270 | 525ms | Lucky | 0.37 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 271 | 526ms | Cfkua | 0.78 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 272 | 529ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 273 | 534ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 274 | 542ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 275 | 548ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 276 | 551ms | Gh | 1.26 MB/s | `https://gh.dpik.top` | 通用代理 |
| 277 | 551ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 278 | 552ms | V4 | 0.78 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 279 | 561ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 280 | 566ms | 3d-set-visualizer | 0.05 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 281 | 566ms | Ygdj7 | 0.05 MB/s | `https://ygdj7.com` | 通用代理 |
| 282 | 575ms | Im | 0.43 MB/s | `https://im.codes` | 通用代理 |
| 283 | 575ms | Support | 0.16 MB/s | `https://support.apple.com` | 通用代理 |
| 284 | 582ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 285 | 585ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 286 | 604ms | Clawbiz | 0.04 MB/s | `https://clawbiz.io` | 通用代理 |
| 287 | 618ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 288 | 628ms | Github | 0.45 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 289 | 643ms | Fastfile | 1.79 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 290 | 644ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 291 | 664ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 292 | 665ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 293 | 673ms | Internhack | 0.08 MB/s | `https://internhack.xyz` | 通用代理 |
| 294 | 680ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 295 | 683ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 296 | 685ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 297 | 693ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 298 | 708ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 299 | 728ms | Os | 0.08 MB/s | `https://os.ryo.lu` | 通用代理 |
| 300 | 729ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 301 | 739ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 302 | 740ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 303 | 743ms | Aif | 0.03 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 304 | 747ms | Ghproxy | 0.39 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 305 | 752ms | Docs | 0.14 MB/s | `https://docs.transifex.com` | 通用代理 |
| 306 | 753ms | Gh | 0.41 MB/s | `https://gh.39.al` | 通用代理 |
| 307 | 760ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 308 | 760ms | Tracely-studio | 0.05 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 309 | 768ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 310 | 793ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 311 | 798ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 312 | 814ms | Git | 0.25 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 313 | 825ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 314 | 837ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 315 | 864ms | Ccgather | 0.07 MB/s | `https://ccgather.com` | 通用代理 |
| 316 | 865ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 317 | 876ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 318 | 897ms | GHProxy Net | 0.08 MB/s | `https://ghproxy.net` | 通用代理 |
| 319 | 911ms | Task | 0.01 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 320 | 913ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 321 | 916ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 322 | 941ms | Md | 0.09 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 323 | 942ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 324 | 947ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 325 | 958ms | Mimo | 0.2 MB/s | `https://mimo.mi.com` | 通用代理 |
| 326 | 962ms | Yibiao | 0.16 MB/s | `https://yibiao.pro` | 通用代理 |
| 327 | 966ms | Dbgate | 0.1 MB/s | `https://dbgate.org` | 通用代理 |
| 328 | 971ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 329 | 974ms | Web | - | `https://web.4399.com` | 通用代理 |
| 330 | 1010ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 331 | 1026ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 332 | 1028ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 333 | 1039ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 334 | 1053ms | Dimagent | 0.16 MB/s | `https://dimagent.com` | 通用代理 |
| 335 | 1068ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 336 | 1072ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 337 | 1125ms | Honeymeta | 0.02 MB/s | `https://honeymeta.com` | 通用代理 |
| 338 | 1140ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 339 | 1145ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 340 | 1168ms | V | - | `https://v.douyin.com` | 通用代理 |
| 341 | 1180ms | Your-domain | 0.08 MB/s | `https://your-domain.com` | 通用代理 |
| 342 | 1181ms | Aliexpress | 0.02 MB/s | `https://aliexpress.com` | 通用代理 |
| 343 | 1181ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 344 | 1182ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 345 | 1195ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 346 | 1201ms | Atomcode | 0.09 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 347 | 1203ms | Hevolve | 0.09 MB/s | `https://hevolve.ai` | 通用代理 |
| 348 | 1214ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 349 | 1218ms | Ghproxy | 0.3 MB/s | `https://ghproxy.cc` | 通用代理 |
| 350 | 1260ms | Pew | 0.03 MB/s | `https://pew.md` | 通用代理 |
| 351 | 1300ms | Git | 0.86 MB/s | `https://git.669966.xyz` | 通用代理 |
| 352 | 1311ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 353 | 1314ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 354 | 1324ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 355 | 1330ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 356 | 1334ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 357 | 1356ms | Cf | 0.33 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 358 | 1375ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 359 | 1378ms | Mobilevc | 0.02 MB/s | `https://mobilevc.top` | 通用代理 |
| 360 | 1379ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 361 | 1382ms | Github | 0.17 MB/s | `https://github.chenc.dev` | 通用代理 |
| 362 | 1387ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 363 | 1413ms | Docs | 0.02 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 364 | 1493ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 365 | 1585ms | SLink | 0.09 MB/s | `https://slink.ltd` | 通用代理 |
| 366 | 1620ms | I-qps | 0.04 MB/s | `https://i-qps.net` | 通用代理 |
| 367 | 1674ms | Heycall-e | 0.12 MB/s | `https://heycall-e.com` | 通用代理 |
| 368 | 1692ms | Docs | 0.02 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 369 | 1693ms | Invent | 0.01 MB/s | `https://invent.kde.org` | 通用代理 |
| 370 | 2083ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 371 | 2088ms | Img | - | `https://img.ink` | 通用代理 |
| 372 | 2140ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 373 | 2144ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 374 | 2508ms | Provider | - | `https://provider.com` | 通用代理 |
| 375 | 2512ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 376 | 2758ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 377 | 3024ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 378 | 3098ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 379 | 3136ms | Ghproxy | 0.14 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 380 | 3155ms | Gh | 0.24 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 381 | 3308ms | G | 0.03 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 382 | 4126ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 383 | 6333ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 8 次 |
| GitClone (`gitclone-com`) | 3 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Proxy (`proxy-vvvv-ee`) | 3 次 |
| 5555 (`5555-cab`) | 20 次 |
| Doxygen (`doxygen-org`) | 16 次 |
| Axonhub (`axonhub-onrender-com`) | 2 次 |
| Flashtype (`flashtype-com`) | 3 次 |
| Maplecode (`maplecode-art`) | 9 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 5 次 |
| Adult (`adult-contents-fc2-com`) | 1 次 |

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
