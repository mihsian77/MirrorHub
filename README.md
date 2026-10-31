# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-31T21:05:37Z**，每 6 小时刷新一次。当前 ✅ **392** 在线 / ⚠️ **19** 不稳定 / ⚰️ **53** 已失效归档。

## 核心特性

- **411 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 73ms | Microsoftedge | 0.19 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 83ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 3 | 86ms | Linkedin | 0.14 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 89ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 5 | 94ms | Githubstatus | 2.8 MB/s | `https://githubstatus.com` | 通用代理 |
| 6 | 99ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 7 | 100ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 8 | 100ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 9 | 101ms | Wordpaper | 0.49 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 10 | 102ms | X | 1.5 MB/s | `https://x.com` | 通用代理 |
| 11 | 103ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 12 | 104ms | Resume-5lv | 0.2 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 13 | 104ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 14 | 105ms | Huly-mcp | 0.22 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 15 | 106ms | Godocs | 0.06 MB/s | `https://godocs.io` | 通用代理 |
| 16 | 107ms | Zebrunner | 1.98 MB/s | `https://zebrunner.com` | 通用代理 |
| 17 | 108ms | Game | 0.13 MB/s | `https://game.chozo.net` | 通用代理 |
| 18 | 108ms | Tools | 2.14 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 19 | 108ms | Xjtu-nyxf-study-material | 0.16 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 20 | 108ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 21 | 109ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 22 | 113ms | App | 0.09 MB/s | `https://app.netlify.com` | 通用代理 |
| 23 | 114ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 24 | 118ms | Kighelper-cloud | 0.1 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 25 | 119ms | Deno | 0.19 MB/s | `https://deno.com` | 通用代理 |
| 26 | 119ms | Opresume | 0.62 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 27 | 120ms | Lawyer-yu | 0.08 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 28 | 124ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 29 | 124ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 30 | 126ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 31 | 127ms | Dilo-d14 | 0.21 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 32 | 127ms | Impeccable | 1.07 MB/s | `https://impeccable.style` | 通用代理 |
| 33 | 127ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 34 | 130ms | Megacrit | 0.24 MB/s | `https://megacrit.com` | 通用代理 |
| 35 | 134ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 36 | 137ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 37 | 139ms | Components | 0.09 MB/s | `https://components.dereekb.com` | 通用代理 |
| 38 | 140ms | Opentakeoff | 0.03 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 39 | 142ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 40 | 146ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 41 | 147ms | Music-cli | 0.18 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 42 | 149ms | Discord | 0.07 MB/s | `https://discord.gg` | 通用代理 |
| 43 | 150ms | Img | - | `https://img.shields.io` | 通用代理 |
| 44 | 150ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 45 | 151ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 46 | 151ms | Bolt2github | 0.04 MB/s | `https://bolt2github.com` | 通用代理 |
| 47 | 151ms | Serac | 0.08 MB/s | `https://serac.build` | 通用代理 |
| 48 | 153ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 49 | 153ms | Opensunsama | 0.09 MB/s | `https://opensunsama.com` | 通用代理 |
| 50 | 154ms | Training | 0.26 MB/s | `https://training.ti.com` | 通用代理 |
| 51 | 155ms | Openchamber | 0.84 MB/s | `https://openchamber.dev` | 通用代理 |
| 52 | 156ms | Cumora | 0.35 MB/s | `https://cumora.ai` | 通用代理 |
| 53 | 157ms | Codeeraser | 0.12 MB/s | `https://codeeraser.dev` | 通用代理 |
| 54 | 157ms | Git | 2.0 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 55 | 158ms | GH-Proxy | 1.22 MB/s | `https://gh-proxy.com` | 通用代理 |
| 56 | 160ms | Git | 2.6 MB/s | `https://git.820828.xyz` | 通用代理 |
| 57 | 161ms | Github | 2.92 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 58 | 161ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 59 | 162ms | Caiji | - | `https://caiji.cyou` | 通用代理 |
| 60 | 162ms | Gp | 2.94 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 61 | 162ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 62 | 165ms | Impro | 2.28 MB/s | `https://impro.social` | 通用代理 |
| 63 | 165ms | Openpua | 0.48 MB/s | `https://openpua.ai` | 通用代理 |
| 64 | 165ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 65 | 166ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 66 | 167ms | Gh | 2.72 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 67 | 168ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 68 | 169ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 69 | 170ms | Vibesql | 0.14 MB/s | `https://vibesql.org` | 通用代理 |
| 70 | 172ms | Gh | 2.18 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 71 | 173ms | Agentlimb | 0.2 MB/s | `https://agentlimb.com` | 通用代理 |
| 72 | 173ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 73 | 173ms | Ghproxy | 2.14 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 74 | 173ms | Github | 2.97 MB/s | `https://github.788787.xyz` | 通用代理 |
| 75 | 173ms | Gpui | 0.21 MB/s | `https://gpui.rs` | 通用代理 |
| 76 | 173ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 77 | 174ms | Anh | 0.21 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 78 | 174ms | Bestdori | 0.14 MB/s | `https://bestdori.com` | 通用代理 |
| 79 | 174ms | Gitea-mirror | 0.86 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 80 | 176ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 81 | 177ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 82 | 178ms | Cody | 0.19 MB/s | `https://cody.todyle.com` | 通用代理 |
| 83 | 179ms | Caw | 0.07 MB/s | `https://caw.rocks` | 通用代理 |
| 84 | 179ms | L4d2 | 0.16 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 85 | 180ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 86 | 180ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 87 | 183ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 88 | 184ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 89 | 184ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 90 | 184ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 91 | 185ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 92 | 186ms | Chops | 0.04 MB/s | `https://chops.md` | 通用代理 |
| 93 | 186ms | Pidash | 0.05 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 94 | 187ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 95 | 188ms | Github | 2.24 MB/s | `https://github.880824.xyz` | 通用代理 |
| 96 | 190ms | Clayrune | 0.14 MB/s | `https://clayrune.io` | 通用代理 |
| 97 | 190ms | Glass | 0.25 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 98 | 190ms | Tokei | 0.52 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 99 | 194ms | Polgarand | 0.07 MB/s | `https://polgarand.org` | 通用代理 |
| 100 | 195ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 101 | 195ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 102 | 195ms | Tms | 0.1 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 103 | 196ms | Twitter | 0.81 MB/s | `https://twitter.com` | 通用代理 |
| 104 | 197ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 105 | 197ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 106 | 199ms | Aiblackboxfc | 0.4 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 107 | 200ms | Shiori-v1 | 0.03 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 108 | 201ms | Alas | 0.99 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 109 | 201ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 110 | 202ms | Ghproxy | 2.54 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 111 | 202ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 112 | 203ms | Hopp | 0.04 MB/s | `https://hopp.sh` | 通用代理 |
| 113 | 204ms | Coffeecli | 0.14 MB/s | `https://coffeecli.com` | 通用代理 |
| 114 | 205ms | Ai-trend-publish | 0.03 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 115 | 205ms | Clypra | 0.07 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 116 | 205ms | Opencovibe | 0.39 MB/s | `https://opencovibe.com` | 通用代理 |
| 117 | 206ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 118 | 206ms | GH-Proxy Org | 1.22 MB/s | `https://gh-proxy.org` | 通用代理 |
| 119 | 207ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 120 | 207ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 121 | 209ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 122 | 209ms | Cherryai | 0.05 MB/s | `https://cherryai.com` | 通用代理 |
| 123 | 210ms | Github | 2.06 MB/s | `https://github.ihnic.com` | 通用代理 |
| 124 | 210ms | Ode | - | `https://ode.fun` | 通用代理 |
| 125 | 211ms | Axios-http | 0.38 MB/s | `https://axios-http.com` | 通用代理 |
| 126 | 212ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 127 | 212ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 128 | 214ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 129 | 215ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 130 | 215ms | Ampcode | 0.3 MB/s | `https://ampcode.com` | 通用代理 |
| 131 | 216ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 132 | 216ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 133 | 216ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 134 | 216ms | Thumb | 1.03 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 135 | 217ms | Agoramarket | 0.09 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 136 | 218ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 137 | 218ms | Ghproxy | 1.89 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 138 | 219ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 139 | 223ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 140 | 224ms | Cognitum | 0.12 MB/s | `https://cognitum.one` | 通用代理 |
| 141 | 224ms | Tvv | 2.83 MB/s | `https://tvv.tw` | 通用代理 |
| 142 | 226ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 143 | 226ms | Sina | 0.47 MB/s | `https://sina.dev` | 通用代理 |
| 144 | 228ms | Gh | 1.67 MB/s | `https://gh.1k.ink` | 通用代理 |
| 145 | 231ms | Github | 2.5 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 146 | 232ms | Api | 0.18 MB/s | `https://api.solov.cc` | 通用代理 |
| 147 | 234ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 148 | 235ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 149 | 236ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 150 | 236ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 151 | 238ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 152 | 243ms | Coreos | 1.94 MB/s | `https://coreos.com` | 通用代理 |
| 153 | 245ms | Ggg | 2.7 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 154 | 245ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 155 | 249ms | GH Monlor | 1.53 MB/s | `https://gh.monlor.com` | 通用代理 |
| 156 | 250ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 157 | 252ms | Cbrowser | 0.85 MB/s | `https://cbrowser.ai` | 通用代理 |
| 158 | 252ms | FastGit CC | 1.78 MB/s | `https://fastgit.cc` | 通用代理 |
| 159 | 256ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 160 | 258ms | Visionmemorymcp | 0.2 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 161 | 260ms | Kuroutoshikou | 1.03 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 162 | 264ms | Gsd | 0.09 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 163 | 265ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 164 | 269ms | Docs | 0.06 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 165 | 269ms | Gh | 1.55 MB/s | `https://gh.padao.fun` | 通用代理 |
| 166 | 269ms | Microcoreos | 0.36 MB/s | `https://microcoreos.com` | 通用代理 |
| 167 | 270ms | Bananaslides | 0.82 MB/s | `https://bananaslides.online` | 通用代理 |
| 168 | 270ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 169 | 270ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 170 | 272ms | Kenyu | 1.98 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 171 | 272ms | Open | 0.03 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 172 | 273ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 173 | 273ms | Cursor | 0.33 MB/s | `https://cursor.com` | 通用代理 |
| 174 | 276ms | Youtu | 1.4 MB/s | `https://youtu.be` | 通用代理 |
| 175 | 277ms | CrashMC CDN | 1.99 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 176 | 277ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 177 | 280ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 178 | 282ms | Code | 1.6 MB/s | `https://code.claude.com` | 通用代理 |
| 179 | 282ms | Nisar | 1.43 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 180 | 284ms | Contrib | 0.28 MB/s | `https://contrib.rocks` | 通用代理 |
| 181 | 287ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 182 | 288ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 183 | 292ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 184 | 293ms | Aka | 0.25 MB/s | `https://aka.ms` | 通用代理 |
| 185 | 293ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 186 | 294ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 187 | 294ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 188 | 295ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 189 | 296ms | Ginlix | 0.33 MB/s | `https://ginlix.ai` | 通用代理 |
| 190 | 296ms | Savannah | 0.02 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 191 | 296ms | Tools | 0.06 MB/s | `https://tools.ietf.org` | 通用代理 |
| 192 | 296ms | Travis-ci | 0.15 MB/s | `https://travis-ci.org` | 通用代理 |
| 193 | 297ms | Flashtype | - | `https://flashtype.com` | 通用代理 |
| 194 | 300ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 195 | 305ms | Steamcommunity | 0.11 MB/s | `https://steamcommunity.com` | 通用代理 |
| 196 | 309ms | Hk | 1.27 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 197 | 309ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 198 | 310ms | Agenticcorporation | 0.04 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 199 | 319ms | B23 | - | `https://b23.tv` | 通用代理 |
| 200 | 319ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 201 | 320ms | Tiktok | 0.12 MB/s | `https://tiktok.com` | 通用代理 |
| 202 | 320ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 203 | 321ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 204 | 322ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 205 | 327ms | 30006000 | 1.05 MB/s | `https://30006000.xyz` | 通用代理 |
| 206 | 328ms | Getgit | 2.28 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 207 | 329ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 208 | 331ms | Claude | 0.19 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 209 | 334ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 210 | 336ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 211 | 336ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 212 | 339ms | Github | 2.81 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 213 | 343ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 214 | 347ms | Github | 2.47 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 215 | 352ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 216 | 353ms | Store | 0.85 MB/s | `https://store.steampowered.com` | 通用代理 |
| 217 | 354ms | Sonarcloud | 0.25 MB/s | `https://sonarcloud.io` | 通用代理 |
| 218 | 358ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 219 | 358ms | Turborepo-starter-kit-web | 0.08 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 220 | 363ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 221 | 367ms | Cfkua | 1.87 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 222 | 367ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 223 | 369ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 224 | 369ms | V4 | 2.66 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 225 | 372ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 226 | 373ms | Docs | 0.64 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 227 | 380ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 228 | 384ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 229 | 386ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 230 | 404ms | Weaverse | 0.66 MB/s | `https://weaverse.io` | 通用代理 |
| 231 | 405ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 232 | 406ms | Bailian | 0.08 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 233 | 408ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 234 | 410ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 235 | 411ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 236 | 412ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 237 | 413ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 238 | 417ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 239 | 423ms | Your-domain | 0.07 MB/s | `https://your-domain.com` | 通用代理 |
| 240 | 427ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 241 | 428ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 242 | 429ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 243 | 431ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 244 | 432ms | Msdn | 0.05 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 245 | 444ms | Bible-ai-explorer | 0.08 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 246 | 446ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 247 | 446ms | YYLX Git | 0.4 MB/s | `https://git.yylx.win` | 通用代理 |
| 248 | 450ms | GH Nxnow | 0.3 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 249 | 453ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 250 | 454ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 251 | 456ms | Im | 0.17 MB/s | `https://im.codes` | 通用代理 |
| 252 | 467ms | Lucky | 0.53 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 253 | 467ms | SLink | 0.09 MB/s | `https://slink.ltd` | 通用代理 |
| 254 | 470ms | Ark | 1.54 MB/s | `https://ark.intel.com` | 通用代理 |
| 255 | 475ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 256 | 476ms | Wl | - | `https://wl.do` | 通用代理 |
| 257 | 480ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 258 | 480ms | Safedocx | 0.12 MB/s | `https://safedocx.com` | 通用代理 |
| 259 | 481ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 260 | 486ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 261 | 490ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 262 | 501ms | Lecvdemarius | 0.05 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 263 | 504ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 264 | 511ms | Ygdj7 | 0.05 MB/s | `https://ygdj7.com` | 通用代理 |
| 265 | 512ms | Serverkit | 0.04 MB/s | `https://serverkit.ai` | 通用代理 |
| 266 | 522ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 267 | 524ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 268 | 527ms | Github | 2.51 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 269 | 528ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 270 | 532ms | Agentkey | 0.8 MB/s | `https://agentkey.app` | 通用代理 |
| 271 | 534ms | Patchworkos | 0.24 MB/s | `https://patchworkos.com` | 通用代理 |
| 272 | 537ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 273 | 541ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 274 | 541ms | Api | - | `https://api.river.ai` | 通用代理 |
| 275 | 548ms | You | 0.85 MB/s | `https://you.piccalc.com` | 通用代理 |
| 276 | 550ms | Easyboardgame | 0.01 MB/s | `https://easyboardgame.top` | 通用代理 |
| 277 | 553ms | Gh | 0.58 MB/s | `https://gh.noki.icu` | 通用代理 |
| 278 | 566ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 279 | 573ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 280 | 577ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 281 | 586ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 282 | 591ms | Aosmd | 0.12 MB/s | `https://aosmd.com` | 通用代理 |
| 283 | 597ms | Memstack | 0.01 MB/s | `https://memstack.pro` | 通用代理 |
| 284 | 603ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 285 | 604ms | Github | 0.58 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 286 | 606ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 287 | 614ms | Support | 1.42 MB/s | `https://support.apple.com` | 通用代理 |
| 288 | 619ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 289 | 622ms | Tracely-studio | 0.04 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 290 | 627ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 291 | 634ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 292 | 640ms | Umami-mcp | 0.93 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 293 | 643ms | Fastfile | 1.72 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 294 | 655ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 295 | 656ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 296 | 656ms | Ghproxy | 0.36 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 297 | 660ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 298 | 672ms | Tsukuyomi | 0.13 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 299 | 679ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 300 | 694ms | Os | 0.08 MB/s | `https://os.ryo.lu` | 通用代理 |
| 301 | 695ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 302 | 705ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 303 | 706ms | Onetwin | 0.03 MB/s | `https://onetwin.cn` | 通用代理 |
| 304 | 707ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 305 | 711ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 306 | 712ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 307 | 757ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 308 | 761ms | Ccgather | 0.04 MB/s | `https://ccgather.com` | 通用代理 |
| 309 | 782ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 310 | 786ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 311 | 797ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 312 | 802ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 313 | 807ms | Internhack | 0.04 MB/s | `https://internhack.xyz` | 通用代理 |
| 314 | 810ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 315 | 817ms | Gh | 1.89 MB/s | `https://gh.39.al` | 通用代理 |
| 316 | 829ms | Docs | 0.16 MB/s | `https://docs.transifex.com` | 通用代理 |
| 317 | 833ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 318 | 836ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 319 | 848ms | Gh | 0.63 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 320 | 860ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 321 | 864ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 322 | 878ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 323 | 885ms | Dbgate | 0.12 MB/s | `https://dbgate.org` | 通用代理 |
| 324 | 891ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 325 | 892ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 326 | 893ms | Yibiao | 0.14 MB/s | `https://yibiao.pro` | 通用代理 |
| 327 | 896ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 328 | 925ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 329 | 929ms | Mimo | 0.19 MB/s | `https://mimo.mi.com` | 通用代理 |
| 330 | 936ms | Code | 0.01 MB/s | `https://code.videolan.org` | 通用代理 |
| 331 | 936ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 332 | 940ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 333 | 958ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 334 | 969ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 335 | 998ms | Ednovas Mirror | 0.16 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 336 | 999ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 337 | 1006ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 338 | 1016ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 339 | 1035ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 340 | 1052ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 341 | 1067ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 342 | 1074ms | Web | - | `https://web.4399.com` | 通用代理 |
| 343 | 1081ms | Dimagent | 0.17 MB/s | `https://dimagent.com` | 通用代理 |
| 344 | 1087ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 345 | 1089ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 346 | 1091ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 347 | 1094ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 348 | 1117ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 349 | 1126ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 350 | 1142ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 351 | 1143ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 352 | 1146ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 353 | 1147ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 354 | 1166ms | V | 0.06 MB/s | `https://v.douyin.com` | 通用代理 |
| 355 | 1174ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 356 | 1174ms | Web | 0.25 MB/s | `https://web.archive.org` | 通用代理 |
| 357 | 1183ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 358 | 1202ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 359 | 1214ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 360 | 1215ms | Atomcode | 0.07 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 361 | 1239ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 362 | 1268ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 363 | 1272ms | Github | 0.18 MB/s | `https://github.chenc.dev` | 通用代理 |
| 364 | 1282ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 365 | 1407ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 366 | 1411ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 367 | 1445ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 368 | 1445ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 369 | 1471ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 370 | 1598ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 371 | 1608ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 372 | 1617ms | GHProxy Net | 0.28 MB/s | `https://ghproxy.net` | 通用代理 |
| 373 | 1620ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 374 | 1661ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 375 | 1685ms | Git | 0.39 MB/s | `https://git.669966.xyz` | 通用代理 |
| 376 | 1699ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 377 | 1770ms | Gh | 0.89 MB/s | `https://gh.dpik.top` | 通用代理 |
| 378 | 1995ms | Img | - | `https://img.ink` | 通用代理 |
| 379 | 2069ms | G | 0.2 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 380 | 2204ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 381 | 2211ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 382 | 2270ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 383 | 2285ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 384 | 2344ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 385 | 2456ms | Provider | - | `https://provider.com` | 通用代理 |
| 386 | 2539ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 387 | 2744ms | Tcl | 0.01 MB/s | `https://tcl.tk` | 通用代理 |
| 388 | 2755ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 389 | 2856ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 390 | 3030ms | Ghproxy | 0.95 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 391 | 3470ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 392 | 6123ms | Proxy | 0.04 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（19 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFast (`ghfast-top`) | 3 次 |
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 22 次 |
| GitClone (`gitclone-com`) | 1 次 |
| Gh (`gh-llkk-cc`) | 6 次 |
| Gh (`gh-idayer-com`) | 3 次 |
| Cf (`cf-ghproxy-cc`) | 3 次 |
| Ghproxy (`ghproxy-cc`) | 3 次 |
| Git (`git-tangbai-cc`) | 5 次 |
| Gh (`gh-b52m-cn`) | 9 次 |
| Sub (`sub-ikar-eu-org`) | 4 次 |
| Nssurge (`nssurge-com`) | 8 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 8 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 13 次 |
| Maplecode (`maplecode-art`) | 23 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 19 次 |
| Adult (`adult-contents-fc2-com`) | 5 次 |
| Git (`git-net2o-de`) | 1 次 |
| Free (`free-cn-eu-org`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 404 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **411** | |

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
