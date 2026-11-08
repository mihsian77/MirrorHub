# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-11-08T12:55:35Z**，每 6 小时刷新一次。当前 ✅ **507** 在线 / ⚠️ **25** 不稳定 / ⚰️ **60** 已失效归档。

## 核心特性

- **532 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 68ms | Opencode | 0.35 MB/s | `https://opencode.ai` | 通用代理 |
| 2 | 73ms | Crypto-funding-arbitrage | 0.11 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 3 | 76ms | Linkedin | 0.32 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 77ms | Xjtu-nyxf-study-material | 0.22 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 5 | 78ms | Dilo-d14 | 0.32 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 6 | 78ms | Docs | 0.07 MB/s | `https://docs.tibco.com` | 通用代理 |
| 7 | 78ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 8 | 78ms | Microsoftedge | 0.7 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 9 | 82ms | App | 1.76 MB/s | `https://app.snowflake.com` | 通用代理 |
| 10 | 84ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 11 | 86ms | Resume-5lv | 0.29 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 12 | 86ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 13 | 87ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 14 | 87ms | Opresume | 0.71 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 15 | 88ms | Dsh | - | `https://dsh.jiangjiangze.icu` | 通用代理 |
| 16 | 89ms | Kighelper-cloud | 0.13 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 17 | 89ms | X | 1.29 MB/s | `https://x.com` | 通用代理 |
| 18 | 90ms | Img | - | `https://img.shields.io` | 通用代理 |
| 19 | 90ms | Tools | 2.29 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 20 | 93ms | Wordpaper | 0.82 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 21 | 94ms | Docs | 3.0 MB/s | `https://docs.uxway.app` | 通用代理 |
| 22 | 95ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 23 | 96ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 24 | 96ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 25 | 96ms | Huly-mcp | 0.29 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 26 | 98ms | Deno | 0.48 MB/s | `https://deno.com` | 通用代理 |
| 27 | 102ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 28 | 104ms | Bestofbi | - | `https://bestofbi.com` | 通用代理 |
| 29 | 106ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 30 | 107ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 31 | 109ms | Oreports | - | `https://oreports.com` | 通用代理 |
| 32 | 109ms | Wiki | - | `https://wiki.mozilla.org` | 通用代理 |
| 33 | 110ms | Agentlimb | 0.33 MB/s | `https://agentlimb.com` | 通用代理 |
| 34 | 110ms | App | 0.22 MB/s | `https://app.netlify.com` | 通用代理 |
| 35 | 111ms | App | 0.07 MB/s | `https://app.codecov.io` | 通用代理 |
| 36 | 111ms | Cumora | 0.44 MB/s | `https://cumora.ai` | 通用代理 |
| 37 | 112ms | Coffeecli | 0.28 MB/s | `https://coffeecli.com` | 通用代理 |
| 38 | 112ms | Githubstatus | 1.05 MB/s | `https://githubstatus.com` | 通用代理 |
| 39 | 112ms | Godocs | 0.13 MB/s | `https://godocs.io` | 通用代理 |
| 40 | 112ms | Repsy | 0.15 MB/s | `https://repsy.io` | 通用代理 |
| 41 | 113ms | Anh | 0.29 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 42 | 113ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 43 | 113ms | Miaozitie | 0.12 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 44 | 113ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 45 | 114ms | Lawyer-yu | 0.18 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 46 | 114ms | Serac | 0.11 MB/s | `https://serac.build` | 通用代理 |
| 47 | 115ms | Caw | 0.1 MB/s | `https://caw.rocks` | 通用代理 |
| 48 | 116ms | Vidocq | 0.17 MB/s | `https://vidocq.dev` | 通用代理 |
| 49 | 120ms | Cloud | 0.34 MB/s | `https://cloud.google.com` | 通用代理 |
| 50 | 120ms | Freeport | 0.05 MB/s | `https://freeport.network` | 通用代理 |
| 51 | 121ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 52 | 121ms | Eng-3385e | 0.07 MB/s | `https://eng-3385e.firebaseapp.com` | 通用代理 |
| 53 | 121ms | Impro | 2.36 MB/s | `https://impro.social` | 通用代理 |
| 54 | 122ms | Impeccable | 1.39 MB/s | `https://impeccable.style` | 通用代理 |
| 55 | 122ms | Opencovibe | 0.57 MB/s | `https://opencovibe.com` | 通用代理 |
| 56 | 123ms | Gitea-mirror | 1.26 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 57 | 123ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 58 | 124ms | L4d2 | 0.21 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 59 | 124ms | Tokei | 0.57 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 60 | 125ms | Codeeraser | 0.18 MB/s | `https://codeeraser.dev` | 通用代理 |
| 61 | 125ms | Glass | 0.28 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 62 | 125ms | Openchamber | 2.27 MB/s | `https://openchamber.dev` | 通用代理 |
| 63 | 126ms | Gh | 2.36 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 64 | 126ms | Gpui | 0.31 MB/s | `https://gpui.rs` | 通用代理 |
| 65 | 126ms | Openpua | 0.44 MB/s | `https://openpua.ai` | 通用代理 |
| 66 | 127ms | Eng-3385e | 0.08 MB/s | `https://eng-3385e.web.app` | 通用代理 |
| 67 | 127ms | Github | 3.63 MB/s | `https://github.880824.xyz` | 通用代理 |
| 68 | 127ms | You | 1.58 MB/s | `https://you.piccalc.com` | 通用代理 |
| 69 | 128ms | Alas | 0.92 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 70 | 128ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 71 | 128ms | Fxin | 0.1 MB/s | `https://fxin.cc` | 通用代理 |
| 72 | 129ms | Ghproxy | 3.82 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 73 | 129ms | Gp | 3.23 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 74 | 130ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 75 | 130ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 76 | 131ms | Polgarand | 0.13 MB/s | `https://polgarand.org` | 通用代理 |
| 77 | 132ms | Caiji | - | `https://caiji.cyou` | 通用代理 |
| 78 | 132ms | Clayrune | 0.22 MB/s | `https://clayrune.io` | 通用代理 |
| 79 | 132ms | Github | 2.71 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 80 | 132ms | Goreportcard | 0.04 MB/s | `https://goreportcard.com` | 通用代理 |
| 81 | 134ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 82 | 135ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 83 | 135ms | Chops | 0.05 MB/s | `https://chops.md` | 通用代理 |
| 84 | 135ms | Gh | 2.85 MB/s | `https://gh.404cafe.fun` | 通用代理 |
| 85 | 135ms | Git | 3.21 MB/s | `https://git.820828.xyz` | 通用代理 |
| 86 | 136ms | Cody | 0.27 MB/s | `https://cody.todyle.com` | 通用代理 |
| 87 | 136ms | Gh | 2.71 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 88 | 136ms | Zebrunner | 1.61 MB/s | `https://zebrunner.com` | 通用代理 |
| 89 | 137ms | Cognitum | 0.21 MB/s | `https://cognitum.one` | 通用代理 |
| 90 | 137ms | Ghproxy | 0.38 MB/s | `https://ghproxy.cfd` | 通用代理 |
| 91 | 137ms | Vibesql | 0.06 MB/s | `https://vibesql.org` | 通用代理 |
| 92 | 139ms | Demo | 0.05 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 93 | 141ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 94 | 141ms | Play | 0.06 MB/s | `https://play.templatical.com` | 通用代理 |
| 95 | 143ms | Cherryai | 0.03 MB/s | `https://cherryai.com` | 通用代理 |
| 96 | 143ms | Thumb | 3.0 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 97 | 145ms | Ghproxy | 2.65 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 98 | 145ms | Opentakeoff | 0.09 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 99 | 146ms | Github | 2.66 MB/s | `https://github.788787.xyz` | 通用代理 |
| 100 | 147ms | Github | 3.03 MB/s | `https://github.ihnic.com` | 通用代理 |
| 101 | 147ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 102 | 151ms | Bestdori | 0.08 MB/s | `https://bestdori.com` | 通用代理 |
| 103 | 151ms | Git | 3.07 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 104 | 154ms | Ireasoning | 0.07 MB/s | `https://ireasoning.com` | 通用代理 |
| 105 | 155ms | Game | 0.18 MB/s | `https://game.chozo.net` | 通用代理 |
| 106 | 155ms | Osf | 0.07 MB/s | `https://osf.io` | 通用代理 |
| 107 | 156ms | Discord | 0.12 MB/s | `https://discord.gg` | 通用代理 |
| 108 | 157ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 109 | 160ms | GH-Proxy | 1.58 MB/s | `https://gh-proxy.com` | 通用代理 |
| 110 | 162ms | Bolt2github | 0.05 MB/s | `https://bolt2github.com` | 通用代理 |
| 111 | 163ms | Components | 0.16 MB/s | `https://components.dereekb.com` | 通用代理 |
| 112 | 164ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 113 | 165ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 114 | 165ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 115 | 166ms | Tvv | 2.45 MB/s | `https://tvv.tw` | 通用代理 |
| 116 | 170ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 117 | 170ms | Megacrit | 0.12 MB/s | `https://megacrit.com` | 通用代理 |
| 118 | 171ms | Music-cli | 0.48 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 119 | 175ms | Nextup-resource | 0.04 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 120 | 177ms | Microcoreos | 0.55 MB/s | `https://microcoreos.com` | 通用代理 |
| 121 | 178ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 122 | 179ms | Datamelt | 0.08 MB/s | `https://datamelt.org` | 通用代理 |
| 123 | 180ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 124 | 181ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 125 | 183ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 126 | 184ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 127 | 184ms | GH-Proxy Org | 2.86 MB/s | `https://gh-proxy.org` | 通用代理 |
| 128 | 186ms | Twitter | 1.03 MB/s | `https://twitter.com` | 通用代理 |
| 129 | 187ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 130 | 187ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 131 | 188ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 132 | 189ms | Bananaslides | 0.17 MB/s | `https://bananaslides.online` | 通用代理 |
| 133 | 189ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 134 | 190ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 135 | 191ms | Contrib | 0.54 MB/s | `https://contrib.rocks` | 通用代理 |
| 136 | 191ms | Ode | - | `https://ode.fun` | 通用代理 |
| 137 | 191ms | Shiori-v1 | 0.04 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 138 | 192ms | Tools | 0.16 MB/s | `https://tools.ietf.org` | 通用代理 |
| 139 | 192ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 140 | 193ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 141 | 193ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 142 | 194ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 143 | 195ms | Taigi-life-islands | 1.43 MB/s | `https://taigi-life-islands.cjs-1359.chatgpt.site` | 通用代理 |
| 144 | 195ms | Tomcat1235 | 1.08 MB/s | `https://tomcat1235.nyc.mn` | 通用代理 |
| 145 | 196ms | Agoramarket | 0.05 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 146 | 198ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 147 | 200ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 148 | 200ms | Training | 3.05 MB/s | `https://training.ti.com` | 通用代理 |
| 149 | 201ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 150 | 201ms | Ai-trend-publish | 0.04 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 151 | 202ms | Ggg | 3.02 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 152 | 202ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 153 | 204ms | Misaligned | 2.58 MB/s | `https://misaligned.top` | 通用代理 |
| 154 | 204ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 155 | 208ms | Pnfsoftware | 0.03 MB/s | `https://pnfsoftware.com` | 通用代理 |
| 156 | 209ms | Tms | 0.14 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 157 | 210ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 158 | 211ms | CrashMC CDN | 1.53 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 159 | 213ms | Api | 0.15 MB/s | `https://api.solov.cc` | 通用代理 |
| 160 | 213ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 161 | 214ms | Clypra | 0.09 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 162 | 214ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 163 | 217ms | Axios-http | 1.16 MB/s | `https://axios-http.com` | 通用代理 |
| 164 | 220ms | FastGit CC | 1.91 MB/s | `https://fastgit.cc` | 通用代理 |
| 165 | 220ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 166 | 221ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 167 | 221ms | Tjf | 0.21 MB/s | `https://tjf.totvs.com.br` | 通用代理 |
| 168 | 227ms | Kenyu | 2.51 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 169 | 227ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 170 | 228ms | GH Monlor | 1.78 MB/s | `https://gh.monlor.com` | 通用代理 |
| 171 | 228ms | Gvsu | - | `https://gvsu.edu` | 通用代理 |
| 172 | 229ms | Aiblackboxfc | 0.35 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 173 | 229ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 174 | 230ms | Chatgpt | 2.04 MB/s | `https://chatgpt.com` | 通用代理 |
| 175 | 230ms | Slack | 0.23 MB/s | `https://slack.kubernetes.io` | 通用代理 |
| 176 | 233ms | Ginlix | 0.92 MB/s | `https://ginlix.ai` | 通用代理 |
| 177 | 235ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 178 | 236ms | Cdn | 1.72 MB/s | `https://cdn.gh-proxy.org` | 通用代理 |
| 179 | 237ms | Congressmcp | 0.05 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 180 | 237ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 181 | 238ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 182 | 240ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 183 | 240ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 184 | 241ms | Ghproxy | 0.68 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 185 | 241ms | Web4j | - | `https://web4j.com` | 通用代理 |
| 186 | 242ms | Radio-browser | 0.06 MB/s | `https://radio-browser.info` | 通用代理 |
| 187 | 242ms | Travis-ci | 0.34 MB/s | `https://travis-ci.org` | 通用代理 |
| 188 | 243ms | Bisguard | - | `https://bisguard.com` | 通用代理 |
| 189 | 243ms | Nisar | 0.84 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 190 | 245ms | Pulse-commerce | 0.26 MB/s | `https://pulse-commerce.com` | 通用代理 |
| 191 | 248ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 192 | 248ms | Gradle | - | `https://gradle.org` | 通用代理 |
| 193 | 250ms | Claude | 0.44 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 194 | 251ms | Gsd | 0.39 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 195 | 251ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 196 | 255ms | Code | 1.17 MB/s | `https://code.claude.com` | 通用代理 |
| 197 | 255ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 198 | 256ms | Ghproxy | 0.69 MB/s | `https://ghproxy.vip` | 通用代理 |
| 199 | 256ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 200 | 257ms | Gh | 0.58 MB/s | `https://gh.padao.fun` | 通用代理 |
| 201 | 257ms | Zuckerbot | 0.04 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 202 | 258ms | V4 | 2.63 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 203 | 259ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 204 | 259ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 205 | 260ms | Datomic | 0.07 MB/s | `https://datomic.com` | 通用代理 |
| 206 | 261ms | Edgeone | 2.09 MB/s | `https://edgeone.gh-proxy.org` | 通用代理 |
| 207 | 262ms | Hk | 1.37 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 208 | 263ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 209 | 264ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 210 | 264ms | Themolt | 0.06 MB/s | `https://themolt.net` | 通用代理 |
| 211 | 266ms | Aka | 0.78 MB/s | `https://aka.ms` | 通用代理 |
| 212 | 266ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 213 | 267ms | Youtu | 1.89 MB/s | `https://youtu.be` | 通用代理 |
| 214 | 268ms | Coreos | 2.79 MB/s | `https://coreos.com` | 通用代理 |
| 215 | 269ms | Visionmemorymcp | 0.2 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 216 | 270ms | Phabricator | 0.12 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 217 | 272ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 218 | 273ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 219 | 275ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 220 | 277ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 221 | 278ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 222 | 285ms | Ghproxy | 0.45 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 223 | 290ms | Gh | 0.74 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 224 | 290ms | Github | 0.59 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 225 | 292ms | Cursor | 0.79 MB/s | `https://cursor.com` | 通用代理 |
| 226 | 293ms | Sina | 0.72 MB/s | `https://sina.dev` | 通用代理 |
| 227 | 294ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 228 | 294ms | Kalix | 0.42 MB/s | `https://kalix.io` | 通用代理 |
| 229 | 297ms | Agenticcorporation | 0.08 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 230 | 298ms | Aistudio | 2.45 MB/s | `https://aistudio.google.com` | 通用代理 |
| 231 | 299ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 232 | 304ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 233 | 310ms | Lagarto | - | `https://lagarto.jodd.org` | 通用代理 |
| 234 | 310ms | Tiktok | 0.12 MB/s | `https://tiktok.com` | 通用代理 |
| 235 | 312ms | Ipaslogo | - | `https://ipaslogo.com` | 通用代理 |
| 236 | 315ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 237 | 316ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 238 | 317ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 239 | 317ms | Wandoukj | - | `https://wandoukj.eu.org` | 通用代理 |
| 240 | 319ms | Cfkua | 3.05 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 241 | 320ms | Bailian | 0.05 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 242 | 322ms | Db | - | `https://db.jodd.org` | 通用代理 |
| 243 | 322ms | Docs | 0.57 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 244 | 325ms | Props | - | `https://props.jodd.org` | 通用代理 |
| 245 | 329ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 246 | 329ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 247 | 333ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 248 | 334ms | B23 | - | `https://b23.tv` | 通用代理 |
| 249 | 335ms | Erp | 0.01 MB/s | `https://erp.kacon.ai` | 通用代理 |
| 250 | 337ms | Ghproxy | 0.5 MB/s | `https://ghproxy.it` | 通用代理 |
| 251 | 339ms | Github | 3.19 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 252 | 340ms | Savannah | 0.08 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 253 | 341ms | Steamcommunity | 0.1 MB/s | `https://steamcommunity.com` | 通用代理 |
| 254 | 343ms | 30006000 | 0.5 MB/s | `https://30006000.xyz` | 通用代理 |
| 255 | 344ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 256 | 344ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 257 | 352ms | Docs | 0.02 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 258 | 353ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 259 | 353ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 260 | 354ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 261 | 355ms | Agitar | 0.05 MB/s | `https://agitar.com` | 通用代理 |
| 262 | 356ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 263 | 358ms | GHFast | 0.45 MB/s | `https://ghfast.top` | 通用代理 |
| 264 | 360ms | Appdynamics | 0.52 MB/s | `https://appdynamics.com` | 通用代理 |
| 265 | 361ms | Getgit | 3.09 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 266 | 362ms | Docs | - | `https://docs.chartsql.com` | 通用代理 |
| 267 | 362ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 268 | 365ms | Proxetta | - | `https://proxetta.jodd.org` | 通用代理 |
| 269 | 366ms | Ednovas Mirror | 0.45 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 270 | 367ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 271 | 369ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 272 | 372ms | Sonarcloud | 0.16 MB/s | `https://sonarcloud.io` | 通用代理 |
| 273 | 375ms | Store | 1.28 MB/s | `https://store.steampowered.com` | 通用代理 |
| 274 | 379ms | Vatrasoft | - | `https://vatrasoft.de` | 通用代理 |
| 275 | 381ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 276 | 382ms | Agentkey | 0.57 MB/s | `https://agentkey.app` | 通用代理 |
| 277 | 383ms | Weaverse | 0.97 MB/s | `https://weaverse.io` | 通用代理 |
| 278 | 389ms | Gh | 0.66 MB/s | `https://gh.noki.icu` | 通用代理 |
| 279 | 389ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 280 | 391ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 281 | 392ms | Datastax | 0.51 MB/s | `https://datastax.com` | 通用代理 |
| 282 | 394ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 283 | 397ms | Bseindia | 0.04 MB/s | `https://bseindia.com` | 通用代理 |
| 284 | 397ms | Turborepo-starter-kit-web | 0.1 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 285 | 400ms | Core | 0.02 MB/s | `https://core.telegram.org` | 通用代理 |
| 286 | 400ms | Gh | 1.32 MB/s | `https://gh.noki.eu.org` | 通用代理 |
| 287 | 400ms | Petite | - | `https://petite.jodd.org` | 通用代理 |
| 288 | 404ms | Jonas | - | `https://jonas.ow2.org` | 通用代理 |
| 289 | 406ms | App | 0.02 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 290 | 413ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 291 | 417ms | Hub | 0.36 MB/s | `https://hub.glowp.xyz` | 通用代理 |
| 292 | 421ms | Kuroutoshikou | 0.72 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 293 | 421ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 294 | 422ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 295 | 424ms | Forgerock | 0.31 MB/s | `https://forgerock.com` | 通用代理 |
| 296 | 426ms | Github | 2.96 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 297 | 428ms | Msdn | 0.09 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 298 | 435ms | Bible-ai-explorer | 0.08 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 299 | 436ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 300 | 436ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 301 | 437ms | Lucky | 0.65 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 302 | 438ms | Your-domain | 0.04 MB/s | `https://your-domain.com` | 通用代理 |
| 303 | 440ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 304 | 441ms | YYLX Git | 1.93 MB/s | `https://git.yylx.win` | 通用代理 |
| 305 | 447ms | Ark | 0.4 MB/s | `https://ark.intel.com` | 通用代理 |
| 306 | 459ms | Visual-paradigm | 1.46 MB/s | `https://visual-paradigm.com` | 通用代理 |
| 307 | 464ms | Readsync | 0.06 MB/s | `https://readsync.org` | 通用代理 |
| 308 | 474ms | Wl | - | `https://wl.do` | 通用代理 |
| 309 | 475ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 310 | 479ms | Isi | 0.23 MB/s | `https://isi.edu` | 通用代理 |
| 311 | 482ms | Unhaut | - | `https://unhaut.epizy.com` | 通用代理 |
| 312 | 483ms | Threadmine | 0.25 MB/s | `https://threadmine.dev` | 通用代理 |
| 313 | 484ms | Gitlab | 0.02 MB/s | `https://gitlab.ow2.org` | 通用代理 |
| 314 | 489ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 315 | 492ms | Axonivy | 0.47 MB/s | `https://axonivy.com` | 通用代理 |
| 316 | 494ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 317 | 497ms | Libusb-java | 0.03 MB/s | `https://libusb-java.ch` | 通用代理 |
| 318 | 497ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 319 | 503ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 320 | 506ms | Adult | 0.01 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 321 | 508ms | Umami-mcp | 0.55 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 322 | 513ms | Patchworkos | 0.34 MB/s | `https://patchworkos.com` | 通用代理 |
| 323 | 522ms | Lecvdemarius | 0.11 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 324 | 522ms | Vt | 0.69 MB/s | `https://vt.tiktok.com` | 通用代理 |
| 325 | 523ms | Aosmd | 0.27 MB/s | `https://aosmd.com` | 通用代理 |
| 326 | 523ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 327 | 527ms | Doc | 0.03 MB/s | `https://doc.sibvisions.com` | 通用代理 |
| 328 | 528ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 329 | 534ms | Luna | 0.05 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 330 | 535ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 331 | 535ms | Mxnet | 0.04 MB/s | `https://mxnet.apache.org` | 通用代理 |
| 332 | 537ms | Github | 3.52 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 333 | 543ms | Gh | 1.91 MB/s | `https://gh.dpik.top` | 通用代理 |
| 334 | 544ms | Proxy | 0.52 MB/s | `https://proxy.vvvv.ee` | 通用代理 |
| 335 | 545ms | Wiki | - | `https://wiki.easyrpg.org` | 通用代理 |
| 336 | 546ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 337 | 548ms | Vaultproject | 0.23 MB/s | `https://vaultproject.io` | 通用代理 |
| 338 | 550ms | Paymentcomponents | 0.67 MB/s | `https://paymentcomponents.com` | 通用代理 |
| 339 | 553ms | Api | - | `https://api.river.ai` | 通用代理 |
| 340 | 556ms | Safedocx | 0.16 MB/s | `https://safedocx.com` | 通用代理 |
| 341 | 560ms | Mt4j | 0.01 MB/s | `https://mt4j.org` | 通用代理 |
| 342 | 560ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 343 | 562ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 344 | 562ms | Tridium | 0.23 MB/s | `https://tridium.com` | 通用代理 |
| 345 | 563ms | Fastfile | 1.98 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 346 | 565ms | GHProxy Net | 0.02 MB/s | `https://ghproxy.net` | 通用代理 |
| 347 | 568ms | Oapi | - | `https://oapi.dingtalk.com` | 通用代理 |
| 348 | 573ms | Aps | 0.05 MB/s | `https://aps.com` | 通用代理 |
| 349 | 575ms | Lkkushan | - | `https://lkkushan.gitbook.io` | 通用代理 |
| 350 | 584ms | Community | 0.47 MB/s | `https://community.snowflake.com` | 通用代理 |
| 351 | 588ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 352 | 590ms | Easyxls | 0.09 MB/s | `https://easyxls.com` | 通用代理 |
| 353 | 594ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 354 | 597ms | Github | 0.1 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 355 | 614ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 356 | 627ms | Clawbiz | 0.04 MB/s | `https://clawbiz.io` | 通用代理 |
| 357 | 635ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 358 | 637ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 359 | 638ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 360 | 645ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 361 | 649ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 362 | 654ms | Ghproxy | 0.27 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 363 | 669ms | Agoracitizen | 0.03 MB/s | `https://agoracitizen.app` | 通用代理 |
| 364 | 676ms | Jpro | - | `https://jpro.one` | 通用代理 |
| 365 | 677ms | Structure101 | 0.48 MB/s | `https://structure101.com` | 通用代理 |
| 366 | 681ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 367 | 692ms | Support | 0.13 MB/s | `https://support.apple.com` | 通用代理 |
| 368 | 695ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 369 | 697ms | Gh | 1.32 MB/s | `https://gh.sixyin.com` | 通用代理 |
| 370 | 700ms | Groovy-lang | 0.02 MB/s | `https://groovy-lang.org` | 通用代理 |
| 371 | 703ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 372 | 712ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 373 | 712ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 374 | 715ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 375 | 719ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 376 | 729ms | Git | 0.22 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 377 | 734ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 378 | 737ms | Oci-pronghorn | - | `https://oci-pronghorn.gitbook.io` | 通用代理 |
| 379 | 740ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 380 | 741ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 381 | 743ms | Axibase | - | `https://axibase.com` | 通用代理 |
| 382 | 759ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 383 | 768ms | Gh | 0.7 MB/s | `https://gh.39.al` | 通用代理 |
| 384 | 770ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 385 | 780ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 386 | 791ms | Ccgather | 0.05 MB/s | `https://ccgather.com` | 通用代理 |
| 387 | 796ms | Sencha | 0.41 MB/s | `https://sencha.com` | 通用代理 |
| 388 | 800ms | Aif | 0.06 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 389 | 802ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 390 | 803ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 391 | 809ms | Docs | 0.26 MB/s | `https://docs.transifex.com` | 通用代理 |
| 392 | 813ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 393 | 814ms | Springboot-generator | 0.06 MB/s | `https://springboot-generator.com` | 通用代理 |
| 394 | 823ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 395 | 854ms | Eclipse | 0.02 MB/s | `https://eclipse.dev` | 通用代理 |
| 396 | 858ms | Ghproxy | 0.02 MB/s | `https://ghproxy.cn` | 通用代理 |
| 397 | 862ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 398 | 868ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 399 | 876ms | Dbgate | 0.23 MB/s | `https://dbgate.org` | 通用代理 |
| 400 | 884ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 401 | 885ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 402 | 888ms | Maplesoft | 0.11 MB/s | `https://maplesoft.com` | 通用代理 |
| 403 | 892ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 404 | 898ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 405 | 907ms | Zhuanlan | 0.05 MB/s | `https://zhuanlan.zhihu.com` | 通用代理 |
| 406 | 910ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 407 | 918ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 408 | 921ms | Dbschema | - | `https://dbschema.com` | 通用代理 |
| 409 | 922ms | Vulnetix | 0.02 MB/s | `https://vulnetix.com` | 通用代理 |
| 410 | 924ms | Mimo | 0.15 MB/s | `https://mimo.mi.com` | 通用代理 |
| 411 | 932ms | Drjava | 0.08 MB/s | `https://drjava.org` | 通用代理 |
| 412 | 935ms | Code | 0.04 MB/s | `https://code.usgs.gov` | 通用代理 |
| 413 | 937ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 414 | 965ms | Yibiao | 0.11 MB/s | `https://yibiao.pro` | 通用代理 |
| 415 | 979ms | Naiveadmin | - | `https://naiveadmin.com` | 通用代理 |
| 416 | 982ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 417 | 982ms | Dimagent | 0.13 MB/s | `https://dimagent.com` | 通用代理 |
| 418 | 990ms | Honeymeta | 0.03 MB/s | `https://honeymeta.com` | 通用代理 |
| 419 | 990ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 420 | 1003ms | Npmmirror | 0.01 MB/s | `https://npmmirror.com` | 通用代理 |
| 421 | 1004ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 422 | 1004ms | Memstack | 0.04 MB/s | `https://memstack.pro` | 通用代理 |
| 423 | 1004ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 424 | 1006ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 425 | 1013ms | V | - | `https://v.douyin.com` | 通用代理 |
| 426 | 1030ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 427 | 1036ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 428 | 1040ms | Jfxstore | 0.03 MB/s | `https://jfxstore.com` | 通用代理 |
| 429 | 1045ms | Akiroio | 0.01 MB/s | `https://akiroio.com` | 通用代理 |
| 430 | 1075ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 431 | 1075ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 432 | 1080ms | Romaframework | 0.02 MB/s | `https://romaframework.org` | 通用代理 |
| 433 | 1087ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 434 | 1087ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 435 | 1096ms | Doubao | 0.18 MB/s | `https://doubao.com` | 通用代理 |
| 436 | 1099ms | Mdma | 0.05 MB/s | `https://mdma.dev` | 通用代理 |
| 437 | 1101ms | Ghproxy | 0.29 MB/s | `https://ghproxy.cc` | 通用代理 |
| 438 | 1101ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 439 | 1104ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 440 | 1124ms | Web | - | `https://web.4399.com` | 通用代理 |
| 441 | 1136ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 442 | 1152ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 443 | 1154ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 444 | 1156ms | Gitlab | 0.02 MB/s | `https://gitlab.heigit.org` | 通用代理 |
| 445 | 1160ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 446 | 1164ms | Jahia | 0.08 MB/s | `https://jahia.com` | 通用代理 |
| 447 | 1166ms | Sanguinesoftwares | 0.15 MB/s | `https://sanguinesoftwares.com` | 通用代理 |
| 448 | 1174ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 449 | 1176ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 450 | 1222ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 451 | 1250ms | GHFile Geekertao | 1.57 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 452 | 1251ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 453 | 1255ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 454 | 1262ms | Douyin | - | `https://douyin.com` | 通用代理 |
| 455 | 1274ms | Esa | - | `https://esa.console.aliyun.com` | 通用代理 |
| 456 | 1300ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 457 | 1310ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 458 | 1347ms | Jboltai | 0.05 MB/s | `https://jboltai.com` | 通用代理 |
| 459 | 1363ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 460 | 1376ms | Atomcode | 0.04 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 461 | 1379ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 462 | 1389ms | Cf | 0.26 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 463 | 1439ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 464 | 1471ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 465 | 1493ms | Tech | - | `https://tech.meituan.com` | 通用代理 |
| 466 | 1529ms | Heycall-e | 0.23 MB/s | `https://heycall-e.com` | 通用代理 |
| 467 | 1530ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 468 | 1535ms | Git | 0.11 MB/s | `https://git.669966.xyz` | 通用代理 |
| 469 | 1556ms | Gitlab | 0.02 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 470 | 1589ms | Tmaxsoft | - | `https://tmaxsoft.com` | 通用代理 |
| 471 | 1615ms | Jadasite | 0.08 MB/s | `https://jadasite.com` | 通用代理 |
| 472 | 1627ms | Wget | - | `https://wget.la` | 通用代理 |
| 473 | 1674ms | Dplayer | 0.04 MB/s | `https://dplayer.diandian.com` | 通用代理 |
| 474 | 1696ms | Github | 0.11 MB/s | `https://github.chenc.dev` | 通用代理 |
| 475 | 1789ms | Web | 0.07 MB/s | `https://web.archive.org` | 通用代理 |
| 476 | 1825ms | Teambition | 0.08 MB/s | `https://teambition.com` | 通用代理 |
| 477 | 1831ms | 4kf9kfxujfhg2 | 0.01 MB/s | `https://4kf9kfxujfhg2.space.mcode.cn` | 通用代理 |
| 478 | 1989ms | Adv | 0.01 MB/s | `https://adv.co.jp` | 通用代理 |
| 479 | 2077ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 480 | 2112ms | Clougence | 0.01 MB/s | `https://clougence.com` | 通用代理 |
| 481 | 2129ms | Img | - | `https://img.ink` | 通用代理 |
| 482 | 2165ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 483 | 2174ms | Primeton | 0.02 MB/s | `https://primeton.com` | 通用代理 |
| 484 | 2209ms | Grafana | - | `https://grafana.nav.cloud.nais.io` | 通用代理 |
| 485 | 2221ms | F2bpm | - | `https://f2bpm.com` | 通用代理 |
| 486 | 2302ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 487 | 2322ms | My | - | `https://my.oschina.net` | 通用代理 |
| 488 | 2329ms | Provider | - | `https://provider.com` | 通用代理 |
| 489 | 2343ms | Shopjsp | 0.14 MB/s | `https://shopjsp.com` | 通用代理 |
| 490 | 2385ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 491 | 2410ms | Visionx | 0.03 MB/s | `https://visionx.sibvisions.com` | 通用代理 |
| 492 | 2443ms | Cs | 0.11 MB/s | `https://cs.waikato.ac.nz` | 通用代理 |
| 493 | 2506ms | G | 0.12 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 494 | 2553ms | Infoq | - | `https://infoq.cn` | 通用代理 |
| 495 | 2621ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 496 | 2676ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 497 | 2782ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 498 | 2989ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 499 | 3094ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 500 | 3200ms | Wiki | - | `https://wiki.wocommunity.org` | 通用代理 |
| 501 | 3286ms | Informat | 0.01 MB/s | `https://informat.cn` | 通用代理 |
| 502 | 3303ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 503 | 3577ms | Developer | 0.03 MB/s | `https://developer.jdcloud.com` | 通用代理 |
| 504 | 3895ms | Kuaishou | - | `https://kuaishou.com` | 通用代理 |
| 505 | 4476ms | Tongtech | - | `https://tongtech.com` | 通用代理 |
| 506 | 5033ms | Jwebmp | - | `https://jwebmp.com` | 通用代理 |
| 507 | 11411ms | 5555 | 0.01 MB/s | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（25 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Gh (`gh-llkk-cc`) | 27 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Gh (`gh-1k-ink`) | 3 次 |
| Proxy (`proxy-yaoyaoling-net`) | 1 次 |
| Mirror (`mirror-houlang-cloud`) | 2 次 |
| Comfyit (`comfyit-cn`) | 1 次 |
| Ampcode (`ampcode-com`) | 5 次 |
| Sub (`sub-ikar-eu-org`) | 25 次 |
| Cbrowser (`cbrowser-ai`) | 1 次 |
| Flashtype (`flashtype-com`) | 8 次 |
| Im (`im-codes`) | 8 次 |
| Leereilly (`leereilly-net`) | 16 次 |
| Opensunsama (`opensunsama-com`) | 11 次 |
| Vibetrading (`vibetrading-wiki`) | 9 次 |
| Git (`git-net2o-de`) | 11 次 |
| Caiji (`caiji-maotaizy-cc`) | 4 次 |
| Free (`free-cn-eu-org`) | 22 次 |
| Proxy (`proxy-scdn-io`) | 8 次 |
| Gh (`gh-ddlc-top`) | 15 次 |
| Github (`github-dpik-top`) | 15 次 |
| Gitlab (`gitlab-pasteur-fr`) | 11 次 |
| Lightlycode (`lightlycode-com`) | 1 次 |
| 104 (`104-com-tw`) | 7 次 |
| Bsr (`bsr-twse-com-tw`) | 3 次 |
| Mopsov (`mopsov-twse-com-tw`) | 3 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 525 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **532** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（60 个）。

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
