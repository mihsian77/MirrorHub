# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-11-02T14:54:28Z**，每 6 小时刷新一次。当前 ✅ **398** 在线 / ⚠️ **20** 不稳定 / ⚰️ **54** 已失效归档。

## 核心特性

- **418 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 71ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 2 | 79ms | Microsoftedge | 0.2 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 82ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 4 | 90ms | Xjtu-nyxf-study-material | 0.17 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 5 | 94ms | Resume-5lv | 0.18 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 6 | 94ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 7 | 95ms | Wordpaper | 0.5 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 8 | 98ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 9 | 98ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 10 | 100ms | Githubstatus | 0.87 MB/s | `https://githubstatus.com` | 通用代理 |
| 11 | 101ms | Crypto-funding-arbitrage | 0.06 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 12 | 102ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 13 | 102ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 14 | 102ms | Linkedin | 0.14 MB/s | `https://linkedin.com` | 通用代理 |
| 15 | 102ms | Tools | 1.28 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 16 | 102ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 17 | 103ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 18 | 105ms | Huly-mcp | 0.07 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 19 | 105ms | Img | - | `https://img.shields.io` | 通用代理 |
| 20 | 106ms | Opresume | 0.35 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 21 | 106ms | X | 0.98 MB/s | `https://x.com` | 通用代理 |
| 22 | 111ms | Zebrunner | 1.15 MB/s | `https://zebrunner.com` | 通用代理 |
| 23 | 114ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 24 | 116ms | Ghproxy | 0.29 MB/s | `https://ghproxy.cfd` | 通用代理 |
| 25 | 117ms | Caiji | 0.09 MB/s | `https://caiji.cyou` | 通用代理 |
| 26 | 117ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 27 | 117ms | Kighelper-cloud | 0.08 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 28 | 117ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 29 | 119ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 30 | 119ms | Serac | 0.09 MB/s | `https://serac.build` | 通用代理 |
| 31 | 120ms | Impeccable | 0.9 MB/s | `https://impeccable.style` | 通用代理 |
| 32 | 122ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 33 | 123ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 34 | 124ms | Impro | 1.33 MB/s | `https://impro.social` | 通用代理 |
| 35 | 125ms | Game | 0.11 MB/s | `https://game.chozo.net` | 通用代理 |
| 36 | 125ms | Git | 2.25 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 37 | 125ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 38 | 125ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 39 | 126ms | Bestdori | 0.09 MB/s | `https://bestdori.com` | 通用代理 |
| 40 | 126ms | Dilo-d14 | 0.12 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 41 | 127ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 42 | 127ms | Github | 2.01 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 43 | 129ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 44 | 130ms | App | 0.11 MB/s | `https://app.netlify.com` | 通用代理 |
| 45 | 131ms | Gh | 1.87 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 46 | 131ms | Git | 2.16 MB/s | `https://git.820828.xyz` | 通用代理 |
| 47 | 133ms | Github | 2.12 MB/s | `https://github.880824.xyz` | 通用代理 |
| 48 | 133ms | Megacrit | 0.16 MB/s | `https://megacrit.com` | 通用代理 |
| 49 | 134ms | Cumora | 0.35 MB/s | `https://cumora.ai` | 通用代理 |
| 50 | 134ms | Deno | 0.63 MB/s | `https://deno.com` | 通用代理 |
| 51 | 134ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 52 | 135ms | Agentlimb | 0.24 MB/s | `https://agentlimb.com` | 通用代理 |
| 53 | 135ms | Gp | 2.11 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 54 | 136ms | Openpua | 0.5 MB/s | `https://openpua.ai` | 通用代理 |
| 55 | 137ms | Api | 0.12 MB/s | `https://api.solov.cc` | 通用代理 |
| 56 | 138ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 57 | 138ms | Lawyer-yu | 0.02 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 58 | 139ms | Codeeraser | 0.14 MB/s | `https://codeeraser.dev` | 通用代理 |
| 59 | 139ms | Gitea-mirror | 0.71 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 60 | 139ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 61 | 140ms | Anh | 0.23 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 62 | 140ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 63 | 142ms | Alas | 0.63 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 64 | 143ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 65 | 144ms | Gh | 2.01 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 66 | 144ms | Polgarand | 0.1 MB/s | `https://polgarand.org` | 通用代理 |
| 67 | 145ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 68 | 145ms | Vibesql | 0.13 MB/s | `https://vibesql.org` | 通用代理 |
| 69 | 146ms | Openchamber | 0.66 MB/s | `https://openchamber.dev` | 通用代理 |
| 70 | 147ms | Cody | 0.23 MB/s | `https://cody.todyle.com` | 通用代理 |
| 71 | 147ms | Github | 1.88 MB/s | `https://github.788787.xyz` | 通用代理 |
| 72 | 148ms | L4d2 | 0.16 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 73 | 149ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 74 | 149ms | Clayrune | 0.17 MB/s | `https://clayrune.io` | 通用代理 |
| 75 | 149ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 76 | 150ms | Coffeecli | 0.16 MB/s | `https://coffeecli.com` | 通用代理 |
| 77 | 150ms | Discord | 0.06 MB/s | `https://discord.gg` | 通用代理 |
| 78 | 150ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 79 | 151ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 80 | 151ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 81 | 152ms | Glass | 0.24 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 82 | 152ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 83 | 152ms | Gpui | 0.21 MB/s | `https://gpui.rs` | 通用代理 |
| 84 | 153ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 85 | 153ms | Cherryai | 0.04 MB/s | `https://cherryai.com` | 通用代理 |
| 86 | 154ms | Components | 0.07 MB/s | `https://components.dereekb.com` | 通用代理 |
| 87 | 154ms | Github | 1.96 MB/s | `https://github.ihnic.com` | 通用代理 |
| 88 | 154ms | Opensunsama | 0.04 MB/s | `https://opensunsama.com` | 通用代理 |
| 89 | 154ms | Opentakeoff | 0.03 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 90 | 154ms | Play | 0.05 MB/s | `https://play.templatical.com` | 通用代理 |
| 91 | 155ms | Ghproxy | 2.07 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 92 | 155ms | Opencovibe | 0.45 MB/s | `https://opencovibe.com` | 通用代理 |
| 93 | 156ms | Tokei | 0.52 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 94 | 159ms | Demo | 0.03 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 95 | 159ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 96 | 163ms | Training | 0.15 MB/s | `https://training.ti.com` | 通用代理 |
| 97 | 163ms | Tvv | 1.85 MB/s | `https://tvv.tw` | 通用代理 |
| 98 | 164ms | Agoramarket | 0.05 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 99 | 165ms | Bananaslides | 0.43 MB/s | `https://bananaslides.online` | 通用代理 |
| 100 | 165ms | Music-cli | 0.15 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 101 | 166ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 102 | 167ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 103 | 171ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 104 | 171ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 105 | 171ms | Thumb | 1.07 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 106 | 172ms | Ghproxy | 1.95 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 107 | 173ms | Caw | 0.07 MB/s | `https://caw.rocks` | 通用代理 |
| 108 | 173ms | GH-Proxy | 0.98 MB/s | `https://gh-proxy.com` | 通用代理 |
| 109 | 175ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 110 | 177ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 111 | 178ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 112 | 179ms | Cognitum | 0.18 MB/s | `https://cognitum.one` | 通用代理 |
| 113 | 181ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 114 | 182ms | Ghproxy | 0.82 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 115 | 183ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 116 | 186ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 117 | 187ms | Osf | 0.03 MB/s | `https://osf.io` | 通用代理 |
| 118 | 188ms | Misaligned | 0.75 MB/s | `https://misaligned.top` | 通用代理 |
| 119 | 195ms | Tomcat1235 | 0.72 MB/s | `https://tomcat1235.nyc.mn` | 通用代理 |
| 120 | 196ms | Aiblackboxfc | 0.32 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 121 | 198ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 122 | 199ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 123 | 199ms | GH-Proxy Org | 0.83 MB/s | `https://gh-proxy.org` | 通用代理 |
| 124 | 201ms | Shiori-v1 | 0.01 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 125 | 202ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 126 | 203ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 127 | 204ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 128 | 204ms | Gh | 2.13 MB/s | `https://gh.1k.ink` | 通用代理 |
| 129 | 204ms | Tms | 0.14 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 130 | 204ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 131 | 206ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 132 | 206ms | Twitter | 0.74 MB/s | `https://twitter.com` | 通用代理 |
| 133 | 207ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 134 | 207ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 135 | 208ms | Contrib | 0.14 MB/s | `https://contrib.rocks` | 通用代理 |
| 136 | 208ms | Nisar | 0.82 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 137 | 209ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 138 | 210ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 139 | 210ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 140 | 213ms | Cbrowser | 1.63 MB/s | `https://cbrowser.ai` | 通用代理 |
| 141 | 213ms | Gh | 0.58 MB/s | `https://gh.padao.fun` | 通用代理 |
| 142 | 214ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 143 | 215ms | Clypra | 0.05 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 144 | 215ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 145 | 215ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 146 | 216ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 147 | 216ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 148 | 216ms | Slack | 0.12 MB/s | `https://slack.kubernetes.io` | 通用代理 |
| 149 | 218ms | Kenyu | 1.66 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 150 | 220ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 151 | 220ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 152 | 220ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 153 | 221ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 154 | 221ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 155 | 222ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 156 | 228ms | Ode | - | `https://ode.fun` | 通用代理 |
| 157 | 228ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 158 | 228ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 159 | 230ms | GH Monlor | 0.88 MB/s | `https://gh.monlor.com` | 通用代理 |
| 160 | 232ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 161 | 236ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 162 | 237ms | Ggg | 1.89 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 163 | 237ms | Github | 0.72 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 164 | 238ms | CrashMC CDN | 0.9 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 165 | 240ms | Sina | 0.78 MB/s | `https://sina.dev` | 通用代理 |
| 166 | 244ms | Ampcode | 0.13 MB/s | `https://ampcode.com` | 通用代理 |
| 167 | 245ms | Axios-http | 0.3 MB/s | `https://axios-http.com` | 通用代理 |
| 168 | 247ms | Microcoreos | 0.36 MB/s | `https://microcoreos.com` | 通用代理 |
| 169 | 247ms | Tools | 0.07 MB/s | `https://tools.ietf.org` | 通用代理 |
| 170 | 252ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 171 | 255ms | Ginlix | 0.42 MB/s | `https://ginlix.ai` | 通用代理 |
| 172 | 256ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 173 | 258ms | Visionmemorymcp | 0.2 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 174 | 259ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 175 | 263ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 176 | 264ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 177 | 264ms | Kuroutoshikou | 0.1 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 178 | 266ms | FastGit CC | 0.77 MB/s | `https://fastgit.cc` | 通用代理 |
| 179 | 268ms | GHFast | 0.67 MB/s | `https://ghfast.top` | 通用代理 |
| 180 | 268ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 181 | 269ms | Getgit | 2.14 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 182 | 270ms | Code | 1.28 MB/s | `https://code.claude.com` | 通用代理 |
| 183 | 270ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 184 | 270ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 185 | 271ms | Aka | 0.32 MB/s | `https://aka.ms` | 通用代理 |
| 186 | 276ms | Travis-ci | 0.16 MB/s | `https://travis-ci.org` | 通用代理 |
| 187 | 280ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 188 | 282ms | Gsd | 0.27 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 189 | 284ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 190 | 286ms | Hk | 0.84 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 191 | 289ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 192 | 291ms | Savannah | 0.03 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 193 | 292ms | Cursor | 0.45 MB/s | `https://cursor.com` | 通用代理 |
| 194 | 292ms | Wandoukj | - | `https://wandoukj.eu.org` | 通用代理 |
| 195 | 293ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 196 | 295ms | Github | 2.31 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 197 | 299ms | Docs | 0.05 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 198 | 301ms | Youtu | 1.25 MB/s | `https://youtu.be` | 通用代理 |
| 199 | 305ms | Steamcommunity | 0.07 MB/s | `https://steamcommunity.com` | 通用代理 |
| 200 | 308ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 201 | 309ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 202 | 310ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 203 | 310ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 204 | 311ms | B23 | - | `https://b23.tv` | 通用代理 |
| 205 | 313ms | Claude | 0.29 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 206 | 313ms | Tiktok | 0.08 MB/s | `https://tiktok.com` | 通用代理 |
| 207 | 314ms | 30006000 | 0.76 MB/s | `https://30006000.xyz` | 通用代理 |
| 208 | 317ms | Coreos | 1.4 MB/s | `https://coreos.com` | 通用代理 |
| 209 | 317ms | V4 | 1.05 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 210 | 323ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 211 | 327ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 212 | 327ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 213 | 331ms | Cfkua | 1.78 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 214 | 331ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 215 | 331ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 216 | 339ms | Gh | 0.86 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 217 | 341ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 218 | 343ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 219 | 344ms | Store | 0.79 MB/s | `https://store.steampowered.com` | 通用代理 |
| 220 | 346ms | Github | 2.11 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 221 | 347ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 222 | 348ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 223 | 354ms | Bailian | 0.06 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 224 | 359ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 225 | 360ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 226 | 365ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 227 | 365ms | Docs | 0.6 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 228 | 369ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 229 | 370ms | YYLX Git | 0.69 MB/s | `https://git.yylx.win` | 通用代理 |
| 230 | 370ms | You | 0.86 MB/s | `https://you.piccalc.com` | 通用代理 |
| 231 | 372ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 232 | 380ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 233 | 381ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 234 | 384ms | Im | 0.98 MB/s | `https://im.codes` | 通用代理 |
| 235 | 386ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 236 | 387ms | Sonarcloud | 0.49 MB/s | `https://sonarcloud.io` | 通用代理 |
| 237 | 391ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 238 | 393ms | Serverkit | 0.04 MB/s | `https://serverkit.ai` | 通用代理 |
| 239 | 393ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 240 | 394ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 241 | 396ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 242 | 396ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 243 | 397ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 244 | 399ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 245 | 399ms | Github | 2.19 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 246 | 405ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 247 | 414ms | GH Nxnow | 0.41 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 248 | 418ms | Agentkey | 0.14 MB/s | `https://agentkey.app` | 通用代理 |
| 249 | 419ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 250 | 427ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 251 | 428ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 252 | 429ms | Weaverse | 0.59 MB/s | `https://weaverse.io` | 通用代理 |
| 253 | 437ms | Gh | 0.65 MB/s | `https://gh.noki.icu` | 通用代理 |
| 254 | 438ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 255 | 439ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 256 | 442ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 257 | 445ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 258 | 448ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 259 | 450ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 260 | 450ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 261 | 456ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 262 | 457ms | Bible-ai-explorer | 0.05 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 263 | 457ms | Wl | - | `https://wl.do` | 通用代理 |
| 264 | 462ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 265 | 472ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 266 | 475ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 267 | 476ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 268 | 476ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 269 | 478ms | Lucky | 0.52 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 270 | 488ms | Msdn | 0.02 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 271 | 489ms | Ark | 0.4 MB/s | `https://ark.intel.com` | 通用代理 |
| 272 | 503ms | Easyboardgame | 0.01 MB/s | `https://easyboardgame.top` | 通用代理 |
| 273 | 503ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 274 | 513ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 275 | 513ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 276 | 515ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 277 | 517ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 278 | 518ms | Bseindia | 0.02 MB/s | `https://bseindia.com` | 通用代理 |
| 279 | 522ms | Safedocx | 0.08 MB/s | `https://safedocx.com` | 通用代理 |
| 280 | 527ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 281 | 543ms | Api | - | `https://api.river.ai` | 通用代理 |
| 282 | 543ms | Support | 0.36 MB/s | `https://support.apple.com` | 通用代理 |
| 283 | 555ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 284 | 556ms | Patchworkos | 0.3 MB/s | `https://patchworkos.com` | 通用代理 |
| 285 | 557ms | Oapi | - | `https://oapi.dingtalk.com` | 通用代理 |
| 286 | 565ms | Github | 0.33 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 287 | 568ms | Umami-mcp | 1.28 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 288 | 581ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 289 | 588ms | Fastfile | 1.57 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 290 | 591ms | Vaultproject | 0.17 MB/s | `https://vaultproject.io` | 通用代理 |
| 291 | 593ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 292 | 602ms | 3d-set-visualizer | 0.01 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 293 | 608ms | Aosmd | 0.15 MB/s | `https://aosmd.com` | 通用代理 |
| 294 | 618ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 295 | 618ms | Gh | 0.57 MB/s | `https://gh.39.al` | 通用代理 |
| 296 | 623ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 297 | 626ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 298 | 641ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 299 | 659ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 300 | 664ms | Ghproxy | 0.26 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 301 | 669ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 302 | 678ms | Lecvdemarius | 0.03 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 303 | 685ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 304 | 690ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 305 | 694ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 306 | 695ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 307 | 718ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 308 | 721ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 309 | 723ms | Onetwin | 0.01 MB/s | `https://onetwin.cn` | 通用代理 |
| 310 | 725ms | Os | 0.09 MB/s | `https://os.ryo.lu` | 通用代理 |
| 311 | 726ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 312 | 752ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 313 | 758ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 314 | 763ms | Clawbiz | 0.02 MB/s | `https://clawbiz.io` | 通用代理 |
| 315 | 764ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 316 | 786ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 317 | 802ms | Kw-aigc | - | `https://kw-aigc.cn` | 通用代理 |
| 318 | 806ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 319 | 808ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 320 | 813ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 321 | 815ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 322 | 829ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 323 | 834ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 324 | 837ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 325 | 870ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 326 | 874ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 327 | 876ms | Aif | 0.05 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 328 | 877ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 329 | 898ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 330 | 900ms | Yibiao | 0.13 MB/s | `https://yibiao.pro` | 通用代理 |
| 331 | 902ms | Ccgather | 0.07 MB/s | `https://ccgather.com` | 通用代理 |
| 332 | 905ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 333 | 906ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 334 | 921ms | Dbgate | 0.12 MB/s | `https://dbgate.org` | 通用代理 |
| 335 | 923ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 336 | 930ms | Docs | 0.18 MB/s | `https://docs.transifex.com` | 通用代理 |
| 337 | 937ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 338 | 938ms | Honeymeta | - | `https://honeymeta.com` | 通用代理 |
| 339 | 946ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 340 | 950ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 341 | 963ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 342 | 965ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 343 | 990ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 344 | 1015ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 345 | 1049ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 346 | 1067ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 347 | 1072ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 348 | 1073ms | Ghproxy | 0.26 MB/s | `https://ghproxy.cc` | 通用代理 |
| 349 | 1081ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 350 | 1099ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 351 | 1106ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 352 | 1107ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 353 | 1128ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 354 | 1145ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 355 | 1163ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 356 | 1171ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 357 | 1180ms | Atomcode | 0.05 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 358 | 1193ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 359 | 1202ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 360 | 1213ms | V | - | `https://v.douyin.com` | 通用代理 |
| 361 | 1217ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 362 | 1218ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 363 | 1233ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 364 | 1234ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 365 | 1253ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 366 | 1283ms | Cf | 0.27 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 367 | 1294ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 368 | 1312ms | Web | - | `https://web.4399.com` | 通用代理 |
| 369 | 1335ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 370 | 1410ms | Ghproxy | 0.51 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 371 | 1416ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 372 | 1436ms | Git | 0.29 MB/s | `https://git.669966.xyz` | 通用代理 |
| 373 | 1449ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 374 | 1514ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 375 | 1546ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 376 | 1579ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 377 | 1596ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 378 | 1667ms | Heycall-e | 0.1 MB/s | `https://heycall-e.com` | 通用代理 |
| 379 | 1754ms | Gh | 0.35 MB/s | `https://gh.dpik.top` | 通用代理 |
| 380 | 1812ms | Github | 0.01 MB/s | `https://github.chenc.dev` | 通用代理 |
| 381 | 1859ms | G | 0.22 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 382 | 1911ms | Dplayer | 0.04 MB/s | `https://dplayer.diandian.com` | 通用代理 |
| 383 | 1913ms | Wget | 0.15 MB/s | `https://wget.la` | 通用代理 |
| 384 | 2153ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 385 | 2182ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 386 | 2265ms | Img | - | `https://img.ink` | 通用代理 |
| 387 | 2466ms | GHProxy Net | 0.02 MB/s | `https://ghproxy.net` | 通用代理 |
| 388 | 2652ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 389 | 2714ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 390 | 2795ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 391 | 2802ms | Web | 0.1 MB/s | `https://web.archive.org` | 通用代理 |
| 392 | 2824ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 393 | 2964ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 394 | 2969ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 395 | 2998ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 396 | 3363ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 397 | 5656ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 398 | 6310ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（20 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Ednovas Mirror (`github-ednovas-xyz`) | 1 次 |
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 27 次 |
| GitClone (`gitclone-com`) | 6 次 |
| Gh (`gh-llkk-cc`) | 11 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Git (`git-tangbai-cc`) | 10 次 |
| Gh (`gh-b52m-cn`) | 14 次 |
| Proxy (`proxy-vvvv-ee`) | 2 次 |
| Sub (`sub-ikar-eu-org`) | 9 次 |
| Nssurge (`nssurge-com`) | 13 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 13 次 |
| Axonhub (`axonhub-onrender-com`) | 1 次 |
| Flashtype (`flashtype-com`) | 5 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 18 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 24 次 |
| Adult (`adult-contents-fc2-com`) | 10 次 |
| Dimagent (`dimagent-com`) | 1 次 |
| Free (`free-cn-eu-org`) | 6 次 |
| Proxy (`proxy-scdn-io`) | 4 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 411 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **418** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（54 个）。

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
