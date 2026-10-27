# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-27T11:42:49Z**，每 6 小时刷新一次。当前 ✅ **372** 在线 / ⚠️ **17** 不稳定 / ⚰️ **51** 已失效归档。

## 核心特性

- **389 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 57ms | Microsoftedge | 0.86 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 57ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 3 | 67ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 4 | 67ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 5 | 75ms | Deno | 0.57 MB/s | `https://deno.com` | 通用代理 |
| 6 | 78ms | Linkedin | 0.47 MB/s | `https://linkedin.com` | 通用代理 |
| 7 | 80ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 8 | 80ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 9 | 81ms | Img | - | `https://img.shields.io` | 通用代理 |
| 10 | 82ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 11 | 89ms | Dilo-d14 | 0.25 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 12 | 91ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 13 | 94ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 14 | 96ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 15 | 96ms | X | 1.32 MB/s | `https://x.com` | 通用代理 |
| 16 | 97ms | Wordpaper | 1.01 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 17 | 99ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 18 | 100ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 19 | 100ms | Godocs | 0.12 MB/s | `https://godocs.io` | 通用代理 |
| 20 | 101ms | Crypto-funding-arbitrage | 0.08 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 21 | 101ms | Kighelper-cloud | 0.11 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 22 | 102ms | Githubstatus | 2.42 MB/s | `https://githubstatus.com` | 通用代理 |
| 23 | 102ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 24 | 103ms | Lawyer-yu | 0.27 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 25 | 103ms | Xjtu-nyxf-study-material | 0.18 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 26 | 104ms | App | 0.19 MB/s | `https://app.netlify.com` | 通用代理 |
| 27 | 108ms | Opresume | 0.72 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 28 | 109ms | Osf | 0.06 MB/s | `https://osf.io` | 通用代理 |
| 29 | 112ms | App | 0.08 MB/s | `https://app.codecov.io` | 通用代理 |
| 30 | 113ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 31 | 113ms | Tools | 4.23 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 32 | 115ms | Huly-mcp | 0.16 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 33 | 117ms | Impeccable | 1.41 MB/s | `https://impeccable.style` | 通用代理 |
| 34 | 117ms | Zebrunner | 2.75 MB/s | `https://zebrunner.com` | 通用代理 |
| 35 | 122ms | Impro | 2.54 MB/s | `https://impro.social` | 通用代理 |
| 36 | 123ms | Resume-5lv | 0.23 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 37 | 125ms | Cognitum | 0.27 MB/s | `https://cognitum.one` | 通用代理 |
| 38 | 125ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 39 | 125ms | Goreportcard | 0.04 MB/s | `https://goreportcard.com` | 通用代理 |
| 40 | 127ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 41 | 127ms | Thumb | 6.0 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 42 | 130ms | Agentlimb | 0.3 MB/s | `https://agentlimb.com` | 通用代理 |
| 43 | 131ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 44 | 131ms | Opentakeoff | 0.1 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 45 | 132ms | Freeport | 0.05 MB/s | `https://freeport.network` | 通用代理 |
| 46 | 133ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 47 | 136ms | Clayrune | 0.18 MB/s | `https://clayrune.io` | 通用代理 |
| 48 | 138ms | Discord | 0.15 MB/s | `https://discord.gg` | 通用代理 |
| 49 | 138ms | Gp | 3.35 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 50 | 139ms | Gpui | 0.31 MB/s | `https://gpui.rs` | 通用代理 |
| 51 | 140ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 52 | 140ms | Tms | 0.18 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 53 | 140ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 54 | 141ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 55 | 141ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 56 | 142ms | Github | 2.49 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 57 | 142ms | Music-cli | 0.53 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 58 | 142ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 59 | 143ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 60 | 143ms | Github | 3.12 MB/s | `https://github.788787.xyz` | 通用代理 |
| 61 | 143ms | Travis-ci | 0.33 MB/s | `https://travis-ci.org` | 通用代理 |
| 62 | 144ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 63 | 144ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 64 | 144ms | Gh | 3.03 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 65 | 144ms | Git | 2.77 MB/s | `https://git.820828.xyz` | 通用代理 |
| 66 | 144ms | Tokei | 0.8 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 67 | 144ms | Vibesql | 0.15 MB/s | `https://vibesql.org` | 通用代理 |
| 68 | 145ms | GH-Proxy | 1.3 MB/s | `https://gh-proxy.com` | 通用代理 |
| 69 | 145ms | Github | 2.19 MB/s | `https://github.880824.xyz` | 通用代理 |
| 70 | 145ms | Savannah | 0.08 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 71 | 146ms | Gh | 2.53 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 72 | 146ms | Gitea-mirror | 0.98 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 73 | 147ms | Git | 2.49 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 74 | 147ms | Serac | 0.09 MB/s | `https://serac.build` | 通用代理 |
| 75 | 148ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 76 | 149ms | Hopp | 0.05 MB/s | `https://hopp.sh` | 通用代理 |
| 77 | 149ms | L4d2 | 0.18 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 78 | 150ms | Anh | 0.16 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 79 | 150ms | Cbrowser | 2.21 MB/s | `https://cbrowser.ai` | 通用代理 |
| 80 | 150ms | Openpua | 0.45 MB/s | `https://openpua.ai` | 通用代理 |
| 81 | 153ms | Bestdori | 0.1 MB/s | `https://bestdori.com` | 通用代理 |
| 82 | 153ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 83 | 154ms | Demo | 0.05 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 84 | 154ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 85 | 154ms | Opencovibe | 0.51 MB/s | `https://opencovibe.com` | 通用代理 |
| 86 | 154ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 87 | 157ms | Caw | 0.06 MB/s | `https://caw.rocks` | 通用代理 |
| 88 | 157ms | Codeeraser | 0.16 MB/s | `https://codeeraser.dev` | 通用代理 |
| 89 | 159ms | Chops | 0.04 MB/s | `https://chops.md` | 通用代理 |
| 90 | 159ms | Components | 0.17 MB/s | `https://components.dereekb.com` | 通用代理 |
| 91 | 159ms | Miaozitie | 0.09 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 92 | 159ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 93 | 160ms | Cody | 0.27 MB/s | `https://cody.todyle.com` | 通用代理 |
| 94 | 160ms | Nextup-resource | 0.05 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 95 | 161ms | Coffeecli | 0.13 MB/s | `https://coffeecli.com` | 通用代理 |
| 96 | 161ms | Gh | 2.05 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 97 | 162ms | Caiji | 0.07 MB/s | `https://caiji.cyou` | 通用代理 |
| 98 | 162ms | Contrib | 0.51 MB/s | `https://contrib.rocks` | 通用代理 |
| 99 | 162ms | Glass | 0.3 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 100 | 164ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 101 | 165ms | Alas | 1.22 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 102 | 165ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 103 | 165ms | Shiori-v1 | 0.05 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 104 | 167ms | Gsd | 0.37 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 105 | 168ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 106 | 170ms | Training | 0.28 MB/s | `https://training.ti.com` | 通用代理 |
| 107 | 171ms | Bolt2github | 0.07 MB/s | `https://bolt2github.com` | 通用代理 |
| 108 | 171ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 109 | 171ms | Play | 0.05 MB/s | `https://play.templatical.com` | 通用代理 |
| 110 | 172ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 111 | 172ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 112 | 173ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 113 | 174ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 114 | 174ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 115 | 174ms | GH Monlor | 1.36 MB/s | `https://gh.monlor.com` | 通用代理 |
| 116 | 174ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 117 | 175ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 118 | 176ms | Github | 2.25 MB/s | `https://github.ihnic.com` | 通用代理 |
| 119 | 178ms | Ghproxy | 2.39 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 120 | 178ms | Holyclaude | 0.14 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 121 | 180ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 122 | 181ms | Polgarand | 0.11 MB/s | `https://polgarand.org` | 通用代理 |
| 123 | 185ms | Opensunsama | 0.08 MB/s | `https://opensunsama.com` | 通用代理 |
| 124 | 186ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 125 | 186ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 126 | 187ms | Kuroutoshikou | 1.42 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 127 | 187ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 128 | 194ms | Ai-trend-publish | 0.06 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 129 | 195ms | Phabricator | 0.14 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 130 | 196ms | Bananaslides | 0.35 MB/s | `https://bananaslides.online` | 通用代理 |
| 131 | 196ms | GH-Proxy Org | 1.09 MB/s | `https://gh-proxy.org` | 通用代理 |
| 132 | 196ms | Gh | 2.34 MB/s | `https://gh.1k.ink` | 通用代理 |
| 133 | 200ms | Ghproxy | 3.52 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 134 | 201ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 135 | 201ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 136 | 203ms | Ginlix | 0.96 MB/s | `https://ginlix.ai` | 通用代理 |
| 137 | 204ms | Ode | - | `https://ode.fun` | 通用代理 |
| 138 | 204ms | Themolt | 0.07 MB/s | `https://themolt.net` | 通用代理 |
| 139 | 205ms | Aiblackboxfc | 0.65 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 140 | 206ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 141 | 208ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 142 | 212ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 143 | 213ms | Coreos | 6.33 MB/s | `https://coreos.com` | 通用代理 |
| 144 | 215ms | Axios-http | 1.59 MB/s | `https://axios-http.com` | 通用代理 |
| 145 | 215ms | Kenyu | 3.16 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 146 | 216ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 147 | 216ms | Twitter | 1.28 MB/s | `https://twitter.com` | 通用代理 |
| 148 | 217ms | Ampcode | 0.35 MB/s | `https://ampcode.com` | 通用代理 |
| 149 | 218ms | Congressmcp | 0.04 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 150 | 219ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 151 | 222ms | CrashMC CDN | 1.49 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 152 | 223ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 153 | 226ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 154 | 227ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 155 | 229ms | Cursor | 0.79 MB/s | `https://cursor.com` | 通用代理 |
| 156 | 229ms | Tvv | 2.46 MB/s | `https://tvv.tw` | 通用代理 |
| 157 | 230ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 158 | 232ms | Clypra | 0.12 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 159 | 232ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 160 | 235ms | Wings | 0.04 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 161 | 235ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 162 | 237ms | Ggg | 2.04 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 163 | 238ms | Microcoreos | 0.42 MB/s | `https://microcoreos.com` | 通用代理 |
| 164 | 239ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 165 | 244ms | Aka | 1.38 MB/s | `https://aka.ms` | 通用代理 |
| 166 | 244ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 167 | 246ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 168 | 247ms | Ai-watch | 0.04 MB/s | `https://ai-watch.dev` | 通用代理 |
| 169 | 250ms | Ghproxy | 0.6 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 170 | 256ms | Api | 0.06 MB/s | `https://api.solov.cc` | 通用代理 |
| 171 | 261ms | Agoramarket | 0.03 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 172 | 261ms | Zuckerbot | 0.05 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 173 | 262ms | Nisar | 0.86 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 174 | 265ms | Tiktok | 0.24 MB/s | `https://tiktok.com` | 通用代理 |
| 175 | 266ms | Code | 2.35 MB/s | `https://code.claude.com` | 通用代理 |
| 176 | 266ms | FastGit CC | 1.68 MB/s | `https://fastgit.cc` | 通用代理 |
| 177 | 268ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 178 | 270ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 179 | 272ms | Sub | 0.21 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 180 | 277ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 181 | 278ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 182 | 279ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 183 | 279ms | Visionmemorymcp | 0.24 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 184 | 284ms | Github | 0.6 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 185 | 285ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 186 | 288ms | Aomedia | 0.38 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 187 | 288ms | Youtu | 2.76 MB/s | `https://youtu.be` | 通用代理 |
| 188 | 293ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 189 | 303ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 190 | 304ms | Claude | 0.46 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 191 | 304ms | Data | 0.04 MB/s | `https://data.openecon.ai` | 通用代理 |
| 192 | 308ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 193 | 311ms | Sina | 0.69 MB/s | `https://sina.dev` | 通用代理 |
| 194 | 313ms | Agenticcorporation | 0.05 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 195 | 313ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 196 | 317ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 197 | 317ms | Weaverse | 1.12 MB/s | `https://weaverse.io` | 通用代理 |
| 198 | 318ms | Sonarcloud | 0.02 MB/s | `https://sonarcloud.io` | 通用代理 |
| 199 | 319ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 200 | 320ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 201 | 323ms | 30006000 | 0.5 MB/s | `https://30006000.xyz` | 通用代理 |
| 202 | 325ms | Steamcommunity | 0.15 MB/s | `https://steamcommunity.com` | 通用代理 |
| 203 | 326ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 204 | 326ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 205 | 327ms | Github | 2.64 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 206 | 327ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 207 | 328ms | Gh | 0.46 MB/s | `https://gh.padao.fun` | 通用代理 |
| 208 | 330ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 209 | 332ms | Radio-browser | 0.05 MB/s | `https://radio-browser.info` | 通用代理 |
| 210 | 335ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 211 | 335ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 212 | 337ms | B23 | - | `https://b23.tv` | 通用代理 |
| 213 | 338ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 214 | 343ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 215 | 344ms | Agent-room | 0.03 MB/s | `https://agent-room.com` | 通用代理 |
| 216 | 345ms | Store | 1.62 MB/s | `https://store.steampowered.com` | 通用代理 |
| 217 | 347ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 218 | 349ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 219 | 352ms | Github | 2.77 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 220 | 359ms | Getgit | 3.06 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 221 | 359ms | Turborepo-starter-kit-web | 0.13 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 222 | 368ms | Agentkey | 0.11 MB/s | `https://agentkey.app` | 通用代理 |
| 223 | 369ms | Bailian | 0.06 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 224 | 372ms | GH Nxnow | 0.49 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 225 | 373ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 226 | 375ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 227 | 376ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 228 | 378ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 229 | 380ms | Ednovas Mirror | 0.33 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 230 | 381ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 231 | 388ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 232 | 388ms | You | 0.06 MB/s | `https://you.piccalc.com` | 通用代理 |
| 233 | 390ms | Autonomi | 0.04 MB/s | `https://autonomi.dev` | 通用代理 |
| 234 | 391ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 235 | 393ms | Hk | 1.39 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 236 | 394ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 237 | 402ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 238 | 413ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 239 | 414ms | Aps | 0.04 MB/s | `https://aps.com` | 通用代理 |
| 240 | 414ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 241 | 415ms | Gh | 0.69 MB/s | `https://gh.noki.icu` | 通用代理 |
| 242 | 416ms | Github | 2.31 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 243 | 424ms | Bseindia | - | `https://bseindia.com` | 通用代理 |
| 244 | 424ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 245 | 425ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 246 | 446ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 247 | 449ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 248 | 450ms | Ark | 0.47 MB/s | `https://ark.intel.com` | 通用代理 |
| 249 | 453ms | Adult | 0.01 MB/s | `https://adult.contents.fc2.com` | 通用代理 |
| 250 | 453ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 251 | 456ms | Msdn | 0.11 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 252 | 458ms | Bible-ai-explorer | 0.08 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 253 | 459ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 254 | 465ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 255 | 467ms | Lecvdemarius | 0.1 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 256 | 467ms | Memstack | 0.09 MB/s | `https://memstack.pro` | 通用代理 |
| 257 | 472ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 258 | 476ms | Patchworkos | 0.4 MB/s | `https://patchworkos.com` | 通用代理 |
| 259 | 476ms | Safedocx | 0.18 MB/s | `https://safedocx.com` | 通用代理 |
| 260 | 484ms | GHFast | 0.39 MB/s | `https://ghfast.top` | 通用代理 |
| 261 | 489ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 262 | 497ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 263 | 497ms | Umami-mcp | 1.04 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 264 | 519ms | Wl | - | `https://wl.do` | 通用代理 |
| 265 | 521ms | Lucky | 0.55 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 266 | 524ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 267 | 534ms | Aosmd | 0.3 MB/s | `https://aosmd.com` | 通用代理 |
| 268 | 545ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 269 | 546ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 270 | 553ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 271 | 566ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 272 | 570ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 273 | 571ms | Gh | 3.2 MB/s | `https://gh.dpik.top` | 通用代理 |
| 274 | 573ms | Tsukuyomi | 0.13 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 275 | 573ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 276 | 574ms | Im | 0.26 MB/s | `https://im.codes` | 通用代理 |
| 277 | 580ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 278 | 585ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 279 | 588ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 280 | 604ms | 3d-set-visualizer | 0.06 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 281 | 610ms | Support | 0.12 MB/s | `https://support.apple.com` | 通用代理 |
| 282 | 620ms | Clawbiz | 0.05 MB/s | `https://clawbiz.io` | 通用代理 |
| 283 | 628ms | Internhack | 0.04 MB/s | `https://internhack.xyz` | 通用代理 |
| 284 | 629ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 285 | 634ms | Github | 0.35 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 286 | 656ms | Agoracitizen | 0.03 MB/s | `https://agoracitizen.app` | 通用代理 |
| 287 | 658ms | Fastfile | 2.22 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 288 | 678ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 289 | 685ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 290 | 686ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 291 | 689ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 292 | 695ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 293 | 711ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 294 | 714ms | Gh | 0.61 MB/s | `https://gh.39.al` | 通用代理 |
| 295 | 720ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 296 | 722ms | Os | 0.06 MB/s | `https://os.ryo.lu` | 通用代理 |
| 297 | 723ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 298 | 729ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 299 | 740ms | Docs | 0.28 MB/s | `https://docs.transifex.com` | 通用代理 |
| 300 | 741ms | Chinamnos | - | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 301 | 743ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 302 | 756ms | Tracely-studio | 0.03 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 303 | 760ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 304 | 771ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 305 | 799ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 306 | 812ms | Git | - | `https://git.tangbai.cc` | 通用代理 |
| 307 | 830ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 308 | 885ms | Ccgather | 0.05 MB/s | `https://ccgather.com` | 通用代理 |
| 309 | 907ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 310 | 907ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 311 | 909ms | Task | 0.01 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 312 | 916ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 313 | 943ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 314 | 952ms | Md | 0.06 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 315 | 957ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 316 | 958ms | Mimo | 0.16 MB/s | `https://mimo.mi.com` | 通用代理 |
| 317 | 978ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 318 | 981ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 319 | 984ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 320 | 1022ms | Web | - | `https://web.4399.com` | 通用代理 |
| 321 | 1027ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 322 | 1032ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 323 | 1039ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 324 | 1051ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 325 | 1056ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 326 | 1057ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 327 | 1060ms | Dbgate | 0.13 MB/s | `https://dbgate.org` | 通用代理 |
| 328 | 1140ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 329 | 1145ms | V | - | `https://v.douyin.com` | 通用代理 |
| 330 | 1151ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 331 | 1157ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 332 | 1169ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 333 | 1170ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 334 | 1177ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 335 | 1190ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 336 | 1198ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 337 | 1211ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 338 | 1215ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 339 | 1228ms | Ghproxy | 0.24 MB/s | `https://ghproxy.cc` | 通用代理 |
| 340 | 1233ms | Hevolve | 0.07 MB/s | `https://hevolve.ai` | 通用代理 |
| 341 | 1235ms | Atomcode | 0.06 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 342 | 1252ms | GHProxy Net | 0.03 MB/s | `https://ghproxy.net` | 通用代理 |
| 343 | 1290ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 344 | 1298ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 345 | 1302ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 346 | 1332ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 347 | 1358ms | Git | 0.26 MB/s | `https://git.669966.xyz` | 通用代理 |
| 348 | 1359ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 349 | 1363ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 350 | 1378ms | Cf | 0.08 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 351 | 1387ms | Github | 0.13 MB/s | `https://github.chenc.dev` | 通用代理 |
| 352 | 1415ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 353 | 1423ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 354 | 1437ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 355 | 1610ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 356 | 1623ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 357 | 1629ms | I-qps | 0.02 MB/s | `https://i-qps.net` | 通用代理 |
| 358 | 1682ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 359 | 1682ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 360 | 1770ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 361 | 2152ms | Git | 0.01 MB/s | `https://git.net2o.de` | 通用代理 |
| 362 | 2153ms | Img | - | `https://img.ink` | 通用代理 |
| 363 | 2287ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 364 | 2458ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 365 | 2464ms | Provider | - | `https://provider.com` | 通用代理 |
| 366 | 2472ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 367 | 2838ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 368 | 2902ms | G | 0.03 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 369 | 3080ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 370 | 3106ms | Ghproxy | 0.06 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 371 | 3249ms | Gh | 0.1 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 372 | 4224ms | GHProxy MonkeyRay | 0.08 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（17 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 1 次 |
| YYLX Git (`git-yylx-win`) | 4 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 7 次 |
| GitClone (`gitclone-com`) | 2 次 |
| Wget (`wget-la`) | 1 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Mirror (`mirror-houlang-cloud`) | 3 次 |
| Proxy (`proxy-vvvv-ee`) | 2 次 |
| 5555 (`5555-cab`) | 19 次 |
| Doxygen (`doxygen-org`) | 15 次 |
| Aistack (`aistack-to`) | 1 次 |
| Axonhub (`axonhub-onrender-com`) | 1 次 |
| Easyboardgame (`easyboardgame-top`) | 1 次 |
| Flashtype (`flashtype-com`) | 2 次 |
| Maplecode (`maplecode-art`) | 8 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 4 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 382 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **389** | |

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
