# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-30T12:15:33Z**，每 6 小时刷新一次。当前 ✅ **386** 在线 / ⚠️ **16** 不稳定 / ⚰️ **52** 已失效归档。

## 核心特性

- **402 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 59ms | Microsoftedge | 1.06 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 63ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 3 | 71ms | Linkedin | 0.48 MB/s | `https://linkedin.com` | 通用代理 |
| 4 | 78ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 5 | 79ms | App | 0.23 MB/s | `https://app.netlify.com` | 通用代理 |
| 6 | 82ms | Githubstatus | 1.97 MB/s | `https://githubstatus.com` | 通用代理 |
| 7 | 83ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 8 | 86ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 9 | 88ms | Godocs | 0.08 MB/s | `https://godocs.io` | 通用代理 |
| 10 | 96ms | Lawyer-yu | 0.2 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 11 | 98ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 12 | 99ms | Zebrunner | 2.88 MB/s | `https://zebrunner.com` | 通用代理 |
| 13 | 100ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 14 | 100ms | X | 1.72 MB/s | `https://x.com` | 通用代理 |
| 15 | 102ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 16 | 102ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 17 | 103ms | Deno | 0.43 MB/s | `https://deno.com` | 通用代理 |
| 18 | 104ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 19 | 111ms | Xjtu-nyxf-study-material | 0.19 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 20 | 116ms | Goreportcard | 0.07 MB/s | `https://goreportcard.com` | 通用代理 |
| 21 | 118ms | Opentakeoff | 0.09 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 22 | 118ms | Resume-5lv | 0.2 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 23 | 118ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 24 | 119ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 25 | 120ms | Music-cli | 0.56 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 26 | 122ms | App | 0.06 MB/s | `https://app.codecov.io` | 通用代理 |
| 27 | 125ms | Discord | 0.12 MB/s | `https://discord.gg` | 通用代理 |
| 28 | 127ms | Opresume | 0.26 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 29 | 128ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 30 | 134ms | Components | 0.11 MB/s | `https://components.dereekb.com` | 通用代理 |
| 31 | 136ms | Img | - | `https://img.shields.io` | 通用代理 |
| 32 | 136ms | Training | 0.25 MB/s | `https://training.ti.com` | 通用代理 |
| 33 | 139ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 34 | 143ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 35 | 144ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 36 | 144ms | Nextup-resource | 0.05 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 37 | 144ms | Opensunsama | 0.09 MB/s | `https://opensunsama.com` | 通用代理 |
| 38 | 145ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 39 | 145ms | Impeccable | 0.55 MB/s | `https://impeccable.style` | 通用代理 |
| 40 | 146ms | Osf | 0.03 MB/s | `https://osf.io` | 通用代理 |
| 41 | 149ms | Bolt2github | 0.06 MB/s | `https://bolt2github.com` | 通用代理 |
| 42 | 149ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 43 | 154ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 44 | 156ms | Git | 2.94 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 45 | 156ms | Kighelper-cloud | 0.09 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 46 | 157ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 47 | 157ms | Ode | - | `https://ode.fun` | 通用代理 |
| 48 | 157ms | Shiori-v1 | 0.04 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 49 | 159ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 50 | 160ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 51 | 160ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 52 | 161ms | Caw | 0.05 MB/s | `https://caw.rocks` | 通用代理 |
| 53 | 161ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 54 | 163ms | Play | 0.02 MB/s | `https://play.templatical.com` | 通用代理 |
| 55 | 164ms | Git | 2.46 MB/s | `https://git.820828.xyz` | 通用代理 |
| 56 | 164ms | Github | 2.87 MB/s | `https://github.788787.xyz` | 通用代理 |
| 57 | 164ms | Tms | 0.18 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 58 | 166ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 59 | 166ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 60 | 167ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 61 | 168ms | Vibesql | 0.16 MB/s | `https://vibesql.org` | 通用代理 |
| 62 | 169ms | Gitea-mirror | 0.64 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 63 | 171ms | Clypra | 0.1 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 64 | 171ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 65 | 172ms | Tokei | 0.6 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 66 | 173ms | L4d2 | 0.16 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 67 | 175ms | Openpua | 0.51 MB/s | `https://openpua.ai` | 通用代理 |
| 68 | 176ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 69 | 176ms | Crypto-funding-arbitrage | 0.08 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 70 | 177ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 71 | 177ms | Ghproxy | 2.3 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 72 | 177ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 73 | 178ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 74 | 179ms | Axios-http | 1.34 MB/s | `https://axios-http.com` | 通用代理 |
| 75 | 179ms | Dilo-d14 | 0.19 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 76 | 180ms | Ai-trend-publish | 0.06 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 77 | 180ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 78 | 180ms | Caiji | 0.08 MB/s | `https://caiji.cyou` | 通用代理 |
| 79 | 180ms | Gh | 1.92 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 80 | 181ms | Github | 2.62 MB/s | `https://github.880824.xyz` | 通用代理 |
| 81 | 182ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 82 | 182ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 83 | 185ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 84 | 185ms | Glass | 0.19 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 85 | 186ms | Bestdori | 0.11 MB/s | `https://bestdori.com` | 通用代理 |
| 86 | 188ms | Cody | 0.24 MB/s | `https://cody.todyle.com` | 通用代理 |
| 87 | 189ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 88 | 189ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 89 | 189ms | GH Monlor | 1.77 MB/s | `https://gh.monlor.com` | 通用代理 |
| 90 | 189ms | GH-Proxy | 1.64 MB/s | `https://gh-proxy.com` | 通用代理 |
| 91 | 190ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 92 | 192ms | Cognitum | 0.09 MB/s | `https://cognitum.one` | 通用代理 |
| 93 | 195ms | Github | 1.78 MB/s | `https://github.ihnic.com` | 通用代理 |
| 94 | 195ms | Twitter | 0.92 MB/s | `https://twitter.com` | 通用代理 |
| 95 | 196ms | Cbrowser | 2.0 MB/s | `https://cbrowser.ai` | 通用代理 |
| 96 | 196ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 97 | 196ms | Radio-browser | 0.06 MB/s | `https://radio-browser.info` | 通用代理 |
| 98 | 199ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 99 | 200ms | Ghproxy | 2.05 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 100 | 202ms | Aiblackboxfc | 0.32 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 101 | 202ms | Clayrune | 0.17 MB/s | `https://clayrune.io` | 通用代理 |
| 102 | 203ms | Alas | 1.12 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 103 | 203ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 104 | 204ms | Coreos | 5.21 MB/s | `https://coreos.com` | 通用代理 |
| 105 | 204ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 106 | 204ms | Polgarand | 0.09 MB/s | `https://polgarand.org` | 通用代理 |
| 107 | 205ms | Codeeraser | 0.09 MB/s | `https://codeeraser.dev` | 通用代理 |
| 108 | 205ms | Hopp | 0.04 MB/s | `https://hopp.sh` | 通用代理 |
| 109 | 205ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 110 | 207ms | Docs | 0.04 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 111 | 209ms | Coffeecli | 0.13 MB/s | `https://coffeecli.com` | 通用代理 |
| 112 | 211ms | Ampcode | 0.33 MB/s | `https://ampcode.com` | 通用代理 |
| 113 | 212ms | Themolt | 0.07 MB/s | `https://themolt.net` | 通用代理 |
| 114 | 213ms | Thumb | 0.49 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 115 | 214ms | Cursor | 1.04 MB/s | `https://cursor.com` | 通用代理 |
| 116 | 214ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 117 | 215ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 118 | 216ms | Cherryai | 0.07 MB/s | `https://cherryai.com` | 通用代理 |
| 119 | 218ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 120 | 220ms | Ai-watch | 0.04 MB/s | `https://ai-watch.dev` | 通用代理 |
| 121 | 220ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 122 | 231ms | Agoramarket | 0.03 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 123 | 232ms | Sub | 0.28 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 124 | 236ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 125 | 237ms | Sina | 0.68 MB/s | `https://sina.dev` | 通用代理 |
| 126 | 239ms | Ghproxy | 0.3 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 127 | 239ms | Gsd | 0.43 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 128 | 242ms | Ggg | 2.61 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 129 | 243ms | GH-Proxy Org | 0.98 MB/s | `https://gh-proxy.org` | 通用代理 |
| 130 | 243ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 131 | 245ms | Agentlimb | 0.27 MB/s | `https://agentlimb.com` | 通用代理 |
| 132 | 246ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 133 | 246ms | Opencovibe | 0.44 MB/s | `https://opencovibe.com` | 通用代理 |
| 134 | 249ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 135 | 254ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 136 | 254ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 137 | 256ms | Travis-ci | 0.31 MB/s | `https://travis-ci.org` | 通用代理 |
| 138 | 258ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 139 | 259ms | Github | 0.55 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 140 | 260ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 141 | 260ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 142 | 267ms | Microcoreos | 0.4 MB/s | `https://microcoreos.com` | 通用代理 |
| 143 | 267ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 144 | 268ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 145 | 269ms | Visionmemorymcp | 0.2 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 146 | 270ms | Aka | 0.81 MB/s | `https://aka.ms` | 通用代理 |
| 147 | 270ms | Flashtype | - | `https://flashtype.com` | 通用代理 |
| 148 | 272ms | Code | 0.99 MB/s | `https://code.claude.com` | 通用代理 |
| 149 | 272ms | Youtu | 2.32 MB/s | `https://youtu.be` | 通用代理 |
| 150 | 274ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 151 | 277ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 152 | 278ms | Agenticcorporation | 0.06 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 153 | 279ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 154 | 281ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 155 | 282ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 156 | 287ms | CrashMC CDN | 1.88 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 157 | 288ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 158 | 294ms | Api | 0.05 MB/s | `https://api.solov.cc` | 通用代理 |
| 159 | 297ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 160 | 299ms | Tiktok | 0.22 MB/s | `https://tiktok.com` | 通用代理 |
| 161 | 301ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 162 | 301ms | Nisar | 0.87 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 163 | 301ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 164 | 305ms | Bananaslides | 0.26 MB/s | `https://bananaslides.online` | 通用代理 |
| 165 | 307ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 166 | 308ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 167 | 309ms | Kuroutoshikou | 0.11 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 168 | 310ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 169 | 311ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 170 | 312ms | Gh | 0.09 MB/s | `https://gh.padao.fun` | 通用代理 |
| 171 | 312ms | Turborepo-starter-kit-web | 0.13 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 172 | 315ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 173 | 319ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 174 | 319ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 175 | 322ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 176 | 322ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 177 | 323ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 178 | 323ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 179 | 323ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 180 | 324ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 181 | 325ms | Steamcommunity | 0.18 MB/s | `https://steamcommunity.com` | 通用代理 |
| 182 | 326ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 183 | 335ms | B23 | - | `https://b23.tv` | 通用代理 |
| 184 | 339ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 185 | 340ms | Sonarcloud | 0.15 MB/s | `https://sonarcloud.io` | 通用代理 |
| 186 | 342ms | 30006000 | 0.07 MB/s | `https://30006000.xyz` | 通用代理 |
| 187 | 342ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 188 | 342ms | Autonomi | 0.03 MB/s | `https://autonomi.dev` | 通用代理 |
| 189 | 342ms | Claude | 0.35 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 190 | 344ms | FastGit CC | 1.41 MB/s | `https://fastgit.cc` | 通用代理 |
| 191 | 344ms | Gpui | 0.16 MB/s | `https://gpui.rs` | 通用代理 |
| 192 | 344ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 193 | 359ms | Store | 1.17 MB/s | `https://store.steampowered.com` | 通用代理 |
| 194 | 369ms | GHFast | - | `https://ghfast.top` | 通用代理 |
| 195 | 372ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 196 | 372ms | Serac | 0.08 MB/s | `https://serac.build` | 通用代理 |
| 197 | 375ms | App | 0.02 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 198 | 375ms | Contrib | 0.3 MB/s | `https://contrib.rocks` | 通用代理 |
| 199 | 375ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 200 | 377ms | Readsync | 0.05 MB/s | `https://readsync.org` | 通用代理 |
| 201 | 384ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 202 | 386ms | Weaverse | 1.12 MB/s | `https://weaverse.io` | 通用代理 |
| 203 | 388ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 204 | 388ms | Im | 0.59 MB/s | `https://im.codes` | 通用代理 |
| 205 | 389ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 206 | 391ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 207 | 392ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 208 | 392ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 209 | 393ms | Bailian | 0.05 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 210 | 393ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 211 | 399ms | Ednovas Mirror | - | `https://github.ednovas.xyz` | 通用代理 |
| 212 | 406ms | GH Nxnow | 0.59 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 213 | 407ms | Api | - | `https://api.river.ai` | 通用代理 |
| 214 | 410ms | Getgit | 2.36 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 215 | 411ms | V4 | 1.7 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 216 | 413ms | Msdn | 0.14 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 217 | 417ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 218 | 418ms | Hk | 1.23 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 219 | 419ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 220 | 423ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 221 | 428ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 222 | 428ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 223 | 436ms | YYLX Git | - | `https://git.yylx.win` | 通用代理 |
| 224 | 438ms | Tvv | 1.64 MB/s | `https://tvv.tw` | 通用代理 |
| 225 | 439ms | Bible-ai-explorer | 0.08 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 226 | 439ms | Lecvdemarius | 0.18 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 227 | 442ms | Safedocx | 0.15 MB/s | `https://safedocx.com` | 通用代理 |
| 228 | 445ms | Huly-mcp | 0.14 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 229 | 453ms | You | 0.08 MB/s | `https://you.piccalc.com` | 通用代理 |
| 230 | 456ms | Gh | 2.19 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 231 | 456ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 232 | 457ms | Aps | 0.07 MB/s | `https://aps.com` | 通用代理 |
| 233 | 460ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 234 | 465ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 235 | 466ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 236 | 473ms | Ark | 0.48 MB/s | `https://ark.intel.com` | 通用代理 |
| 237 | 480ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 238 | 483ms | Lucky | 0.66 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 239 | 484ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 240 | 487ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 241 | 487ms | Patchworkos | 0.4 MB/s | `https://patchworkos.com` | 通用代理 |
| 242 | 499ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 243 | 500ms | Memstack | 0.03 MB/s | `https://memstack.pro` | 通用代理 |
| 244 | 501ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 245 | 502ms | Adult | 0.01 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 246 | 502ms | Aosmd | 0.15 MB/s | `https://aosmd.com` | 通用代理 |
| 247 | 506ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 248 | 507ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 249 | 509ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 250 | 512ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 251 | 514ms | Wl | - | `https://wl.do` | 通用代理 |
| 252 | 520ms | Impro | 2.03 MB/s | `https://impro.social` | 通用代理 |
| 253 | 529ms | 3d-set-visualizer | 0.04 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 254 | 540ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 255 | 547ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 256 | 548ms | Clawbiz | 0.04 MB/s | `https://clawbiz.io` | 通用代理 |
| 257 | 548ms | Gh | 0.41 MB/s | `https://gh.noki.icu` | 通用代理 |
| 258 | 554ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 259 | 561ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 260 | 571ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 261 | 572ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 262 | 572ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 263 | 573ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 264 | 573ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 265 | 573ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 266 | 573ms | Gp | 3.27 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 267 | 579ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 268 | 580ms | Fastfile | 1.61 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 269 | 594ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 270 | 609ms | Gh | 2.01 MB/s | `https://gh.1k.ink` | 通用代理 |
| 271 | 614ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 272 | 623ms | Umami-mcp | 0.53 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 273 | 626ms | Bseindia | 0.04 MB/s | `https://bseindia.com` | 通用代理 |
| 274 | 634ms | Github | 3.28 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 275 | 646ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 276 | 659ms | Agoracitizen | 0.03 MB/s | `https://agoracitizen.app` | 通用代理 |
| 277 | 660ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 278 | 663ms | Github | 2.63 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 279 | 671ms | Github | 0.16 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 280 | 674ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 281 | 676ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 282 | 680ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 283 | 681ms | Internhack | 0.05 MB/s | `https://internhack.xyz` | 通用代理 |
| 284 | 681ms | Support | 0.1 MB/s | `https://support.apple.com` | 通用代理 |
| 285 | 691ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 286 | 692ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 287 | 697ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 288 | 698ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 289 | 699ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 290 | 724ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 291 | 725ms | Agentkey | 0.73 MB/s | `https://agentkey.app` | 通用代理 |
| 292 | 734ms | Wordpaper | 0.51 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 293 | 735ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 294 | 747ms | Congressmcp | 0.04 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 295 | 752ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 296 | 758ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 297 | 759ms | Aif | 0.06 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 298 | 765ms | Docs | 0.28 MB/s | `https://docs.transifex.com` | 通用代理 |
| 299 | 767ms | Ghproxy | 0.25 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 300 | 778ms | Anh | 0.23 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 301 | 791ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 302 | 793ms | Dbgate | 0.24 MB/s | `https://dbgate.org` | 通用代理 |
| 303 | 793ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 304 | 802ms | Cumora | 0.28 MB/s | `https://cumora.ai` | 通用代理 |
| 305 | 820ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 306 | 837ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 307 | 839ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 308 | 848ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 309 | 850ms | Tools | 3.05 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 310 | 850ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 311 | 854ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 312 | 880ms | Kw-aigc | - | `https://kw-aigc.cn` | 通用代理 |
| 313 | 881ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 314 | 897ms | Git | 0.21 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 315 | 918ms | Web | - | `https://web.4399.com` | 通用代理 |
| 316 | 921ms | Yibiao | 0.11 MB/s | `https://yibiao.pro` | 通用代理 |
| 317 | 927ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 318 | 929ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 319 | 931ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 320 | 937ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 321 | 950ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 322 | 952ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 323 | 953ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 324 | 969ms | Ginlix | 0.52 MB/s | `https://ginlix.ai` | 通用代理 |
| 325 | 980ms | Github | 2.29 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 326 | 983ms | Mimo | 0.16 MB/s | `https://mimo.mi.com` | 通用代理 |
| 327 | 986ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 328 | 999ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 329 | 1036ms | Cfkua | 2.35 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 330 | 1038ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 331 | 1053ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 332 | 1060ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 333 | 1069ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 334 | 1076ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 335 | 1080ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 336 | 1081ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 337 | 1087ms | V | - | `https://v.douyin.com` | 通用代理 |
| 338 | 1090ms | Kenyu | 2.09 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 339 | 1134ms | Dimagent | 0.13 MB/s | `https://dimagent.com` | 通用代理 |
| 340 | 1152ms | GHProxy Net | 0.04 MB/s | `https://ghproxy.net` | 通用代理 |
| 341 | 1177ms | Github | 2.53 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 342 | 1190ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 343 | 1192ms | Ghproxy | 0.17 MB/s | `https://ghproxy.cc` | 通用代理 |
| 344 | 1210ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 345 | 1210ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 346 | 1239ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 347 | 1250ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 348 | 1258ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 349 | 1261ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 350 | 1293ms | Gh | 0.94 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 351 | 1297ms | Atomcode | 0.03 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 352 | 1320ms | Github | 0.14 MB/s | `https://github.chenc.dev` | 通用代理 |
| 353 | 1331ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 354 | 1350ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 355 | 1353ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 356 | 1369ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 357 | 1376ms | Gh | 0.09 MB/s | `https://gh.39.al` | 通用代理 |
| 358 | 1395ms | Cf | 0.1 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 359 | 1399ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 360 | 1404ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 361 | 1423ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 362 | 1453ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 363 | 1453ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 364 | 1486ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 365 | 1536ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 366 | 1659ms | I-qps | 0.02 MB/s | `https://i-qps.net` | 通用代理 |
| 367 | 1704ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 368 | 1804ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 369 | 1811ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 370 | 1833ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 371 | 1845ms | Git | 0.28 MB/s | `https://git.669966.xyz` | 通用代理 |
| 372 | 2117ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 373 | 2136ms | Img | - | `https://img.ink` | 通用代理 |
| 374 | 2192ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 375 | 2274ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 376 | 2283ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 377 | 2323ms | Provider | - | `https://provider.com` | 通用代理 |
| 378 | 2326ms | Gh | 0.22 MB/s | `https://gh.dpik.top` | 通用代理 |
| 379 | 2345ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 380 | 2454ms | G | 0.01 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 381 | 2648ms | Tcl | 0.01 MB/s | `https://tcl.tk` | 通用代理 |
| 382 | 2727ms | Ghproxy | 0.04 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 383 | 2785ms | Wget | 0.07 MB/s | `https://wget.la` | 通用代理 |
| 384 | 3090ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 385 | 3225ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 386 | 3496ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（16 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 17 次 |
| Gh (`gh-llkk-cc`) | 1 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Gh (`gh-b52m-cn`) | 4 次 |
| Proxy (`proxy-vvvv-ee`) | 5 次 |
| Nssurge (`nssurge-com`) | 3 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 3 次 |
| Doxygen (`doxygen-org`) | 25 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 8 次 |
| Maplecode (`maplecode-art`) | 18 次 |
| Mobilevc (`mobilevc-top`) | 1 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 14 次 |
| Git (`git-net2o-de`) | 1 次 |
| Savannah (`savannah-gnu-org`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 395 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **402** | |

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
