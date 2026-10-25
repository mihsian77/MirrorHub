# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-25T10:52:35Z**，每 6 小时刷新一次。当前 ✅ **365** 在线 / ⚠️ **12** 不稳定 / ⚰️ **49** 已失效归档。

## 核心特性

- **377 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 41ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 2 | 50ms | Microsoftedge | 0.59 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 54ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 4 | 66ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 73ms | Gpui | 0.4 MB/s | `https://gpui.rs` | 通用代理 |
| 6 | 74ms | Linkedin | 0.15 MB/s | `https://linkedin.com` | 通用代理 |
| 7 | 79ms | Deno | 0.86 MB/s | `https://deno.com` | 通用代理 |
| 8 | 79ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 9 | 82ms | Huly-mcp | 0.25 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 10 | 82ms | Tools | 2.42 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 11 | 84ms | Dilo-d14 | 0.25 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 12 | 85ms | Img | - | `https://img.shields.io` | 通用代理 |
| 13 | 85ms | X | 1.32 MB/s | `https://x.com` | 通用代理 |
| 14 | 86ms | Githubstatus | 1.18 MB/s | `https://githubstatus.com` | 通用代理 |
| 15 | 86ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 16 | 86ms | Xjtu-nyxf-study-material | 0.22 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 17 | 87ms | Wordpaper | 0.27 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 18 | 88ms | Kighelper-cloud | 0.12 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 19 | 88ms | Opresume | 0.7 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 20 | 90ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 21 | 92ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 22 | 93ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 23 | 95ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 24 | 98ms | App | 0.06 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 25 | 100ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 26 | 102ms | Alas | 1.19 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 27 | 102ms | Crypto-funding-arbitrage | 0.13 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 28 | 104ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 29 | 105ms | Godocs | 0.05 MB/s | `https://godocs.io` | 通用代理 |
| 30 | 105ms | Impeccable | 1.45 MB/s | `https://impeccable.style` | 通用代理 |
| 31 | 105ms | Zebrunner | 1.04 MB/s | `https://zebrunner.com` | 通用代理 |
| 32 | 108ms | App | 0.1 MB/s | `https://app.netlify.com` | 通用代理 |
| 33 | 108ms | Freeport | 0.05 MB/s | `https://freeport.network` | 通用代理 |
| 34 | 109ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 35 | 110ms | Caw | 0.09 MB/s | `https://caw.rocks` | 通用代理 |
| 36 | 112ms | Impro | 3.11 MB/s | `https://impro.social` | 通用代理 |
| 37 | 116ms | Resume-5lv | 0.25 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 38 | 117ms | Clayrune | 0.2 MB/s | `https://clayrune.io` | 通用代理 |
| 39 | 117ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 40 | 118ms | Anh | 0.29 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 41 | 118ms | Serac | 0.11 MB/s | `https://serac.build` | 通用代理 |
| 42 | 119ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 43 | 119ms | Lawyer-yu | 0.08 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 44 | 119ms | Polgarand | 0.13 MB/s | `https://polgarand.org` | 通用代理 |
| 45 | 120ms | L4d2 | 0.18 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 46 | 120ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 47 | 120ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 48 | 120ms | Opencovibe | 0.54 MB/s | `https://opencovibe.com` | 通用代理 |
| 49 | 120ms | Thumb | 1.05 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 50 | 121ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 51 | 121ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 52 | 121ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 53 | 122ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 54 | 122ms | Codeeraser | 0.15 MB/s | `https://codeeraser.dev` | 通用代理 |
| 55 | 122ms | Tokei | 0.64 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 56 | 123ms | Demo | 0.05 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 57 | 124ms | Bananaslides | 0.63 MB/s | `https://bananaslides.online` | 通用代理 |
| 58 | 126ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 59 | 127ms | Agentlimb | 0.27 MB/s | `https://agentlimb.com` | 通用代理 |
| 60 | 129ms | Chops | 0.04 MB/s | `https://chops.md` | 通用代理 |
| 61 | 130ms | Discord | 0.1 MB/s | `https://discord.gg` | 通用代理 |
| 62 | 131ms | Coffeecli | 0.2 MB/s | `https://coffeecli.com` | 通用代理 |
| 63 | 131ms | Goreportcard | 0.03 MB/s | `https://goreportcard.com` | 通用代理 |
| 64 | 133ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 65 | 134ms | App | 0.05 MB/s | `https://app.opencastor.com` | 通用代理 |
| 66 | 134ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 67 | 134ms | Vibesql | 0.2 MB/s | `https://vibesql.org` | 通用代理 |
| 68 | 135ms | Gitea-mirror | 1.07 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 69 | 136ms | Cognitum | 0.23 MB/s | `https://cognitum.one` | 通用代理 |
| 70 | 136ms | Gh | 2.95 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 71 | 136ms | Gh | 2.68 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 72 | 136ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 73 | 137ms | Github | 2.97 MB/s | `https://github.788787.xyz` | 通用代理 |
| 74 | 137ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 75 | 138ms | Glass | 0.4 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 76 | 139ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 77 | 139ms | Gp | 3.59 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 78 | 140ms | Git | 3.39 MB/s | `https://git.820828.xyz` | 通用代理 |
| 79 | 140ms | Github | 3.44 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 80 | 140ms | Openpua | 0.91 MB/s | `https://openpua.ai` | 通用代理 |
| 81 | 140ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 82 | 141ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 83 | 141ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 84 | 142ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 85 | 143ms | Git | 3.03 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 86 | 145ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 87 | 148ms | Ghproxy | 3.76 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 88 | 148ms | Play | 0.08 MB/s | `https://play.templatical.com` | 通用代理 |
| 89 | 151ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 90 | 152ms | Cody | 0.41 MB/s | `https://cody.todyle.com` | 通用代理 |
| 91 | 154ms | Miaozitie | 0.1 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 92 | 158ms | Bestdori | 0.11 MB/s | `https://bestdori.com` | 通用代理 |
| 93 | 158ms | Gh | 2.03 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 94 | 158ms | Github | 3.75 MB/s | `https://github.880824.xyz` | 通用代理 |
| 95 | 158ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 96 | 159ms | GH Monlor | 1.37 MB/s | `https://gh.monlor.com` | 通用代理 |
| 97 | 160ms | GH-Proxy | 1.26 MB/s | `https://gh-proxy.com` | 通用代理 |
| 98 | 163ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 99 | 166ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 100 | 167ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 101 | 167ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 102 | 167ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 103 | 168ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 104 | 171ms | Music-cli | 0.19 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 105 | 174ms | Holyclaude | 0.17 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 106 | 174ms | Tms | 0.19 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 107 | 176ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 108 | 176ms | Github | 3.0 MB/s | `https://github.ihnic.com` | 通用代理 |
| 109 | 177ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 110 | 177ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 111 | 178ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 112 | 179ms | Twitter | 0.8 MB/s | `https://twitter.com` | 通用代理 |
| 113 | 180ms | Cbrowser | 1.22 MB/s | `https://cbrowser.ai` | 通用代理 |
| 114 | 180ms | Ghproxy | 3.35 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 115 | 180ms | Opensunsama | 0.04 MB/s | `https://opensunsama.com` | 通用代理 |
| 116 | 182ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 117 | 182ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 118 | 183ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 119 | 184ms | Contrib | 0.61 MB/s | `https://contrib.rocks` | 通用代理 |
| 120 | 186ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 121 | 186ms | Openttd | 0.06 MB/s | `https://openttd.org` | 通用代理 |
| 122 | 187ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 123 | 188ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 124 | 188ms | Training | 0.15 MB/s | `https://training.ti.com` | 通用代理 |
| 125 | 192ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 126 | 194ms | Axios-http | 0.41 MB/s | `https://axios-http.com` | 通用代理 |
| 127 | 195ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 128 | 195ms | Congressmcp | 0.04 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 129 | 196ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 130 | 197ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 131 | 198ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 132 | 198ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 133 | 201ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 134 | 201ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 135 | 202ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 136 | 203ms | Ampcode | 0.18 MB/s | `https://ampcode.com` | 通用代理 |
| 137 | 204ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 138 | 207ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 139 | 208ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 140 | 210ms | Microcoreos | 0.53 MB/s | `https://microcoreos.com` | 通用代理 |
| 141 | 210ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 142 | 210ms | Tvv | 3.01 MB/s | `https://tvv.tw` | 通用代理 |
| 143 | 211ms | Ginlix | 0.59 MB/s | `https://ginlix.ai` | 通用代理 |
| 144 | 211ms | Ode | - | `https://ode.fun` | 通用代理 |
| 145 | 212ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 146 | 214ms | Api | 0.17 MB/s | `https://api.solov.cc` | 通用代理 |
| 147 | 214ms | Cursor | 0.39 MB/s | `https://cursor.com` | 通用代理 |
| 148 | 215ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 149 | 216ms | Components | 0.11 MB/s | `https://components.dereekb.com` | 通用代理 |
| 150 | 216ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 151 | 219ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 152 | 219ms | Sub | 0.14 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 153 | 219ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 154 | 220ms | FastGit CC | 1.33 MB/s | `https://fastgit.cc` | 通用代理 |
| 155 | 220ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 156 | 220ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 157 | 223ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 158 | 228ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 159 | 229ms | CrashMC CDN | 1.41 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 160 | 230ms | GH-Proxy Org | 1.26 MB/s | `https://gh-proxy.org` | 通用代理 |
| 161 | 232ms | Aka | 0.77 MB/s | `https://aka.ms` | 通用代理 |
| 162 | 233ms | Visionmemorymcp | 0.21 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 163 | 234ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 164 | 234ms | Clypra | 0.04 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 165 | 234ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 166 | 235ms | Kenyu | 3.06 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 167 | 244ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 168 | 244ms | Gsd | 0.18 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 169 | 247ms | Gh | 2.6 MB/s | `https://gh.1k.ink` | 通用代理 |
| 170 | 249ms | Ggg | 3.24 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 171 | 250ms | Coreos | 1.47 MB/s | `https://coreos.com` | 通用代理 |
| 172 | 251ms | Nisar | 0.76 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 173 | 253ms | Code | 1.73 MB/s | `https://code.claude.com` | 通用代理 |
| 174 | 253ms | Ghproxy | 0.79 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 175 | 253ms | Sonarcloud | 0.15 MB/s | `https://sonarcloud.io` | 通用代理 |
| 176 | 254ms | You | 0.08 MB/s | `https://you.piccalc.com` | 通用代理 |
| 177 | 259ms | Aiblackboxfc | 0.37 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 178 | 259ms | Oem | 0.05 MB/s | `https://oem.re` | 通用代理 |
| 179 | 262ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 180 | 262ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 181 | 266ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 182 | 268ms | Claude | 0.5 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 183 | 269ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 184 | 269ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 185 | 270ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 186 | 270ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 187 | 274ms | Caiji | 0.16 MB/s | `https://caiji.cyou` | 通用代理 |
| 188 | 276ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 189 | 276ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 190 | 279ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 191 | 280ms | Kuroutoshikou | 0.66 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 192 | 282ms | Agoramarket | 0.54 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 193 | 282ms | Tiktok | 0.1 MB/s | `https://tiktok.com` | 通用代理 |
| 194 | 289ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 195 | 291ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 196 | 296ms | Gh | 0.59 MB/s | `https://gh.padao.fun` | 通用代理 |
| 197 | 296ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 198 | 300ms | Steamcommunity | 0.12 MB/s | `https://steamcommunity.com` | 通用代理 |
| 199 | 302ms | Weaverse | 0.68 MB/s | `https://weaverse.io` | 通用代理 |
| 200 | 306ms | Aomedia | 0.23 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 201 | 312ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 202 | 316ms | B23 | - | `https://b23.tv` | 通用代理 |
| 203 | 317ms | Youtu | 1.24 MB/s | `https://youtu.be` | 通用代理 |
| 204 | 318ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 205 | 320ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 206 | 321ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 207 | 325ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 208 | 325ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 209 | 330ms | 30006000 | 0.64 MB/s | `https://30006000.xyz` | 通用代理 |
| 210 | 331ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 211 | 332ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 212 | 333ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 213 | 334ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 214 | 335ms | Ednovas Mirror | 0.5 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 215 | 335ms | Github | 0.74 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 216 | 341ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 217 | 349ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 218 | 350ms | Hk | 1.15 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 219 | 357ms | Github | 3.5 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 220 | 357ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 221 | 359ms | Store | 1.3 MB/s | `https://store.steampowered.com` | 通用代理 |
| 222 | 371ms | Aps | 0.02 MB/s | `https://aps.com` | 通用代理 |
| 223 | 374ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 224 | 375ms | Github | 2.85 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 225 | 378ms | Turborepo-starter-kit-web | 0.06 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 226 | 379ms | Bailian | 0.11 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 227 | 380ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 228 | 380ms | YYLX Git | 0.8 MB/s | `https://git.yylx.win` | 通用代理 |
| 229 | 390ms | Serverkit | 0.05 MB/s | `https://serverkit.ai` | 通用代理 |
| 230 | 394ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 231 | 397ms | Getgit | 3.1 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 232 | 398ms | GHFast | 0.39 MB/s | `https://ghfast.top` | 通用代理 |
| 233 | 402ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 234 | 408ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 235 | 416ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 236 | 417ms | Gh | 0.99 MB/s | `https://gh.noki.icu` | 通用代理 |
| 237 | 419ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 238 | 422ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 239 | 424ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 240 | 425ms | GH Nxnow | 0.4 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 241 | 425ms | Github | 3.55 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 242 | 426ms | Support | 0.37 MB/s | `https://support.apple.com` | 通用代理 |
| 243 | 428ms | Bible-ai-explorer | 0.05 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 244 | 433ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 245 | 440ms | Safedocx | 0.12 MB/s | `https://safedocx.com` | 通用代理 |
| 246 | 444ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 247 | 445ms | Ark | 0.5 MB/s | `https://ark.intel.com` | 通用代理 |
| 248 | 450ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 249 | 473ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 250 | 474ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 251 | 474ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 252 | 482ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 253 | 484ms | Wl | - | `https://wl.do` | 通用代理 |
| 254 | 485ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 255 | 487ms | Lecvdemarius | 0.05 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 256 | 487ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 257 | 489ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 258 | 499ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 259 | 509ms | Agentkey | 1.95 MB/s | `https://agentkey.app` | 通用代理 |
| 260 | 511ms | Patchworkos | 0.29 MB/s | `https://patchworkos.com` | 通用代理 |
| 261 | 512ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 262 | 518ms | Aosmd | 0.15 MB/s | `https://aosmd.com` | 通用代理 |
| 263 | 523ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 264 | 530ms | Umami-mcp | 1.2 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 265 | 530ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 266 | 533ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 267 | 538ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 268 | 540ms | Nyx | 0.07 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 269 | 545ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 270 | 548ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 271 | 550ms | Lucky | 0.37 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 272 | 550ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 273 | 551ms | GHFile Geekertao | 1.3 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 274 | 555ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 275 | 560ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 276 | 569ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 277 | 573ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 278 | 573ms | Gh | 0.57 MB/s | `https://gh.39.al` | 通用代理 |
| 279 | 582ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 280 | 584ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 281 | 587ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 282 | 598ms | Os | 0.11 MB/s | `https://os.ryo.lu` | 通用代理 |
| 283 | 606ms | Gh | 1.79 MB/s | `https://gh.dpik.top` | 通用代理 |
| 284 | 616ms | Github | 0.38 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 285 | 620ms | Tsukuyomi | 0.11 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 286 | 636ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 287 | 637ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 288 | 645ms | Im | 0.32 MB/s | `https://im.codes` | 通用代理 |
| 289 | 647ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 290 | 656ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 291 | 664ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 292 | 683ms | Ghproxy | 0.23 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 293 | 693ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 294 | 698ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 295 | 708ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 296 | 721ms | Fastfile | 3.55 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 297 | 733ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 298 | 745ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 299 | 749ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 300 | 753ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 301 | 776ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 302 | 778ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 303 | 787ms | Docs | 0.17 MB/s | `https://docs.transifex.com` | 通用代理 |
| 304 | 792ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 305 | 800ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 306 | 808ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 307 | 822ms | Aif | 0.03 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 308 | 823ms | Ccgather | 0.07 MB/s | `https://ccgather.com` | 通用代理 |
| 309 | 824ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 310 | 866ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 311 | 874ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 312 | 900ms | Md | 0.02 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 313 | 907ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 314 | 910ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 315 | 914ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 316 | 934ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 317 | 940ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 318 | 950ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 319 | 956ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 320 | 973ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 321 | 987ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 322 | 987ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 323 | 1026ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 324 | 1028ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 325 | 1058ms | Web | - | `https://web.4399.com` | 通用代理 |
| 326 | 1080ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 327 | 1096ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 328 | 1120ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 329 | 1124ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 330 | 1132ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 331 | 1156ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 332 | 1163ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 333 | 1181ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 334 | 1185ms | Ghproxy | 0.26 MB/s | `https://ghproxy.cc` | 通用代理 |
| 335 | 1217ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 336 | 1219ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 337 | 1219ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 338 | 1226ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 339 | 1246ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 340 | 1251ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 341 | 1255ms | GHProxy Net | 0.02 MB/s | `https://ghproxy.net` | 通用代理 |
| 342 | 1282ms | V | - | `https://v.douyin.com` | 通用代理 |
| 343 | 1292ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 344 | 1319ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 345 | 1320ms | Github | 0.09 MB/s | `https://github.chenc.dev` | 通用代理 |
| 346 | 1352ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 347 | 1414ms | Cf | 0.25 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 348 | 1491ms | Git | 0.11 MB/s | `https://git.669966.xyz` | 通用代理 |
| 349 | 1562ms | Mobilevc | - | `https://mobilevc.top` | 通用代理 |
| 350 | 1588ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 351 | 1619ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 352 | 1698ms | Invent | 0.01 MB/s | `https://invent.kde.org` | 通用代理 |
| 353 | 1702ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 354 | 1769ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 355 | 1890ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 356 | 2067ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 357 | 2106ms | Img | - | `https://img.ink` | 通用代理 |
| 358 | 2403ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 359 | 2484ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 360 | 2588ms | Wget | - | `https://wget.la` | 通用代理 |
| 361 | 2683ms | G | 0.03 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 362 | 2857ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 363 | 2964ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 364 | 3000ms | Ghproxy | 0.12 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 365 | 4010ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Npee Down (`down-npee-cn`) | 22 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Gh (`gh-halonice-com`) | 21 次 |
| Git (`git-tangbai-cc`) | 22 次 |
| Proxy (`proxy-yaoyaoling-net`) | 1 次 |
| Gh (`gh-b52m-cn`) | 3 次 |
| Proxy (`proxy-vvvv-ee`) | 5 次 |
| 5555 (`5555-cab`) | 12 次 |
| Projects (`projects-ow2-org`) | 1 次 |
| Doxygen (`doxygen-org`) | 8 次 |
| Flashtype (`flashtype-com`) | 2 次 |
| Maplecode (`maplecode-art`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 370 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **377** | |

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
