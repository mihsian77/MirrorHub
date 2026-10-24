# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-24T20:20:15Z**，每 6 小时刷新一次。当前 ✅ **361** 在线 / ⚠️ **11** 不稳定 / ⚰️ **48** 已失效归档。

## 核心特性

- **372 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 50ms | Microsoftedge | 1.22 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 56ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 3 | 58ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 4 | 68ms | Linkedin | 0.12 MB/s | `https://linkedin.com` | 通用代理 |
| 5 | 70ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 6 | 76ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 7 | 81ms | Deno | 2.83 MB/s | `https://deno.com` | 通用代理 |
| 8 | 83ms | Dilo-d14 | 0.18 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 9 | 84ms | Huly-mcp | 0.21 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 10 | 85ms | Githubstatus | 2.06 MB/s | `https://githubstatus.com` | 通用代理 |
| 11 | 86ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 12 | 88ms | X | 1.65 MB/s | `https://x.com` | 通用代理 |
| 13 | 88ms | Xjtu-nyxf-study-material | 0.16 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 14 | 90ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 15 | 90ms | Opresume | 0.29 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 16 | 90ms | Tools | 3.13 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 17 | 91ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 18 | 93ms | Kighelper-cloud | 0.1 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 19 | 96ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 20 | 97ms | Wordpaper | 0.36 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 21 | 98ms | Img | - | `https://img.shields.io` | 通用代理 |
| 22 | 100ms | Alas | 1.25 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 23 | 100ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 24 | 100ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 25 | 101ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 26 | 102ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 27 | 104ms | Impeccable | 1.16 MB/s | `https://impeccable.style` | 通用代理 |
| 28 | 104ms | Zebrunner | 2.65 MB/s | `https://zebrunner.com` | 通用代理 |
| 29 | 105ms | App | 0.12 MB/s | `https://app.netlify.com` | 通用代理 |
| 30 | 106ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 31 | 108ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 32 | 110ms | Thumb | 1.03 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 33 | 112ms | Caw | 0.07 MB/s | `https://caw.rocks` | 通用代理 |
| 34 | 112ms | Impro | 1.44 MB/s | `https://impro.social` | 通用代理 |
| 35 | 112ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 36 | 113ms | Discord | 0.07 MB/s | `https://discord.gg` | 通用代理 |
| 37 | 114ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 38 | 114ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 39 | 114ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 40 | 115ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 41 | 119ms | Polgarand | 0.11 MB/s | `https://polgarand.org` | 通用代理 |
| 42 | 121ms | Lawyer-yu | 0.12 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 43 | 121ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 44 | 123ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 45 | 123ms | L4d2 | 0.15 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 46 | 123ms | Resume-5lv | 0.22 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 47 | 124ms | Anh | 0.23 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 48 | 124ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 49 | 125ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 50 | 126ms | Codeeraser | 0.14 MB/s | `https://codeeraser.dev` | 通用代理 |
| 51 | 126ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 52 | 126ms | Serac | 0.07 MB/s | `https://serac.build` | 通用代理 |
| 53 | 127ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 54 | 127ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 55 | 127ms | Opencovibe | 0.44 MB/s | `https://opencovibe.com` | 通用代理 |
| 56 | 128ms | Agentlimb | 0.25 MB/s | `https://agentlimb.com` | 通用代理 |
| 57 | 128ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 58 | 128ms | Clayrune | 0.18 MB/s | `https://clayrune.io` | 通用代理 |
| 59 | 129ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 60 | 130ms | Vibesql | 0.12 MB/s | `https://vibesql.org` | 通用代理 |
| 61 | 134ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 62 | 134ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 63 | 134ms | Tokei | 0.53 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 64 | 135ms | Gitea-mirror | 0.7 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 65 | 135ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 66 | 136ms | Bananaslides | 0.38 MB/s | `https://bananaslides.online` | 通用代理 |
| 67 | 137ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 68 | 137ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 69 | 138ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 70 | 138ms | Coffeecli | 0.11 MB/s | `https://coffeecli.com` | 通用代理 |
| 71 | 138ms | Gh | 1.8 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 72 | 139ms | Play | 0.05 MB/s | `https://play.templatical.com` | 通用代理 |
| 73 | 141ms | Git | 2.13 MB/s | `https://git.820828.xyz` | 通用代理 |
| 74 | 143ms | Gp | 3.06 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 75 | 143ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 76 | 143ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 77 | 144ms | Github | 2.44 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 78 | 146ms | Opentakeoff | 0.06 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 79 | 148ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 80 | 148ms | Bestdori | 0.08 MB/s | `https://bestdori.com` | 通用代理 |
| 81 | 148ms | Git | 2.23 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 82 | 149ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 83 | 150ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 84 | 151ms | Github | 3.37 MB/s | `https://github.788787.xyz` | 通用代理 |
| 85 | 154ms | Shiori-v1 | 0.03 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 86 | 155ms | Gh | 1.97 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 87 | 156ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 88 | 156ms | Cody | 0.23 MB/s | `https://cody.todyle.com` | 通用代理 |
| 89 | 156ms | Glass | 0.24 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 90 | 156ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 91 | 158ms | Cognitum | 0.15 MB/s | `https://cognitum.one` | 通用代理 |
| 92 | 158ms | Openpua | 0.45 MB/s | `https://openpua.ai` | 通用代理 |
| 93 | 159ms | Hopp | 0.04 MB/s | `https://hopp.sh` | 通用代理 |
| 94 | 160ms | Gh | 2.07 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 95 | 162ms | Ghproxy | 1.63 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 96 | 162ms | You | 0.05 MB/s | `https://you.piccalc.com` | 通用代理 |
| 97 | 163ms | GH-Proxy | 1.28 MB/s | `https://gh-proxy.com` | 通用代理 |
| 98 | 163ms | Github | 2.16 MB/s | `https://github.880824.xyz` | 通用代理 |
| 99 | 163ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 100 | 163ms | Opensunsama | 0.05 MB/s | `https://opensunsama.com` | 通用代理 |
| 101 | 164ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 102 | 166ms | GH Monlor | 1.33 MB/s | `https://gh.monlor.com` | 通用代理 |
| 103 | 168ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 104 | 171ms | Ai-trend-publish | 0.03 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 105 | 171ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 106 | 176ms | Miaozitie | 0.07 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 107 | 177ms | Bolt2github | 0.04 MB/s | `https://bolt2github.com` | 通用代理 |
| 108 | 178ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 109 | 181ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 110 | 181ms | Twitter | 0.98 MB/s | `https://twitter.com` | 通用代理 |
| 111 | 182ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 112 | 182ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 113 | 184ms | Github | 2.01 MB/s | `https://github.ihnic.com` | 通用代理 |
| 114 | 184ms | Music-cli | 0.26 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 115 | 185ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 116 | 185ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 117 | 185ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 118 | 186ms | Contrib | 0.28 MB/s | `https://contrib.rocks` | 通用代理 |
| 119 | 186ms | Holyclaude | 0.12 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 120 | 187ms | Ghproxy | 3.17 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 121 | 190ms | Axios-http | 0.53 MB/s | `https://axios-http.com` | 通用代理 |
| 122 | 190ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 123 | 192ms | Phabricator | 0.09 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 124 | 193ms | Ampcode | 0.21 MB/s | `https://ampcode.com` | 通用代理 |
| 125 | 195ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 126 | 196ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 127 | 197ms | Openttd | 0.06 MB/s | `https://openttd.org` | 通用代理 |
| 128 | 197ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 129 | 200ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 130 | 200ms | Radio-browser | 0.03 MB/s | `https://radio-browser.info` | 通用代理 |
| 131 | 201ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 132 | 203ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 133 | 206ms | Cursor | 0.82 MB/s | `https://cursor.com` | 通用代理 |
| 134 | 206ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 135 | 207ms | Paypal | 0.05 MB/s | `https://paypal.com` | 通用代理 |
| 136 | 207ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 137 | 208ms | FastGit CC | 1.4 MB/s | `https://fastgit.cc` | 通用代理 |
| 138 | 208ms | Tvv | 2.19 MB/s | `https://tvv.tw` | 通用代理 |
| 139 | 209ms | Ode | - | `https://ode.fun` | 通用代理 |
| 140 | 209ms | Tms | 0.26 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 141 | 210ms | Training | 0.25 MB/s | `https://training.ti.com` | 通用代理 |
| 142 | 210ms | Visionmemorymcp | 0.3 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 143 | 214ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 144 | 214ms | Microcoreos | 0.47 MB/s | `https://microcoreos.com` | 通用代理 |
| 145 | 215ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 146 | 215ms | Sub | 0.19 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 147 | 216ms | Cbrowser | 2.12 MB/s | `https://cbrowser.ai` | 通用代理 |
| 148 | 218ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 149 | 218ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 150 | 218ms | GH-Proxy Org | 1.01 MB/s | `https://gh-proxy.org` | 通用代理 |
| 151 | 223ms | Api | 0.14 MB/s | `https://api.solov.cc` | 通用代理 |
| 152 | 224ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 153 | 226ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 154 | 226ms | Themolt | 0.04 MB/s | `https://themolt.net` | 通用代理 |
| 155 | 228ms | Ginlix | 0.64 MB/s | `https://ginlix.ai` | 通用代理 |
| 156 | 230ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 157 | 231ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 158 | 236ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 159 | 236ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 160 | 237ms | CrashMC CDN | 1.31 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 161 | 243ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 162 | 244ms | Aka | 0.42 MB/s | `https://aka.ms` | 通用代理 |
| 163 | 247ms | Claude | 0.24 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 164 | 248ms | Flashtype | 0.26 MB/s | `https://flashtype.com` | 通用代理 |
| 165 | 249ms | Kenyu | 1.98 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 166 | 250ms | Ggg | 2.28 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 167 | 251ms | Code | 2.46 MB/s | `https://code.claude.com` | 通用代理 |
| 168 | 252ms | Nisar | 0.98 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 169 | 252ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 170 | 253ms | Coreos | 4.04 MB/s | `https://coreos.com` | 通用代理 |
| 171 | 253ms | Zuckerbot | 0.04 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 172 | 254ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 173 | 256ms | Ghproxy | 0.63 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 174 | 257ms | Gh | 3.25 MB/s | `https://gh.1k.ink` | 通用代理 |
| 175 | 259ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 176 | 260ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 177 | 262ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 178 | 262ms | Components | 0.23 MB/s | `https://components.dereekb.com` | 通用代理 |
| 179 | 268ms | Clypra | 0.05 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 180 | 275ms | Kuroutoshikou | 1.86 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 181 | 277ms | Tiktok | 0.23 MB/s | `https://tiktok.com` | 通用代理 |
| 182 | 278ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 183 | 280ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 184 | 284ms | Oem | 0.04 MB/s | `https://oem.re` | 通用代理 |
| 185 | 285ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 186 | 289ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 187 | 293ms | Agoramarket | 0.52 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 188 | 294ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 189 | 296ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 190 | 296ms | Gh | 0.62 MB/s | `https://gh.padao.fun` | 通用代理 |
| 191 | 296ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 192 | 301ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 193 | 302ms | Aiblackboxfc | 0.31 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 194 | 302ms | Aomedia | 0.32 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 195 | 302ms | Im | 0.28 MB/s | `https://im.codes` | 通用代理 |
| 196 | 302ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 197 | 303ms | Gsd | 0.29 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 198 | 306ms | Steamcommunity | 0.17 MB/s | `https://steamcommunity.com` | 通用代理 |
| 199 | 308ms | Weaverse | 0.69 MB/s | `https://weaverse.io` | 通用代理 |
| 200 | 317ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 201 | 317ms | Github | 0.55 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 202 | 318ms | 30006000 | 0.5 MB/s | `https://30006000.xyz` | 通用代理 |
| 203 | 318ms | B23 | - | `https://b23.tv` | 通用代理 |
| 204 | 322ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 205 | 330ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 206 | 331ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 207 | 332ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 208 | 333ms | GHFast | 0.6 MB/s | `https://ghfast.top` | 通用代理 |
| 209 | 333ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 210 | 334ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 211 | 336ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 212 | 340ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 213 | 347ms | Aps | 0.02 MB/s | `https://aps.com` | 通用代理 |
| 214 | 355ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 215 | 355ms | Github | 3.19 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 216 | 355ms | Github | 1.96 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 217 | 357ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 218 | 358ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 219 | 361ms | Store | 1.47 MB/s | `https://store.steampowered.com` | 通用代理 |
| 220 | 362ms | Ednovas Mirror | 0.61 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 221 | 363ms | Bailian | 0.06 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 222 | 370ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 223 | 371ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 224 | 373ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 225 | 376ms | Hk | 0.81 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 226 | 377ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 227 | 398ms | Turborepo-starter-kit-web | 0.07 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 228 | 405ms | Github | 2.16 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 229 | 411ms | GH Nxnow | 0.69 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 230 | 411ms | Support | 0.1 MB/s | `https://support.apple.com` | 通用代理 |
| 231 | 414ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 232 | 416ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 233 | 418ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 234 | 421ms | Gh | 0.93 MB/s | `https://gh.noki.icu` | 通用代理 |
| 235 | 423ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 236 | 423ms | Safedocx | 0.13 MB/s | `https://safedocx.com` | 通用代理 |
| 237 | 428ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 238 | 428ms | Msdn | 0.05 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 239 | 432ms | Bible-ai-explorer | 0.06 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 240 | 438ms | Getgit | 2.79 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 241 | 451ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 242 | 451ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 243 | 452ms | YYLX Git | 0.73 MB/s | `https://git.yylx.win` | 通用代理 |
| 244 | 454ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 245 | 465ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 246 | 465ms | Wl | - | `https://wl.do` | 通用代理 |
| 247 | 466ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 248 | 469ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 249 | 471ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 250 | 484ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 251 | 489ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 252 | 497ms | Ark | 0.72 MB/s | `https://ark.intel.com` | 通用代理 |
| 253 | 503ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 254 | 506ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 255 | 507ms | Lecvdemarius | 0.09 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 256 | 510ms | Aosmd | 0.16 MB/s | `https://aosmd.com` | 通用代理 |
| 257 | 511ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 258 | 515ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 259 | 520ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 260 | 524ms | Patchworkos | 0.3 MB/s | `https://patchworkos.com` | 通用代理 |
| 261 | 527ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 262 | 534ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 263 | 541ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 264 | 543ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 265 | 545ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 266 | 549ms | Gh | 0.76 MB/s | `https://gh.39.al` | 通用代理 |
| 267 | 551ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 268 | 557ms | Nyx | 0.04 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 269 | 567ms | Umami-mcp | 0.44 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 270 | 568ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 271 | 570ms | Lucky | 0.44 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 272 | 576ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 273 | 588ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 274 | 591ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 275 | 598ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 276 | 605ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 277 | 613ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 278 | 622ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 279 | 624ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 280 | 624ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 281 | 629ms | Github | 0.43 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 282 | 631ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 283 | 636ms | Agentkey | 0.46 MB/s | `https://agentkey.app` | 通用代理 |
| 284 | 662ms | Os | 0.13 MB/s | `https://os.ryo.lu` | 通用代理 |
| 285 | 669ms | Ghproxy | 0.23 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 286 | 679ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 287 | 682ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 288 | 684ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 289 | 688ms | Gh | 0.51 MB/s | `https://gh.dpik.top` | 通用代理 |
| 290 | 692ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 291 | 739ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 292 | 748ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 293 | 750ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 294 | 757ms | Docs | 0.2 MB/s | `https://docs.transifex.com` | 通用代理 |
| 295 | 775ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 296 | 779ms | GHProxy Net | 0.27 MB/s | `https://ghproxy.net` | 通用代理 |
| 297 | 780ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 298 | 788ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 299 | 791ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 300 | 793ms | Fastfile | 2.41 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 301 | 796ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 302 | 798ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 303 | 802ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 304 | 828ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 305 | 833ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 306 | 836ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 307 | 849ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 308 | 849ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 309 | 859ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 310 | 862ms | Yibiao | 0.15 MB/s | `https://yibiao.pro` | 通用代理 |
| 311 | 867ms | Maplecode | - | `https://maplecode.art` | 通用代理 |
| 312 | 883ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 313 | 892ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 314 | 909ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 315 | 909ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 316 | 935ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 317 | 935ms | Mimo | 0.17 MB/s | `https://mimo.mi.com` | 通用代理 |
| 318 | 938ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 319 | 940ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 320 | 991ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 321 | 1015ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 322 | 1025ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 323 | 1046ms | Atomcode | 0.08 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 324 | 1049ms | Web | - | `https://web.4399.com` | 通用代理 |
| 325 | 1051ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 326 | 1067ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 327 | 1090ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 328 | 1107ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 329 | 1112ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 330 | 1140ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 331 | 1176ms | Ghproxy | 0.26 MB/s | `https://ghproxy.cc` | 通用代理 |
| 332 | 1180ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 333 | 1209ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 334 | 1218ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 335 | 1226ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 336 | 1262ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 337 | 1268ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 338 | 1279ms | V | - | `https://v.douyin.com` | 通用代理 |
| 339 | 1284ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 340 | 1295ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 341 | 1358ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 342 | 1417ms | Cf | 0.25 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 343 | 1547ms | Github | 0.14 MB/s | `https://github.chenc.dev` | 通用代理 |
| 344 | 1552ms | Git | 0.11 MB/s | `https://git.669966.xyz` | 通用代理 |
| 345 | 1593ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 346 | 1623ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 347 | 1666ms | Mobilevc | - | `https://mobilevc.top` | 通用代理 |
| 348 | 1698ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 349 | 1746ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 350 | 1882ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 351 | 2055ms | G | 0.14 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 352 | 2064ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 353 | 2134ms | Img | - | `https://img.ink` | 通用代理 |
| 354 | 2353ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 355 | 2354ms | Ghproxy | 0.14 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 356 | 2382ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 357 | 2875ms | Wget | - | `https://wget.la` | 通用代理 |
| 358 | 2899ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 359 | 2966ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 360 | 4003ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 361 | 6160ms | Proxy | 0.04 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（11 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| Npee Down (`down-npee-cn`) | 20 次 |
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 27 次 |
| Gh (`gh-idayer-com`) | 3 次 |
| Gh (`gh-halonice-com`) | 19 次 |
| Git (`git-tangbai-cc`) | 20 次 |
| Gh (`gh-b52m-cn`) | 1 次 |
| Proxy (`proxy-vvvv-ee`) | 3 次 |
| 5555 (`5555-cab`) | 10 次 |
| Doxygen (`doxygen-org`) | 6 次 |
| Youtu (`youtu-be`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 365 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **372** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（48 个）。

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
