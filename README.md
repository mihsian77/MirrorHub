# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-24T15:29:51Z**，每 6 小时刷新一次。当前 ✅ **357** 在线 / ⚠️ **13** 不稳定 / ⚰️ **48** 已失效归档。

## 核心特性

- **370 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 58ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 2 | 58ms | Microsoftedge | 0.26 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 60ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 4 | 73ms | Kighelper-cloud | 0.08 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 5 | 73ms | Linkedin | 0.14 MB/s | `https://linkedin.com` | 通用代理 |
| 6 | 76ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 7 | 78ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 8 | 84ms | Dilo-d14 | 0.22 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 9 | 85ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 10 | 86ms | Huly-mcp | 0.19 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 11 | 87ms | Deno | 0.2 MB/s | `https://deno.com` | 通用代理 |
| 12 | 91ms | Tools | 1.9 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 13 | 92ms | Xjtu-nyxf-study-material | 0.16 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 14 | 93ms | X | 1.39 MB/s | `https://x.com` | 通用代理 |
| 15 | 94ms | Alas | 0.94 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 16 | 94ms | Opresume | 0.63 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 17 | 95ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 18 | 96ms | Bananaslides | 0.88 MB/s | `https://bananaslides.online` | 通用代理 |
| 19 | 96ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 20 | 97ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 21 | 97ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 22 | 98ms | Githubstatus | 1.69 MB/s | `https://githubstatus.com` | 通用代理 |
| 23 | 103ms | Img | - | `https://img.shields.io` | 通用代理 |
| 24 | 104ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 25 | 104ms | Godocs | 0.06 MB/s | `https://godocs.io` | 通用代理 |
| 26 | 105ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 27 | 105ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 28 | 107ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 29 | 108ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 30 | 108ms | Impeccable | 0.82 MB/s | `https://impeccable.style` | 通用代理 |
| 31 | 109ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 32 | 109ms | Wordpaper | 0.37 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 33 | 110ms | App | 0.08 MB/s | `https://app.netlify.com` | 通用代理 |
| 34 | 110ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 35 | 110ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 36 | 111ms | Serac | 0.1 MB/s | `https://serac.build` | 通用代理 |
| 37 | 113ms | Zebrunner | 2.44 MB/s | `https://zebrunner.com` | 通用代理 |
| 38 | 118ms | Thumb | 1.02 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 39 | 119ms | L4d2 | 0.16 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 40 | 120ms | Impro | 1.7 MB/s | `https://impro.social` | 通用代理 |
| 41 | 121ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 42 | 122ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 43 | 122ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 44 | 123ms | Anh | 0.21 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 45 | 123ms | Discord | 0.06 MB/s | `https://discord.gg` | 通用代理 |
| 46 | 123ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 47 | 123ms | Resume-5lv | 0.2 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 48 | 124ms | Bestdori | 0.14 MB/s | `https://bestdori.com` | 通用代理 |
| 49 | 124ms | Coffeecli | 0.16 MB/s | `https://coffeecli.com` | 通用代理 |
| 50 | 124ms | Polgarand | 0.08 MB/s | `https://polgarand.org` | 通用代理 |
| 51 | 125ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 52 | 125ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 53 | 125ms | Clayrune | 0.14 MB/s | `https://clayrune.io` | 通用代理 |
| 54 | 125ms | Opencovibe | 0.41 MB/s | `https://opencovibe.com` | 通用代理 |
| 55 | 126ms | Codeeraser | 0.12 MB/s | `https://codeeraser.dev` | 通用代理 |
| 56 | 127ms | Agentlimb | 0.24 MB/s | `https://agentlimb.com` | 通用代理 |
| 57 | 127ms | Glass | 0.22 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 58 | 127ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 59 | 128ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 60 | 130ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 61 | 130ms | Gitea-mirror | 0.84 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 62 | 131ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 63 | 131ms | Lawyer-yu | 0.06 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 64 | 132ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 65 | 134ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 66 | 135ms | Tokei | 0.54 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 67 | 135ms | Vibesql | 0.13 MB/s | `https://vibesql.org` | 通用代理 |
| 68 | 136ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 69 | 137ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 70 | 137ms | Pidash | 0.06 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 71 | 140ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 72 | 141ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 73 | 142ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 74 | 142ms | Opensunsama | 0.1 MB/s | `https://opensunsama.com` | 通用代理 |
| 75 | 144ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 76 | 144ms | Git | 2.47 MB/s | `https://git.820828.xyz` | 通用代理 |
| 77 | 145ms | Gh | 2.23 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 78 | 145ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 79 | 146ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 80 | 147ms | Gp | 2.46 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 81 | 148ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 82 | 148ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 83 | 150ms | Github | 2.88 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 84 | 151ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 85 | 153ms | Openpua | 0.69 MB/s | `https://openpua.ai` | 通用代理 |
| 86 | 155ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 87 | 155ms | Git | 2.38 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 88 | 156ms | Cognitum | 0.18 MB/s | `https://cognitum.one` | 通用代理 |
| 89 | 156ms | Github | 2.43 MB/s | `https://github.788787.xyz` | 通用代理 |
| 90 | 156ms | Shiori-v1 | 0.03 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 91 | 157ms | Cody | 0.22 MB/s | `https://cody.todyle.com` | 通用代理 |
| 92 | 160ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 93 | 161ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 94 | 162ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 95 | 163ms | Gh | 1.23 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 96 | 165ms | Gh | 2.56 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 97 | 166ms | Ghproxy | 2.32 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 98 | 167ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 99 | 167ms | Microcoreos | 0.23 MB/s | `https://microcoreos.com` | 通用代理 |
| 100 | 167ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 101 | 168ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 102 | 169ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 103 | 169ms | GH-Proxy | 1.09 MB/s | `https://gh-proxy.com` | 通用代理 |
| 104 | 170ms | GH Monlor | 1.61 MB/s | `https://gh.monlor.com` | 通用代理 |
| 105 | 172ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 106 | 174ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 107 | 175ms | Github | 1.91 MB/s | `https://github.880824.xyz` | 通用代理 |
| 108 | 175ms | Ode | - | `https://ode.fun` | 通用代理 |
| 109 | 176ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 110 | 184ms | Github | 2.5 MB/s | `https://github.ihnic.com` | 通用代理 |
| 111 | 185ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 112 | 188ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 113 | 189ms | Holyclaude | 0.15 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 114 | 189ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 115 | 190ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 116 | 191ms | Contrib | 0.24 MB/s | `https://contrib.rocks` | 通用代理 |
| 117 | 191ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 118 | 192ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 119 | 192ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 120 | 194ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 121 | 194ms | Ghproxy | 2.14 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 122 | 194ms | Twitter | 0.87 MB/s | `https://twitter.com` | 通用代理 |
| 123 | 195ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 124 | 195ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 125 | 196ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 126 | 197ms | Ampcode | 0.23 MB/s | `https://ampcode.com` | 通用代理 |
| 127 | 197ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 128 | 198ms | Visionmemorymcp | 0.23 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 129 | 199ms | Axios-http | 0.44 MB/s | `https://axios-http.com` | 通用代理 |
| 130 | 201ms | Music-cli | 0.21 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 131 | 202ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 132 | 204ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 133 | 208ms | Sub | 0.11 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 134 | 210ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 135 | 212ms | Phabricator | 0.03 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 136 | 213ms | FastGit CC | 1.18 MB/s | `https://fastgit.cc` | 通用代理 |
| 137 | 213ms | Tvv | 2.8 MB/s | `https://tvv.tw` | 通用代理 |
| 138 | 216ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 139 | 218ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 140 | 219ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 141 | 220ms | Cursor | 0.51 MB/s | `https://cursor.com` | 通用代理 |
| 142 | 223ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 143 | 223ms | GH-Proxy Org | 1.33 MB/s | `https://gh-proxy.org` | 通用代理 |
| 144 | 223ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 145 | 224ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 146 | 231ms | Claude | 0.25 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 147 | 232ms | Training | 0.46 MB/s | `https://training.ti.com` | 通用代理 |
| 148 | 235ms | Api | 0.18 MB/s | `https://api.solov.cc` | 通用代理 |
| 149 | 235ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 150 | 236ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 151 | 236ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 152 | 237ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 153 | 239ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 154 | 239ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 155 | 240ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 156 | 241ms | Cbrowser | 0.88 MB/s | `https://cbrowser.ai` | 通用代理 |
| 157 | 245ms | Ginlix | 0.35 MB/s | `https://ginlix.ai` | 通用代理 |
| 158 | 246ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 159 | 246ms | CrashMC CDN | 1.86 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 160 | 247ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 161 | 248ms | Ghproxy | 1.15 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 162 | 248ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 163 | 249ms | Gh | 2.51 MB/s | `https://gh.1k.ink` | 通用代理 |
| 164 | 250ms | Kenyu | 2.43 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 165 | 251ms | Nisar | 1.79 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 166 | 251ms | Tms | 0.09 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 167 | 252ms | Coreos | 1.9 MB/s | `https://coreos.com` | 通用代理 |
| 168 | 254ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 169 | 254ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 170 | 259ms | Code | 1.48 MB/s | `https://code.claude.com` | 通用代理 |
| 171 | 259ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 172 | 264ms | Im | 0.43 MB/s | `https://im.codes` | 通用代理 |
| 173 | 266ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 174 | 267ms | Ggg | 2.47 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 175 | 267ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 176 | 270ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 177 | 273ms | Components | 0.1 MB/s | `https://components.dereekb.com` | 通用代理 |
| 178 | 275ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 179 | 276ms | Agenticcorporation | 0.04 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 180 | 279ms | Clypra | 0.09 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 181 | 280ms | Aka | 0.42 MB/s | `https://aka.ms` | 通用代理 |
| 182 | 282ms | Gh | 2.12 MB/s | `https://gh.padao.fun` | 通用代理 |
| 183 | 282ms | Kuroutoshikou | 0.14 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 184 | 284ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 185 | 286ms | Agoramarket | 1.7 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 186 | 288ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 187 | 292ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 188 | 295ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 189 | 298ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 190 | 302ms | B23 | - | `https://b23.tv` | 通用代理 |
| 191 | 304ms | Github | 1.46 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 192 | 307ms | Aomedia | 0.13 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 193 | 307ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 194 | 310ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 195 | 318ms | Tiktok | 0.09 MB/s | `https://tiktok.com` | 通用代理 |
| 196 | 321ms | Weaverse | 0.5 MB/s | `https://weaverse.io` | 通用代理 |
| 197 | 322ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 198 | 325ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 199 | 325ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 200 | 325ms | Steamcommunity | 0.07 MB/s | `https://steamcommunity.com` | 通用代理 |
| 201 | 327ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 202 | 330ms | 30006000 | 1.83 MB/s | `https://30006000.xyz` | 通用代理 |
| 203 | 332ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 204 | 333ms | Aps | 0.08 MB/s | `https://aps.com` | 通用代理 |
| 205 | 339ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 206 | 347ms | Aiblackboxfc | 0.26 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 207 | 349ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 208 | 350ms | GHFast | 1.11 MB/s | `https://ghfast.top` | 通用代理 |
| 209 | 353ms | Github | 2.24 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 210 | 356ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 211 | 360ms | Bailian | 0.14 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 212 | 365ms | Github | 2.34 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 213 | 365ms | Serverkit | 0.03 MB/s | `https://serverkit.ai` | 通用代理 |
| 214 | 367ms | Gsd | 0.07 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 215 | 367ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 216 | 369ms | Store | 0.82 MB/s | `https://store.steampowered.com` | 通用代理 |
| 217 | 372ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 218 | 374ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 219 | 374ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 220 | 375ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 221 | 377ms | Youtu | 1.05 MB/s | `https://youtu.be` | 通用代理 |
| 222 | 378ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 223 | 386ms | Bseindia | 0.02 MB/s | `https://bseindia.com` | 通用代理 |
| 224 | 393ms | Support | 0.14 MB/s | `https://support.apple.com` | 通用代理 |
| 225 | 398ms | Hk | 1.41 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 226 | 406ms | Turborepo-starter-kit-web | 0.08 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 227 | 410ms | Github | 2.44 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 228 | 412ms | Gh | 0.53 MB/s | `https://gh.noki.icu` | 通用代理 |
| 229 | 414ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 230 | 421ms | Ednovas Mirror | 0.38 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 231 | 422ms | Bible-ai-explorer | 0.06 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 232 | 431ms | GH Nxnow | 0.46 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 233 | 431ms | Safedocx | 0.11 MB/s | `https://safedocx.com` | 通用代理 |
| 234 | 432ms | Getgit | 2.6 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 235 | 438ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 236 | 438ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 237 | 442ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 238 | 448ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 239 | 448ms | Wl | - | `https://wl.do` | 通用代理 |
| 240 | 449ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 241 | 451ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 242 | 455ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 243 | 461ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 244 | 467ms | Codeflying | 0.01 MB/s | `https://codeflying.app` | 通用代理 |
| 245 | 468ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 246 | 476ms | Internhack | 0.04 MB/s | `https://internhack.xyz` | 通用代理 |
| 247 | 484ms | Ark | 1.24 MB/s | `https://ark.intel.com` | 通用代理 |
| 248 | 488ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 249 | 495ms | Gh | 1.8 MB/s | `https://gh.39.al` | 通用代理 |
| 250 | 495ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 251 | 502ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 252 | 503ms | Your-domain | 0.1 MB/s | `https://your-domain.com` | 通用代理 |
| 253 | 507ms | Aosmd | 0.1 MB/s | `https://aosmd.com` | 通用代理 |
| 254 | 518ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 255 | 519ms | Lecvdemarius | 0.04 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 256 | 520ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 257 | 522ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 258 | 527ms | SLink | 0.07 MB/s | `https://slink.ltd` | 通用代理 |
| 259 | 544ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 260 | 550ms | Patchworkos | 0.23 MB/s | `https://patchworkos.com` | 通用代理 |
| 261 | 551ms | Ygdj7 | 0.07 MB/s | `https://ygdj7.com` | 通用代理 |
| 262 | 554ms | Open | 0.03 MB/s | `https://open.feishu.cn` | 通用代理 |
| 263 | 569ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 264 | 580ms | Nyx | 0.02 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 265 | 580ms | Umami-mcp | 0.33 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 266 | 585ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 267 | 591ms | Lucky | 0.37 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 268 | 592ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 269 | 598ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 270 | 600ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 271 | 604ms | 3d-set-visualizer | 0.04 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 272 | 607ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 273 | 609ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 274 | 610ms | Github | 0.24 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 275 | 620ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 276 | 626ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 277 | 635ms | Tracely-studio | 0.04 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 278 | 643ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 279 | 644ms | Memstack | 0.04 MB/s | `https://memstack.pro` | 通用代理 |
| 280 | 645ms | Os | 0.04 MB/s | `https://os.ryo.lu` | 通用代理 |
| 281 | 654ms | Ghproxy | 0.35 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 282 | 661ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 283 | 668ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 284 | 697ms | Tsukuyomi | 0.09 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 285 | 704ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 286 | 722ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 287 | 725ms | Gh | 0.4 MB/s | `https://gh.dpik.top` | 通用代理 |
| 288 | 729ms | Clawbiz | 0.04 MB/s | `https://clawbiz.io` | 通用代理 |
| 289 | 741ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 290 | 768ms | GHProxy Net | 0.09 MB/s | `https://ghproxy.net` | 通用代理 |
| 291 | 771ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 292 | 774ms | Docs | 0.15 MB/s | `https://docs.transifex.com` | 通用代理 |
| 293 | 788ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 294 | 789ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 295 | 793ms | Fastfile | 1.62 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 296 | 793ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 297 | 802ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 298 | 804ms | Maplecode | - | `https://maplecode.art` | 通用代理 |
| 299 | 804ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 300 | 817ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 301 | 818ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 302 | 837ms | Ccgather | 0.05 MB/s | `https://ccgather.com` | 通用代理 |
| 303 | 841ms | Agentkey | 1.51 MB/s | `https://agentkey.app` | 通用代理 |
| 304 | 864ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 305 | 872ms | Yibiao | 0.14 MB/s | `https://yibiao.pro` | 通用代理 |
| 306 | 886ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 307 | 892ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 308 | 896ms | Aif | 0.03 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 309 | 897ms | Md | 0.07 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 310 | 907ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 311 | 909ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 312 | 911ms | Onetwin | 0.01 MB/s | `https://onetwin.cn` | 通用代理 |
| 313 | 913ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 314 | 913ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 315 | 934ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 316 | 976ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 317 | 992ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 318 | 994ms | Web | - | `https://web.4399.com` | 通用代理 |
| 319 | 1011ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 320 | 1051ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 321 | 1087ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 322 | 1128ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 323 | 1128ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 324 | 1142ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 325 | 1143ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 326 | 1146ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 327 | 1157ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 328 | 1171ms | Ghproxy | 0.3 MB/s | `https://ghproxy.cc` | 通用代理 |
| 329 | 1175ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 330 | 1192ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 331 | 1192ms | V | - | `https://v.douyin.com` | 通用代理 |
| 332 | 1228ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 333 | 1248ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 334 | 1253ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 335 | 1272ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 336 | 1286ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 337 | 1292ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 338 | 1332ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 339 | 1411ms | Cf | 0.34 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 340 | 1472ms | Git | 0.48 MB/s | `https://git.669966.xyz` | 通用代理 |
| 341 | 1539ms | Github | 0.05 MB/s | `https://github.chenc.dev` | 通用代理 |
| 342 | 1566ms | I-qps | 0.04 MB/s | `https://i-qps.net` | 通用代理 |
| 343 | 1603ms | Heycall-e | 0.12 MB/s | `https://heycall-e.com` | 通用代理 |
| 344 | 1641ms | Mobilevc | - | `https://mobilevc.top` | 通用代理 |
| 345 | 1668ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 346 | 1671ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 347 | 1951ms | G | 0.22 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 348 | 2061ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 349 | 2161ms | Img | - | `https://img.ink` | 通用代理 |
| 350 | 2164ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 351 | 2341ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 352 | 2594ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 353 | 2970ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 354 | 3014ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 355 | 3285ms | Gh | 0.1 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 356 | 3370ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 357 | 3987ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（13 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| YYLX Git (`git-yylx-win`) | 1 次 |
| Npee Down (`down-npee-cn`) | 19 次 |
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 26 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Gh (`gh-halonice-com`) | 18 次 |
| Ghproxy (`ghproxy-mirror-skybyte-me`) | 1 次 |
| Git (`git-tangbai-cc`) | 19 次 |
| Proxy (`proxy-yaoyaoling-net`) | 3 次 |
| Proxy (`proxy-vvvv-ee`) | 2 次 |
| 5555 (`5555-cab`) | 9 次 |
| Doxygen (`doxygen-org`) | 5 次 |
| Flashtype (`flashtype-com`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 363 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **370** | |

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
