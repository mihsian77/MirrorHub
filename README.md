# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-27T03:54:01Z**，每 6 小时刷新一次。当前 ✅ **368** 在线 / ⚠️ **16** 不稳定 / ⚰️ **50** 已失效归档。

## 核心特性

- **384 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 59ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 2 | 61ms | Microsoftedge | 0.31 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 65ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 4 | 68ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 5 | 74ms | Deno | 0.77 MB/s | `https://deno.com` | 通用代理 |
| 6 | 81ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 7 | 81ms | Linkedin | 0.12 MB/s | `https://linkedin.com` | 通用代理 |
| 8 | 84ms | Img | - | `https://img.shields.io` | 通用代理 |
| 9 | 84ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 10 | 88ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 11 | 91ms | Dilo-d14 | 0.19 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 12 | 95ms | Wordpaper | 0.31 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 13 | 97ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 14 | 97ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 15 | 98ms | X | 0.93 MB/s | `https://x.com` | 通用代理 |
| 16 | 99ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 17 | 99ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 18 | 100ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 19 | 100ms | Kighelper-cloud | 0.1 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 20 | 101ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 21 | 104ms | Crypto-funding-arbitrage | 0.07 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 22 | 105ms | Xjtu-nyxf-study-material | 0.11 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 23 | 107ms | Osf | 0.03 MB/s | `https://osf.io` | 通用代理 |
| 24 | 108ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 25 | 109ms | Lawyer-yu | 0.08 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 26 | 110ms | Opresume | 0.5 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 27 | 111ms | Githubstatus | 1.1 MB/s | `https://githubstatus.com` | 通用代理 |
| 28 | 113ms | App | 0.02 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 29 | 114ms | App | 0.1 MB/s | `https://app.netlify.com` | 通用代理 |
| 30 | 116ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 31 | 116ms | Huly-mcp | 0.19 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 32 | 116ms | Tools | 1.42 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 33 | 121ms | Resume-5lv | 0.23 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 34 | 122ms | Impeccable | 0.76 MB/s | `https://impeccable.style` | 通用代理 |
| 35 | 124ms | Cognitum | 0.27 MB/s | `https://cognitum.one` | 通用代理 |
| 36 | 126ms | Impro | 1.55 MB/s | `https://impro.social` | 通用代理 |
| 37 | 128ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 38 | 129ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 39 | 129ms | Zebrunner | 1.21 MB/s | `https://zebrunner.com` | 通用代理 |
| 40 | 130ms | Agentlimb | 0.19 MB/s | `https://agentlimb.com` | 通用代理 |
| 41 | 132ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 42 | 132ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 43 | 137ms | Clayrune | 0.13 MB/s | `https://clayrune.io` | 通用代理 |
| 44 | 139ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 45 | 139ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 46 | 139ms | Opentakeoff | 0.05 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 47 | 140ms | Thumb | 1.05 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 48 | 141ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 49 | 141ms | Discord | 0.09 MB/s | `https://discord.gg` | 通用代理 |
| 50 | 142ms | Gpui | 0.14 MB/s | `https://gpui.rs` | 通用代理 |
| 51 | 143ms | Gp | 2.55 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 52 | 143ms | Vibesql | 0.1 MB/s | `https://vibesql.org` | 通用代理 |
| 53 | 144ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 54 | 144ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 55 | 145ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 56 | 145ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 57 | 145ms | Gh | - | `https://gh.198962.xyz` | 通用代理 |
| 58 | 145ms | Github | 2.41 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 59 | 147ms | Gitea-mirror | 0.63 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 60 | 147ms | Tokei | 0.37 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 61 | 148ms | GH-Proxy | - | `https://gh-proxy.com` | 通用代理 |
| 62 | 148ms | Github | 1.55 MB/s | `https://github.788787.xyz` | 通用代理 |
| 63 | 149ms | Cbrowser | 1.48 MB/s | `https://cbrowser.ai` | 通用代理 |
| 64 | 149ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 65 | 149ms | Serac | 0.07 MB/s | `https://serac.build` | 通用代理 |
| 66 | 150ms | Anh | 0.2 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 67 | 150ms | Tms | 0.15 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 68 | 151ms | Git | 2.23 MB/s | `https://git.820828.xyz` | 通用代理 |
| 69 | 151ms | Music-cli | 0.19 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 70 | 152ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 71 | 152ms | Gh | 0.41 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 72 | 152ms | Opencovibe | 0.31 MB/s | `https://opencovibe.com` | 通用代理 |
| 73 | 153ms | Github | 2.24 MB/s | `https://github.880824.xyz` | 通用代理 |
| 74 | 153ms | L4d2 | 0.13 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 75 | 154ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 76 | 154ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 77 | 154ms | Git | 2.49 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 78 | 155ms | Caw | 0.04 MB/s | `https://caw.rocks` | 通用代理 |
| 79 | 155ms | Openpua | 0.46 MB/s | `https://openpua.ai` | 通用代理 |
| 80 | 156ms | Codeeraser | 0.11 MB/s | `https://codeeraser.dev` | 通用代理 |
| 81 | 156ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 82 | 156ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 83 | 157ms | Bestdori | 0.09 MB/s | `https://bestdori.com` | 通用代理 |
| 84 | 157ms | Coffeecli | 0.07 MB/s | `https://coffeecli.com` | 通用代理 |
| 85 | 157ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 86 | 157ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 87 | 158ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 88 | 159ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 89 | 161ms | Miaozitie | 0.07 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 90 | 162ms | Gh | 2.02 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 91 | 162ms | Glass | 0.23 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 92 | 164ms | Contrib | 0.39 MB/s | `https://contrib.rocks` | 通用代理 |
| 93 | 165ms | Alas | 0.68 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 94 | 165ms | Caiji | 0.1 MB/s | `https://caiji.cyou` | 通用代理 |
| 95 | 166ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 96 | 166ms | Cody | 0.19 MB/s | `https://cody.todyle.com` | 通用代理 |
| 97 | 166ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 98 | 170ms | Gsd | 0.18 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 99 | 171ms | Ghproxy | 2.1 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 100 | 171ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 101 | 172ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 102 | 173ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 103 | 174ms | Nextup-resource | 0.03 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 104 | 175ms | Components | 0.09 MB/s | `https://components.dereekb.com` | 通用代理 |
| 105 | 177ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 106 | 178ms | Bolt2github | 0.04 MB/s | `https://bolt2github.com` | 通用代理 |
| 107 | 180ms | GH Monlor | - | `https://gh.monlor.com` | 通用代理 |
| 108 | 180ms | Github | 1.38 MB/s | `https://github.ihnic.com` | 通用代理 |
| 109 | 180ms | Holyclaude | 0.12 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 110 | 181ms | Bananaslides | 0.27 MB/s | `https://bananaslides.online` | 通用代理 |
| 111 | 181ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 112 | 182ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 113 | 182ms | Training | 0.17 MB/s | `https://training.ti.com` | 通用代理 |
| 114 | 182ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 115 | 184ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 116 | 184ms | Polgarand | 0.1 MB/s | `https://polgarand.org` | 通用代理 |
| 117 | 186ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 118 | 186ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 119 | 187ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 120 | 192ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 121 | 192ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 122 | 192ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 123 | 193ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 124 | 194ms | Kuroutoshikou | 0.67 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 125 | 196ms | GH-Proxy Org | - | `https://gh-proxy.org` | 通用代理 |
| 126 | 196ms | Ghproxy | 1.87 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 127 | 196ms | Opensunsama | 0.05 MB/s | `https://opensunsama.com` | 通用代理 |
| 128 | 201ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 129 | 202ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 130 | 203ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 131 | 204ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 132 | 205ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 133 | 205ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 134 | 208ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 135 | 211ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 136 | 211ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 137 | 213ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 138 | 213ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 139 | 215ms | Ginlix | 0.41 MB/s | `https://ginlix.ai` | 通用代理 |
| 140 | 216ms | Kenyu | 2.58 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 141 | 216ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 142 | 220ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 143 | 220ms | Ode | - | `https://ode.fun` | 通用代理 |
| 144 | 220ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 145 | 222ms | Aiblackboxfc | 0.23 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 146 | 222ms | Twitter | 0.81 MB/s | `https://twitter.com` | 通用代理 |
| 147 | 223ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 148 | 224ms | FastGit CC | - | `https://fastgit.cc` | 通用代理 |
| 149 | 225ms | Ampcode | 0.18 MB/s | `https://ampcode.com` | 通用代理 |
| 150 | 226ms | CrashMC CDN | - | `https://cdn.crashmc.com` | 通用代理 |
| 151 | 229ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 152 | 230ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 153 | 230ms | Tvv | 1.9 MB/s | `https://tvv.tw` | 通用代理 |
| 154 | 231ms | Api | 0.12 MB/s | `https://api.solov.cc` | 通用代理 |
| 155 | 231ms | Ggg | - | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 156 | 231ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 157 | 235ms | Axios-http | 0.37 MB/s | `https://axios-http.com` | 通用代理 |
| 158 | 235ms | Coreos | 1.0 MB/s | `https://coreos.com` | 通用代理 |
| 159 | 238ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 160 | 239ms | Microcoreos | 0.45 MB/s | `https://microcoreos.com` | 通用代理 |
| 161 | 240ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 162 | 241ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 163 | 242ms | Gh | - | `https://gh.idayer.com` | 通用代理 |
| 164 | 244ms | Gh | - | `https://gh.1k.ink` | 通用代理 |
| 165 | 244ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 166 | 245ms | Cursor | 0.43 MB/s | `https://cursor.com` | 通用代理 |
| 167 | 246ms | Ghproxy | 0.67 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 168 | 252ms | Clypra | 0.07 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 169 | 257ms | Aka | 0.47 MB/s | `https://aka.ms` | 通用代理 |
| 170 | 259ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 171 | 260ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 172 | 262ms | Nisar | 0.82 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 173 | 263ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 174 | 263ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 175 | 263ms | Code | 1.15 MB/s | `https://code.claude.com` | 通用代理 |
| 176 | 269ms | Agoramarket | 0.04 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 177 | 269ms | Sub | 0.18 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 178 | 270ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 179 | 271ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 180 | 272ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 181 | 279ms | Visionmemorymcp | 0.22 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 182 | 280ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 183 | 281ms | Tiktok | 0.21 MB/s | `https://tiktok.com` | 通用代理 |
| 184 | 284ms | Github | 0.82 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 185 | 290ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 186 | 291ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 187 | 294ms | Claude | 0.4 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 188 | 298ms | Youtu | 1.26 MB/s | `https://youtu.be` | 通用代理 |
| 189 | 299ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 190 | 301ms | Aomedia | 0.27 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 191 | 308ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 192 | 308ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 193 | 308ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 194 | 313ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 195 | 314ms | Sonarcloud | 0.02 MB/s | `https://sonarcloud.io` | 通用代理 |
| 196 | 315ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 197 | 318ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 198 | 320ms | 30006000 | 0.61 MB/s | `https://30006000.xyz` | 通用代理 |
| 199 | 320ms | Gh | 0.62 MB/s | `https://gh.padao.fun` | 通用代理 |
| 200 | 320ms | Sina | 0.62 MB/s | `https://sina.dev` | 通用代理 |
| 201 | 322ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 202 | 323ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 203 | 325ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 204 | 327ms | Weaverse | 0.67 MB/s | `https://weaverse.io` | 通用代理 |
| 205 | 329ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 206 | 330ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 207 | 330ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 208 | 332ms | B23 | - | `https://b23.tv` | 通用代理 |
| 209 | 334ms | Steamcommunity | 0.11 MB/s | `https://steamcommunity.com` | 通用代理 |
| 210 | 343ms | Github | 1.78 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 211 | 344ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 212 | 346ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 213 | 352ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 214 | 353ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 215 | 355ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 216 | 357ms | Store | 0.96 MB/s | `https://store.steampowered.com` | 通用代理 |
| 217 | 362ms | Github | 1.92 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 218 | 364ms | Getgit | - | `https://getgit.love8yun.eu.org` | 通用代理 |
| 219 | 368ms | Bailian | 0.1 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 220 | 371ms | GH Nxnow | 0.37 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 221 | 380ms | GHFast | 0.4 MB/s | `https://ghfast.top` | 通用代理 |
| 222 | 381ms | Agentkey | 1.22 MB/s | `https://agentkey.app` | 通用代理 |
| 223 | 381ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 224 | 383ms | Hk | 0.58 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 225 | 385ms | You | 0.08 MB/s | `https://you.piccalc.com` | 通用代理 |
| 226 | 386ms | Turborepo-starter-kit-web | 0.07 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 227 | 387ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 228 | 393ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 229 | 397ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 230 | 397ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 231 | 400ms | Ednovas Mirror | 0.7 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 232 | 404ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 233 | 404ms | Gh | - | `https://gh.noki.icu` | 通用代理 |
| 234 | 411ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 235 | 411ms | Github | 2.54 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 236 | 413ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 237 | 415ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 238 | 415ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 239 | 417ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 240 | 422ms | Aps | 0.03 MB/s | `https://aps.com` | 通用代理 |
| 241 | 423ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 242 | 432ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 243 | 434ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 244 | 434ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 245 | 446ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 246 | 454ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 247 | 455ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 248 | 467ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 249 | 471ms | Api | 0.02 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 250 | 472ms | Bible-ai-explorer | 0.06 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 251 | 481ms | Lecvdemarius | 0.06 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 252 | 483ms | Patchworkos | 0.28 MB/s | `https://patchworkos.com` | 通用代理 |
| 253 | 486ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 254 | 489ms | Umami-mcp | 0.91 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 255 | 491ms | Ark | 0.45 MB/s | `https://ark.intel.com` | 通用代理 |
| 256 | 494ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 257 | 497ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 258 | 500ms | Safedocx | 0.09 MB/s | `https://safedocx.com` | 通用代理 |
| 259 | 508ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 260 | 508ms | Wl | - | `https://wl.do` | 通用代理 |
| 261 | 510ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 262 | 512ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 263 | 521ms | Im | 1.47 MB/s | `https://im.codes` | 通用代理 |
| 264 | 533ms | Lucky | 0.41 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 265 | 543ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 266 | 544ms | Nyx | 0.06 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 267 | 547ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 268 | 553ms | Aosmd | 0.18 MB/s | `https://aosmd.com` | 通用代理 |
| 269 | 559ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 270 | 561ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 271 | 569ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 272 | 570ms | Support | 0.14 MB/s | `https://support.apple.com` | 通用代理 |
| 273 | 579ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 274 | 581ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 275 | 582ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 276 | 600ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 277 | 613ms | Github | 0.08 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 278 | 630ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 279 | 633ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 280 | 644ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 281 | 656ms | Gh | 0.39 MB/s | `https://gh.dpik.top` | 通用代理 |
| 282 | 666ms | Tsukuyomi | 0.07 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 283 | 675ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 284 | 676ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 285 | 678ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 286 | 679ms | Fastfile | 1.48 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 287 | 684ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 288 | 685ms | Gh | 0.82 MB/s | `https://gh.39.al` | 通用代理 |
| 289 | 693ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 290 | 693ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 291 | 702ms | Ghproxy | 0.22 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 292 | 712ms | GHFile Geekertao | 0.28 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 293 | 714ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 294 | 744ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 295 | 746ms | Os | 0.1 MB/s | `https://os.ryo.lu` | 通用代理 |
| 296 | 752ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 297 | 755ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 298 | 760ms | Aif | 0.02 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 299 | 764ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 300 | 769ms | Docs | 0.19 MB/s | `https://docs.transifex.com` | 通用代理 |
| 301 | 770ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 302 | 797ms | Git | 0.22 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 303 | 810ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 304 | 816ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 305 | 819ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 306 | 828ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 307 | 846ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 308 | 884ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 309 | 898ms | Task | 0.01 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 310 | 912ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 311 | 918ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 312 | 924ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 313 | 926ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 314 | 932ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 315 | 950ms | Mimo | 0.17 MB/s | `https://mimo.mi.com` | 通用代理 |
| 316 | 953ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 317 | 965ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 318 | 980ms | Web | - | `https://web.4399.com` | 通用代理 |
| 319 | 982ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 320 | 1007ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 321 | 1009ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 322 | 1024ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 323 | 1032ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 324 | 1039ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 325 | 1055ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 326 | 1075ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 327 | 1136ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 328 | 1153ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 329 | 1158ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 330 | 1170ms | V | - | `https://v.douyin.com` | 通用代理 |
| 331 | 1174ms | Your-domain | 0.04 MB/s | `https://your-domain.com` | 通用代理 |
| 332 | 1176ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 333 | 1185ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 334 | 1201ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 335 | 1213ms | Ghproxy | 0.24 MB/s | `https://ghproxy.cc` | 通用代理 |
| 336 | 1220ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 337 | 1225ms | Atomcode | 0.07 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 338 | 1225ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 339 | 1243ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 340 | 1267ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 341 | 1273ms | GHProxy Net | 0.04 MB/s | `https://ghproxy.net` | 通用代理 |
| 342 | 1290ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 343 | 1317ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 344 | 1332ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 345 | 1346ms | Git | - | `https://git.669966.xyz` | 通用代理 |
| 346 | 1352ms | Github | 0.11 MB/s | `https://github.chenc.dev` | 通用代理 |
| 347 | 1380ms | Cf | 0.24 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 348 | 1396ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 349 | 1405ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 350 | 1441ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 351 | 1535ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 352 | 1604ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 353 | 1604ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 354 | 1685ms | Heycall-e | 0.09 MB/s | `https://heycall-e.com` | 通用代理 |
| 355 | 1700ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 356 | 1901ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 357 | 2169ms | Img | - | `https://img.ink` | 通用代理 |
| 358 | 2329ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 359 | 2334ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 360 | 2442ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 361 | 2480ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 362 | 2748ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 363 | 2874ms | G | - | `https://g.blfrp.cn` | 通用代理 |
| 364 | 3049ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 365 | 3135ms | Ghproxy | 0.06 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 366 | 3175ms | Gh | 0.23 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 367 | 3275ms | Wget | 0.01 MB/s | `https://wget.la` | 通用代理 |
| 368 | 4311ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（16 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| YYLX Git (`git-yylx-win`) | 3 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 6 次 |
| GitClone (`gitclone-com`) | 1 次 |
| Gh (`gh-halonice-com`) | 27 次 |
| Proxy (`proxy-yaoyaoling-net`) | 1 次 |
| Mirror (`mirror-houlang-cloud`) | 2 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |
| 5555 (`5555-cab`) | 18 次 |
| Code (`code-leez-tech`) | 1 次 |
| Status (`status-leez-tech`) | 1 次 |
| Doxygen (`doxygen-org`) | 14 次 |
| Flashtype (`flashtype-com`) | 1 次 |
| Maplecode (`maplecode-art`) | 7 次 |
| Mobilevc (`mobilevc-top`) | 3 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 3 次 |
| Adult (`adult-contents-fc2-com`) | 2 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 377 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **384** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（50 个）。

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
