# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-25T03:23:30Z**，每 6 小时刷新一次。当前 ✅ **366** 在线 / ⚠️ **9** 不稳定 / ⚰️ **49** 已失效归档。

## 核心特性

- **375 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 48ms | Microsoftedge | 1.07 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 54ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 3 | 57ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 4 | 68ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 69ms | Linkedin | 0.12 MB/s | `https://linkedin.com` | 通用代理 |
| 6 | 78ms | Githubstatus | 3.04 MB/s | `https://githubstatus.com` | 通用代理 |
| 7 | 81ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 8 | 82ms | Deno | 1.88 MB/s | `https://deno.com` | 通用代理 |
| 9 | 83ms | Dilo-d14 | 0.24 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 10 | 84ms | Huly-mcp | 0.19 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 11 | 85ms | Img | - | `https://img.shields.io` | 通用代理 |
| 12 | 85ms | Tools | 1.21 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 13 | 86ms | X | 1.28 MB/s | `https://x.com` | 通用代理 |
| 14 | 86ms | Xjtu-nyxf-study-material | 0.17 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 15 | 88ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 16 | 89ms | Opresume | 0.59 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 17 | 90ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 18 | 90ms | Wordpaper | 0.6 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 19 | 91ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 20 | 91ms | Kighelper-cloud | 0.1 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 21 | 92ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 22 | 96ms | Zebrunner | 3.04 MB/s | `https://zebrunner.com` | 通用代理 |
| 23 | 96ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 24 | 99ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 25 | 101ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 26 | 102ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 27 | 103ms | Alas | 1.26 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 28 | 104ms | Crypto-funding-arbitrage | 0.08 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 29 | 105ms | App | 0.13 MB/s | `https://app.netlify.com` | 通用代理 |
| 30 | 107ms | Godocs | 0.08 MB/s | `https://godocs.io` | 通用代理 |
| 31 | 107ms | Thumb | 1.09 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 32 | 111ms | Impeccable | 1.4 MB/s | `https://impeccable.style` | 通用代理 |
| 33 | 112ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 34 | 113ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 35 | 113ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 36 | 113ms | Lawyer-yu | 0.02 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 37 | 114ms | Impro | 2.26 MB/s | `https://impro.social` | 通用代理 |
| 38 | 118ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 39 | 119ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 40 | 119ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 41 | 120ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 42 | 120ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 43 | 120ms | Polgarand | 0.09 MB/s | `https://polgarand.org` | 通用代理 |
| 44 | 121ms | Resume-5lv | 0.2 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 45 | 122ms | Anh | 0.21 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 46 | 122ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 47 | 123ms | Discord | 0.1 MB/s | `https://discord.gg` | 通用代理 |
| 48 | 124ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 49 | 124ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 50 | 124ms | L4d2 | 0.16 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 51 | 124ms | Serac | 0.08 MB/s | `https://serac.build` | 通用代理 |
| 52 | 126ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 53 | 126ms | Opencovibe | 0.44 MB/s | `https://opencovibe.com` | 通用代理 |
| 54 | 127ms | Bananaslides | 0.39 MB/s | `https://bananaslides.online` | 通用代理 |
| 55 | 127ms | Clayrune | 0.2 MB/s | `https://clayrune.io` | 通用代理 |
| 56 | 127ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 57 | 128ms | Agentlimb | 0.21 MB/s | `https://agentlimb.com` | 通用代理 |
| 58 | 128ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 59 | 128ms | Tokei | 0.57 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 60 | 129ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 61 | 130ms | Codeeraser | 0.14 MB/s | `https://codeeraser.dev` | 通用代理 |
| 62 | 134ms | Coffeecli | 0.15 MB/s | `https://coffeecli.com` | 通用代理 |
| 63 | 135ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 64 | 135ms | Gh | 2.09 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 65 | 135ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 66 | 136ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 67 | 136ms | Gitea-mirror | 0.67 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 68 | 136ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 69 | 137ms | Gp | 2.36 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 70 | 139ms | Git | 2.55 MB/s | `https://git.820828.xyz` | 通用代理 |
| 71 | 139ms | Opentakeoff | 0.05 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 72 | 139ms | Vibesql | 0.1 MB/s | `https://vibesql.org` | 通用代理 |
| 73 | 140ms | Github | 2.57 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 74 | 140ms | Nextup-resource | 0.04 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 75 | 141ms | Hopp | 0.05 MB/s | `https://hopp.sh` | 通用代理 |
| 76 | 142ms | App | 0.06 MB/s | `https://app.codecov.io` | 通用代理 |
| 77 | 142ms | Github | 2.73 MB/s | `https://github.788787.xyz` | 通用代理 |
| 78 | 143ms | App | 0.02 MB/s | `https://app.opencastor.com` | 通用代理 |
| 79 | 143ms | Bestdori | 0.07 MB/s | `https://bestdori.com` | 通用代理 |
| 80 | 144ms | Git | 2.11 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 81 | 146ms | Glass | 0.26 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 82 | 146ms | Shiori-v1 | 0.03 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 83 | 148ms | Cognitum | 0.31 MB/s | `https://cognitum.one` | 通用代理 |
| 84 | 148ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 85 | 148ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 86 | 148ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 87 | 150ms | Openpua | 0.51 MB/s | `https://openpua.ai` | 通用代理 |
| 88 | 151ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 89 | 153ms | Gh | 2.56 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 90 | 154ms | Ghproxy | 3.11 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 91 | 154ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 92 | 156ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 93 | 158ms | GH Monlor | 1.04 MB/s | `https://gh.monlor.com` | 通用代理 |
| 94 | 158ms | Gh | 3.11 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 95 | 159ms | Github | 2.62 MB/s | `https://github.880824.xyz` | 通用代理 |
| 96 | 159ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 97 | 162ms | GH-Proxy | - | `https://gh-proxy.com` | 通用代理 |
| 98 | 162ms | Miaozitie | 0.1 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 99 | 162ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 100 | 163ms | Cody | 0.28 MB/s | `https://cody.todyle.com` | 通用代理 |
| 101 | 167ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 102 | 168ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 103 | 169ms | Opensunsama | 0.05 MB/s | `https://opensunsama.com` | 通用代理 |
| 104 | 170ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 105 | 171ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 106 | 172ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 107 | 173ms | Twitter | 1.18 MB/s | `https://twitter.com` | 通用代理 |
| 108 | 174ms | Axios-http | 0.56 MB/s | `https://axios-http.com` | 通用代理 |
| 109 | 174ms | Pidash | 0.04 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 110 | 175ms | Ai-trend-publish | 0.03 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 111 | 176ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 112 | 177ms | Music-cli | 0.27 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 113 | 177ms | Tms | 0.23 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 114 | 181ms | Github | 2.4 MB/s | `https://github.ihnic.com` | 通用代理 |
| 115 | 181ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 116 | 184ms | Training | 0.26 MB/s | `https://training.ti.com` | 通用代理 |
| 117 | 185ms | Contrib | 0.44 MB/s | `https://contrib.rocks` | 通用代理 |
| 118 | 186ms | Phabricator | 0.09 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 119 | 187ms | Ghproxy | 1.99 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 120 | 187ms | Holyclaude | 0.16 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 121 | 188ms | Ampcode | 0.2 MB/s | `https://ampcode.com` | 通用代理 |
| 122 | 188ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 123 | 188ms | Wings | 0.04 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 124 | 189ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 125 | 190ms | Tvv | 1.86 MB/s | `https://tvv.tw` | 通用代理 |
| 126 | 190ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 127 | 192ms | Ode | - | `https://ode.fun` | 通用代理 |
| 128 | 192ms | Openttd | 0.07 MB/s | `https://openttd.org` | 通用代理 |
| 129 | 193ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 130 | 194ms | Bolt2github | 0.02 MB/s | `https://bolt2github.com` | 通用代理 |
| 131 | 197ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 132 | 198ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 133 | 199ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 134 | 199ms | Paypal | 0.05 MB/s | `https://paypal.com` | 通用代理 |
| 135 | 201ms | Cbrowser | 1.81 MB/s | `https://cbrowser.ai` | 通用代理 |
| 136 | 201ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 137 | 204ms | Cursor | 0.82 MB/s | `https://cursor.com` | 通用代理 |
| 138 | 204ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 139 | 205ms | Sub | 0.19 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 140 | 206ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 141 | 206ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 142 | 206ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 143 | 208ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 144 | 212ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 145 | 213ms | Themolt | 0.04 MB/s | `https://themolt.net` | 通用代理 |
| 146 | 214ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 147 | 216ms | Gh | 2.85 MB/s | `https://gh.idayer.com` | 通用代理 |
| 148 | 217ms | Microcoreos | 0.44 MB/s | `https://microcoreos.com` | 通用代理 |
| 149 | 217ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 150 | 219ms | Visionmemorymcp | 0.27 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 151 | 220ms | Api | 0.13 MB/s | `https://api.solov.cc` | 通用代理 |
| 152 | 220ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 153 | 221ms | FastGit CC | - | `https://fastgit.cc` | 通用代理 |
| 154 | 224ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 155 | 225ms | Ginlix | 0.62 MB/s | `https://ginlix.ai` | 通用代理 |
| 156 | 227ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 157 | 227ms | Components | 0.2 MB/s | `https://components.dereekb.com` | 通用代理 |
| 158 | 230ms | CrashMC CDN | 1.74 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 159 | 230ms | GH-Proxy Org | - | `https://gh-proxy.org` | 通用代理 |
| 160 | 232ms | Aka | 0.73 MB/s | `https://aka.ms` | 通用代理 |
| 161 | 235ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 162 | 238ms | Coreos | 3.35 MB/s | `https://coreos.com` | 通用代理 |
| 163 | 238ms | Gh | 0.97 MB/s | `https://gh.1k.ink` | 通用代理 |
| 164 | 241ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 165 | 243ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 166 | 244ms | Kenyu | 2.12 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 167 | 246ms | Clypra | 0.07 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 168 | 246ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 169 | 248ms | Nisar | 0.95 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 170 | 253ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 171 | 256ms | Code | 2.45 MB/s | `https://code.claude.com` | 通用代理 |
| 172 | 256ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 173 | 262ms | Ghproxy | - | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 174 | 262ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 175 | 263ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 176 | 263ms | Tiktok | 0.13 MB/s | `https://tiktok.com` | 通用代理 |
| 177 | 263ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 178 | 264ms | Aiblackboxfc | 0.52 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 179 | 265ms | Gsd | 0.22 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 180 | 266ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 181 | 269ms | Ggg | 3.17 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 182 | 269ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 183 | 270ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 184 | 271ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 185 | 272ms | Kuroutoshikou | 1.21 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 186 | 277ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 187 | 288ms | Agoramarket | 0.56 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 188 | 288ms | Claude | 0.37 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 189 | 290ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 190 | 293ms | Aomedia | 0.39 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 191 | 293ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 192 | 296ms | Gh | - | `https://gh.padao.fun` | 通用代理 |
| 193 | 297ms | Steamcommunity | 0.18 MB/s | `https://steamcommunity.com` | 通用代理 |
| 194 | 298ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 195 | 304ms | Weaverse | 0.7 MB/s | `https://weaverse.io` | 通用代理 |
| 196 | 308ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 197 | 309ms | B23 | - | `https://b23.tv` | 通用代理 |
| 198 | 310ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 199 | 311ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 200 | 316ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 201 | 316ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 202 | 320ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 203 | 320ms | Youtu | 1.94 MB/s | `https://youtu.be` | 通用代理 |
| 204 | 322ms | 30006000 | - | `https://30006000.xyz` | 通用代理 |
| 205 | 324ms | You | 0.06 MB/s | `https://you.piccalc.com` | 通用代理 |
| 206 | 328ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 207 | 330ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 208 | 333ms | Github | - | `https://github.cnxiaobai.com` | 通用代理 |
| 209 | 335ms | Ednovas Mirror | - | `https://github.ednovas.xyz` | 通用代理 |
| 210 | 338ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 211 | 339ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 212 | 342ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 213 | 348ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 214 | 348ms | Github | 3.08 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 215 | 352ms | Store | 1.79 MB/s | `https://store.steampowered.com` | 通用代理 |
| 216 | 356ms | GHFast | - | `https://ghfast.top` | 通用代理 |
| 217 | 357ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 218 | 358ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 219 | 358ms | Github | 2.77 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 220 | 363ms | Aps | 0.07 MB/s | `https://aps.com` | 通用代理 |
| 221 | 364ms | Bseindia | 0.04 MB/s | `https://bseindia.com` | 通用代理 |
| 222 | 368ms | Hk | - | `https://hk.gh-proxy.com` | 通用代理 |
| 223 | 380ms | Serverkit | 0.04 MB/s | `https://serverkit.ai` | 通用代理 |
| 224 | 380ms | Turborepo-starter-kit-web | 0.09 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 225 | 384ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 226 | 388ms | Bailian | 0.08 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 227 | 401ms | Support | 1.59 MB/s | `https://support.apple.com` | 通用代理 |
| 228 | 402ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 229 | 410ms | Im | 0.11 MB/s | `https://im.codes` | 通用代理 |
| 230 | 412ms | Github | 3.13 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 231 | 415ms | Safedocx | 0.18 MB/s | `https://safedocx.com` | 通用代理 |
| 232 | 416ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 233 | 416ms | GH Nxnow | - | `https://gh.nxnow.top` | 通用代理 |
| 234 | 417ms | Msdn | 0.05 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 235 | 419ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 236 | 419ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 237 | 420ms | Gh | 1.03 MB/s | `https://gh.noki.icu` | 通用代理 |
| 238 | 422ms | Bible-ai-explorer | 0.08 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 239 | 423ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 240 | 427ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 241 | 429ms | Sonarcloud | 0.02 MB/s | `https://sonarcloud.io` | 通用代理 |
| 242 | 436ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 243 | 448ms | YYLX Git | - | `https://git.yylx.win` | 通用代理 |
| 244 | 454ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 245 | 455ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 246 | 456ms | Caiji | 0.04 MB/s | `https://caiji.cyou` | 通用代理 |
| 247 | 457ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 248 | 457ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 249 | 465ms | Getgit | 2.48 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 250 | 470ms | Ark | 0.83 MB/s | `https://ark.intel.com` | 通用代理 |
| 251 | 479ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 252 | 485ms | Lecvdemarius | 0.07 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 253 | 486ms | Wl | - | `https://wl.do` | 通用代理 |
| 254 | 490ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 255 | 492ms | Easyboardgame | 0.01 MB/s | `https://easyboardgame.top` | 通用代理 |
| 256 | 493ms | Aosmd | 0.25 MB/s | `https://aosmd.com` | 通用代理 |
| 257 | 494ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 258 | 504ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 259 | 509ms | Patchworkos | 0.31 MB/s | `https://patchworkos.com` | 通用代理 |
| 260 | 516ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 261 | 518ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 262 | 524ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 263 | 525ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 264 | 526ms | Umami-mcp | 0.43 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 265 | 532ms | Internhack | 0.04 MB/s | `https://internhack.xyz` | 通用代理 |
| 266 | 534ms | Ygdj7 | 0.05 MB/s | `https://ygdj7.com` | 通用代理 |
| 267 | 543ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 268 | 544ms | Nyx | 0.04 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 269 | 546ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 270 | 554ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 271 | 555ms | Lucky | 0.43 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 272 | 560ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 273 | 565ms | Agentkey | 0.32 MB/s | `https://agentkey.app` | 通用代理 |
| 274 | 566ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 275 | 567ms | Memstack | 0.03 MB/s | `https://memstack.pro` | 通用代理 |
| 276 | 573ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 277 | 576ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 278 | 584ms | Gh | - | `https://gh.39.al` | 通用代理 |
| 279 | 600ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 280 | 616ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 281 | 631ms | Gh | 0.87 MB/s | `https://gh.dpik.top` | 通用代理 |
| 282 | 633ms | Github | 0.39 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 283 | 638ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 284 | 639ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 285 | 644ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 286 | 645ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 287 | 647ms | Clawbiz | 0.04 MB/s | `https://clawbiz.io` | 通用代理 |
| 288 | 662ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 289 | 663ms | GHFile Geekertao | 0.47 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 290 | 668ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 291 | 672ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 292 | 681ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 293 | 685ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 294 | 696ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 295 | 713ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 296 | 721ms | Fastfile | 1.75 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 297 | 721ms | Tsukuyomi | 0.16 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 298 | 729ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 299 | 737ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 300 | 747ms | Docs | 0.24 MB/s | `https://docs.transifex.com` | 通用代理 |
| 301 | 757ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 302 | 766ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 303 | 787ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 304 | 790ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 305 | 800ms | Ccgather | 0.07 MB/s | `https://ccgather.com` | 通用代理 |
| 306 | 805ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 307 | 809ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 308 | 811ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 309 | 831ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 310 | 846ms | Maplecode | - | `https://maplecode.art` | 通用代理 |
| 311 | 855ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 312 | 865ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 313 | 880ms | Md | 0.07 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 314 | 892ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 315 | 896ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 316 | 913ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 317 | 915ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 318 | 935ms | Mimo | 0.17 MB/s | `https://mimo.mi.com` | 通用代理 |
| 319 | 943ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 320 | 950ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 321 | 961ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 322 | 991ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 323 | 1001ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 324 | 1006ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 325 | 1036ms | Web | - | `https://web.4399.com` | 通用代理 |
| 326 | 1045ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 327 | 1057ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 328 | 1075ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 329 | 1094ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 330 | 1095ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 331 | 1118ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 332 | 1132ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 333 | 1138ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 334 | 1168ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 335 | 1185ms | Ghproxy | 0.04 MB/s | `https://ghproxy.cc` | 通用代理 |
| 336 | 1190ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 337 | 1220ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 338 | 1227ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 339 | 1237ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 340 | 1243ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 341 | 1265ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 342 | 1271ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 343 | 1285ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 344 | 1304ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 345 | 1309ms | V | - | `https://v.douyin.com` | 通用代理 |
| 346 | 1372ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 347 | 1417ms | Cf | - | `https://cf.ghproxy.cc` | 通用代理 |
| 348 | 1484ms | Mobilevc | - | `https://mobilevc.top` | 通用代理 |
| 349 | 1534ms | Git | - | `https://git.669966.xyz` | 通用代理 |
| 350 | 1552ms | Github | - | `https://github.chenc.dev` | 通用代理 |
| 351 | 1578ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 352 | 1628ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 353 | 1661ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 354 | 1681ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 355 | 1874ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 356 | 2100ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 357 | 2105ms | G | - | `https://g.blfrp.cn` | 通用代理 |
| 358 | 2155ms | Img | - | `https://img.ink` | 通用代理 |
| 359 | 2293ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 360 | 2454ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 361 | 2569ms | Wget | - | `https://wget.la` | 通用代理 |
| 362 | 2919ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 363 | 2969ms | Ghproxy | 0.04 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 364 | 2976ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 365 | 3999ms | GHProxy MonkeyRay | 0.03 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 366 | 6576ms | Proxy | 0.03 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（9 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Npee Down (`down-npee-cn`) | 21 次 |
| Gh (`gh-halonice-com`) | 20 次 |
| Git (`git-tangbai-cc`) | 21 次 |
| Gitproxy (`gitproxy-click`) | 1 次 |
| Gh (`gh-b52m-cn`) | 2 次 |
| Proxy (`proxy-vvvv-ee`) | 4 次 |
| 5555 (`5555-cab`) | 11 次 |
| Doxygen (`doxygen-org`) | 7 次 |
| Flashtype (`flashtype-com`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 368 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **375** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（49 个）。

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
