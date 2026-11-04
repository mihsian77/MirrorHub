# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-11-04T13:58:42Z**，每 6 小时刷新一次。当前 ✅ **495** 在线 / ⚠️ **18** 不稳定 / ⚰️ **56** 已失效归档。

## 核心特性

- **513 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 86ms | Microsoftedge | 0.3 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 91ms | Xjtu-nyxf-study-material | 0.12 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 3 | 92ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 4 | 94ms | Wordpaper | 0.53 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 5 | 98ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 6 | 99ms | Resume-5lv | 0.18 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 7 | 99ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 8 | 100ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 9 | 102ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 10 | 102ms | Linkedin | 0.14 MB/s | `https://linkedin.com` | 通用代理 |
| 11 | 104ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 12 | 106ms | Githubstatus | 0.85 MB/s | `https://githubstatus.com` | 通用代理 |
| 13 | 106ms | Huly-mcp | 0.17 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 14 | 111ms | Kighelper-cloud | 0.04 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 15 | 111ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 16 | 111ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 17 | 111ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 18 | 113ms | Img | - | `https://img.shields.io` | 通用代理 |
| 19 | 113ms | X | 0.97 MB/s | `https://x.com` | 通用代理 |
| 20 | 114ms | Opresume | 0.48 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 21 | 114ms | Tools | 1.54 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 22 | 115ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 23 | 116ms | Dilo-d14 | 0.17 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 24 | 118ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 25 | 118ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 26 | 119ms | Wiki | - | `https://wiki.mozilla.org` | 通用代理 |
| 27 | 120ms | Repsy | 0.12 MB/s | `https://repsy.io` | 通用代理 |
| 28 | 124ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 29 | 125ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 30 | 126ms | Vidocq | 0.18 MB/s | `https://vidocq.dev` | 通用代理 |
| 31 | 127ms | Lawyer-yu | 0.06 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 32 | 127ms | Zebrunner | 1.32 MB/s | `https://zebrunner.com` | 通用代理 |
| 33 | 128ms | Deno | 0.43 MB/s | `https://deno.com` | 通用代理 |
| 34 | 128ms | Openpua | 0.42 MB/s | `https://openpua.ai` | 通用代理 |
| 35 | 128ms | Oreports | - | `https://oreports.com` | 通用代理 |
| 36 | 129ms | Cumora | 0.31 MB/s | `https://cumora.ai` | 通用代理 |
| 37 | 130ms | Impro | 1.44 MB/s | `https://impro.social` | 通用代理 |
| 38 | 130ms | Serac | 0.08 MB/s | `https://serac.build` | 通用代理 |
| 39 | 131ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 40 | 131ms | Fxin | 0.07 MB/s | `https://fxin.cc` | 通用代理 |
| 41 | 132ms | Gh | 1.83 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 42 | 133ms | Impeccable | 0.85 MB/s | `https://impeccable.style` | 通用代理 |
| 43 | 134ms | Github | 1.8 MB/s | `https://github.880824.xyz` | 通用代理 |
| 44 | 135ms | Caiji | 0.08 MB/s | `https://caiji.cyou` | 通用代理 |
| 45 | 135ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 46 | 136ms | App | 0.07 MB/s | `https://app.netlify.com` | 通用代理 |
| 47 | 136ms | Bestdori | 0.09 MB/s | `https://bestdori.com` | 通用代理 |
| 48 | 136ms | Gh | 1.79 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 49 | 136ms | Tokei | 0.42 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 50 | 137ms | Agentlimb | 0.23 MB/s | `https://agentlimb.com` | 通用代理 |
| 51 | 137ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 52 | 137ms | Opensunsama | 0.07 MB/s | `https://opensunsama.com` | 通用代理 |
| 53 | 138ms | Git | 1.84 MB/s | `https://git.820828.xyz` | 通用代理 |
| 54 | 138ms | Github | 1.41 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 55 | 138ms | Opencovibe | 0.38 MB/s | `https://opencovibe.com` | 通用代理 |
| 56 | 138ms | Vibesql | 0.13 MB/s | `https://vibesql.org` | 通用代理 |
| 57 | 139ms | Ghproxy | 0.35 MB/s | `https://ghproxy.cfd` | 通用代理 |
| 58 | 141ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 59 | 141ms | Git | 1.5 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 60 | 141ms | Gitea-mirror | 0.76 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 61 | 143ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 62 | 143ms | Coffeecli | 0.12 MB/s | `https://coffeecli.com` | 通用代理 |
| 63 | 143ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 64 | 143ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 65 | 143ms | Polgarand | 0.09 MB/s | `https://polgarand.org` | 通用代理 |
| 66 | 144ms | Anh | 0.23 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 67 | 144ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 68 | 144ms | L4d2 | 0.13 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 69 | 145ms | Clayrune | 0.15 MB/s | `https://clayrune.io` | 通用代理 |
| 70 | 145ms | Codeeraser | 0.11 MB/s | `https://codeeraser.dev` | 通用代理 |
| 71 | 145ms | Github | 1.72 MB/s | `https://github.788787.xyz` | 通用代理 |
| 72 | 145ms | Gp | 1.88 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 73 | 145ms | Megacrit | 0.11 MB/s | `https://megacrit.com` | 通用代理 |
| 74 | 146ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 75 | 147ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 76 | 148ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 77 | 148ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 78 | 148ms | Openchamber | 1.23 MB/s | `https://openchamber.dev` | 通用代理 |
| 79 | 151ms | Cody | 0.22 MB/s | `https://cody.todyle.com` | 通用代理 |
| 80 | 151ms | Discord | 0.05 MB/s | `https://discord.gg` | 通用代理 |
| 81 | 153ms | Ghproxy | 1.69 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 82 | 153ms | Goreportcard | 0.01 MB/s | `https://goreportcard.com` | 通用代理 |
| 83 | 154ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 84 | 154ms | Docs | 1.57 MB/s | `https://docs.uxway.app` | 通用代理 |
| 85 | 155ms | Components | 0.08 MB/s | `https://components.dereekb.com` | 通用代理 |
| 86 | 155ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 87 | 157ms | Agoramarket | 0.04 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 88 | 157ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 89 | 158ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 90 | 158ms | Glass | 0.19 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 91 | 158ms | Gpui | 0.2 MB/s | `https://gpui.rs` | 通用代理 |
| 92 | 158ms | Opentakeoff | 0.03 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 93 | 159ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 94 | 160ms | Demo | 0.03 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 95 | 160ms | Github | 1.93 MB/s | `https://github.ihnic.com` | 通用代理 |
| 96 | 160ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 97 | 161ms | Cherryai | 0.04 MB/s | `https://cherryai.com` | 通用代理 |
| 98 | 161ms | You | 0.87 MB/s | `https://you.piccalc.com` | 通用代理 |
| 99 | 162ms | Ghproxy | 1.76 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 100 | 162ms | Pidash | 0.04 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 101 | 163ms | Alas | 0.54 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 102 | 163ms | Bestofbi | - | `https://bestofbi.com` | 通用代理 |
| 103 | 164ms | Bananaslides | 0.38 MB/s | `https://bananaslides.online` | 通用代理 |
| 104 | 165ms | Cognitum | 0.19 MB/s | `https://cognitum.one` | 通用代理 |
| 105 | 166ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 106 | 166ms | Game | 0.1 MB/s | `https://game.chozo.net` | 通用代理 |
| 107 | 169ms | Training | 0.11 MB/s | `https://training.ti.com` | 通用代理 |
| 108 | 170ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 109 | 172ms | GH-Proxy | 0.92 MB/s | `https://gh-proxy.com` | 通用代理 |
| 110 | 174ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 111 | 174ms | Eng-3385e | 0.02 MB/s | `https://eng-3385e.firebaseapp.com` | 通用代理 |
| 112 | 178ms | Gh | 1.67 MB/s | `https://gh.404cafe.fun` | 通用代理 |
| 113 | 178ms | Thumb | 0.72 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 114 | 179ms | Cloud | 0.16 MB/s | `https://cloud.google.com` | 通用代理 |
| 115 | 179ms | Docs | 0.04 MB/s | `https://docs.tibco.com` | 通用代理 |
| 116 | 180ms | Eng-3385e | 0.02 MB/s | `https://eng-3385e.web.app` | 通用代理 |
| 117 | 181ms | Bolt2github | 0.02 MB/s | `https://bolt2github.com` | 通用代理 |
| 118 | 182ms | Tvv | 0.91 MB/s | `https://tvv.tw` | 通用代理 |
| 119 | 183ms | Cbrowser | 0.73 MB/s | `https://cbrowser.ai` | 通用代理 |
| 120 | 185ms | GH Monlor | 1.03 MB/s | `https://gh.monlor.com` | 通用代理 |
| 121 | 186ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 122 | 189ms | Ghproxy | 0.83 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 123 | 191ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 124 | 191ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 125 | 192ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 126 | 192ms | Ireasoning | 0.08 MB/s | `https://ireasoning.com` | 通用代理 |
| 127 | 192ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 128 | 193ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 129 | 193ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 130 | 193ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 131 | 194ms | Pnfsoftware | 0.05 MB/s | `https://pnfsoftware.com` | 通用代理 |
| 132 | 195ms | Gh | 0.79 MB/s | `https://gh.padao.fun` | 通用代理 |
| 133 | 196ms | Api | 0.05 MB/s | `https://api.solov.cc` | 通用代理 |
| 134 | 197ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 135 | 199ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 136 | 200ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 137 | 200ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 138 | 200ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 139 | 204ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 140 | 205ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 141 | 205ms | Tms | 0.11 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 142 | 206ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 143 | 207ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 144 | 208ms | Ode | - | `https://ode.fun` | 通用代理 |
| 145 | 209ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 146 | 210ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 147 | 211ms | Nisar | 0.85 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 148 | 212ms | Contrib | 0.29 MB/s | `https://contrib.rocks` | 通用代理 |
| 149 | 213ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 150 | 213ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 151 | 215ms | Tomcat1235 | 0.45 MB/s | `https://tomcat1235.nyc.mn` | 通用代理 |
| 152 | 216ms | Gvsu | - | `https://gvsu.edu` | 通用代理 |
| 153 | 217ms | Aiblackboxfc | 0.22 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 154 | 217ms | Tjf | 0.16 MB/s | `https://tjf.totvs.com.br` | 通用代理 |
| 155 | 219ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 156 | 221ms | Twitter | 0.7 MB/s | `https://twitter.com` | 通用代理 |
| 157 | 223ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 158 | 224ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 159 | 224ms | Kenyu | 1.71 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 160 | 225ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 161 | 226ms | Ampcode | 0.29 MB/s | `https://ampcode.com` | 通用代理 |
| 162 | 229ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 163 | 229ms | Music-cli | 0.16 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 164 | 230ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 165 | 231ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 166 | 232ms | Slack | 0.09 MB/s | `https://slack.kubernetes.io` | 通用代理 |
| 167 | 235ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 168 | 236ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 169 | 237ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 170 | 240ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 171 | 241ms | Ggg | 1.7 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 172 | 241ms | Gh | 1.79 MB/s | `https://gh.1k.ink` | 通用代理 |
| 173 | 241ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 174 | 245ms | GH-Proxy Org | 0.87 MB/s | `https://gh-proxy.org` | 通用代理 |
| 175 | 250ms | CrashMC CDN | 1.14 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 176 | 251ms | Axios-http | 0.23 MB/s | `https://axios-http.com` | 通用代理 |
| 177 | 252ms | Sina | 0.97 MB/s | `https://sina.dev` | 通用代理 |
| 178 | 253ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 179 | 254ms | Tools | 0.05 MB/s | `https://tools.ietf.org` | 通用代理 |
| 180 | 256ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 181 | 257ms | Ghproxy | 0.63 MB/s | `https://ghproxy.vip` | 通用代理 |
| 182 | 258ms | Clypra | 0.04 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 183 | 258ms | Github | 0.89 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 184 | 259ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 185 | 259ms | Visionmemorymcp | 0.27 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 186 | 260ms | Microcoreos | 0.29 MB/s | `https://microcoreos.com` | 通用代理 |
| 187 | 260ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 188 | 261ms | Aka | 0.34 MB/s | `https://aka.ms` | 通用代理 |
| 189 | 264ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 190 | 266ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 191 | 269ms | Congressmcp | 0.01 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 192 | 269ms | FastGit CC | 0.9 MB/s | `https://fastgit.cc` | 通用代理 |
| 193 | 269ms | Ginlix | 0.32 MB/s | `https://ginlix.ai` | 通用代理 |
| 194 | 270ms | Misaligned | 0.56 MB/s | `https://misaligned.top` | 通用代理 |
| 195 | 273ms | Travis-ci | 0.12 MB/s | `https://travis-ci.org` | 通用代理 |
| 196 | 275ms | Kuroutoshikou | 0.54 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 197 | 276ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 198 | 281ms | Radio-browser | 0.01 MB/s | `https://radio-browser.info` | 通用代理 |
| 199 | 283ms | Code | 0.85 MB/s | `https://code.claude.com` | 通用代理 |
| 200 | 287ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 201 | 289ms | Gsd | 0.2 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 202 | 290ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 203 | 291ms | Savannah | 0.03 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 204 | 295ms | Cursor | 0.34 MB/s | `https://cursor.com` | 通用代理 |
| 205 | 295ms | Wandoukj | - | `https://wandoukj.eu.org` | 通用代理 |
| 206 | 299ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 207 | 302ms | Bisguard | - | `https://bisguard.com` | 通用代理 |
| 208 | 307ms | Coreos | 1.0 MB/s | `https://coreos.com` | 通用代理 |
| 209 | 307ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 210 | 309ms | B23 | - | `https://b23.tv` | 通用代理 |
| 211 | 309ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 212 | 309ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 213 | 314ms | Docs | 0.04 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 214 | 315ms | Bailian | 0.04 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 215 | 317ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 216 | 317ms | Ghproxy | 0.64 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 217 | 318ms | Hk | 0.76 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 218 | 318ms | Phabricator | 0.03 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 219 | 319ms | Github | 1.74 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 220 | 319ms | YYLX Git | 0.39 MB/s | `https://git.yylx.win` | 通用代理 |
| 221 | 320ms | Flashtype | - | `https://flashtype.com` | 通用代理 |
| 222 | 321ms | Claude | 0.24 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 223 | 326ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 224 | 328ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 225 | 329ms | Steamcommunity | 0.08 MB/s | `https://steamcommunity.com` | 通用代理 |
| 226 | 329ms | Youtu | 1.26 MB/s | `https://youtu.be` | 通用代理 |
| 227 | 330ms | GHFast | 0.64 MB/s | `https://ghfast.top` | 通用代理 |
| 228 | 334ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 229 | 336ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 230 | 337ms | 30006000 | 0.72 MB/s | `https://30006000.xyz` | 通用代理 |
| 231 | 337ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 232 | 341ms | Gh | 0.71 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 233 | 343ms | Kalix | 0.28 MB/s | `https://kalix.io` | 通用代理 |
| 234 | 344ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 235 | 345ms | Tiktok | 0.08 MB/s | `https://tiktok.com` | 通用代理 |
| 236 | 349ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 237 | 351ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 238 | 353ms | Datamelt | 0.05 MB/s | `https://datamelt.org` | 通用代理 |
| 239 | 353ms | Github | 1.8 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 240 | 353ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 241 | 358ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 242 | 359ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 243 | 361ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 244 | 363ms | GH Nxnow | 0.36 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 245 | 365ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 246 | 366ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 247 | 368ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 248 | 375ms | Open | 0.03 MB/s | `https://open.feishu.cn` | 通用代理 |
| 249 | 377ms | Appdynamics | 0.44 MB/s | `https://appdynamics.com` | 通用代理 |
| 250 | 378ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 251 | 378ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 252 | 379ms | Cfkua | 1.5 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 253 | 379ms | Isi | 0.16 MB/s | `https://isi.edu` | 通用代理 |
| 254 | 379ms | Sonarcloud | 0.1 MB/s | `https://sonarcloud.io` | 通用代理 |
| 255 | 386ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 256 | 386ms | Jonas | - | `https://jonas.ow2.org` | 通用代理 |
| 257 | 387ms | Gradle | - | `https://gradle.org` | 通用代理 |
| 258 | 390ms | Store | 0.84 MB/s | `https://store.steampowered.com` | 通用代理 |
| 259 | 391ms | Gh | 0.69 MB/s | `https://gh.noki.icu` | 通用代理 |
| 260 | 392ms | Docs | 0.61 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 261 | 392ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 262 | 394ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 263 | 396ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 264 | 399ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 265 | 400ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 266 | 400ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 267 | 404ms | Serverkit | 0.04 MB/s | `https://serverkit.ai` | 通用代理 |
| 268 | 404ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 269 | 405ms | Vatrasoft | - | `https://vatrasoft.de` | 通用代理 |
| 270 | 411ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 271 | 411ms | Themolt | 0.01 MB/s | `https://themolt.net` | 通用代理 |
| 272 | 413ms | Github | 1.89 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 273 | 418ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 274 | 418ms | V4 | 1.27 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 275 | 422ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 276 | 422ms | Tridium | 0.25 MB/s | `https://tridium.com` | 通用代理 |
| 277 | 423ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 278 | 423ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 279 | 425ms | Weaverse | 0.42 MB/s | `https://weaverse.io` | 通用代理 |
| 280 | 434ms | SLink | 0.06 MB/s | `https://slink.ltd` | 通用代理 |
| 281 | 435ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 282 | 442ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 283 | 443ms | Core | 0.01 MB/s | `https://core.telegram.org` | 通用代理 |
| 284 | 447ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 285 | 455ms | Tsukuyomi | 0.12 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 286 | 456ms | Easyxls | 0.18 MB/s | `https://easyxls.com` | 通用代理 |
| 287 | 460ms | Code | 0.03 MB/s | `https://code.usgs.gov` | 通用代理 |
| 288 | 460ms | Turborepo-starter-kit-web | 0.04 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 289 | 464ms | Wl | - | `https://wl.do` | 通用代理 |
| 290 | 465ms | Aistudio | 0.93 MB/s | `https://aistudio.google.com` | 通用代理 |
| 291 | 466ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 292 | 469ms | Lucky | 0.49 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 293 | 469ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 294 | 470ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 295 | 473ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 296 | 479ms | Gh | 0.87 MB/s | `https://gh.39.al` | 通用代理 |
| 297 | 480ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 298 | 482ms | Getgit | 1.53 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 299 | 483ms | Ark | 0.55 MB/s | `https://ark.intel.com` | 通用代理 |
| 300 | 483ms | Datomic | 0.02 MB/s | `https://datomic.com` | 通用代理 |
| 301 | 485ms | Agitar | 0.02 MB/s | `https://agitar.com` | 通用代理 |
| 302 | 494ms | Bible-ai-explorer | 0.06 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 303 | 494ms | Hub | 0.32 MB/s | `https://hub.glowp.xyz` | 通用代理 |
| 304 | 505ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 305 | 510ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 306 | 513ms | Godocs | - | `https://godocs.io` | 通用代理 |
| 307 | 516ms | Threadmine | 0.19 MB/s | `https://threadmine.dev` | 通用代理 |
| 308 | 518ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 309 | 528ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 310 | 528ms | Msdn | 0.02 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 311 | 529ms | Support | 0.37 MB/s | `https://support.apple.com` | 通用代理 |
| 312 | 539ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 313 | 542ms | Agentkey | 1.85 MB/s | `https://agentkey.app` | 通用代理 |
| 314 | 543ms | Api | - | `https://api.river.ai` | 通用代理 |
| 315 | 544ms | Libusb-java | 0.02 MB/s | `https://libusb-java.ch` | 通用代理 |
| 316 | 544ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 317 | 544ms | Safedocx | 0.08 MB/s | `https://safedocx.com` | 通用代理 |
| 318 | 548ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 319 | 549ms | Visual-paradigm | 0.41 MB/s | `https://visual-paradigm.com` | 通用代理 |
| 320 | 552ms | Umami-mcp | 1.09 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 321 | 554ms | Patchworkos | 0.29 MB/s | `https://patchworkos.com` | 通用代理 |
| 322 | 557ms | Doc | 0.02 MB/s | `https://doc.sibvisions.com` | 通用代理 |
| 323 | 566ms | Gitlab | 0.01 MB/s | `https://gitlab.pasteur.fr` | 通用代理 |
| 324 | 568ms | Fastfile | 1.46 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 325 | 572ms | Aosmd | 0.11 MB/s | `https://aosmd.com` | 通用代理 |
| 326 | 575ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 327 | 575ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 328 | 578ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 329 | 578ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 330 | 578ms | Vaultproject | 0.14 MB/s | `https://vaultproject.io` | 通用代理 |
| 331 | 588ms | Oapi | - | `https://oapi.dingtalk.com` | 通用代理 |
| 332 | 604ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 333 | 609ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 334 | 612ms | Mt4j | 0.01 MB/s | `https://mt4j.org` | 通用代理 |
| 335 | 619ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 336 | 627ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 337 | 631ms | Github | 0.38 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 338 | 634ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 339 | 636ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 340 | 637ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 341 | 642ms | Mxnet | 0.02 MB/s | `https://mxnet.apache.org` | 通用代理 |
| 342 | 644ms | Gitlab | 0.02 MB/s | `https://gitlab.ow2.org` | 通用代理 |
| 343 | 663ms | Axonivy | 0.28 MB/s | `https://axonivy.com` | 通用代理 |
| 344 | 663ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 345 | 665ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 346 | 683ms | Lecvdemarius | 0.04 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 347 | 685ms | Jpro | - | `https://jpro.one` | 通用代理 |
| 348 | 694ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 349 | 709ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 350 | 714ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 351 | 718ms | Ghproxy | 0.32 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 352 | 724ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 353 | 733ms | Gh | 0.43 MB/s | `https://gh.noki.eu.org` | 通用代理 |
| 354 | 742ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 355 | 758ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 356 | 763ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 357 | 770ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 358 | 772ms | Forgerock | 0.25 MB/s | `https://forgerock.com` | 通用代理 |
| 359 | 772ms | Memstack | 0.03 MB/s | `https://memstack.pro` | 通用代理 |
| 360 | 774ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 361 | 774ms | Paymentcomponents | 0.35 MB/s | `https://paymentcomponents.com` | 通用代理 |
| 362 | 778ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 363 | 783ms | Pulse-commerce | 0.05 MB/s | `https://pulse-commerce.com` | 通用代理 |
| 364 | 794ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 365 | 795ms | Onetwin | 0.01 MB/s | `https://onetwin.cn` | 通用代理 |
| 366 | 813ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 367 | 819ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 368 | 824ms | Datastax | 0.19 MB/s | `https://datastax.com` | 通用代理 |
| 369 | 833ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 370 | 845ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 371 | 852ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 372 | 852ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 373 | 853ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 374 | 864ms | Props | - | `https://props.jodd.org` | 通用代理 |
| 375 | 867ms | Axibase | - | `https://axibase.com` | 通用代理 |
| 376 | 867ms | Docs | - | `https://docs.chartsql.com` | 通用代理 |
| 377 | 873ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 378 | 873ms | Petite | - | `https://petite.jodd.org` | 通用代理 |
| 379 | 875ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 380 | 877ms | Structure101 | 0.35 MB/s | `https://structure101.com` | 通用代理 |
| 381 | 879ms | Groovy-lang | 0.02 MB/s | `https://groovy-lang.org` | 通用代理 |
| 382 | 882ms | Proxetta | - | `https://proxetta.jodd.org` | 通用代理 |
| 383 | 886ms | Yibiao | 0.16 MB/s | `https://yibiao.pro` | 通用代理 |
| 384 | 893ms | Naiveadmin | 0.01 MB/s | `https://naiveadmin.com` | 通用代理 |
| 385 | 895ms | Springboot-generator | 0.04 MB/s | `https://springboot-generator.com` | 通用代理 |
| 386 | 897ms | Dbgate | 0.11 MB/s | `https://dbgate.org` | 通用代理 |
| 387 | 899ms | Eclipse | 0.01 MB/s | `https://eclipse.dev` | 通用代理 |
| 388 | 912ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 389 | 917ms | Dbschema | - | `https://dbschema.com` | 通用代理 |
| 390 | 921ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 391 | 950ms | Invent | 0.01 MB/s | `https://invent.kde.org` | 通用代理 |
| 392 | 950ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 393 | 951ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 394 | 951ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 395 | 953ms | Docs | 0.15 MB/s | `https://docs.transifex.com` | 通用代理 |
| 396 | 955ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 397 | 960ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 398 | 979ms | Ednovas Mirror | 0.78 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 399 | 983ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 400 | 998ms | Sencha | 0.27 MB/s | `https://sencha.com` | 通用代理 |
| 401 | 1003ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 402 | 1009ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 403 | 1011ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 404 | 1015ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 405 | 1015ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 406 | 1019ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 407 | 1019ms | Im | 0.1 MB/s | `https://im.codes` | 通用代理 |
| 408 | 1030ms | Romaframework | 0.02 MB/s | `https://romaframework.org` | 通用代理 |
| 409 | 1034ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 410 | 1034ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 411 | 1038ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 412 | 1040ms | Jfxstore | 0.02 MB/s | `https://jfxstore.com` | 通用代理 |
| 413 | 1059ms | Code | 0.01 MB/s | `https://code.videolan.org` | 通用代理 |
| 414 | 1074ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 415 | 1083ms | Zhuanlan | 0.02 MB/s | `https://zhuanlan.zhihu.com` | 通用代理 |
| 416 | 1104ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 417 | 1116ms | Sanguinesoftwares | 0.12 MB/s | `https://sanguinesoftwares.com` | 通用代理 |
| 418 | 1118ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 419 | 1126ms | Jboltai | 0.08 MB/s | `https://jboltai.com` | 通用代理 |
| 420 | 1128ms | Drjava | 0.08 MB/s | `https://drjava.org` | 通用代理 |
| 421 | 1131ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 422 | 1131ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 423 | 1132ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 424 | 1153ms | Lagarto | - | `https://lagarto.jodd.org` | 通用代理 |
| 425 | 1169ms | Atomcode | 0.09 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 426 | 1169ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 427 | 1172ms | Akiroio | 0.01 MB/s | `https://akiroio.com` | 通用代理 |
| 428 | 1177ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 429 | 1188ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 430 | 1196ms | Oci-pronghorn | - | `https://oci-pronghorn.gitbook.io` | 通用代理 |
| 431 | 1198ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 432 | 1212ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 433 | 1214ms | V | - | `https://v.douyin.com` | 通用代理 |
| 434 | 1231ms | Tech | - | `https://tech.meituan.com` | 通用代理 |
| 435 | 1236ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 436 | 1236ms | Gh | 0.24 MB/s | `https://gh.sixyin.com` | 通用代理 |
| 437 | 1250ms | Ghproxy | 0.3 MB/s | `https://ghproxy.cc` | 通用代理 |
| 438 | 1250ms | Lkkushan | - | `https://lkkushan.gitbook.io` | 通用代理 |
| 439 | 1266ms | Web | - | `https://web.4399.com` | 通用代理 |
| 440 | 1276ms | Cf | 0.23 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 441 | 1288ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 442 | 1292ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 443 | 1297ms | GHProxy Net | 0.02 MB/s | `https://ghproxy.net` | 通用代理 |
| 444 | 1317ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 445 | 1336ms | Gitlab | 0.01 MB/s | `https://gitlab.heigit.org` | 通用代理 |
| 446 | 1363ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 447 | 1363ms | Git | 0.23 MB/s | `https://git.669966.xyz` | 通用代理 |
| 448 | 1373ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 449 | 1406ms | Mdma | 0.03 MB/s | `https://mdma.dev` | 通用代理 |
| 450 | 1439ms | Maplesoft | 0.03 MB/s | `https://maplesoft.com` | 通用代理 |
| 451 | 1444ms | Teambition | 0.06 MB/s | `https://teambition.com` | 通用代理 |
| 452 | 1462ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 453 | 1466ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 454 | 1517ms | Db | - | `https://db.jodd.org` | 通用代理 |
| 455 | 1526ms | Wget | 0.14 MB/s | `https://wget.la` | 通用代理 |
| 456 | 1530ms | Dimagent | 0.24 MB/s | `https://dimagent.com` | 通用代理 |
| 457 | 1582ms | Tmaxsoft | - | `https://tmaxsoft.com` | 通用代理 |
| 458 | 1601ms | Adv | 0.01 MB/s | `https://adv.co.jp` | 通用代理 |
| 459 | 1607ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 460 | 1637ms | Clougence | 0.07 MB/s | `https://clougence.com` | 通用代理 |
| 461 | 1679ms | F2bpm | - | `https://f2bpm.com` | 通用代理 |
| 462 | 1682ms | Heycall-e | 0.1 MB/s | `https://heycall-e.com` | 通用代理 |
| 463 | 1717ms | Gitlab | - | `https://gitlab.phaidra.org` | 通用代理 |
| 464 | 1761ms | Github | 0.03 MB/s | `https://github.chenc.dev` | 通用代理 |
| 465 | 1805ms | Primeton | 0.03 MB/s | `https://primeton.com` | 通用代理 |
| 466 | 1939ms | Dplayer | 0.03 MB/s | `https://dplayer.diandian.com` | 通用代理 |
| 467 | 2117ms | Jahia | 0.04 MB/s | `https://jahia.com` | 通用代理 |
| 468 | 2154ms | My | - | `https://my.oschina.net` | 通用代理 |
| 469 | 2216ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 470 | 2222ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 471 | 2314ms | Infoq | - | `https://infoq.cn` | 通用代理 |
| 472 | 2315ms | Img | - | `https://img.ink` | 通用代理 |
| 473 | 2352ms | Jadasite | 0.03 MB/s | `https://jadasite.com` | 通用代理 |
| 474 | 2425ms | Cs | 0.14 MB/s | `https://cs.waikato.ac.nz` | 通用代理 |
| 475 | 2442ms | Grafana | - | `https://grafana.nav.cloud.nais.io` | 通用代理 |
| 476 | 2493ms | Wiki | - | `https://wiki.wocommunity.org` | 通用代理 |
| 477 | 2596ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 478 | 2607ms | Web | 0.22 MB/s | `https://web.archive.org` | 通用代理 |
| 479 | 2658ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 480 | 2679ms | Visionx | 0.02 MB/s | `https://visionx.sibvisions.com` | 通用代理 |
| 481 | 2703ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 482 | 2754ms | G | 0.1 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 483 | 2768ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 484 | 2787ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 485 | 2844ms | Shopjsp | 0.09 MB/s | `https://shopjsp.com` | 通用代理 |
| 486 | 2913ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 487 | 3106ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 488 | 3243ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 489 | 3269ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 490 | 3313ms | Lightlycode | - | `https://lightlycode.com` | 通用代理 |
| 491 | 3439ms | Informat | 0.01 MB/s | `https://informat.cn` | 通用代理 |
| 492 | 3706ms | Tongtech | - | `https://tongtech.com` | 通用代理 |
| 493 | 5203ms | Developer | 0.03 MB/s | `https://developer.jdcloud.com` | 通用代理 |
| 494 | 5452ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 495 | 6474ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（18 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| Gh (`gh-llkk-cc`) | 16 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Gh (`gh-dpik-top`) | 1 次 |
| Git (`git-tangbai-cc`) | 15 次 |
| Gh (`gh-b52m-cn`) | 19 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |
| Sub (`sub-ikar-eu-org`) | 14 次 |
| Nssurge (`nssurge-com`) | 18 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 18 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 23 次 |
| Leereilly (`leereilly-net`) | 5 次 |
| Adult (`adult-contents-fc2-com`) | 4 次 |
| Free (`free-cn-eu-org`) | 11 次 |
| Proxy (`proxy-scdn-io`) | 9 次 |
| Gh (`gh-ddlc-top`) | 4 次 |
| Github (`github-dpik-top`) | 4 次 |
| 5555 (`5555-cab`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 506 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **513** | |

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
