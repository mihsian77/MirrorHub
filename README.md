# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-31T16:56:50Z**，每 6 小时刷新一次。当前 ✅ **388** 在线 / ⚠️ **22** 不稳定 / ⚰️ **53** 已失效归档。

## 核心特性

- **410 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 75ms | Microsoftedge | 0.64 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 84ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 88ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 4 | 88ms | Linkedin | 0.09 MB/s | `https://linkedin.com` | 通用代理 |
| 5 | 91ms | Githubstatus | 1.13 MB/s | `https://githubstatus.com` | 通用代理 |
| 6 | 99ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 7 | 100ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 8 | 101ms | Crypto-funding-arbitrage | 0.06 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 9 | 101ms | Wordpaper | 0.5 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 10 | 101ms | X | 1.24 MB/s | `https://x.com` | 通用代理 |
| 11 | 102ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 12 | 103ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 13 | 104ms | Huly-mcp | 0.17 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 14 | 104ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 15 | 105ms | Zebrunner | 1.59 MB/s | `https://zebrunner.com` | 通用代理 |
| 16 | 106ms | App | 0.1 MB/s | `https://app.netlify.com` | 通用代理 |
| 17 | 106ms | Resume-5lv | 0.1 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 18 | 107ms | Xjtu-nyxf-study-material | 0.13 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 19 | 108ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 20 | 108ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 21 | 108ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 22 | 109ms | Godocs | 0.03 MB/s | `https://godocs.io` | 通用代理 |
| 23 | 110ms | Tools | 1.81 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 24 | 115ms | Lawyer-yu | 0.07 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 25 | 118ms | Kighelper-cloud | 0.05 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 26 | 119ms | Deno | 0.81 MB/s | `https://deno.com` | 通用代理 |
| 27 | 121ms | Opresume | 0.48 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 28 | 123ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 29 | 123ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 30 | 123ms | Impeccable | 0.69 MB/s | `https://impeccable.style` | 通用代理 |
| 31 | 125ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 32 | 127ms | Dilo-d14 | 0.14 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 33 | 129ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 34 | 130ms | Openchamber | 0.56 MB/s | `https://openchamber.dev` | 通用代理 |
| 35 | 136ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 36 | 140ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 37 | 140ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 38 | 141ms | Components | 0.08 MB/s | `https://components.dereekb.com` | 通用代理 |
| 39 | 142ms | Megacrit | 0.08 MB/s | `https://megacrit.com` | 通用代理 |
| 40 | 143ms | Music-cli | 0.19 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 41 | 146ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 42 | 148ms | Training | 0.16 MB/s | `https://training.ti.com` | 通用代理 |
| 43 | 149ms | Img | - | `https://img.shields.io` | 通用代理 |
| 44 | 151ms | Discord | 0.06 MB/s | `https://discord.gg` | 通用代理 |
| 45 | 152ms | Serac | 0.06 MB/s | `https://serac.build` | 通用代理 |
| 46 | 152ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 47 | 153ms | Opensunsama | 0.04 MB/s | `https://opensunsama.com` | 通用代理 |
| 48 | 155ms | Cumora | 0.22 MB/s | `https://cumora.ai` | 通用代理 |
| 49 | 156ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 50 | 158ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 51 | 158ms | Git | 1.73 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 52 | 158ms | Gp | 2.09 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 53 | 159ms | Codeeraser | 0.09 MB/s | `https://codeeraser.dev` | 通用代理 |
| 54 | 164ms | Git | 1.82 MB/s | `https://git.820828.xyz` | 通用代理 |
| 55 | 164ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 56 | 164ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 57 | 165ms | Github | 2.04 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 58 | 165ms | Impro | 1.22 MB/s | `https://impro.social` | 通用代理 |
| 59 | 165ms | Openpua | 0.34 MB/s | `https://openpua.ai` | 通用代理 |
| 60 | 166ms | Gh | 1.69 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 61 | 168ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 62 | 168ms | Caiji | - | `https://caiji.cyou` | 通用代理 |
| 63 | 169ms | Gitea-mirror | 0.6 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 64 | 170ms | Gpui | 0.17 MB/s | `https://gpui.rs` | 通用代理 |
| 65 | 170ms | Osf | 0.03 MB/s | `https://osf.io` | 通用代理 |
| 66 | 170ms | Vibesql | 0.11 MB/s | `https://vibesql.org` | 通用代理 |
| 67 | 171ms | Gh | 1.72 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 68 | 171ms | Ghproxy | 1.83 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 69 | 171ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 70 | 171ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 71 | 172ms | Anh | 0.17 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 72 | 173ms | Bestdori | 0.07 MB/s | `https://bestdori.com` | 通用代理 |
| 73 | 173ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 74 | 173ms | Github | 2.16 MB/s | `https://github.788787.xyz` | 通用代理 |
| 75 | 176ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 76 | 176ms | L4d2 | 0.12 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 77 | 176ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 78 | 177ms | Agentlimb | 0.12 MB/s | `https://agentlimb.com` | 通用代理 |
| 79 | 177ms | Glass | 0.15 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 80 | 177ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 81 | 179ms | Cody | 0.19 MB/s | `https://cody.todyle.com` | 通用代理 |
| 82 | 179ms | GH-Proxy | 0.82 MB/s | `https://gh-proxy.com` | 通用代理 |
| 83 | 180ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 84 | 180ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 85 | 180ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 86 | 181ms | App | 0.02 MB/s | `https://app.opencastor.com` | 通用代理 |
| 87 | 183ms | Tokei | 0.4 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 88 | 184ms | Chops | 0.02 MB/s | `https://chops.md` | 通用代理 |
| 89 | 184ms | Github | 1.81 MB/s | `https://github.880824.xyz` | 通用代理 |
| 90 | 184ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 91 | 184ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 92 | 185ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 93 | 185ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 94 | 185ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 95 | 188ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 96 | 190ms | Clayrune | 0.11 MB/s | `https://clayrune.io` | 通用代理 |
| 97 | 191ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 98 | 193ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 99 | 194ms | Tms | 0.14 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 100 | 194ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 101 | 195ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 102 | 195ms | Polgarand | 0.07 MB/s | `https://polgarand.org` | 通用代理 |
| 103 | 196ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 104 | 197ms | Miaozitie | 0.07 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 105 | 197ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 106 | 198ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 107 | 198ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 108 | 198ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 109 | 198ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 110 | 198ms | Twitter | 0.63 MB/s | `https://twitter.com` | 通用代理 |
| 111 | 200ms | Alas | 0.66 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 112 | 202ms | Opencovibe | 0.28 MB/s | `https://opencovibe.com` | 通用代理 |
| 113 | 202ms | Sina | 0.76 MB/s | `https://sina.dev` | 通用代理 |
| 114 | 203ms | Clypra | 0.05 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 115 | 204ms | Ghproxy | 1.73 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 116 | 204ms | Github | 1.47 MB/s | `https://github.ihnic.com` | 通用代理 |
| 117 | 204ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 118 | 205ms | Ai-trend-publish | 0.01 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 119 | 205ms | Coffeecli | 0.11 MB/s | `https://coffeecli.com` | 通用代理 |
| 120 | 206ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 121 | 207ms | Ode | - | `https://ode.fun` | 通用代理 |
| 122 | 208ms | Cherryai | 0.04 MB/s | `https://cherryai.com` | 通用代理 |
| 123 | 208ms | Tvv | 1.76 MB/s | `https://tvv.tw` | 通用代理 |
| 124 | 209ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 125 | 209ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 126 | 211ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 127 | 212ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 128 | 213ms | Axios-http | 0.27 MB/s | `https://axios-http.com` | 通用代理 |
| 129 | 213ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 130 | 214ms | Openttd | 0.04 MB/s | `https://openttd.org` | 通用代理 |
| 131 | 215ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 132 | 215ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 133 | 216ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 134 | 216ms | Thumb | 1.05 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 135 | 217ms | Agoramarket | 0.03 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 136 | 218ms | Cognitum | 0.09 MB/s | `https://cognitum.one` | 通用代理 |
| 137 | 219ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 138 | 220ms | Aiblackboxfc | 0.25 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 139 | 221ms | Ghproxy | 0.85 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 140 | 223ms | Ampcode | 0.18 MB/s | `https://ampcode.com` | 通用代理 |
| 141 | 224ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 142 | 228ms | GH-Proxy Org | 0.85 MB/s | `https://gh-proxy.org` | 通用代理 |
| 143 | 230ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 144 | 231ms | Api | 0.11 MB/s | `https://api.solov.cc` | 通用代理 |
| 145 | 232ms | Cbrowser | 1.86 MB/s | `https://cbrowser.ai` | 通用代理 |
| 146 | 232ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 147 | 232ms | Gh | 1.55 MB/s | `https://gh.1k.ink` | 通用代理 |
| 148 | 234ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 149 | 236ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 150 | 237ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 151 | 239ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 152 | 241ms | Github | 0.72 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 153 | 243ms | Coreos | 1.56 MB/s | `https://coreos.com` | 通用代理 |
| 154 | 247ms | Ggg | 1.53 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 155 | 248ms | FastGit CC | 0.71 MB/s | `https://fastgit.cc` | 通用代理 |
| 156 | 248ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 157 | 249ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 158 | 251ms | GH Monlor | 0.78 MB/s | `https://gh.monlor.com` | 通用代理 |
| 159 | 255ms | Visionmemorymcp | 0.24 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 160 | 255ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 161 | 257ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 162 | 264ms | Microcoreos | 0.29 MB/s | `https://microcoreos.com` | 通用代理 |
| 163 | 266ms | Cursor | 0.55 MB/s | `https://cursor.com` | 通用代理 |
| 164 | 267ms | Gh | 0.62 MB/s | `https://gh.padao.fun` | 通用代理 |
| 165 | 267ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 166 | 269ms | Bananaslides | 0.24 MB/s | `https://bananaslides.online` | 通用代理 |
| 167 | 269ms | Contrib | 0.28 MB/s | `https://contrib.rocks` | 通用代理 |
| 168 | 269ms | CrashMC CDN | 0.6 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 169 | 270ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 170 | 271ms | Kenyu | 1.7 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 171 | 272ms | Docs | 0.03 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 172 | 272ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 173 | 274ms | Kuroutoshikou | 0.66 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 174 | 275ms | Youtu | 0.98 MB/s | `https://youtu.be` | 通用代理 |
| 175 | 276ms | Savannah | 0.02 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 176 | 277ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 177 | 280ms | Code | 1.1 MB/s | `https://code.claude.com` | 通用代理 |
| 178 | 281ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 179 | 282ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 180 | 286ms | Nisar | 0.39 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 181 | 287ms | Gsd | 0.26 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 182 | 287ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 183 | 288ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 184 | 290ms | Aka | 0.29 MB/s | `https://aka.ms` | 通用代理 |
| 185 | 290ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 186 | 292ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 187 | 293ms | Ginlix | 0.43 MB/s | `https://ginlix.ai` | 通用代理 |
| 188 | 294ms | Travis-ci | 0.2 MB/s | `https://travis-ci.org` | 通用代理 |
| 189 | 294ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 190 | 296ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 191 | 297ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 192 | 302ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 193 | 304ms | 30006000 | 0.68 MB/s | `https://30006000.xyz` | 通用代理 |
| 194 | 306ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 195 | 308ms | Hk | 1.09 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 196 | 309ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 197 | 312ms | Steamcommunity | 0.07 MB/s | `https://steamcommunity.com` | 通用代理 |
| 198 | 315ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 199 | 317ms | Tiktok | 0.07 MB/s | `https://tiktok.com` | 通用代理 |
| 200 | 318ms | Docs | 0.68 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 201 | 318ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 202 | 319ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 203 | 321ms | B23 | - | `https://b23.tv` | 通用代理 |
| 204 | 324ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 205 | 325ms | Claude | 0.21 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 206 | 329ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 207 | 333ms | Getgit | 2.0 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 208 | 334ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 209 | 336ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 210 | 336ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 211 | 337ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 212 | 344ms | Github | 1.62 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 213 | 344ms | Store | 0.95 MB/s | `https://store.steampowered.com` | 通用代理 |
| 214 | 345ms | Github | 1.48 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 215 | 346ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 216 | 352ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 217 | 358ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 218 | 366ms | V4 | 1.6 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 219 | 367ms | Nyx | 0.06 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 220 | 368ms | Cfkua | 1.18 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 221 | 371ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 222 | 371ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 223 | 374ms | Sonarcloud | 0.12 MB/s | `https://sonarcloud.io` | 通用代理 |
| 224 | 375ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 225 | 382ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 226 | 388ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 227 | 404ms | Weaverse | 0.64 MB/s | `https://weaverse.io` | 通用代理 |
| 228 | 405ms | Bailian | 0.07 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 229 | 411ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 230 | 411ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 231 | 412ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 232 | 415ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 233 | 418ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 234 | 420ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 235 | 422ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 236 | 424ms | Im | 0.15 MB/s | `https://im.codes` | 通用代理 |
| 237 | 425ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 238 | 427ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 239 | 427ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 240 | 428ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 241 | 430ms | YYLX Git | 0.74 MB/s | `https://git.yylx.win` | 通用代理 |
| 242 | 448ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 243 | 454ms | Bible-ai-explorer | 0.06 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 244 | 455ms | GH Nxnow | 0.45 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 245 | 455ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 246 | 458ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 247 | 467ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 248 | 473ms | Lucky | 0.51 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 249 | 478ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 250 | 482ms | Lecvdemarius | 0.06 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 251 | 482ms | Wl | - | `https://wl.do` | 通用代理 |
| 252 | 486ms | Ark | 0.49 MB/s | `https://ark.intel.com` | 通用代理 |
| 253 | 488ms | Safedocx | 0.09 MB/s | `https://safedocx.com` | 通用代理 |
| 254 | 490ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 255 | 491ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 256 | 491ms | SLink | 0.06 MB/s | `https://slink.ltd` | 通用代理 |
| 257 | 493ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 258 | 498ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 259 | 499ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 260 | 500ms | Github | 1.67 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 261 | 500ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 262 | 517ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 263 | 523ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 264 | 531ms | Patchworkos | 0.3 MB/s | `https://patchworkos.com` | 通用代理 |
| 265 | 534ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 266 | 536ms | Api | - | `https://api.river.ai` | 通用代理 |
| 267 | 537ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 268 | 541ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 269 | 552ms | Easyboardgame | 0.02 MB/s | `https://easyboardgame.top` | 通用代理 |
| 270 | 556ms | Gh | 0.85 MB/s | `https://gh.noki.icu` | 通用代理 |
| 271 | 565ms | You | 0.59 MB/s | `https://you.piccalc.com` | 通用代理 |
| 272 | 566ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 273 | 570ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 274 | 574ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 275 | 589ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 276 | 598ms | Aosmd | 0.17 MB/s | `https://aosmd.com` | 通用代理 |
| 277 | 599ms | Agentkey | 0.73 MB/s | `https://agentkey.app` | 通用代理 |
| 278 | 604ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 279 | 612ms | Clawbiz | 0.02 MB/s | `https://clawbiz.io` | 通用代理 |
| 280 | 625ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 281 | 627ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 282 | 632ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 283 | 633ms | Fastfile | 1.16 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 284 | 634ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 285 | 635ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 286 | 635ms | Github | 0.28 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 287 | 644ms | Umami-mcp | 0.42 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 288 | 646ms | Ghproxy | 0.25 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 289 | 653ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 290 | 658ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 291 | 660ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 292 | 671ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 293 | 681ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 294 | 687ms | Bseindia | 0.02 MB/s | `https://bseindia.com` | 通用代理 |
| 295 | 702ms | Os | 0.09 MB/s | `https://os.ryo.lu` | 通用代理 |
| 296 | 705ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 297 | 706ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 298 | 716ms | Support | 0.13 MB/s | `https://support.apple.com` | 通用代理 |
| 299 | 721ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 300 | 726ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 301 | 733ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 302 | 738ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 303 | 757ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 304 | 786ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 305 | 787ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 306 | 790ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 307 | 792ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 308 | 809ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 309 | 815ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 310 | 821ms | Aif | 0.05 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 311 | 825ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 312 | 829ms | Dbgate | 0.16 MB/s | `https://dbgate.org` | 通用代理 |
| 313 | 838ms | Gh | 1.24 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 314 | 842ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 315 | 858ms | Docs | 0.2 MB/s | `https://docs.transifex.com` | 通用代理 |
| 316 | 872ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 317 | 891ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 318 | 894ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 319 | 895ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 320 | 898ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 321 | 900ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 322 | 929ms | Mimo | 0.17 MB/s | `https://mimo.mi.com` | 通用代理 |
| 323 | 936ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 324 | 941ms | Task | 0.02 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 325 | 946ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 326 | 953ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 327 | 953ms | Ednovas Mirror | 0.44 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 328 | 982ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 329 | 996ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 330 | 1014ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 331 | 1020ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 332 | 1025ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 333 | 1037ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 334 | 1043ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 335 | 1062ms | Web | - | `https://web.4399.com` | 通用代理 |
| 336 | 1064ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 337 | 1069ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 338 | 1073ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 339 | 1089ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 340 | 1100ms | Dimagent | 0.14 MB/s | `https://dimagent.com` | 通用代理 |
| 341 | 1109ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 342 | 1119ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 343 | 1124ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 344 | 1130ms | Web | 0.12 MB/s | `https://web.archive.org` | 通用代理 |
| 345 | 1146ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 346 | 1148ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 347 | 1155ms | V | - | `https://v.douyin.com` | 通用代理 |
| 348 | 1167ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 349 | 1168ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 350 | 1175ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 351 | 1193ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 352 | 1211ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 353 | 1226ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 354 | 1257ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 355 | 1281ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 356 | 1293ms | Github | 0.02 MB/s | `https://github.chenc.dev` | 通用代理 |
| 357 | 1297ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 358 | 1338ms | Gh | 0.51 MB/s | `https://gh.39.al` | 通用代理 |
| 359 | 1375ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 360 | 1392ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 361 | 1429ms | Free | 0.47 MB/s | `https://free.cn.eu.org` | 通用代理 |
| 362 | 1430ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 363 | 1435ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 364 | 1479ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 365 | 1522ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 366 | 1540ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 367 | 1579ms | I-qps | 0.02 MB/s | `https://i-qps.net` | 通用代理 |
| 368 | 1647ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 369 | 1745ms | Gh | 0.28 MB/s | `https://gh.dpik.top` | 通用代理 |
| 370 | 1755ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 371 | 1783ms | GHProxy Net | 0.12 MB/s | `https://ghproxy.net` | 通用代理 |
| 372 | 1792ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 373 | 2011ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 374 | 2049ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 375 | 2064ms | G | 0.06 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 376 | 2107ms | Img | - | `https://img.ink` | 通用代理 |
| 377 | 2295ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 378 | 2304ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 379 | 2324ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 380 | 2393ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 381 | 2431ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 382 | 2613ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 383 | 2761ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 384 | 2915ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 385 | 2992ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 386 | 3176ms | Ghproxy | 0.12 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 387 | 3552ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 388 | 4887ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |


### ⚠️ 不稳定节点（22 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFast (`ghfast-top`) | 2 次 |
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 21 次 |
| Gh (`gh-llkk-cc`) | 5 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Cf (`cf-ghproxy-cc`) | 2 次 |
| Ghproxy (`ghproxy-cc`) | 2 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Git (`git-tangbai-cc`) | 4 次 |
| Proxy (`proxy-yaoyaoling-net`) | 3 次 |
| Gh (`gh-b52m-cn`) | 8 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |
| Sub (`sub-ikar-eu-org`) | 3 次 |
| Nssurge (`nssurge-com`) | 7 次 |
| Code (`code-leez-tech`) | 1 次 |
| Status (`status-leez-tech`) | 1 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 7 次 |
| Flashtype (`flashtype-com`) | 2 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 12 次 |
| Maplecode (`maplecode-art`) | 22 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 18 次 |
| Adult (`adult-contents-fc2-com`) | 4 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 403 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **410** | |

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
