# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-11-04T05:01:12Z**，每 6 小时刷新一次。当前 ✅ **414** 在线 / ⚠️ **15** 不稳定 / ⚰️ **56** 已失效归档。

## 核心特性

- **429 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 81ms | Microsoftedge | 0.3 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 89ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 94ms | Wordpaper | 0.36 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 4 | 94ms | Xjtu-nyxf-study-material | 0.15 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 5 | 97ms | Linkedin | 0.14 MB/s | `https://linkedin.com` | 通用代理 |
| 6 | 99ms | Resume-5lv | 0.17 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 7 | 102ms | Githubstatus | 0.79 MB/s | `https://githubstatus.com` | 通用代理 |
| 8 | 102ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 9 | 103ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 10 | 106ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 11 | 106ms | Img | - | `https://img.shields.io` | 通用代理 |
| 12 | 106ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 13 | 108ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 14 | 108ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 15 | 109ms | Huly-mcp | 0.15 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 16 | 110ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 17 | 111ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 18 | 113ms | Opresume | 0.46 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 19 | 114ms | X | 1.06 MB/s | `https://x.com` | 通用代理 |
| 20 | 117ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 21 | 118ms | Tools | 1.57 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 22 | 120ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 23 | 120ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 24 | 120ms | Dilo-d14 | 0.15 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 25 | 120ms | Kighelper-cloud | 0.07 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 26 | 123ms | Godocs | 0.06 MB/s | `https://godocs.io` | 通用代理 |
| 27 | 123ms | Zebrunner | 1.13 MB/s | `https://zebrunner.com` | 通用代理 |
| 28 | 125ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 29 | 126ms | Deno | 0.39 MB/s | `https://deno.com` | 通用代理 |
| 30 | 126ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 31 | 126ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 32 | 129ms | Lawyer-yu | 0.06 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 33 | 131ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 34 | 131ms | App | 0.07 MB/s | `https://app.netlify.com` | 通用代理 |
| 35 | 132ms | Openpua | 0.36 MB/s | `https://openpua.ai` | 通用代理 |
| 36 | 132ms | Serac | 0.07 MB/s | `https://serac.build` | 通用代理 |
| 37 | 133ms | Cumora | 0.29 MB/s | `https://cumora.ai` | 通用代理 |
| 38 | 133ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 39 | 133ms | Gh | 0.31 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 40 | 134ms | Impro | 1.36 MB/s | `https://impro.social` | 通用代理 |
| 41 | 135ms | Caiji | 0.09 MB/s | `https://caiji.cyou` | 通用代理 |
| 42 | 135ms | Github | 1.79 MB/s | `https://github.880824.xyz` | 通用代理 |
| 43 | 137ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 44 | 137ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 45 | 137ms | Bestdori | 0.08 MB/s | `https://bestdori.com` | 通用代理 |
| 46 | 137ms | Impeccable | 0.92 MB/s | `https://impeccable.style` | 通用代理 |
| 47 | 138ms | Gh | 1.76 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 48 | 139ms | Ghproxy | 0.33 MB/s | `https://ghproxy.cfd` | 通用代理 |
| 49 | 141ms | Agentlimb | 0.23 MB/s | `https://agentlimb.com` | 通用代理 |
| 50 | 141ms | Git | 1.74 MB/s | `https://git.820828.xyz` | 通用代理 |
| 51 | 141ms | Gitea-mirror | 0.72 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 52 | 142ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 53 | 142ms | Github | 1.55 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 54 | 142ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 55 | 143ms | Discord | 0.04 MB/s | `https://discord.gg` | 通用代理 |
| 56 | 143ms | Vibesql | 0.08 MB/s | `https://vibesql.org` | 通用代理 |
| 57 | 144ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 58 | 144ms | Coffeecli | 0.13 MB/s | `https://coffeecli.com` | 通用代理 |
| 59 | 144ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 60 | 144ms | Git | 1.8 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 61 | 144ms | Github | 1.78 MB/s | `https://github.788787.xyz` | 通用代理 |
| 62 | 144ms | Gp | 1.84 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 63 | 145ms | Anh | 0.22 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 64 | 145ms | Opensunsama | 0.05 MB/s | `https://opensunsama.com` | 通用代理 |
| 65 | 146ms | Openchamber | 0.75 MB/s | `https://openchamber.dev` | 通用代理 |
| 66 | 147ms | Codeeraser | 0.11 MB/s | `https://codeeraser.dev` | 通用代理 |
| 67 | 147ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 68 | 147ms | Tokei | 0.39 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 69 | 148ms | Clayrune | 0.11 MB/s | `https://clayrune.io` | 通用代理 |
| 70 | 148ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 71 | 148ms | Megacrit | 0.13 MB/s | `https://megacrit.com` | 通用代理 |
| 72 | 149ms | Opencovibe | 0.33 MB/s | `https://opencovibe.com` | 通用代理 |
| 73 | 150ms | Polgarand | 0.08 MB/s | `https://polgarand.org` | 通用代理 |
| 74 | 150ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 75 | 151ms | L4d2 | 0.13 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 76 | 151ms | Miaozitie | 0.06 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 77 | 152ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 78 | 152ms | Opentakeoff | 0.03 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 79 | 153ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 80 | 155ms | Game | 0.1 MB/s | `https://game.chozo.net` | 通用代理 |
| 81 | 156ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 82 | 157ms | Cody | 0.17 MB/s | `https://cody.todyle.com` | 通用代理 |
| 83 | 158ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 84 | 158ms | Components | 0.08 MB/s | `https://components.dereekb.com` | 通用代理 |
| 85 | 158ms | Demo | 0.02 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 86 | 159ms | Gpui | 0.18 MB/s | `https://gpui.rs` | 通用代理 |
| 87 | 160ms | Cherryai | 0.04 MB/s | `https://cherryai.com` | 通用代理 |
| 88 | 160ms | Glass | 0.18 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 89 | 160ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 90 | 161ms | Alas | 0.53 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 91 | 161ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 92 | 161ms | You | 0.87 MB/s | `https://you.piccalc.com` | 通用代理 |
| 93 | 162ms | Ghproxy | 1.78 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 94 | 162ms | Github | 1.73 MB/s | `https://github.ihnic.com` | 通用代理 |
| 95 | 163ms | Eng-3385e | 0.02 MB/s | `https://eng-3385e.web.app` | 通用代理 |
| 96 | 164ms | Caw | 0.05 MB/s | `https://caw.rocks` | 通用代理 |
| 97 | 165ms | Cognitum | 0.18 MB/s | `https://cognitum.one` | 通用代理 |
| 98 | 165ms | Pidash | 0.04 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 99 | 166ms | Docs | 1.34 MB/s | `https://docs.uxway.app` | 通用代理 |
| 100 | 166ms | Ghproxy | 1.43 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 101 | 169ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 102 | 170ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 103 | 170ms | Thumb | 0.72 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 104 | 170ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 105 | 171ms | Eng-3385e | 0.02 MB/s | `https://eng-3385e.firebaseapp.com` | 通用代理 |
| 106 | 172ms | Agoramarket | 0.04 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 107 | 175ms | GH-Proxy | 0.75 MB/s | `https://gh-proxy.com` | 通用代理 |
| 108 | 176ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 109 | 177ms | Chops | 0.02 MB/s | `https://chops.md` | 通用代理 |
| 110 | 178ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 111 | 179ms | Bananaslides | 0.3 MB/s | `https://bananaslides.online` | 通用代理 |
| 112 | 180ms | Cbrowser | 0.89 MB/s | `https://cbrowser.ai` | 通用代理 |
| 113 | 180ms | Training | 0.13 MB/s | `https://training.ti.com` | 通用代理 |
| 114 | 182ms | Api | 0.05 MB/s | `https://api.solov.cc` | 通用代理 |
| 115 | 182ms | Tvv | 1.38 MB/s | `https://tvv.tw` | 通用代理 |
| 116 | 183ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 117 | 184ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 118 | 185ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 119 | 186ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 120 | 192ms | Ghproxy | 0.77 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 121 | 194ms | Gh | 1.69 MB/s | `https://gh.404cafe.fun` | 通用代理 |
| 122 | 194ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 123 | 194ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 124 | 194ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 125 | 196ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 126 | 197ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 127 | 198ms | Openttd | 0.04 MB/s | `https://openttd.org` | 通用代理 |
| 128 | 199ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 129 | 199ms | Tms | 0.11 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 130 | 200ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 131 | 201ms | Gh | 0.94 MB/s | `https://gh.padao.fun` | 通用代理 |
| 132 | 201ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 133 | 203ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 134 | 203ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 135 | 205ms | Nisar | 0.81 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 136 | 205ms | Ode | - | `https://ode.fun` | 通用代理 |
| 137 | 207ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 138 | 209ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 139 | 209ms | Tomcat1235 | 0.41 MB/s | `https://tomcat1235.nyc.mn` | 通用代理 |
| 140 | 212ms | Ghproxy | 0.63 MB/s | `https://ghproxy.vip` | 通用代理 |
| 141 | 213ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 142 | 214ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 143 | 214ms | Aiblackboxfc | 0.31 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 144 | 217ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 145 | 218ms | Contrib | 0.22 MB/s | `https://contrib.rocks` | 通用代理 |
| 146 | 223ms | Music-cli | 0.19 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 147 | 223ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 148 | 224ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 149 | 224ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 150 | 224ms | Twitter | 0.66 MB/s | `https://twitter.com` | 通用代理 |
| 151 | 225ms | Paypal | 0.02 MB/s | `https://paypal.com` | 通用代理 |
| 152 | 226ms | Gh | 0.42 MB/s | `https://gh.1k.ink` | 通用代理 |
| 153 | 227ms | Kenyu | 0.65 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 154 | 228ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 155 | 233ms | Ampcode | 0.22 MB/s | `https://ampcode.com` | 通用代理 |
| 156 | 234ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 157 | 235ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 158 | 237ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 159 | 238ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 160 | 239ms | Slack | 0.09 MB/s | `https://slack.kubernetes.io` | 通用代理 |
| 161 | 240ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 162 | 242ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 163 | 243ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 164 | 244ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 165 | 245ms | Sina | 1.13 MB/s | `https://sina.dev` | 通用代理 |
| 166 | 248ms | GH Monlor | 0.13 MB/s | `https://gh.monlor.com` | 通用代理 |
| 167 | 248ms | GH-Proxy Org | 0.76 MB/s | `https://gh-proxy.org` | 通用代理 |
| 168 | 251ms | CrashMC CDN | 0.14 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 169 | 251ms | Tools | 0.03 MB/s | `https://tools.ietf.org` | 通用代理 |
| 170 | 252ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 171 | 254ms | Axios-http | 0.31 MB/s | `https://axios-http.com` | 通用代理 |
| 172 | 256ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 173 | 258ms | Clypra | 0.06 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 174 | 259ms | Misaligned | 0.51 MB/s | `https://misaligned.top` | 通用代理 |
| 175 | 261ms | Aka | 0.53 MB/s | `https://aka.ms` | 通用代理 |
| 176 | 261ms | FastGit CC | 0.86 MB/s | `https://fastgit.cc` | 通用代理 |
| 177 | 262ms | Github | 0.74 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 178 | 264ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 179 | 264ms | Travis-ci | 0.13 MB/s | `https://travis-ci.org` | 通用代理 |
| 180 | 265ms | Ginlix | 0.38 MB/s | `https://ginlix.ai` | 通用代理 |
| 181 | 265ms | Visionmemorymcp | 0.26 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 182 | 266ms | Ggg | 0.25 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 183 | 268ms | Radio-browser | 0.01 MB/s | `https://radio-browser.info` | 通用代理 |
| 184 | 270ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 185 | 270ms | Microcoreos | 0.31 MB/s | `https://microcoreos.com` | 通用代理 |
| 186 | 271ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 187 | 272ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 188 | 273ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 189 | 273ms | Kuroutoshikou | 0.46 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 190 | 277ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 191 | 281ms | Code | 1.13 MB/s | `https://code.claude.com` | 通用代理 |
| 192 | 284ms | Gsd | 0.15 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 193 | 286ms | Savannah | 0.03 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 194 | 286ms | Wings | 0.01 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 195 | 291ms | Wandoukj | - | `https://wandoukj.eu.org` | 通用代理 |
| 196 | 292ms | Cursor | 0.32 MB/s | `https://cursor.com` | 通用代理 |
| 197 | 295ms | YYLX Git | 0.72 MB/s | `https://git.yylx.win` | 通用代理 |
| 198 | 296ms | Phabricator | 0.03 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 199 | 301ms | GHFast | 0.4 MB/s | `https://ghfast.top` | 通用代理 |
| 200 | 304ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 201 | 304ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 202 | 312ms | Claude | 0.19 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 203 | 313ms | B23 | - | `https://b23.tv` | 通用代理 |
| 204 | 313ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 205 | 314ms | Coreos | 1.3 MB/s | `https://coreos.com` | 通用代理 |
| 206 | 319ms | Docs | 0.03 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 207 | 319ms | Github | 1.7 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 208 | 319ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 209 | 320ms | Hk | 0.78 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 210 | 321ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 211 | 323ms | Bailian | 0.08 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 212 | 323ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 213 | 324ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 214 | 324ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 215 | 327ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 216 | 327ms | Youtu | 1.32 MB/s | `https://youtu.be` | 通用代理 |
| 217 | 330ms | Steamcommunity | 0.12 MB/s | `https://steamcommunity.com` | 通用代理 |
| 218 | 331ms | Gh | 0.71 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 219 | 332ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 220 | 334ms | 30006000 | 0.79 MB/s | `https://30006000.xyz` | 通用代理 |
| 221 | 339ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 222 | 342ms | Tiktok | 0.08 MB/s | `https://tiktok.com` | 通用代理 |
| 223 | 350ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 224 | 351ms | Agenticcorporation | 0.03 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 225 | 351ms | Github | 1.91 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 226 | 352ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 227 | 357ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 228 | 357ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 229 | 358ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 230 | 368ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 231 | 369ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 232 | 369ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 233 | 369ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 234 | 371ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 235 | 372ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 236 | 373ms | Cfkua | 1.18 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 237 | 373ms | Sonarcloud | 0.22 MB/s | `https://sonarcloud.io` | 通用代理 |
| 238 | 375ms | Turborepo-starter-kit-web | 0.02 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 239 | 377ms | Docs | 0.58 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 240 | 378ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 241 | 379ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 242 | 383ms | Aps | 0.05 MB/s | `https://aps.com` | 通用代理 |
| 243 | 385ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 244 | 385ms | Store | 1.01 MB/s | `https://store.steampowered.com` | 通用代理 |
| 245 | 394ms | Gh | 0.78 MB/s | `https://gh.noki.icu` | 通用代理 |
| 246 | 395ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 247 | 395ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 248 | 397ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 249 | 397ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 250 | 400ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 251 | 401ms | V4 | 1.03 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 252 | 401ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 253 | 405ms | Github | 1.74 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 254 | 407ms | Getgit | 0.37 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 255 | 411ms | Weaverse | 0.39 MB/s | `https://weaverse.io` | 通用代理 |
| 256 | 412ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 257 | 420ms | GH Nxnow | 0.16 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 258 | 422ms | SLink | 0.06 MB/s | `https://slink.ltd` | 通用代理 |
| 259 | 431ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 260 | 436ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 261 | 437ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 262 | 438ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 263 | 445ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 264 | 446ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 265 | 460ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 266 | 466ms | Wl | - | `https://wl.do` | 通用代理 |
| 267 | 467ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 268 | 468ms | Bible-ai-explorer | 0.06 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 269 | 468ms | Lucky | 0.51 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 270 | 468ms | Proxy | 1.15 MB/s | `https://proxy.vvvv.ee` | 通用代理 |
| 271 | 469ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 272 | 470ms | Aistudio | 0.92 MB/s | `https://aistudio.google.com` | 通用代理 |
| 273 | 470ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 274 | 482ms | Ghproxy | 0.54 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 275 | 482ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 276 | 495ms | Hub | 0.28 MB/s | `https://hub.glowp.xyz` | 通用代理 |
| 277 | 506ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 278 | 509ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 279 | 512ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 280 | 521ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 281 | 524ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 282 | 526ms | Gh | 0.19 MB/s | `https://gh.idayer.com` | 通用代理 |
| 283 | 529ms | Ark | 0.53 MB/s | `https://ark.intel.com` | 通用代理 |
| 284 | 530ms | Agentkey | 0.25 MB/s | `https://agentkey.app` | 通用代理 |
| 285 | 530ms | Vaultproject | 0.15 MB/s | `https://vaultproject.io` | 通用代理 |
| 286 | 531ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 287 | 531ms | Umami-mcp | 0.4 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 288 | 532ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 289 | 535ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 290 | 538ms | Api | - | `https://api.river.ai` | 通用代理 |
| 291 | 540ms | Safedocx | 0.07 MB/s | `https://safedocx.com` | 通用代理 |
| 292 | 546ms | Gh | 0.81 MB/s | `https://gh.39.al` | 通用代理 |
| 293 | 551ms | Patchworkos | 0.26 MB/s | `https://patchworkos.com` | 通用代理 |
| 294 | 568ms | Tsukuyomi | 0.1 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 295 | 569ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 296 | 574ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 297 | 575ms | Fastfile | 1.16 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 298 | 579ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 299 | 580ms | Support | 0.09 MB/s | `https://support.apple.com` | 通用代理 |
| 300 | 581ms | Aosmd | 0.15 MB/s | `https://aosmd.com` | 通用代理 |
| 301 | 582ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 302 | 585ms | Github | 0.35 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 303 | 589ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 304 | 597ms | Oapi | - | `https://oapi.dingtalk.com` | 通用代理 |
| 305 | 607ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 306 | 614ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 307 | 616ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 308 | 631ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 309 | 632ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 310 | 634ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 311 | 637ms | Im | 0.05 MB/s | `https://im.codes` | 通用代理 |
| 312 | 642ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 313 | 657ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 314 | 669ms | Lecvdemarius | 0.05 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 315 | 679ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 316 | 698ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 317 | 700ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 318 | 701ms | Gh | 0.82 MB/s | `https://gh.noki.eu.org` | 通用代理 |
| 319 | 706ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 320 | 710ms | Ghproxy | 0.3 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 321 | 711ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 322 | 726ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 323 | 734ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 324 | 752ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 325 | 754ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 326 | 762ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 327 | 778ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 328 | 780ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 329 | 789ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 330 | 800ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 331 | 809ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 332 | 817ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 333 | 822ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 334 | 842ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 335 | 844ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 336 | 870ms | Aif | 0.05 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 337 | 872ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 338 | 876ms | Dbgate | 0.13 MB/s | `https://dbgate.org` | 通用代理 |
| 339 | 878ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 340 | 896ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 341 | 908ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 342 | 910ms | Mimo | 0.19 MB/s | `https://mimo.mi.com` | 通用代理 |
| 343 | 911ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 344 | 933ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 345 | 940ms | Docs | 0.16 MB/s | `https://docs.transifex.com` | 通用代理 |
| 346 | 941ms | Invent | 0.01 MB/s | `https://invent.kde.org` | 通用代理 |
| 347 | 944ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 348 | 954ms | Task | 0.02 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 349 | 955ms | Ednovas Mirror | 0.53 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 350 | 967ms | Ccgather | 0.04 MB/s | `https://ccgather.com` | 通用代理 |
| 351 | 971ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 352 | 974ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 353 | 975ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 354 | 981ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 355 | 1004ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 356 | 1010ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 357 | 1018ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 358 | 1024ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 359 | 1027ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 360 | 1033ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 361 | 1048ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 362 | 1059ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 363 | 1094ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 364 | 1124ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 365 | 1135ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 366 | 1138ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 367 | 1141ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 368 | 1163ms | V | 0.04 MB/s | `https://v.douyin.com` | 通用代理 |
| 369 | 1178ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 370 | 1186ms | Atomcode | 0.07 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 371 | 1203ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 372 | 1205ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 373 | 1210ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 374 | 1211ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 375 | 1228ms | Ghproxy | 0.28 MB/s | `https://ghproxy.cc` | 通用代理 |
| 376 | 1244ms | Web | - | `https://web.4399.com` | 通用代理 |
| 377 | 1249ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 378 | 1253ms | GHFile Geekertao | 0.42 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 379 | 1267ms | Cf | 0.29 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 380 | 1296ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 381 | 1304ms | GHProxy Net | 0.03 MB/s | `https://ghproxy.net` | 通用代理 |
| 382 | 1327ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 383 | 1340ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 384 | 1357ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 385 | 1362ms | Gitlab | 0.01 MB/s | `https://gitlab.heigit.org` | 通用代理 |
| 386 | 1393ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 387 | 1429ms | Gh | 0.26 MB/s | `https://gh.sixyin.com` | 通用代理 |
| 388 | 1454ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 389 | 1472ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 390 | 1499ms | Gh | 0.32 MB/s | `https://gh.dpik.top` | 通用代理 |
| 391 | 1522ms | Dimagent | 0.24 MB/s | `https://dimagent.com` | 通用代理 |
| 392 | 1555ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 393 | 1587ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 394 | 1684ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 395 | 1837ms | Github | 0.18 MB/s | `https://github.chenc.dev` | 通用代理 |
| 396 | 1881ms | Wget | 0.1 MB/s | `https://wget.la` | 通用代理 |
| 397 | 1917ms | Dplayer | 0.03 MB/s | `https://dplayer.diandian.com` | 通用代理 |
| 398 | 2084ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 399 | 2231ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 400 | 2328ms | Img | - | `https://img.ink` | 通用代理 |
| 401 | 2466ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 402 | 2574ms | Web | 0.19 MB/s | `https://web.archive.org` | 通用代理 |
| 403 | 2679ms | Provider | - | `https://provider.com` | 通用代理 |
| 404 | 2722ms | G | 0.25 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 405 | 2763ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 406 | 2800ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 407 | 2841ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 408 | 2894ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 409 | 3059ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 410 | 3209ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 411 | 3262ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 412 | 6124ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 413 | 6220ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 414 | 14541ms | 5555 | 0.01 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（15 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Gh (`gh-llkk-cc`) | 15 次 |
| Git (`git-669966-xyz`) | 2 次 |
| Git (`git-tangbai-cc`) | 14 次 |
| Gh (`gh-b52m-cn`) | 18 次 |
| Sub (`sub-ikar-eu-org`) | 13 次 |
| Nssurge (`nssurge-com`) | 17 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 17 次 |
| Flashtype (`flashtype-com`) | 1 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 22 次 |
| Leereilly (`leereilly-net`) | 4 次 |
| Adult (`adult-contents-fc2-com`) | 3 次 |
| Free (`free-cn-eu-org`) | 10 次 |
| Proxy (`proxy-scdn-io`) | 8 次 |
| Gh (`gh-ddlc-top`) | 3 次 |
| Github (`github-dpik-top`) | 3 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 422 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **429** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（56 个）。

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
