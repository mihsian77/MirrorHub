# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-31T04:18:10Z**，每 6 小时刷新一次。当前 ✅ **390** 在线 / ⚠️ **17** 不稳定 / ⚰️ **52** 已失效归档。

## 核心特性

- **407 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 59ms | Microsoftedge | 0.81 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 77ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 3 | 79ms | Linkedin | 0.29 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 81ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 5 | 81ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 6 | 89ms | Githubstatus | 1.55 MB/s | `https://githubstatus.com` | 通用代理 |
| 7 | 94ms | Godocs | 0.04 MB/s | `https://godocs.io` | 通用代理 |
| 8 | 96ms | App | 0.06 MB/s | `https://app.netlify.com` | 通用代理 |
| 9 | 97ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 10 | 98ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 11 | 99ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 12 | 99ms | X | 1.8 MB/s | `https://x.com` | 通用代理 |
| 13 | 101ms | Zebrunner | 1.53 MB/s | `https://zebrunner.com` | 通用代理 |
| 14 | 102ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 15 | 106ms | Xjtu-nyxf-study-material | 0.18 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 16 | 107ms | Lawyer-yu | 0.05 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 17 | 108ms | Resume-5lv | 0.2 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 18 | 110ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 19 | 112ms | Deno | 0.23 MB/s | `https://deno.com` | 通用代理 |
| 20 | 114ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 21 | 115ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 22 | 117ms | Megacrit | 0.2 MB/s | `https://megacrit.com` | 通用代理 |
| 23 | 119ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 24 | 119ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 25 | 120ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 26 | 125ms | Opresume | 0.51 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 27 | 126ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 28 | 127ms | Impeccable | 1.66 MB/s | `https://impeccable.style` | 通用代理 |
| 29 | 133ms | Opentakeoff | 0.03 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 30 | 134ms | Music-cli | 0.16 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 31 | 139ms | Components | 0.11 MB/s | `https://components.dereekb.com` | 通用代理 |
| 32 | 142ms | Discord | 0.08 MB/s | `https://discord.gg` | 通用代理 |
| 33 | 146ms | Training | 0.24 MB/s | `https://training.ti.com` | 通用代理 |
| 34 | 147ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 35 | 150ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 36 | 150ms | Opensunsama | 0.05 MB/s | `https://opensunsama.com` | 通用代理 |
| 37 | 151ms | Img | - | `https://img.shields.io` | 通用代理 |
| 38 | 151ms | Kighelper-cloud | 0.11 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 39 | 156ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 40 | 157ms | Git | - | `https://git.951959483.xyz` | 通用代理 |
| 41 | 157ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 42 | 162ms | Ghproxy | - | `https://ghproxy.imciel.com` | 通用代理 |
| 43 | 162ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 44 | 163ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 45 | 164ms | Play | 0.03 MB/s | `https://play.templatical.com` | 通用代理 |
| 46 | 166ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 47 | 166ms | Gitea-mirror | 0.48 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 48 | 167ms | Git | - | `https://git.820828.xyz` | 通用代理 |
| 49 | 168ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 50 | 170ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 51 | 170ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 52 | 170ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 53 | 170ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 54 | 171ms | Caiji | - | `https://caiji.cyou` | 通用代理 |
| 55 | 171ms | Crypto-funding-arbitrage | 0.08 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 56 | 171ms | Openpua | 0.39 MB/s | `https://openpua.ai` | 通用代理 |
| 57 | 173ms | Caw | 0.03 MB/s | `https://caw.rocks` | 通用代理 |
| 58 | 173ms | Gh | - | `https://gh.996986.xyz` | 通用代理 |
| 59 | 173ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 60 | 173ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 61 | 174ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 62 | 175ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 63 | 175ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 64 | 176ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 65 | 177ms | Github | - | `https://github.788787.xyz` | 通用代理 |
| 66 | 177ms | Ode | - | `https://ode.fun` | 通用代理 |
| 67 | 177ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 68 | 178ms | Codeeraser | 0.07 MB/s | `https://codeeraser.dev` | 通用代理 |
| 69 | 178ms | Vibesql | 0.07 MB/s | `https://vibesql.org` | 通用代理 |
| 70 | 179ms | Dilo-d14 | 0.22 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 71 | 179ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 72 | 179ms | Tokei | 0.38 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 73 | 180ms | Cody | 0.16 MB/s | `https://cody.todyle.com` | 通用代理 |
| 74 | 180ms | Freeport | 0.02 MB/s | `https://freeport.network` | 通用代理 |
| 75 | 180ms | Glass | 0.16 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 76 | 180ms | Tms | 0.09 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 77 | 181ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 78 | 181ms | L4d2 | 0.06 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 79 | 183ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 80 | 183ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 81 | 183ms | GH-Proxy | 1.32 MB/s | `https://gh-proxy.com` | 通用代理 |
| 82 | 184ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 83 | 185ms | Axios-http | 0.32 MB/s | `https://axios-http.com` | 通用代理 |
| 84 | 185ms | Github | - | `https://github.880824.xyz` | 通用代理 |
| 85 | 187ms | Polgarand | 0.05 MB/s | `https://polgarand.org` | 通用代理 |
| 86 | 188ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 87 | 190ms | Bestdori | 0.1 MB/s | `https://bestdori.com` | 通用代理 |
| 88 | 190ms | GH Monlor | 1.25 MB/s | `https://gh.monlor.com` | 通用代理 |
| 89 | 190ms | Twitter | 1.03 MB/s | `https://twitter.com` | 通用代理 |
| 90 | 196ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 91 | 196ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 92 | 196ms | Miaozitie | 0.04 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 93 | 197ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 94 | 199ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 95 | 200ms | Clypra | 0.09 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 96 | 200ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 97 | 201ms | Alas | 0.72 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 98 | 202ms | Ghproxy | - | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 99 | 205ms | Github | - | `https://github.ihnic.com` | 通用代理 |
| 100 | 205ms | Radio-browser | 0.01 MB/s | `https://radio-browser.info` | 通用代理 |
| 101 | 206ms | Pidash | 0.06 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 102 | 207ms | Coffeecli | 0.08 MB/s | `https://coffeecli.com` | 通用代理 |
| 103 | 208ms | Cbrowser | 0.9 MB/s | `https://cbrowser.ai` | 通用代理 |
| 104 | 208ms | Clayrune | 0.13 MB/s | `https://clayrune.io` | 通用代理 |
| 105 | 209ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 106 | 209ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 107 | 210ms | Demo | 0.03 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 108 | 211ms | Cherryai | 0.03 MB/s | `https://cherryai.com` | 通用代理 |
| 109 | 212ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 110 | 212ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 111 | 215ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 112 | 216ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 113 | 217ms | Cognitum | 0.12 MB/s | `https://cognitum.one` | 通用代理 |
| 114 | 221ms | Agoramarket | 0.04 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 115 | 221ms | Aiblackboxfc | 0.23 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 116 | 221ms | Ampcode | 0.15 MB/s | `https://ampcode.com` | 通用代理 |
| 117 | 221ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 118 | 223ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 119 | 225ms | Ghproxy | - | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 120 | 225ms | Sina | 1.04 MB/s | `https://sina.dev` | 通用代理 |
| 121 | 226ms | Docs | 0.05 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 122 | 228ms | Coreos | 1.84 MB/s | `https://coreos.com` | 通用代理 |
| 123 | 229ms | Ggg | - | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 124 | 229ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 125 | 231ms | Themolt | 0.02 MB/s | `https://themolt.net` | 通用代理 |
| 126 | 231ms | Thumb | 0.75 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 127 | 234ms | GH-Proxy Org | 1.35 MB/s | `https://gh-proxy.org` | 通用代理 |
| 128 | 235ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 129 | 240ms | Agentlimb | 0.21 MB/s | `https://agentlimb.com` | 通用代理 |
| 130 | 240ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 131 | 244ms | Chops | 0.02 MB/s | `https://chops.md` | 通用代理 |
| 132 | 246ms | Opencovibe | 0.35 MB/s | `https://opencovibe.com` | 通用代理 |
| 133 | 247ms | Cursor | 0.41 MB/s | `https://cursor.com` | 通用代理 |
| 134 | 251ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 135 | 251ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 136 | 253ms | Gsd | 0.08 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 137 | 255ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 138 | 256ms | Github | - | `https://github.cnxiaobai.com` | 通用代理 |
| 139 | 256ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 140 | 257ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 141 | 259ms | Microcoreos | 0.25 MB/s | `https://microcoreos.com` | 通用代理 |
| 142 | 262ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 143 | 263ms | Youtu | 2.14 MB/s | `https://youtu.be` | 通用代理 |
| 144 | 265ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 145 | 266ms | Api | 0.12 MB/s | `https://api.solov.cc` | 通用代理 |
| 146 | 266ms | Visionmemorymcp | 0.53 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 147 | 267ms | Kuroutoshikou | 0.6 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 148 | 268ms | Code | 2.13 MB/s | `https://code.claude.com` | 通用代理 |
| 149 | 272ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 150 | 277ms | Travis-ci | 0.1 MB/s | `https://travis-ci.org` | 通用代理 |
| 151 | 278ms | Aka | 0.51 MB/s | `https://aka.ms` | 通用代理 |
| 152 | 278ms | Flashtype | 0.09 MB/s | `https://flashtype.com` | 通用代理 |
| 153 | 279ms | GHFast | - | `https://ghfast.top` | 通用代理 |
| 154 | 279ms | Phabricator | 0.03 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 155 | 279ms | Savannah | 0.02 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 156 | 281ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 157 | 283ms | Gh | - | `https://gh.padao.fun` | 通用代理 |
| 158 | 283ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 159 | 284ms | Bananaslides | 0.43 MB/s | `https://bananaslides.online` | 通用代理 |
| 160 | 287ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 161 | 291ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 162 | 292ms | CrashMC CDN | - | `https://cdn.crashmc.com` | 通用代理 |
| 163 | 294ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 164 | 295ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 165 | 295ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 166 | 298ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 167 | 299ms | FastGit CC | 1.13 MB/s | `https://fastgit.cc` | 通用代理 |
| 168 | 299ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 169 | 303ms | Nisar | 0.59 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 170 | 305ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 171 | 313ms | Tiktok | 0.09 MB/s | `https://tiktok.com` | 通用代理 |
| 172 | 314ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 173 | 314ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 174 | 315ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 175 | 317ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 176 | 318ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 177 | 318ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 178 | 319ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 179 | 321ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 180 | 322ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 181 | 323ms | B23 | - | `https://b23.tv` | 通用代理 |
| 182 | 325ms | Steamcommunity | 0.14 MB/s | `https://steamcommunity.com` | 通用代理 |
| 183 | 328ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 184 | 331ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 185 | 334ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 186 | 336ms | 30006000 | - | `https://30006000.xyz` | 通用代理 |
| 187 | 338ms | Claude | 0.22 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 188 | 339ms | Sonarcloud | 1.97 MB/s | `https://sonarcloud.io` | 通用代理 |
| 189 | 347ms | Gpui | 0.16 MB/s | `https://gpui.rs` | 通用代理 |
| 190 | 348ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 191 | 348ms | Im | 0.41 MB/s | `https://im.codes` | 通用代理 |
| 192 | 349ms | Store | 1.71 MB/s | `https://store.steampowered.com` | 通用代理 |
| 193 | 351ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 194 | 354ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 195 | 365ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 196 | 365ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 197 | 368ms | Serac | 0.05 MB/s | `https://serac.build` | 通用代理 |
| 198 | 377ms | Bailian | 0.12 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 199 | 379ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 200 | 380ms | Ednovas Mirror | - | `https://github.ednovas.xyz` | 通用代理 |
| 201 | 383ms | V4 | 2.21 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 202 | 384ms | Contrib | 0.21 MB/s | `https://contrib.rocks` | 通用代理 |
| 203 | 386ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 204 | 394ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 205 | 396ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 206 | 398ms | Hk | 1.6 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 207 | 401ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 208 | 404ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 209 | 407ms | Getgit | - | `https://getgit.love8yun.eu.org` | 通用代理 |
| 210 | 407ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 211 | 410ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 212 | 412ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 213 | 413ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 214 | 417ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 215 | 421ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 216 | 421ms | Weaverse | 0.56 MB/s | `https://weaverse.io` | 通用代理 |
| 217 | 422ms | Aps | 0.09 MB/s | `https://aps.com` | 通用代理 |
| 218 | 422ms | Msdn | 0.06 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 219 | 424ms | Tvv | - | `https://tvv.tw` | 通用代理 |
| 220 | 430ms | Huly-mcp | 0.14 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 221 | 434ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 222 | 441ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 223 | 442ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 224 | 445ms | Nyx | 0.05 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 225 | 451ms | Bible-ai-explorer | 0.06 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 226 | 456ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 227 | 461ms | Gh | - | `https://gh.198962.xyz` | 通用代理 |
| 228 | 461ms | Safedocx | 0.1 MB/s | `https://safedocx.com` | 通用代理 |
| 229 | 467ms | YYLX Git | 0.34 MB/s | `https://git.yylx.win` | 通用代理 |
| 230 | 470ms | Lecvdemarius | 0.06 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 231 | 476ms | Ark | 0.81 MB/s | `https://ark.intel.com` | 通用代理 |
| 232 | 477ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 233 | 481ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 234 | 482ms | Lucky | 0.47 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 235 | 484ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 236 | 487ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 237 | 492ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 238 | 496ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 239 | 496ms | Wl | - | `https://wl.do` | 通用代理 |
| 240 | 497ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 241 | 500ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 242 | 510ms | Patchworkos | 0.23 MB/s | `https://patchworkos.com` | 通用代理 |
| 243 | 510ms | SLink | 0.06 MB/s | `https://slink.ltd` | 通用代理 |
| 244 | 511ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 245 | 516ms | Gh | - | `https://gh.idayer.com` | 通用代理 |
| 246 | 524ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 247 | 525ms | Impro | 1.37 MB/s | `https://impro.social` | 通用代理 |
| 248 | 525ms | Ygdj7 | 0.05 MB/s | `https://ygdj7.com` | 通用代理 |
| 249 | 528ms | Memstack | 0.01 MB/s | `https://memstack.pro` | 通用代理 |
| 250 | 532ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 251 | 533ms | Api | - | `https://api.river.ai` | 通用代理 |
| 252 | 537ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 253 | 539ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 254 | 541ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 255 | 550ms | Gh | 0.62 MB/s | `https://gh.noki.icu` | 通用代理 |
| 256 | 556ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 257 | 562ms | Aosmd | 0.13 MB/s | `https://aosmd.com` | 通用代理 |
| 258 | 565ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 259 | 566ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 260 | 567ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 261 | 572ms | You | 0.13 MB/s | `https://you.piccalc.com` | 通用代理 |
| 262 | 576ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 263 | 577ms | Gp | - | `https://gp.871201.xyz` | 通用代理 |
| 264 | 582ms | Agentkey | 0.48 MB/s | `https://agentkey.app` | 通用代理 |
| 265 | 598ms | Fastfile | 0.11 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 266 | 613ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 267 | 618ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 268 | 618ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 269 | 622ms | Gh | - | `https://gh.1k.ink` | 通用代理 |
| 270 | 624ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 271 | 634ms | Github | - | `https://github.zzrbk.xyz` | 通用代理 |
| 272 | 639ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 273 | 640ms | Bseindia | 0.01 MB/s | `https://bseindia.com` | 通用代理 |
| 274 | 650ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 275 | 654ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 276 | 658ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 277 | 661ms | Github | - | `https://github.1ms.xx.kg` | 通用代理 |
| 278 | 668ms | Github | 0.58 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 279 | 672ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 280 | 672ms | Umami-mcp | 0.32 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 281 | 674ms | Os | 0.03 MB/s | `https://os.ryo.lu` | 通用代理 |
| 282 | 685ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 283 | 693ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 284 | 698ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 285 | 709ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 286 | 713ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 287 | 716ms | Support | 0.12 MB/s | `https://support.apple.com` | 通用代理 |
| 288 | 723ms | Wordpaper | 0.7 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 289 | 726ms | Ghproxy | 0.4 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 290 | 726ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 291 | 729ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 292 | 737ms | Cumora | 0.24 MB/s | `https://cumora.ai` | 通用代理 |
| 293 | 743ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 294 | 750ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 295 | 759ms | Congressmcp | 0.01 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 296 | 765ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 297 | 775ms | Ccgather | 0.07 MB/s | `https://ccgather.com` | 通用代理 |
| 298 | 776ms | Anh | 0.12 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 299 | 790ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 300 | 811ms | Docs | 0.14 MB/s | `https://docs.transifex.com` | 通用代理 |
| 301 | 815ms | Dbgate | 0.12 MB/s | `https://dbgate.org` | 通用代理 |
| 302 | 819ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 303 | 825ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 304 | 830ms | Code | 0.01 MB/s | `https://code.videolan.org` | 通用代理 |
| 305 | 832ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 306 | 848ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 307 | 849ms | Tools | 2.58 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 308 | 858ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 309 | 858ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 310 | 860ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 311 | 864ms | Invent | 0.01 MB/s | `https://invent.kde.org` | 通用代理 |
| 312 | 868ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 313 | 887ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 314 | 894ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 315 | 913ms | GHFile Geekertao | 0.24 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 316 | 914ms | Yibiao | 0.15 MB/s | `https://yibiao.pro` | 通用代理 |
| 317 | 919ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 318 | 920ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 319 | 925ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 320 | 944ms | Cfkua | 1.18 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 321 | 952ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 322 | 953ms | Mimo | 0.21 MB/s | `https://mimo.mi.com` | 通用代理 |
| 323 | 967ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 324 | 977ms | Ginlix | 0.21 MB/s | `https://ginlix.ai` | 通用代理 |
| 325 | 999ms | Github | - | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 326 | 1003ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 327 | 1015ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 328 | 1034ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 329 | 1036ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 330 | 1038ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 331 | 1057ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 332 | 1064ms | Web | - | `https://web.4399.com` | 通用代理 |
| 333 | 1067ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 334 | 1076ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 335 | 1099ms | Kenyu | - | `https://kenyu.ggff.net` | 通用代理 |
| 336 | 1110ms | Dimagent | 0.14 MB/s | `https://dimagent.com` | 通用代理 |
| 337 | 1113ms | Gh | 0.55 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 338 | 1113ms | V | - | `https://v.douyin.com` | 通用代理 |
| 339 | 1116ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 340 | 1136ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 341 | 1153ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 342 | 1171ms | Ghproxy | 0.26 MB/s | `https://ghproxy.cc` | 通用代理 |
| 343 | 1175ms | Github | - | `https://github.crdz.eu.org` | 通用代理 |
| 344 | 1177ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 345 | 1186ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 346 | 1190ms | Hevolve | 0.09 MB/s | `https://hevolve.ai` | 通用代理 |
| 347 | 1202ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 348 | 1219ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 349 | 1231ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 350 | 1235ms | Github | 0.21 MB/s | `https://github.chenc.dev` | 通用代理 |
| 351 | 1237ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 352 | 1252ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 353 | 1273ms | Atomcode | 0.04 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 354 | 1310ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 355 | 1319ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 356 | 1351ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 357 | 1353ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 358 | 1384ms | Gh | 0.57 MB/s | `https://gh.39.al` | 通用代理 |
| 359 | 1385ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 360 | 1386ms | Cf | 0.25 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 361 | 1394ms | Docs | 0.02 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 362 | 1403ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 363 | 1440ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 364 | 1451ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 365 | 1467ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 366 | 1507ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 367 | 1628ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 368 | 1683ms | Heycall-e | 0.12 MB/s | `https://heycall-e.com` | 通用代理 |
| 369 | 1789ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 370 | 1790ms | Git | 0.66 MB/s | `https://git.669966.xyz` | 通用代理 |
| 371 | 1809ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 372 | 1850ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 373 | 1961ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 374 | 2051ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 375 | 2058ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 376 | 2073ms | Wget | 0.18 MB/s | `https://wget.la` | 通用代理 |
| 377 | 2086ms | Img | - | `https://img.ink` | 通用代理 |
| 378 | 2311ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 379 | 2313ms | Provider | - | `https://provider.com` | 通用代理 |
| 380 | 2334ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 381 | 2342ms | Gh | 1.07 MB/s | `https://gh.dpik.top` | 通用代理 |
| 382 | 2346ms | G | - | `https://g.blfrp.cn` | 通用代理 |
| 383 | 2363ms | Upyun | 0.01 MB/s | `https://upyun.com` | 通用代理 |
| 384 | 2695ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 385 | 2703ms | Ghproxy | 0.04 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 386 | 2708ms | Free | 0.64 MB/s | `https://free.cn.eu.org` | 通用代理 |
| 387 | 2982ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 388 | 3064ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 389 | 3481ms | GHProxy MonkeyRay | - | `https://ghproxy.monkeyray.net` | 通用代理 |
| 390 | 3764ms | Git | - | `https://git.net2o.de` | 通用代理 |


### ⚠️ 不稳定节点（17 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GH Zwnes (`gh-zwnes-xyz`) | 19 次 |
| GH Nxnow (`gh-nxnow-top`) | 1 次 |
| Gh (`gh-llkk-cc`) | 3 次 |
| Git (`git-tangbai-cc`) | 2 次 |
| Proxy (`proxy-yaoyaoling-net`) | 1 次 |
| Gh (`gh-b52m-cn`) | 6 次 |
| Proxy (`proxy-vvvv-ee`) | 7 次 |
| Sub (`sub-ikar-eu-org`) | 1 次 |
| Nssurge (`nssurge-com`) | 5 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 5 次 |
| Doxygen (`doxygen-org`) | 27 次 |
| Agenticcorporation (`agenticcorporation-net`) | 1 次 |
| Demo (`demo-mcphub-app`) | 2 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 10 次 |
| Maplecode (`maplecode-art`) | 20 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 16 次 |
| Adult (`adult-contents-fc2-com`) | 2 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 400 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **407** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（52 个）。

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
