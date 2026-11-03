# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-11-03T13:46:24Z**，每 6 小时刷新一次。当前 ✅ **404** 在线 / ⚠️ **18** 不稳定 / ⚰️ **55** 已失效归档。

## 核心特性

- **422 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 84ms | Microsoftedge | 0.2 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 88ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 91ms | Xjtu-nyxf-study-material | 0.13 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 4 | 92ms | Linkedin | 0.41 MB/s | `https://linkedin.com` | 通用代理 |
| 5 | 94ms | Wordpaper | 0.38 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 6 | 95ms | Resume-5lv | 0.17 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 7 | 100ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 8 | 103ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 9 | 104ms | Crypto-funding-arbitrage | 0.05 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 10 | 105ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 11 | 106ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 12 | 106ms | Githubstatus | 4.13 MB/s | `https://githubstatus.com` | 通用代理 |
| 13 | 107ms | Img | - | `https://img.shields.io` | 通用代理 |
| 14 | 107ms | Tools | 1.86 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 15 | 108ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 16 | 109ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 17 | 110ms | Huly-mcp | 0.14 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 18 | 110ms | X | 1.12 MB/s | `https://x.com` | 通用代理 |
| 19 | 112ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 20 | 113ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 21 | 113ms | Zebrunner | 1.98 MB/s | `https://zebrunner.com` | 通用代理 |
| 22 | 114ms | Opresume | 0.54 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 23 | 116ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 24 | 117ms | Kighelper-cloud | 0.08 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 25 | 120ms | Dilo-d14 | 0.13 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 26 | 121ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 27 | 122ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 28 | 123ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 29 | 124ms | Impeccable | 0.75 MB/s | `https://impeccable.style` | 通用代理 |
| 30 | 126ms | Impro | 1.77 MB/s | `https://impro.social` | 通用代理 |
| 31 | 127ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 32 | 127ms | Godocs | 0.06 MB/s | `https://godocs.io` | 通用代理 |
| 33 | 129ms | Serac | 0.06 MB/s | `https://serac.build` | 通用代理 |
| 34 | 132ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 35 | 132ms | Gh | 1.93 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 36 | 133ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 37 | 134ms | Caiji | 0.06 MB/s | `https://caiji.cyou` | 通用代理 |
| 38 | 134ms | Deno | 0.19 MB/s | `https://deno.com` | 通用代理 |
| 39 | 134ms | Ghproxy | 0.36 MB/s | `https://ghproxy.cfd` | 通用代理 |
| 40 | 135ms | Openpua | 0.32 MB/s | `https://openpua.ai` | 通用代理 |
| 41 | 136ms | Bestdori | 0.13 MB/s | `https://bestdori.com` | 通用代理 |
| 42 | 138ms | Cumora | 0.22 MB/s | `https://cumora.ai` | 通用代理 |
| 43 | 138ms | Github | 1.98 MB/s | `https://github.880824.xyz` | 通用代理 |
| 44 | 138ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 45 | 139ms | Git | 2.06 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 46 | 139ms | Github | 2.49 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 47 | 141ms | App | 0.08 MB/s | `https://app.netlify.com` | 通用代理 |
| 48 | 141ms | Gp | 2.02 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 49 | 142ms | Agentlimb | 0.2 MB/s | `https://agentlimb.com` | 通用代理 |
| 50 | 142ms | Megacrit | 0.21 MB/s | `https://megacrit.com` | 通用代理 |
| 51 | 143ms | Git | 1.84 MB/s | `https://git.820828.xyz` | 通用代理 |
| 52 | 143ms | Miaozitie | 0.07 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 53 | 144ms | Game | 0.11 MB/s | `https://game.chozo.net` | 通用代理 |
| 54 | 144ms | Lawyer-yu | 0.06 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 55 | 144ms | Openchamber | 0.68 MB/s | `https://openchamber.dev` | 通用代理 |
| 56 | 145ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 57 | 145ms | Vibesql | 0.11 MB/s | `https://vibesql.org` | 通用代理 |
| 58 | 146ms | Alas | 0.71 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 59 | 146ms | Anh | 0.13 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 60 | 146ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 61 | 147ms | Codeeraser | 0.05 MB/s | `https://codeeraser.dev` | 通用代理 |
| 62 | 147ms | Gh | 1.65 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 63 | 148ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 64 | 148ms | Gitea-mirror | 0.8 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 65 | 148ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 66 | 149ms | Coffeecli | 0.1 MB/s | `https://coffeecli.com` | 通用代理 |
| 67 | 149ms | Discord | 0.05 MB/s | `https://discord.gg` | 通用代理 |
| 68 | 150ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 69 | 150ms | Github | 1.75 MB/s | `https://github.788787.xyz` | 通用代理 |
| 70 | 151ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 71 | 152ms | Glass | 0.19 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 72 | 152ms | L4d2 | 0.12 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 73 | 152ms | Polgarand | 0.08 MB/s | `https://polgarand.org` | 通用代理 |
| 74 | 153ms | App | 0.02 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 75 | 153ms | Clayrune | 0.09 MB/s | `https://clayrune.io` | 通用代理 |
| 76 | 153ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 77 | 153ms | Opensunsama | 0.12 MB/s | `https://opensunsama.com` | 通用代理 |
| 78 | 154ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 79 | 154ms | Opencovibe | 0.33 MB/s | `https://opencovibe.com` | 通用代理 |
| 80 | 156ms | Cody | 0.2 MB/s | `https://cody.todyle.com` | 通用代理 |
| 81 | 156ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 82 | 158ms | Opentakeoff | 0.03 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 83 | 158ms | Tokei | 0.34 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 84 | 159ms | Api | 0.18 MB/s | `https://api.solov.cc` | 通用代理 |
| 85 | 159ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 86 | 159ms | Gpui | 0.16 MB/s | `https://gpui.rs` | 通用代理 |
| 87 | 160ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 88 | 160ms | Ghproxy | 1.68 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 89 | 160ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 90 | 161ms | Pidash | 0.05 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 91 | 162ms | Components | 0.11 MB/s | `https://components.dereekb.com` | 通用代理 |
| 92 | 163ms | Agoramarket | 0.09 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 93 | 163ms | Play | 0.03 MB/s | `https://play.templatical.com` | 通用代理 |
| 94 | 164ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 95 | 165ms | Github | 2.05 MB/s | `https://github.ihnic.com` | 通用代理 |
| 96 | 166ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 97 | 167ms | Cherryai | 0.02 MB/s | `https://cherryai.com` | 通用代理 |
| 98 | 168ms | Bananaslides | 0.78 MB/s | `https://bananaslides.online` | 通用代理 |
| 99 | 168ms | Demo | 0.02 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 100 | 169ms | Cognitum | 0.16 MB/s | `https://cognitum.one` | 通用代理 |
| 101 | 169ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 102 | 169ms | Music-cli | 0.17 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 103 | 169ms | Training | 0.24 MB/s | `https://training.ti.com` | 通用代理 |
| 104 | 170ms | Chops | 0.02 MB/s | `https://chops.md` | 通用代理 |
| 105 | 170ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 106 | 173ms | Tvv | 2.05 MB/s | `https://tvv.tw` | 通用代理 |
| 107 | 174ms | GH-Proxy | 0.72 MB/s | `https://gh-proxy.com` | 通用代理 |
| 108 | 174ms | Ghproxy | 1.75 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 109 | 178ms | Caw | 0.04 MB/s | `https://caw.rocks` | 通用代理 |
| 110 | 181ms | Bolt2github | 0.01 MB/s | `https://bolt2github.com` | 通用代理 |
| 111 | 182ms | Thumb | 1.01 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 112 | 185ms | Openttd | 0.03 MB/s | `https://openttd.org` | 通用代理 |
| 113 | 185ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 114 | 186ms | Aiblackboxfc | 0.25 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 115 | 186ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 116 | 188ms | Ghproxy | 1.45 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 117 | 188ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 118 | 189ms | You | 0.69 MB/s | `https://you.piccalc.com` | 通用代理 |
| 119 | 193ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 120 | 194ms | Osf | 0.01 MB/s | `https://osf.io` | 通用代理 |
| 121 | 196ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 122 | 196ms | Tms | 0.1 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 123 | 196ms | Tomcat1235 | 0.41 MB/s | `https://tomcat1235.nyc.mn` | 通用代理 |
| 124 | 200ms | Cbrowser | 0.7 MB/s | `https://cbrowser.ai` | 通用代理 |
| 125 | 203ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 126 | 204ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 127 | 206ms | Docs | 1.69 MB/s | `https://docs.uxway.app` | 通用代理 |
| 128 | 206ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 129 | 207ms | Nisar | 1.56 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 130 | 209ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 131 | 210ms | Shiori-v1 | 0.03 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 132 | 211ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 133 | 211ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 134 | 211ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 135 | 212ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 136 | 213ms | Twitter | 0.53 MB/s | `https://twitter.com` | 通用代理 |
| 137 | 214ms | Slack | 0.09 MB/s | `https://slack.kubernetes.io` | 通用代理 |
| 138 | 215ms | Contrib | 0.28 MB/s | `https://contrib.rocks` | 通用代理 |
| 139 | 216ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 140 | 217ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 141 | 218ms | Gh | 2.43 MB/s | `https://gh.1k.ink` | 通用代理 |
| 142 | 219ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 143 | 220ms | Gh | 1.7 MB/s | `https://gh.padao.fun` | 通用代理 |
| 144 | 220ms | Kenyu | 1.93 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 145 | 223ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 146 | 224ms | Paypal | 0.05 MB/s | `https://paypal.com` | 通用代理 |
| 147 | 225ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 148 | 225ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 149 | 225ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 150 | 228ms | Clypra | 0.07 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 151 | 228ms | Ode | - | `https://ode.fun` | 通用代理 |
| 152 | 229ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 153 | 231ms | Github | 1.14 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 154 | 232ms | Ai-trend-publish | 0.03 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 155 | 234ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 156 | 235ms | GH-Proxy Org | 1.06 MB/s | `https://gh-proxy.org` | 通用代理 |
| 157 | 237ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 158 | 238ms | GH Monlor | 1.18 MB/s | `https://gh.monlor.com` | 通用代理 |
| 159 | 238ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 160 | 239ms | Ampcode | 0.23 MB/s | `https://ampcode.com` | 通用代理 |
| 161 | 239ms | FastGit CC | 1.2 MB/s | `https://fastgit.cc` | 通用代理 |
| 162 | 239ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 163 | 241ms | Tools | 0.06 MB/s | `https://tools.ietf.org` | 通用代理 |
| 164 | 244ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 165 | 244ms | Misaligned | 0.47 MB/s | `https://misaligned.top` | 通用代理 |
| 166 | 244ms | Sina | 1.97 MB/s | `https://sina.dev` | 通用代理 |
| 167 | 245ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 168 | 245ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 169 | 252ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 170 | 253ms | CrashMC CDN | 1.14 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 171 | 256ms | Axios-http | 0.32 MB/s | `https://axios-http.com` | 通用代理 |
| 172 | 257ms | Aka | 0.46 MB/s | `https://aka.ms` | 通用代理 |
| 173 | 259ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 174 | 261ms | Microcoreos | 0.31 MB/s | `https://microcoreos.com` | 通用代理 |
| 175 | 261ms | Open | 0.03 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 176 | 262ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 177 | 264ms | Ggg | 1.79 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 178 | 268ms | Travis-ci | 0.14 MB/s | `https://travis-ci.org` | 通用代理 |
| 179 | 269ms | Ginlix | 0.07 MB/s | `https://ginlix.ai` | 通用代理 |
| 180 | 271ms | Code | 1.09 MB/s | `https://code.claude.com` | 通用代理 |
| 181 | 271ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 182 | 271ms | Visionmemorymcp | 0.36 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 183 | 275ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 184 | 275ms | Kuroutoshikou | 2.48 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 185 | 278ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 186 | 279ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 187 | 284ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 188 | 286ms | Savannah | 0.02 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 189 | 286ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 190 | 287ms | Gsd | 0.06 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 191 | 294ms | Cursor | 0.39 MB/s | `https://cursor.com` | 通用代理 |
| 192 | 294ms | GHFast | 2.02 MB/s | `https://ghfast.top` | 通用代理 |
| 193 | 296ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 194 | 299ms | Wandoukj | - | `https://wandoukj.eu.org` | 通用代理 |
| 195 | 300ms | Phabricator | 0.03 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 196 | 307ms | Hk | 0.81 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 197 | 308ms | Steamcommunity | 0.13 MB/s | `https://steamcommunity.com` | 通用代理 |
| 198 | 308ms | Youtu | 1.35 MB/s | `https://youtu.be` | 通用代理 |
| 199 | 309ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 200 | 309ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 201 | 311ms | Getgit | 1.29 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 202 | 311ms | Github | 2.26 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 203 | 311ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 204 | 312ms | Coreos | 1.91 MB/s | `https://coreos.com` | 通用代理 |
| 205 | 312ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 206 | 314ms | 30006000 | 0.6 MB/s | `https://30006000.xyz` | 通用代理 |
| 207 | 316ms | Flashtype | - | `https://flashtype.com` | 通用代理 |
| 208 | 319ms | Docs | 0.12 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 209 | 321ms | B23 | - | `https://b23.tv` | 通用代理 |
| 210 | 322ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 211 | 323ms | Claude | 0.27 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 212 | 328ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 213 | 329ms | Tiktok | 0.13 MB/s | `https://tiktok.com` | 通用代理 |
| 214 | 330ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 215 | 337ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 216 | 337ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 217 | 338ms | Gh | 0.68 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 218 | 338ms | YYLX Git | 0.69 MB/s | `https://git.yylx.win` | 通用代理 |
| 219 | 342ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 220 | 343ms | Agenticcorporation | 0.03 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 221 | 346ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 222 | 347ms | Github | 1.64 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 223 | 350ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 224 | 352ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 225 | 357ms | V4 | 1.53 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 226 | 358ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 227 | 362ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 228 | 363ms | Cfkua | 1.25 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 229 | 364ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 230 | 368ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 231 | 370ms | Sonarcloud | 0.1 MB/s | `https://sonarcloud.io` | 通用代理 |
| 232 | 370ms | Store | 1.43 MB/s | `https://store.steampowered.com` | 通用代理 |
| 233 | 372ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 234 | 375ms | Docs | 0.61 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 235 | 379ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 236 | 382ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 237 | 382ms | Bailian | 0.1 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 238 | 382ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 239 | 385ms | Aps | 0.05 MB/s | `https://aps.com` | 通用代理 |
| 240 | 388ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 241 | 389ms | Im | 0.31 MB/s | `https://im.codes` | 通用代理 |
| 242 | 393ms | Github | 2.12 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 243 | 395ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 244 | 395ms | Turborepo-starter-kit-web | 0.08 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 245 | 395ms | Your-domain | 0.07 MB/s | `https://your-domain.com` | 通用代理 |
| 246 | 397ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 247 | 402ms | Serverkit | 0.01 MB/s | `https://serverkit.ai` | 通用代理 |
| 248 | 404ms | Gh | 0.24 MB/s | `https://gh.noki.icu` | 通用代理 |
| 249 | 405ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 250 | 410ms | Weaverse | 0.51 MB/s | `https://weaverse.io` | 通用代理 |
| 251 | 412ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 252 | 418ms | SLink | 0.09 MB/s | `https://slink.ltd` | 通用代理 |
| 253 | 423ms | GH Nxnow | 0.28 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 254 | 427ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 255 | 431ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 256 | 435ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 257 | 436ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 258 | 443ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 259 | 451ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 260 | 452ms | Codeflying | 0.01 MB/s | `https://codeflying.app` | 通用代理 |
| 261 | 455ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 262 | 458ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 263 | 458ms | Ygdj7 | 0.07 MB/s | `https://ygdj7.com` | 通用代理 |
| 264 | 463ms | Wl | - | `https://wl.do` | 通用代理 |
| 265 | 466ms | Bible-ai-explorer | 0.07 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 266 | 470ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 267 | 472ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 268 | 473ms | Lucky | 0.48 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 269 | 478ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 270 | 493ms | Agentkey | 0.16 MB/s | `https://agentkey.app` | 通用代理 |
| 271 | 497ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 272 | 498ms | Ark | 1.06 MB/s | `https://ark.intel.com` | 通用代理 |
| 273 | 506ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 274 | 509ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 275 | 512ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 276 | 512ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 277 | 517ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 278 | 520ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 279 | 521ms | Bseindia | 0.05 MB/s | `https://bseindia.com` | 通用代理 |
| 280 | 523ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 281 | 528ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 282 | 539ms | Safedocx | 0.11 MB/s | `https://safedocx.com` | 通用代理 |
| 283 | 545ms | Api | - | `https://api.river.ai` | 通用代理 |
| 284 | 548ms | Support | 0.09 MB/s | `https://support.apple.com` | 通用代理 |
| 285 | 556ms | Patchworkos | 0.26 MB/s | `https://patchworkos.com` | 通用代理 |
| 286 | 558ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 287 | 562ms | Gh | 0.12 MB/s | `https://gh.39.al` | 通用代理 |
| 288 | 565ms | Tsukuyomi | 0.08 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 289 | 571ms | Umami-mcp | 0.34 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 290 | 571ms | Vaultproject | 0.18 MB/s | `https://vaultproject.io` | 通用代理 |
| 291 | 576ms | Github | 0.23 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 292 | 579ms | Fastfile | 1.17 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 293 | 586ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 294 | 591ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 295 | 596ms | Aosmd | 0.11 MB/s | `https://aosmd.com` | 通用代理 |
| 296 | 598ms | Oapi | - | `https://oapi.dingtalk.com` | 通用代理 |
| 297 | 610ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 298 | 627ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 299 | 630ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 300 | 639ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 301 | 642ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 302 | 651ms | Ghproxy | 0.3 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 303 | 682ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 304 | 684ms | Lecvdemarius | 0.06 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 305 | 688ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 306 | 689ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 307 | 697ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 308 | 705ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 309 | 705ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 310 | 713ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 311 | 722ms | Onetwin | 0.01 MB/s | `https://onetwin.cn` | 通用代理 |
| 312 | 738ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 313 | 739ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 314 | 739ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 315 | 748ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 316 | 765ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 317 | 768ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 318 | 776ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 319 | 780ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 320 | 798ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 321 | 818ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 322 | 820ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 323 | 821ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 324 | 826ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 325 | 834ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 326 | 848ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 327 | 852ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 328 | 860ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 329 | 866ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 330 | 873ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 331 | 896ms | Ednovas Mirror | 1.31 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 332 | 899ms | Dbgate | 0.12 MB/s | `https://dbgate.org` | 通用代理 |
| 333 | 903ms | Mimo | 0.19 MB/s | `https://mimo.mi.com` | 通用代理 |
| 334 | 903ms | Yibiao | 0.14 MB/s | `https://yibiao.pro` | 通用代理 |
| 335 | 912ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 336 | 929ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 337 | 932ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 338 | 935ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 339 | 935ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 340 | 935ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 341 | 939ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 342 | 951ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 343 | 951ms | Task | 0.02 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 344 | 957ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 345 | 957ms | Docs | 0.15 MB/s | `https://docs.transifex.com` | 通用代理 |
| 346 | 959ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 347 | 966ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 348 | 977ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 349 | 1040ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 350 | 1045ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 351 | 1051ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 352 | 1057ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 353 | 1058ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 354 | 1118ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 355 | 1123ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 356 | 1124ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 357 | 1130ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 358 | 1134ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 359 | 1157ms | Gitlab | 0.01 MB/s | `https://gitlab.heigit.org` | 通用代理 |
| 360 | 1175ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 361 | 1199ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 362 | 1201ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 363 | 1201ms | V | - | `https://v.douyin.com` | 通用代理 |
| 364 | 1202ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 365 | 1203ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 366 | 1227ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 367 | 1228ms | Ghproxy | 0.98 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 368 | 1258ms | Ghproxy | 0.4 MB/s | `https://ghproxy.cc` | 通用代理 |
| 369 | 1270ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 370 | 1271ms | Cf | 0.39 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 371 | 1304ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 372 | 1342ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 373 | 1353ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 374 | 1378ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 375 | 1405ms | Web | - | `https://web.4399.com` | 通用代理 |
| 376 | 1450ms | Gh | 0.3 MB/s | `https://gh.dpik.top` | 通用代理 |
| 377 | 1482ms | Git | 0.53 MB/s | `https://git.669966.xyz` | 通用代理 |
| 378 | 1490ms | Dimagent | 0.04 MB/s | `https://dimagent.com` | 通用代理 |
| 379 | 1495ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 380 | 1501ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 381 | 1525ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 382 | 1593ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 383 | 1595ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 384 | 1673ms | Heycall-e | 0.09 MB/s | `https://heycall-e.com` | 通用代理 |
| 385 | 1808ms | Github | 0.16 MB/s | `https://github.chenc.dev` | 通用代理 |
| 386 | 1911ms | Wget | 0.11 MB/s | `https://wget.la` | 通用代理 |
| 387 | 1952ms | Dplayer | 0.02 MB/s | `https://dplayer.diandian.com` | 通用代理 |
| 388 | 2129ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 389 | 2178ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 390 | 2181ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 391 | 2380ms | Img | - | `https://img.ink` | 通用代理 |
| 392 | 2497ms | G | - | `https://g.blfrp.cn` | 通用代理 |
| 393 | 2668ms | Provider | - | `https://provider.com` | 通用代理 |
| 394 | 2791ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 395 | 2823ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 396 | 2838ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 397 | 2892ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 398 | 2904ms | Web | 0.09 MB/s | `https://web.archive.org` | 通用代理 |
| 399 | 3005ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 400 | 3236ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 401 | 3353ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 402 | 6108ms | Git | - | `https://git.net2o.de` | 通用代理 |
| 403 | 6205ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |
| 404 | 17662ms | 5555 | - | `https://5555.cab` | 通用代理 |


### ⚠️ 不稳定节点（18 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHProxy Net (`ghproxy-net`) | 1 次 |
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| Gh (`gh-llkk-cc`) | 13 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Git (`git-tangbai-cc`) | 12 次 |
| Gh (`gh-b52m-cn`) | 16 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |
| Sub (`sub-ikar-eu-org`) | 11 次 |
| Nssurge (`nssurge-com`) | 15 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 15 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 20 次 |
| Leereilly (`leereilly-net`) | 2 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 26 次 |
| Adult (`adult-contents-fc2-com`) | 1 次 |
| Free (`free-cn-eu-org`) | 8 次 |
| Proxy (`proxy-scdn-io`) | 6 次 |
| Gh (`gh-ddlc-top`) | 1 次 |
| Github (`github-dpik-top`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 415 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **422** | |

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
