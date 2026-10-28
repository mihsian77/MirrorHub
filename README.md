# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-28T12:15:15Z**，每 6 小时刷新一次。当前 ✅ **384** 在线 / ⚠️ **15** 不稳定 / ⚰️ **51** 已失效归档。

## 核心特性

- **399 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 64ms | Microsoftedge | 0.19 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 71ms | Linkedin | 0.13 MB/s | `https://linkedin.com` | 通用代理 |
| 3 | 78ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 4 | 78ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 79ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 6 | 82ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 7 | 85ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 8 | 86ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 9 | 88ms | Img | - | `https://img.shields.io` | 通用代理 |
| 10 | 94ms | App | 0.08 MB/s | `https://app.netlify.com` | 通用代理 |
| 11 | 96ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 12 | 97ms | Deno | 0.19 MB/s | `https://deno.com` | 通用代理 |
| 13 | 97ms | Githubstatus | 2.26 MB/s | `https://githubstatus.com` | 通用代理 |
| 14 | 97ms | Godocs | 0.05 MB/s | `https://godocs.io` | 通用代理 |
| 15 | 98ms | X | 1.31 MB/s | `https://x.com` | 通用代理 |
| 16 | 101ms | Lawyer-yu | 0.06 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 17 | 102ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 18 | 104ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 19 | 112ms | Xjtu-nyxf-study-material | 0.16 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 20 | 116ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 21 | 117ms | Opresume | 0.63 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 22 | 117ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 23 | 119ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 24 | 120ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 25 | 120ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 26 | 121ms | Zebrunner | 2.25 MB/s | `https://zebrunner.com` | 通用代理 |
| 27 | 121ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 28 | 123ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 29 | 125ms | Music-cli | 0.2 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 30 | 129ms | Cognitum | 0.17 MB/s | `https://cognitum.one` | 通用代理 |
| 31 | 133ms | Thumb | 0.99 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 32 | 134ms | Opentakeoff | 0.03 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 33 | 135ms | Resume-5lv | 0.17 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 34 | 139ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 35 | 140ms | Discord | 0.07 MB/s | `https://discord.gg` | 通用代理 |
| 36 | 144ms | Caiji | 0.06 MB/s | `https://caiji.cyou` | 通用代理 |
| 37 | 144ms | Kighelper-cloud | 0.06 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 38 | 144ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 39 | 146ms | Components | 0.16 MB/s | `https://components.dereekb.com` | 通用代理 |
| 40 | 146ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 41 | 147ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 42 | 147ms | Impeccable | 1.07 MB/s | `https://impeccable.style` | 通用代理 |
| 43 | 148ms | Vibesql | 0.14 MB/s | `https://vibesql.org` | 通用代理 |
| 44 | 149ms | Git | 2.44 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 45 | 149ms | Github | 2.59 MB/s | `https://github.880824.xyz` | 通用代理 |
| 46 | 149ms | Tms | 0.1 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 47 | 150ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 48 | 151ms | Github | 2.8 MB/s | `https://github.788787.xyz` | 通用代理 |
| 49 | 152ms | Gitea-mirror | 0.92 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 50 | 153ms | Bestdori | 0.1 MB/s | `https://bestdori.com` | 通用代理 |
| 51 | 153ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 52 | 154ms | Dilo-d14 | 0.23 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 53 | 154ms | Git | 2.16 MB/s | `https://git.820828.xyz` | 通用代理 |
| 54 | 156ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 55 | 159ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 56 | 159ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 57 | 159ms | Tokei | 0.57 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 58 | 160ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 59 | 160ms | Cbrowser | 1.58 MB/s | `https://cbrowser.ai` | 通用代理 |
| 60 | 162ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 61 | 162ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 62 | 162ms | Glass | 0.28 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 63 | 162ms | Miaozitie | 0.1 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 64 | 162ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 65 | 163ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 66 | 163ms | Openpua | 0.51 MB/s | `https://openpua.ai` | 通用代理 |
| 67 | 163ms | Opensunsama | 0.08 MB/s | `https://opensunsama.com` | 通用代理 |
| 68 | 164ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 69 | 165ms | Play | 0.05 MB/s | `https://play.templatical.com` | 通用代理 |
| 70 | 166ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 71 | 166ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 72 | 167ms | L4d2 | 0.15 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 73 | 167ms | Training | 0.43 MB/s | `https://training.ti.com` | 通用代理 |
| 74 | 167ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 75 | 169ms | Clayrune | 0.18 MB/s | `https://clayrune.io` | 通用代理 |
| 76 | 169ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 77 | 170ms | Cherryai | 0.06 MB/s | `https://cherryai.com` | 通用代理 |
| 78 | 172ms | Github | 2.67 MB/s | `https://github.ihnic.com` | 通用代理 |
| 79 | 172ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 80 | 173ms | Gh | 2.53 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 81 | 173ms | Gh | 1.3 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 82 | 174ms | Coffeecli | 0.16 MB/s | `https://coffeecli.com` | 通用代理 |
| 83 | 174ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 84 | 174ms | Kuroutoshikou | 2.69 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 85 | 175ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 86 | 175ms | Cody | 0.22 MB/s | `https://cody.todyle.com` | 通用代理 |
| 87 | 177ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 88 | 179ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 89 | 180ms | Alas | 1.04 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 90 | 180ms | Ode | - | `https://ode.fun` | 通用代理 |
| 91 | 180ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 92 | 181ms | Ai-trend-publish | 0.03 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 93 | 181ms | GH Monlor | 0.61 MB/s | `https://gh.monlor.com` | 通用代理 |
| 94 | 182ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 95 | 184ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 96 | 185ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 97 | 186ms | GH-Proxy | 2.45 MB/s | `https://gh-proxy.com` | 通用代理 |
| 98 | 188ms | Crypto-funding-arbitrage | 0.08 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 99 | 190ms | Ghproxy | 2.25 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 100 | 190ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 101 | 191ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 102 | 192ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 103 | 192ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 104 | 197ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 105 | 204ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 106 | 205ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 107 | 205ms | Polgarand | 0.09 MB/s | `https://polgarand.org` | 通用代理 |
| 108 | 206ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 109 | 208ms | Codeeraser | 0.08 MB/s | `https://codeeraser.dev` | 通用代理 |
| 110 | 208ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 111 | 208ms | Pidash | 0.05 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 112 | 210ms | Agentlimb | 0.27 MB/s | `https://agentlimb.com` | 通用代理 |
| 113 | 211ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 114 | 212ms | Clypra | 0.06 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 115 | 212ms | Ghproxy | 2.44 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 116 | 215ms | Cursor | 0.3 MB/s | `https://cursor.com` | 通用代理 |
| 117 | 216ms | Aiblackboxfc | 0.45 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 118 | 216ms | Bananaslides | 0.85 MB/s | `https://bananaslides.online` | 通用代理 |
| 119 | 216ms | GH-Proxy Org | 1.27 MB/s | `https://gh-proxy.org` | 通用代理 |
| 120 | 218ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 121 | 220ms | Axios-http | 0.29 MB/s | `https://axios-http.com` | 通用代理 |
| 122 | 221ms | Coreos | 2.28 MB/s | `https://coreos.com` | 通用代理 |
| 123 | 221ms | Ghproxy | 1.68 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 124 | 221ms | Gsd | 0.13 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 125 | 222ms | Ampcode | 0.3 MB/s | `https://ampcode.com` | 通用代理 |
| 126 | 225ms | Agoramarket | 0.1 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 127 | 225ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 128 | 225ms | Twitter | 0.75 MB/s | `https://twitter.com` | 通用代理 |
| 129 | 227ms | Opencovibe | 0.44 MB/s | `https://opencovibe.com` | 通用代理 |
| 130 | 227ms | Travis-ci | 0.14 MB/s | `https://travis-ci.org` | 通用代理 |
| 131 | 230ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 132 | 232ms | Ggg | 2.2 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 133 | 235ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 134 | 237ms | Microcoreos | 0.39 MB/s | `https://microcoreos.com` | 通用代理 |
| 135 | 239ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 136 | 239ms | Chops | 0.04 MB/s | `https://chops.md` | 通用代理 |
| 137 | 239ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 138 | 243ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 139 | 243ms | Sub | 0.14 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 140 | 243ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 141 | 244ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 142 | 245ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 143 | 246ms | Aka | 0.6 MB/s | `https://aka.ms` | 通用代理 |
| 144 | 249ms | Code | 1.96 MB/s | `https://code.claude.com` | 通用代理 |
| 145 | 250ms | Github | 2.33 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 146 | 252ms | CrashMC CDN | 0.66 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 147 | 253ms | Nisar | 1.4 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 148 | 254ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 149 | 260ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 150 | 263ms | Api | 0.21 MB/s | `https://api.solov.cc` | 通用代理 |
| 151 | 265ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 152 | 266ms | Aomedia | 0.17 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 153 | 269ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 154 | 269ms | Sina | 1.66 MB/s | `https://sina.dev` | 通用代理 |
| 155 | 270ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 156 | 274ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 157 | 277ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 158 | 277ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 159 | 280ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 160 | 282ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 161 | 282ms | Youtu | 1.21 MB/s | `https://youtu.be` | 通用代理 |
| 162 | 283ms | Visionmemorymcp | 0.26 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 163 | 286ms | Contrib | 0.26 MB/s | `https://contrib.rocks` | 通用代理 |
| 164 | 288ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 165 | 291ms | Savannah | 0.02 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 166 | 292ms | Tiktok | 0.19 MB/s | `https://tiktok.com` | 通用代理 |
| 167 | 293ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 168 | 295ms | FastGit CC | 1.9 MB/s | `https://fastgit.cc` | 通用代理 |
| 169 | 295ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 170 | 295ms | Flashtype | - | `https://flashtype.com` | 通用代理 |
| 171 | 303ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 172 | 305ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 173 | 305ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 174 | 308ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 175 | 308ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 176 | 310ms | Gh | 1.79 MB/s | `https://gh.padao.fun` | 通用代理 |
| 177 | 311ms | 30006000 | 2.16 MB/s | `https://30006000.xyz` | 通用代理 |
| 178 | 313ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 179 | 316ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 180 | 316ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 181 | 318ms | Claude | 0.37 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 182 | 318ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 183 | 318ms | Openttd | 0.06 MB/s | `https://openttd.org` | 通用代理 |
| 184 | 323ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 185 | 326ms | Gpui | 0.29 MB/s | `https://gpui.rs` | 通用代理 |
| 186 | 326ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 187 | 327ms | Bailian | 0.1 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 188 | 327ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 189 | 333ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 190 | 339ms | B23 | - | `https://b23.tv` | 通用代理 |
| 191 | 339ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 192 | 340ms | Im | 0.45 MB/s | `https://im.codes` | 通用代理 |
| 193 | 341ms | Steamcommunity | 0.13 MB/s | `https://steamcommunity.com` | 通用代理 |
| 194 | 342ms | Oem | 0.04 MB/s | `https://oem.re` | 通用代理 |
| 195 | 350ms | Turborepo-starter-kit-web | 0.07 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 196 | 352ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 197 | 353ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 198 | 358ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 199 | 358ms | Store | 1.26 MB/s | `https://store.steampowered.com` | 通用代理 |
| 200 | 360ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 201 | 361ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 202 | 361ms | You | 0.09 MB/s | `https://you.piccalc.com` | 通用代理 |
| 203 | 362ms | GH Nxnow | 0.62 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 204 | 364ms | Weaverse | 0.63 MB/s | `https://weaverse.io` | 通用代理 |
| 205 | 367ms | Sonarcloud | 0.1 MB/s | `https://sonarcloud.io` | 通用代理 |
| 206 | 371ms | Serac | 0.08 MB/s | `https://serac.build` | 通用代理 |
| 207 | 379ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 208 | 383ms | Ednovas Mirror | 0.75 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 209 | 388ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 210 | 390ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 211 | 392ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 212 | 392ms | Getgit | 2.18 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 213 | 395ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 214 | 398ms | Gh | 0.56 MB/s | `https://gh.noki.icu` | 通用代理 |
| 215 | 402ms | V4 | 1.84 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 216 | 403ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 217 | 406ms | GHFast | 0.6 MB/s | `https://ghfast.top` | 通用代理 |
| 218 | 407ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 219 | 408ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 220 | 408ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 221 | 409ms | Codeflying | 0.01 MB/s | `https://codeflying.app` | 通用代理 |
| 222 | 409ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 223 | 413ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 224 | 423ms | Tvv | 2.79 MB/s | `https://tvv.tw` | 通用代理 |
| 225 | 429ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 226 | 438ms | Gh | 2.67 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 227 | 439ms | YYLX Git | 0.78 MB/s | `https://git.yylx.win` | 通用代理 |
| 228 | 444ms | Aps | 0.06 MB/s | `https://aps.com` | 通用代理 |
| 229 | 449ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 230 | 450ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 231 | 451ms | Msdn | 0.05 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 232 | 456ms | Lecvdemarius | 0.05 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 233 | 456ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 234 | 456ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 235 | 462ms | Bible-ai-explorer | 0.08 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 236 | 462ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 237 | 463ms | Huly-mcp | 0.19 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 238 | 467ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 239 | 475ms | Hk | 1.26 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 240 | 475ms | Serverkit | 0.04 MB/s | `https://serverkit.ai` | 通用代理 |
| 241 | 476ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 242 | 476ms | Ark | 0.64 MB/s | `https://ark.intel.com` | 通用代理 |
| 243 | 478ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 244 | 483ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 245 | 488ms | Patchworkos | 0.23 MB/s | `https://patchworkos.com` | 通用代理 |
| 246 | 489ms | Impro | 1.85 MB/s | `https://impro.social` | 通用代理 |
| 247 | 489ms | Safedocx | 0.11 MB/s | `https://safedocx.com` | 通用代理 |
| 248 | 500ms | Bseindia | 0.01 MB/s | `https://bseindia.com` | 通用代理 |
| 249 | 501ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 250 | 517ms | Wl | - | `https://wl.do` | 通用代理 |
| 251 | 521ms | Aosmd | 0.1 MB/s | `https://aosmd.com` | 通用代理 |
| 252 | 523ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 253 | 531ms | Agentkey | 0.25 MB/s | `https://agentkey.app` | 通用代理 |
| 254 | 531ms | Lucky | 0.37 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 255 | 537ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 256 | 537ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 257 | 539ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 258 | 545ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 259 | 546ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 260 | 546ms | Umami-mcp | 0.32 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 261 | 551ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 262 | 557ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 263 | 558ms | Gp | 2.76 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 264 | 560ms | Gh | 2.19 MB/s | `https://gh.1k.ink` | 通用代理 |
| 265 | 575ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 266 | 579ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 267 | 579ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 268 | 587ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 269 | 591ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 270 | 592ms | Fastfile | 1.54 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 271 | 611ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 272 | 617ms | Tsukuyomi | 0.09 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 273 | 624ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 274 | 626ms | Github | 2.67 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 275 | 655ms | Github | 0.58 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 276 | 664ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 277 | 664ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 278 | 670ms | Github | 2.72 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 279 | 671ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 280 | 679ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 281 | 681ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 282 | 693ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 283 | 693ms | Support | 0.1 MB/s | `https://support.apple.com` | 通用代理 |
| 284 | 698ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 285 | 700ms | Tracely-studio | 0.04 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 286 | 705ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 287 | 707ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 288 | 708ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 289 | 716ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 290 | 732ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 291 | 732ms | Wordpaper | 0.85 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 292 | 745ms | Ghproxy | 0.29 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 293 | 748ms | Aif | 0.03 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 294 | 756ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 295 | 763ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 296 | 764ms | Onetwin | 0.03 MB/s | `https://onetwin.cn` | 通用代理 |
| 297 | 767ms | Anh | 0.24 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 298 | 775ms | Docs | 0.15 MB/s | `https://docs.transifex.com` | 通用代理 |
| 299 | 781ms | Os | 0.03 MB/s | `https://os.ryo.lu` | 通用代理 |
| 300 | 802ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 301 | 812ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 302 | 814ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 303 | 824ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 304 | 834ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 305 | 843ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 306 | 843ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 307 | 859ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 308 | 864ms | Ccgather | 0.05 MB/s | `https://ccgather.com` | 通用代理 |
| 309 | 865ms | Git | 0.24 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 310 | 867ms | Tools | 2.33 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 311 | 870ms | Dbgate | 0.15 MB/s | `https://dbgate.org` | 通用代理 |
| 312 | 908ms | Ginlix | 0.34 MB/s | `https://ginlix.ai` | 通用代理 |
| 313 | 911ms | Github | 2.0 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 314 | 913ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 315 | 921ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 316 | 931ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 317 | 939ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 318 | 939ms | Web | - | `https://web.4399.com` | 通用代理 |
| 319 | 946ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 320 | 952ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 321 | 964ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 322 | 965ms | Mimo | 0.19 MB/s | `https://mimo.mi.com` | 通用代理 |
| 323 | 969ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 324 | 986ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 325 | 990ms | Dimagent | 0.24 MB/s | `https://dimagent.com` | 通用代理 |
| 326 | 1027ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 327 | 1039ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 328 | 1047ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 329 | 1047ms | Kenyu | 1.92 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 330 | 1068ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 331 | 1075ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 332 | 1079ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 333 | 1114ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 334 | 1116ms | V | - | `https://v.douyin.com` | 通用代理 |
| 335 | 1124ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 336 | 1129ms | Github | 2.37 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 337 | 1146ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 338 | 1154ms | Your-domain | 0.08 MB/s | `https://your-domain.com` | 通用代理 |
| 339 | 1170ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 340 | 1178ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 341 | 1201ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 342 | 1208ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 343 | 1218ms | Ghproxy | 0.34 MB/s | `https://ghproxy.cc` | 通用代理 |
| 344 | 1222ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 345 | 1232ms | Gh | 0.09 MB/s | `https://gh.dpik.top` | 通用代理 |
| 346 | 1248ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 347 | 1261ms | Atomcode | 0.04 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 348 | 1263ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 349 | 1268ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 350 | 1299ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 351 | 1331ms | Gh | 1.54 MB/s | `https://gh.39.al` | 通用代理 |
| 352 | 1340ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 353 | 1340ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 354 | 1346ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 355 | 1356ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 356 | 1368ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 357 | 1374ms | Github | 0.17 MB/s | `https://github.chenc.dev` | 通用代理 |
| 358 | 1377ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 359 | 1395ms | Cf | 0.34 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 360 | 1402ms | Gh | 0.69 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 361 | 1446ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 362 | 1456ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 363 | 1491ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 364 | 1542ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 365 | 1570ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 366 | 1645ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 367 | 1702ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 368 | 1734ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 369 | 1740ms | Cumora | 0.39 MB/s | `https://cumora.ai` | 通用代理 |
| 370 | 1779ms | Git | 0.59 MB/s | `https://git.669966.xyz` | 通用代理 |
| 371 | 1962ms | Cfkua | 1.97 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 372 | 2075ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 373 | 2129ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 374 | 2190ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 375 | 2222ms | Img | - | `https://img.ink` | 通用代理 |
| 376 | 2263ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 377 | 2631ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 378 | 2650ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 379 | 2698ms | Ghproxy | 0.04 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 380 | 2754ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 381 | 2974ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 382 | 3191ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 383 | 3197ms | Gh | 0.12 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 384 | 3997ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（15 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 5 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 11 次 |
| GitClone (`gitclone-com`) | 6 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| G (`g-blfrp-cn`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Comfyit (`comfyit-cn`) | 1 次 |
| Proxy (`proxy-vvvv-ee`) | 6 次 |
| 5555 (`5555-cab`) | 23 次 |
| Doxygen (`doxygen-org`) | 19 次 |
| Axonhub (`axonhub-onrender-com`) | 1 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 2 次 |
| Maplecode (`maplecode-art`) | 12 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 8 次 |
| Adult (`adult-contents-fc2-com`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 392 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **399** | |

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
