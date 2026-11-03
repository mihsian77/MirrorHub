# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-11-03T00:39:02Z**，每 6 小时刷新一次。当前 ✅ **402** 在线 / ⚠️ **18** 不稳定 / ⚰️ **55** 已失效归档。

## 核心特性

- **420 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 80ms | Microsoftedge | 0.87 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 83ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 87ms | Xjtu-nyxf-study-material | 0.21 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 4 | 90ms | Wordpaper | 0.7 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 5 | 94ms | Resume-5lv | 0.22 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 6 | 95ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 7 | 96ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 8 | 99ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 9 | 100ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 10 | 101ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 11 | 102ms | Linkedin | 0.45 MB/s | `https://linkedin.com` | 通用代理 |
| 12 | 102ms | Tools | 3.09 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 13 | 102ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 14 | 103ms | X | 1.83 MB/s | `https://x.com` | 通用代理 |
| 15 | 104ms | Githubstatus | 2.23 MB/s | `https://githubstatus.com` | 通用代理 |
| 16 | 104ms | Huly-mcp | 0.2 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 17 | 104ms | Img | - | `https://img.shields.io` | 通用代理 |
| 18 | 105ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 19 | 107ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 20 | 109ms | Opresume | 0.45 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 21 | 112ms | Zebrunner | 2.75 MB/s | `https://zebrunner.com` | 通用代理 |
| 22 | 115ms | Kighelper-cloud | 0.11 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 23 | 116ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 24 | 117ms | Caiji | 0.06 MB/s | `https://caiji.cyou` | 通用代理 |
| 25 | 117ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 26 | 119ms | Dilo-d14 | 0.22 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 27 | 119ms | Impeccable | 1.42 MB/s | `https://impeccable.style` | 通用代理 |
| 28 | 120ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 29 | 120ms | Godocs | 0.13 MB/s | `https://godocs.io` | 通用代理 |
| 30 | 120ms | Serac | 0.07 MB/s | `https://serac.build` | 通用代理 |
| 31 | 121ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 32 | 122ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 33 | 124ms | Impro | 2.0 MB/s | `https://impro.social` | 通用代理 |
| 34 | 125ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 35 | 127ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 36 | 129ms | App | 0.08 MB/s | `https://app.codecov.io` | 通用代理 |
| 37 | 129ms | Cumora | 0.37 MB/s | `https://cumora.ai` | 通用代理 |
| 38 | 130ms | App | 0.21 MB/s | `https://app.netlify.com` | 通用代理 |
| 39 | 130ms | Gh | 1.54 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 40 | 130ms | Git | 1.94 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 41 | 132ms | Game | 0.14 MB/s | `https://game.chozo.net` | 通用代理 |
| 42 | 132ms | Github | 1.24 MB/s | `https://github.880824.xyz` | 通用代理 |
| 43 | 132ms | Openpua | 0.55 MB/s | `https://openpua.ai` | 通用代理 |
| 44 | 133ms | Bestdori | 0.11 MB/s | `https://bestdori.com` | 通用代理 |
| 45 | 133ms | Git | 2.44 MB/s | `https://git.820828.xyz` | 通用代理 |
| 46 | 133ms | Github | 1.87 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 47 | 134ms | Agentlimb | 0.21 MB/s | `https://agentlimb.com` | 通用代理 |
| 48 | 134ms | Gp | 1.28 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 49 | 135ms | Ghproxy | 0.25 MB/s | `https://ghproxy.cfd` | 通用代理 |
| 50 | 135ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 51 | 136ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 52 | 137ms | Deno | 0.5 MB/s | `https://deno.com` | 通用代理 |
| 53 | 137ms | Lawyer-yu | 0.21 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 54 | 137ms | Miaozitie | 0.09 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 55 | 139ms | Alas | 0.9 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 56 | 139ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 57 | 139ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 58 | 140ms | Codeeraser | 0.12 MB/s | `https://codeeraser.dev` | 通用代理 |
| 59 | 142ms | Gh | 2.42 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 60 | 143ms | Anh | 0.23 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 61 | 143ms | Gitea-mirror | 0.87 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 62 | 143ms | Openchamber | 0.73 MB/s | `https://openchamber.dev` | 通用代理 |
| 63 | 144ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 64 | 145ms | Clayrune | 0.09 MB/s | `https://clayrune.io` | 通用代理 |
| 65 | 145ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 66 | 145ms | Glass | 0.23 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 67 | 145ms | Polgarand | 0.09 MB/s | `https://polgarand.org` | 通用代理 |
| 68 | 145ms | Vibesql | 0.12 MB/s | `https://vibesql.org` | 通用代理 |
| 69 | 146ms | Cody | 0.17 MB/s | `https://cody.todyle.com` | 通用代理 |
| 70 | 147ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 71 | 147ms | Github | 2.61 MB/s | `https://github.788787.xyz` | 通用代理 |
| 72 | 147ms | Megacrit | 0.08 MB/s | `https://megacrit.com` | 通用代理 |
| 73 | 148ms | Coffeecli | 0.1 MB/s | `https://coffeecli.com` | 通用代理 |
| 74 | 148ms | L4d2 | 0.17 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 75 | 150ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 76 | 150ms | Discord | 0.11 MB/s | `https://discord.gg` | 通用代理 |
| 77 | 150ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 78 | 150ms | Goreportcard | 0.06 MB/s | `https://goreportcard.com` | 通用代理 |
| 79 | 151ms | Api | 0.07 MB/s | `https://api.solov.cc` | 通用代理 |
| 80 | 151ms | App | 0.02 MB/s | `https://app.opencastor.com` | 通用代理 |
| 81 | 151ms | Gpui | 0.23 MB/s | `https://gpui.rs` | 通用代理 |
| 82 | 153ms | Tokei | 0.46 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 83 | 154ms | Opensunsama | 0.08 MB/s | `https://opensunsama.com` | 通用代理 |
| 84 | 155ms | Opentakeoff | 0.08 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 85 | 156ms | Ghproxy | 2.55 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 86 | 156ms | Opencovibe | 0.39 MB/s | `https://opencovibe.com` | 通用代理 |
| 87 | 156ms | Pidash | 0.02 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 88 | 156ms | Play | 0.03 MB/s | `https://play.templatical.com` | 通用代理 |
| 89 | 157ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 90 | 157ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 91 | 157ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 92 | 158ms | Github | 2.22 MB/s | `https://github.ihnic.com` | 通用代理 |
| 93 | 159ms | Cherryai | 0.05 MB/s | `https://cherryai.com` | 通用代理 |
| 94 | 160ms | Components | 0.07 MB/s | `https://components.dereekb.com` | 通用代理 |
| 95 | 160ms | Demo | 0.03 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 96 | 164ms | Agoramarket | 0.03 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 97 | 164ms | Bananaslides | 0.26 MB/s | `https://bananaslides.online` | 通用代理 |
| 98 | 165ms | Music-cli | 0.47 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 99 | 166ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 100 | 167ms | Tvv | 1.65 MB/s | `https://tvv.tw` | 通用代理 |
| 101 | 168ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 102 | 169ms | Thumb | 0.5 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 103 | 169ms | Training | 0.31 MB/s | `https://training.ti.com` | 通用代理 |
| 104 | 171ms | Ghproxy | 1.7 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 105 | 173ms | Chops | 0.02 MB/s | `https://chops.md` | 通用代理 |
| 106 | 173ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 107 | 174ms | Caw | 0.07 MB/s | `https://caw.rocks` | 通用代理 |
| 108 | 175ms | GH-Proxy | 1.54 MB/s | `https://gh-proxy.com` | 通用代理 |
| 109 | 176ms | Cognitum | 0.18 MB/s | `https://cognitum.one` | 通用代理 |
| 110 | 177ms | Bolt2github | 0.1 MB/s | `https://bolt2github.com` | 通用代理 |
| 111 | 181ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 112 | 182ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 113 | 182ms | Slack | 0.13 MB/s | `https://slack.kubernetes.io` | 通用代理 |
| 114 | 183ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 115 | 187ms | Tomcat1235 | 0.6 MB/s | `https://tomcat1235.nyc.mn` | 通用代理 |
| 116 | 189ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 117 | 189ms | Ghproxy | 0.62 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 118 | 191ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 119 | 192ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 120 | 194ms | Misaligned | 2.33 MB/s | `https://misaligned.top` | 通用代理 |
| 121 | 197ms | Osf | 0.03 MB/s | `https://osf.io` | 通用代理 |
| 122 | 199ms | Tms | 0.18 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 123 | 200ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 124 | 201ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 125 | 202ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 126 | 203ms | Aiblackboxfc | 0.29 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 127 | 203ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 128 | 204ms | Twitter | 1.16 MB/s | `https://twitter.com` | 通用代理 |
| 129 | 204ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 130 | 205ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 131 | 206ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 132 | 206ms | Shiori-v1 | 0.05 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 133 | 207ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 134 | 207ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 135 | 207ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 136 | 207ms | Nisar | 0.86 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 137 | 208ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 138 | 209ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 139 | 210ms | Contrib | 0.3 MB/s | `https://contrib.rocks` | 通用代理 |
| 140 | 211ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 141 | 211ms | GH-Proxy Org | 1.28 MB/s | `https://gh-proxy.org` | 通用代理 |
| 142 | 214ms | Kenyu | 2.59 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 143 | 215ms | Cbrowser | 1.02 MB/s | `https://cbrowser.ai` | 通用代理 |
| 144 | 215ms | Gh | 1.54 MB/s | `https://gh.1k.ink` | 通用代理 |
| 145 | 216ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 146 | 217ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 147 | 219ms | Gh | 0.63 MB/s | `https://gh.padao.fun` | 通用代理 |
| 148 | 220ms | Ai-trend-publish | 0.04 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 149 | 222ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 150 | 222ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 151 | 222ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 152 | 223ms | Docs | 1.38 MB/s | `https://docs.uxway.app` | 通用代理 |
| 153 | 223ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 154 | 229ms | Clypra | 0.1 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 155 | 229ms | Ode | - | `https://ode.fun` | 通用代理 |
| 156 | 229ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 157 | 229ms | Tools | 0.16 MB/s | `https://tools.ietf.org` | 通用代理 |
| 158 | 232ms | GH Monlor | 1.43 MB/s | `https://gh.monlor.com` | 通用代理 |
| 159 | 233ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 160 | 239ms | Ampcode | 0.37 MB/s | `https://ampcode.com` | 通用代理 |
| 161 | 239ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 162 | 240ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 163 | 241ms | FastGit CC | 1.65 MB/s | `https://fastgit.cc` | 通用代理 |
| 164 | 241ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 165 | 242ms | CrashMC CDN | 1.57 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 166 | 242ms | Github | 0.53 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 167 | 242ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 168 | 245ms | Sina | 0.57 MB/s | `https://sina.dev` | 通用代理 |
| 169 | 247ms | Axios-http | 1.27 MB/s | `https://axios-http.com` | 通用代理 |
| 170 | 248ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 171 | 250ms | Microcoreos | 0.3 MB/s | `https://microcoreos.com` | 通用代理 |
| 172 | 252ms | Ginlix | 0.52 MB/s | `https://ginlix.ai` | 通用代理 |
| 173 | 256ms | Ggg | 1.85 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 174 | 258ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 175 | 259ms | Aka | 0.42 MB/s | `https://aka.ms` | 通用代理 |
| 176 | 263ms | Code | 1.89 MB/s | `https://code.claude.com` | 通用代理 |
| 177 | 263ms | Visionmemorymcp | 0.21 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 178 | 266ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 179 | 267ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 180 | 268ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 181 | 268ms | Radio-browser | 0.08 MB/s | `https://radio-browser.info` | 通用代理 |
| 182 | 269ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 183 | 269ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 184 | 271ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 185 | 275ms | GHFast | 0.52 MB/s | `https://ghfast.top` | 通用代理 |
| 186 | 275ms | Kuroutoshikou | 0.11 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 187 | 275ms | Travis-ci | 0.3 MB/s | `https://travis-ci.org` | 通用代理 |
| 188 | 280ms | Wings | 0.05 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 189 | 281ms | Gsd | 0.36 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 190 | 281ms | Savannah | 0.08 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 191 | 287ms | Cursor | 1.06 MB/s | `https://cursor.com` | 通用代理 |
| 192 | 288ms | Themolt | 0.05 MB/s | `https://themolt.net` | 通用代理 |
| 193 | 290ms | Getgit | 1.34 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 194 | 290ms | Github | 1.77 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 195 | 300ms | Hk | 0.46 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 196 | 303ms | Steamcommunity | 0.16 MB/s | `https://steamcommunity.com` | 通用代理 |
| 197 | 304ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 198 | 308ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 199 | 308ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 200 | 308ms | Wandoukj | - | `https://wandoukj.eu.org` | 通用代理 |
| 201 | 309ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 202 | 309ms | You | 1.04 MB/s | `https://you.piccalc.com` | 通用代理 |
| 203 | 310ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 204 | 313ms | 30006000 | 0.49 MB/s | `https://30006000.xyz` | 通用代理 |
| 205 | 316ms | Coreos | 2.76 MB/s | `https://coreos.com` | 通用代理 |
| 206 | 317ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 207 | 317ms | Docs | 0.03 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 208 | 318ms | Claude | 0.35 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 209 | 320ms | Tiktok | 0.12 MB/s | `https://tiktok.com` | 通用代理 |
| 210 | 320ms | V4 | 1.95 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 211 | 322ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 212 | 324ms | B23 | - | `https://b23.tv` | 通用代理 |
| 213 | 324ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 214 | 328ms | Agenticcorporation | 0.08 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 215 | 329ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 216 | 331ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 217 | 335ms | Github | 3.23 MB/s | `https://github.dpik.top` | 通用代理 |
| 218 | 340ms | Cfkua | 1.93 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 219 | 340ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 220 | 341ms | Gh | 0.73 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 221 | 344ms | Bailian | 0.05 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 222 | 344ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 223 | 346ms | Github | 1.67 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 224 | 349ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 225 | 357ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 226 | 357ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 227 | 359ms | Store | 1.55 MB/s | `https://store.steampowered.com` | 通用代理 |
| 228 | 361ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 229 | 361ms | Docs | 0.76 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 230 | 362ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 231 | 363ms | YYLX Git | 1.55 MB/s | `https://git.yylx.win` | 通用代理 |
| 232 | 365ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 233 | 372ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 234 | 374ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 235 | 382ms | Im | 0.57 MB/s | `https://im.codes` | 通用代理 |
| 236 | 383ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 237 | 388ms | Sonarcloud | 0.15 MB/s | `https://sonarcloud.io` | 通用代理 |
| 238 | 390ms | Turborepo-starter-kit-web | 0.11 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 239 | 391ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 240 | 393ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 241 | 394ms | Gh | 0.69 MB/s | `https://gh.noki.icu` | 通用代理 |
| 242 | 394ms | Your-domain | 0.04 MB/s | `https://your-domain.com` | 通用代理 |
| 243 | 395ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 244 | 398ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 245 | 400ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 246 | 403ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 247 | 405ms | GH Nxnow | 0.48 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 248 | 406ms | Github | 1.39 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 249 | 409ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 250 | 425ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 251 | 426ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 252 | 429ms | Agentkey | 0.73 MB/s | `https://agentkey.app` | 通用代理 |
| 253 | 431ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 254 | 432ms | Weaverse | 0.81 MB/s | `https://weaverse.io` | 通用代理 |
| 255 | 437ms | App | 0.02 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 256 | 440ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 257 | 442ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 258 | 445ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 259 | 446ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 260 | 448ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 261 | 448ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 262 | 453ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 263 | 454ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 264 | 461ms | Bible-ai-explorer | 0.09 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 265 | 463ms | Wl | - | `https://wl.do` | 通用代理 |
| 266 | 475ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 267 | 475ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 268 | 477ms | Lucky | 0.68 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 269 | 480ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 270 | 484ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 271 | 495ms | Msdn | 0.08 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 272 | 501ms | Adult | 0.01 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 273 | 501ms | Easyboardgame | 0.02 MB/s | `https://easyboardgame.top` | 通用代理 |
| 274 | 501ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 275 | 504ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 276 | 506ms | Ark | 0.47 MB/s | `https://ark.intel.com` | 通用代理 |
| 277 | 508ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 278 | 512ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 279 | 513ms | Bseindia | 0.05 MB/s | `https://bseindia.com` | 通用代理 |
| 280 | 515ms | Gh | 1.14 MB/s | `https://gh.idayer.com` | 通用代理 |
| 281 | 517ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 282 | 529ms | Safedocx | 0.16 MB/s | `https://safedocx.com` | 通用代理 |
| 283 | 541ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 284 | 544ms | Api | - | `https://api.river.ai` | 通用代理 |
| 285 | 545ms | Oapi | - | `https://oapi.dingtalk.com` | 通用代理 |
| 286 | 553ms | Tsukuyomi | 0.11 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 287 | 555ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 288 | 560ms | Patchworkos | 0.35 MB/s | `https://patchworkos.com` | 通用代理 |
| 289 | 563ms | Support | 0.12 MB/s | `https://support.apple.com` | 通用代理 |
| 290 | 565ms | Fastfile | 1.62 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 291 | 571ms | Umami-mcp | 0.49 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 292 | 576ms | Vaultproject | 0.3 MB/s | `https://vaultproject.io` | 通用代理 |
| 293 | 581ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 294 | 582ms | Github | 0.25 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 295 | 586ms | Gh | 0.5 MB/s | `https://gh.39.al` | 通用代理 |
| 296 | 595ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 297 | 599ms | Aosmd | 0.15 MB/s | `https://aosmd.com` | 通用代理 |
| 298 | 615ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 299 | 618ms | 3d-set-visualizer | 0.05 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 300 | 623ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 301 | 626ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 302 | 639ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 303 | 644ms | Ghproxy | 0.26 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 304 | 665ms | Lecvdemarius | 0.1 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 305 | 676ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 306 | 686ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 307 | 694ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 308 | 702ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 309 | 706ms | Memstack | 0.03 MB/s | `https://memstack.pro` | 通用代理 |
| 310 | 707ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 311 | 710ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 312 | 735ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 313 | 738ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 314 | 739ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 315 | 743ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 316 | 755ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 317 | 756ms | Agoracitizen | 0.03 MB/s | `https://agoracitizen.app` | 通用代理 |
| 318 | 759ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 319 | 776ms | Gh | 0.53 MB/s | `https://gh.ddlc.top` | 通用代理 |
| 320 | 789ms | Clawbiz | 0.05 MB/s | `https://clawbiz.io` | 通用代理 |
| 321 | 806ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 322 | 806ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 323 | 813ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 324 | 823ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 325 | 829ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 326 | 831ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 327 | 833ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 328 | 855ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 329 | 875ms | Aif | 0.06 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 330 | 877ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 331 | 899ms | Yibiao | 0.11 MB/s | `https://yibiao.pro` | 通用代理 |
| 332 | 900ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 333 | 902ms | Mimo | 0.16 MB/s | `https://mimo.mi.com` | 通用代理 |
| 334 | 909ms | Internhack | 0.05 MB/s | `https://internhack.xyz` | 通用代理 |
| 335 | 915ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 336 | 919ms | Ednovas Mirror | 0.58 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 337 | 920ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 338 | 923ms | Dbgate | 0.22 MB/s | `https://dbgate.org` | 通用代理 |
| 339 | 927ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 340 | 931ms | Docs | 0.32 MB/s | `https://docs.transifex.com` | 通用代理 |
| 341 | 935ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 342 | 942ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 343 | 945ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 344 | 946ms | Ccgather | 0.07 MB/s | `https://ccgather.com` | 通用代理 |
| 345 | 948ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 346 | 950ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 347 | 982ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 348 | 985ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 349 | 1002ms | Dimagent | 0.13 MB/s | `https://dimagent.com` | 通用代理 |
| 350 | 1037ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 351 | 1041ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 352 | 1042ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 353 | 1046ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 354 | 1052ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 355 | 1070ms | Ghproxy | 0.27 MB/s | `https://ghproxy.cc` | 通用代理 |
| 356 | 1099ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 357 | 1112ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 358 | 1133ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 359 | 1146ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 360 | 1169ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 361 | 1183ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 362 | 1184ms | Code | 0.03 MB/s | `https://code.videolan.org` | 通用代理 |
| 363 | 1193ms | GHFile Geekertao | 0.09 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 364 | 1194ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 365 | 1197ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 366 | 1200ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 367 | 1204ms | V | - | `https://v.douyin.com` | 通用代理 |
| 368 | 1218ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 369 | 1222ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 370 | 1242ms | Esa | - | `https://esa.console.aliyun.com` | 通用代理 |
| 371 | 1276ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 372 | 1277ms | Ghproxy | 0.38 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 373 | 1286ms | Cf | 0.26 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 374 | 1326ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 375 | 1387ms | Web | - | `https://web.4399.com` | 通用代理 |
| 376 | 1395ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 377 | 1442ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 378 | 1448ms | Gh | 0.96 MB/s | `https://gh.dpik.top` | 通用代理 |
| 379 | 1503ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 380 | 1521ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 381 | 1582ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 382 | 1614ms | Gitlab | - | `https://gitlab.phaidra.org` | 通用代理 |
| 383 | 1647ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 384 | 1807ms | Github | 0.15 MB/s | `https://github.chenc.dev` | 通用代理 |
| 385 | 1857ms | Dplayer | 0.03 MB/s | `https://dplayer.diandian.com` | 通用代理 |
| 386 | 1906ms | GHProxy Net | 0.27 MB/s | `https://ghproxy.net` | 通用代理 |
| 387 | 1912ms | Wget | 0.16 MB/s | `https://wget.la` | 通用代理 |
| 388 | 2062ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 389 | 2184ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 390 | 2215ms | Img | - | `https://img.ink` | 通用代理 |
| 391 | 2289ms | G | 0.08 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 392 | 2482ms | Provider | - | `https://provider.com` | 通用代理 |
| 393 | 2607ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 394 | 2755ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 395 | 2818ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 396 | 2896ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 397 | 2936ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 398 | 2950ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 399 | 3138ms | Web | - | `https://web.archive.org` | 通用代理 |
| 400 | 3355ms | GHProxy MonkeyRay | 0.1 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 401 | 5606ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 402 | 6176ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（18 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GitClone (`gitclone-com`) | 7 次 |
| Gh (`gh-llkk-cc`) | 12 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Git (`git-tangbai-cc`) | 11 次 |
| Gh (`gh-b52m-cn`) | 15 次 |
| Semantic-release (`semantic-release-gitbook-io`) | 1 次 |
| Sub (`sub-ikar-eu-org`) | 10 次 |
| Nssurge (`nssurge-com`) | 14 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 14 次 |
| Axonhub (`axonhub-onrender-com`) | 2 次 |
| Flashtype (`flashtype-com`) | 6 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 19 次 |
| Leereilly (`leereilly-net`) | 1 次 |
| Youtu (`youtu-be`) | 1 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 25 次 |
| Free (`free-cn-eu-org`) | 7 次 |
| Doc (`doc-libsodium-org`) | 1 次 |
| Proxy (`proxy-scdn-io`) | 5 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 413 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **420** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（55 个）。

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
