# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-24T03:28:21Z**，每 6 小时刷新一次。当前 ✅ **360** 在线 / ⚠️ **8** 不稳定 / ⚰️ **48** 已失效归档。

## 核心特性

- **368 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 41ms | Shiori-v1 | 0.06 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 2 | 44ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 3 | 49ms | Ai-trend-publish | 0.09 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 4 | 50ms | Microsoftedge | 0.36 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 5 | 52ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 6 | 53ms | Nextup-resource | 0.09 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 7 | 55ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 8 | 55ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 9 | 56ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 10 | 57ms | Huly-mcp | 0.22 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 11 | 62ms | Kighelper-cloud | 0.16 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 12 | 63ms | Alas | 1.38 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 13 | 63ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 14 | 65ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 15 | 65ms | Linkedin | 0.17 MB/s | `https://linkedin.com` | 通用代理 |
| 16 | 66ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 17 | 67ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 18 | 68ms | Dilo-d14 | 0.24 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 19 | 76ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 20 | 77ms | Deno | 0.22 MB/s | `https://deno.com` | 通用代理 |
| 21 | 77ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 22 | 81ms | Freeport | 0.06 MB/s | `https://freeport.network` | 通用代理 |
| 23 | 82ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 24 | 82ms | Opensunsama | 0.1 MB/s | `https://opensunsama.com` | 通用代理 |
| 25 | 82ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 26 | 83ms | Ode | - | `https://ode.fun` | 通用代理 |
| 27 | 84ms | Xjtu-nyxf-study-material | 0.21 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 28 | 85ms | Impeccable | 1.92 MB/s | `https://impeccable.style` | 通用代理 |
| 29 | 86ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 30 | 88ms | Githubstatus | 3.19 MB/s | `https://githubstatus.com` | 通用代理 |
| 31 | 88ms | L4d2 | 0.22 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 32 | 88ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 33 | 91ms | Caw | 0.08 MB/s | `https://caw.rocks` | 通用代理 |
| 34 | 91ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 35 | 91ms | Discord | 0.08 MB/s | `https://discord.gg` | 通用代理 |
| 36 | 92ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 37 | 92ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 38 | 92ms | Serac | 0.13 MB/s | `https://serac.build` | 通用代理 |
| 39 | 93ms | Tools | 3.7 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 40 | 94ms | Anh | 0.31 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 41 | 94ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 42 | 94ms | X | 1.93 MB/s | `https://x.com` | 通用代理 |
| 43 | 95ms | App | 0.11 MB/s | `https://app.netlify.com` | 通用代理 |
| 44 | 95ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 45 | 96ms | Glass | 0.2 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 46 | 97ms | Bananaslides | 1.04 MB/s | `https://bananaslides.online` | 通用代理 |
| 47 | 98ms | Godocs | 0.06 MB/s | `https://godocs.io` | 通用代理 |
| 48 | 100ms | Pidash | 0.07 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 49 | 100ms | Vibesql | 0.13 MB/s | `https://vibesql.org` | 通用代理 |
| 50 | 101ms | Opresume | 0.39 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 51 | 101ms | Play | 0.04 MB/s | `https://play.templatical.com` | 通用代理 |
| 52 | 101ms | Tokei | 0.61 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 53 | 102ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 54 | 102ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 55 | 104ms | Thumb | 5.22 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 56 | 104ms | Visionmemorymcp | 0.39 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 57 | 105ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 58 | 105ms | Impro | 2.54 MB/s | `https://impro.social` | 通用代理 |
| 59 | 105ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 60 | 106ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 61 | 108ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 62 | 108ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 63 | 109ms | Polgarand | 0.13 MB/s | `https://polgarand.org` | 通用代理 |
| 64 | 110ms | Clayrune | 0.2 MB/s | `https://clayrune.io` | 通用代理 |
| 65 | 112ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 66 | 115ms | Wordpaper | 0.56 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 67 | 116ms | Coffeecli | 0.08 MB/s | `https://coffeecli.com` | 通用代理 |
| 68 | 117ms | Zebrunner | 2.84 MB/s | `https://zebrunner.com` | 通用代理 |
| 69 | 121ms | Demo | 0.06 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 70 | 121ms | Lawyer-yu | 0.09 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 71 | 121ms | Wings | 0.05 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 72 | 122ms | Crypto-funding-arbitrage | 0.13 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 73 | 122ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 74 | 124ms | Clypra | 0.27 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 75 | 126ms | Resume-5lv | 0.21 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 76 | 128ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 77 | 130ms | Codeeraser | 0.14 MB/s | `https://codeeraser.dev` | 通用代理 |
| 78 | 130ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 79 | 131ms | Miaozitie | 0.05 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 80 | 133ms | Bolt2github | 0.04 MB/s | `https://bolt2github.com` | 通用代理 |
| 81 | 133ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 82 | 134ms | Opencovibe | 0.5 MB/s | `https://opencovibe.com` | 通用代理 |
| 83 | 134ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 84 | 135ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 85 | 135ms | Img | - | `https://img.shields.io` | 通用代理 |
| 86 | 135ms | Openpua | 0.75 MB/s | `https://openpua.ai` | 通用代理 |
| 87 | 136ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 88 | 138ms | Gitea-mirror | 0.98 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 89 | 142ms | Autonomi | 0.04 MB/s | `https://autonomi.dev` | 通用代理 |
| 90 | 142ms | Goreportcard | 0.04 MB/s | `https://goreportcard.com` | 通用代理 |
| 91 | 142ms | Music-cli | 0.28 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 92 | 143ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 93 | 144ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 94 | 144ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 95 | 150ms | Opentakeoff | 0.05 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 96 | 151ms | Microcoreos | 0.54 MB/s | `https://microcoreos.com` | 通用代理 |
| 97 | 152ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 98 | 152ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 99 | 152ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 100 | 153ms | Agentlimb | 0.26 MB/s | `https://agentlimb.com` | 通用代理 |
| 101 | 153ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 102 | 154ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 103 | 154ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 104 | 156ms | Ginlix | 0.49 MB/s | `https://ginlix.ai` | 通用代理 |
| 105 | 160ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 106 | 165ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 107 | 166ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 108 | 167ms | Aka | 1.04 MB/s | `https://aka.ms` | 通用代理 |
| 109 | 167ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 110 | 168ms | GH-Proxy | 1.39 MB/s | `https://gh-proxy.com` | 通用代理 |
| 111 | 169ms | Ai-watch | 0.05 MB/s | `https://ai-watch.dev` | 通用代理 |
| 112 | 169ms | Cody | 0.3 MB/s | `https://cody.todyle.com` | 通用代理 |
| 113 | 177ms | Gh | 3.05 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 114 | 178ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 115 | 181ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 116 | 182ms | Agent-room | 0.06 MB/s | `https://agent-room.com` | 通用代理 |
| 117 | 184ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 118 | 187ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 119 | 187ms | Git | 3.11 MB/s | `https://git.820828.xyz` | 通用代理 |
| 120 | 187ms | Github | 3.05 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 121 | 190ms | Github | 3.24 MB/s | `https://github.788787.xyz` | 通用代理 |
| 122 | 190ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 123 | 190ms | Twitter | 1.2 MB/s | `https://twitter.com` | 通用代理 |
| 124 | 191ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 125 | 191ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 126 | 193ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 127 | 194ms | Congressmcp | 0.05 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 128 | 195ms | Sub | 0.27 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 129 | 196ms | GH Monlor | 0.66 MB/s | `https://gh.monlor.com` | 通用代理 |
| 130 | 197ms | Git | 3.5 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 131 | 198ms | Holyclaude | 0.25 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 132 | 198ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 133 | 199ms | Ghproxy | 2.5 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 134 | 200ms | Gh | 3.65 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 135 | 200ms | Github | 4.3 MB/s | `https://github.880824.xyz` | 通用代理 |
| 136 | 201ms | Axios-http | 0.83 MB/s | `https://axios-http.com` | 通用代理 |
| 137 | 201ms | Gp | 4.77 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 138 | 201ms | Hopp | 0.03 MB/s | `https://hopp.sh` | 通用代理 |
| 139 | 201ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 140 | 202ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 141 | 202ms | Cursor | 0.7 MB/s | `https://cursor.com` | 通用代理 |
| 142 | 203ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 143 | 205ms | Ampcode | 0.22 MB/s | `https://ampcode.com` | 通用代理 |
| 144 | 209ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 145 | 211ms | GH-Proxy Org | 1.39 MB/s | `https://gh-proxy.org` | 通用代理 |
| 146 | 211ms | Radio-browser | 0.03 MB/s | `https://radio-browser.info` | 通用代理 |
| 147 | 212ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 148 | 213ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 149 | 214ms | Openttd | 0.08 MB/s | `https://openttd.org` | 通用代理 |
| 150 | 217ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 151 | 219ms | Internhack | 0.07 MB/s | `https://internhack.xyz` | 通用代理 |
| 152 | 220ms | Paypal | 0.05 MB/s | `https://paypal.com` | 通用代理 |
| 153 | 221ms | Github | 3.57 MB/s | `https://github.ihnic.com` | 通用代理 |
| 154 | 222ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 155 | 224ms | Claude | 0.41 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 156 | 225ms | Gh | 3.86 MB/s | `https://gh.1k.ink` | 通用代理 |
| 157 | 226ms | Cognitum | 0.11 MB/s | `https://cognitum.one` | 通用代理 |
| 158 | 226ms | Tms | 0.12 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 159 | 229ms | Safedocx | 0.21 MB/s | `https://safedocx.com` | 通用代理 |
| 160 | 230ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 161 | 231ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 162 | 235ms | Gh | 4.31 MB/s | `https://gh.idayer.com` | 通用代理 |
| 163 | 236ms | Training | 0.17 MB/s | `https://training.ti.com` | 通用代理 |
| 164 | 240ms | Ghproxy | 2.62 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 165 | 246ms | Components | 0.1 MB/s | `https://components.dereekb.com` | 通用代理 |
| 166 | 246ms | Coreos | 1.43 MB/s | `https://coreos.com` | 通用代理 |
| 167 | 246ms | Tvv | 4.12 MB/s | `https://tvv.tw` | 通用代理 |
| 168 | 247ms | Weaverse | 0.66 MB/s | `https://weaverse.io` | 通用代理 |
| 169 | 249ms | Ghproxy | 1.5 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 170 | 250ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 171 | 252ms | FastGit CC | 1.76 MB/s | `https://fastgit.cc` | 通用代理 |
| 172 | 256ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 173 | 257ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 174 | 259ms | Nisar | 1.59 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 175 | 262ms | Contrib | 0.24 MB/s | `https://contrib.rocks` | 通用代理 |
| 176 | 262ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 177 | 270ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 178 | 273ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 179 | 274ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 180 | 274ms | Gh | 1.14 MB/s | `https://gh.padao.fun` | 通用代理 |
| 181 | 278ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 182 | 279ms | Aomedia | 0.12 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 183 | 280ms | Code | 2.45 MB/s | `https://code.claude.com` | 通用代理 |
| 184 | 280ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 185 | 294ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 186 | 295ms | Kuroutoshikou | 1.87 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 187 | 299ms | Cbrowser | 0.69 MB/s | `https://cbrowser.ai` | 通用代理 |
| 188 | 299ms | Flashtype | 0.15 MB/s | `https://flashtype.com` | 通用代理 |
| 189 | 300ms | Kenyu | 3.3 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 190 | 303ms | Agoramarket | 1.27 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 191 | 304ms | Support | 0.15 MB/s | `https://support.apple.com` | 通用代理 |
| 192 | 304ms | Turborepo-starter-kit-web | 0.11 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 193 | 306ms | Github | 2.45 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 194 | 308ms | Bible-ai-explorer | 0.11 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 195 | 309ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 196 | 311ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 197 | 315ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 198 | 316ms | Os | 0.09 MB/s | `https://os.ryo.lu` | 通用代理 |
| 199 | 318ms | Readsync | 0.04 MB/s | `https://readsync.org` | 通用代理 |
| 200 | 319ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 201 | 319ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 202 | 321ms | CrashMC CDN | 0.77 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 203 | 322ms | Ggg | 5.15 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 204 | 325ms | Api | 0.31 MB/s | `https://api.solov.cc` | 通用代理 |
| 205 | 327ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 206 | 334ms | B23 | - | `https://b23.tv` | 通用代理 |
| 207 | 336ms | Agenticcorporation | 0.04 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 208 | 336ms | Steamcommunity | 0.19 MB/s | `https://steamcommunity.com` | 通用代理 |
| 209 | 339ms | Themolt | 0.02 MB/s | `https://themolt.net` | 通用代理 |
| 210 | 343ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 211 | 344ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 212 | 345ms | Oem | 0.04 MB/s | `https://oem.re` | 通用代理 |
| 213 | 352ms | Serverkit | 0.05 MB/s | `https://serverkit.ai` | 通用代理 |
| 214 | 355ms | 30006000 | 1.28 MB/s | `https://30006000.xyz` | 通用代理 |
| 215 | 358ms | 3d-set-visualizer | 0.04 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 216 | 360ms | Tiktok | 0.09 MB/s | `https://tiktok.com` | 通用代理 |
| 217 | 360ms | Wl | - | `https://wl.do` | 通用代理 |
| 218 | 361ms | Gh | 0.58 MB/s | `https://gh.noki.icu` | 通用代理 |
| 219 | 362ms | Store | 1.78 MB/s | `https://store.steampowered.com` | 通用代理 |
| 220 | 366ms | Aiblackboxfc | 0.24 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 221 | 374ms | Github | 5.6 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 222 | 377ms | Bailian | 0.23 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 223 | 379ms | Aps | 0.06 MB/s | `https://aps.com` | 通用代理 |
| 224 | 382ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 225 | 387ms | Tracely-studio | 0.05 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 226 | 392ms | Bseindia | 0.05 MB/s | `https://bseindia.com` | 通用代理 |
| 227 | 395ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 228 | 395ms | Gh | 0.86 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 229 | 397ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 230 | 401ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 231 | 404ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 232 | 404ms | Github | 3.02 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 233 | 404ms | Im | 0.31 MB/s | `https://im.codes` | 通用代理 |
| 234 | 410ms | Data | 0.02 MB/s | `https://data.openecon.ai` | 通用代理 |
| 235 | 410ms | Msdn | 0.07 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 236 | 412ms | GH Nxnow | 0.29 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 237 | 414ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 238 | 415ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 239 | 426ms | GHFast | 1.33 MB/s | `https://ghfast.top` | 通用代理 |
| 240 | 426ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 241 | 428ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 242 | 432ms | Hk | 0.79 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 243 | 446ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 244 | 458ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 245 | 459ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 246 | 462ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 247 | 470ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 248 | 474ms | Gh | 1.22 MB/s | `https://gh.39.al` | 通用代理 |
| 249 | 476ms | Ark | 0.69 MB/s | `https://ark.intel.com` | 通用代理 |
| 250 | 476ms | Github | 2.81 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 251 | 479ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 252 | 480ms | Getgit | 3.05 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 253 | 481ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 254 | 482ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 255 | 487ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 256 | 488ms | Gsd | 0.07 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 257 | 494ms | Aosmd | 0.13 MB/s | `https://aosmd.com` | 通用代理 |
| 258 | 502ms | Lecvdemarius | 0.07 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 259 | 502ms | YYLX Git | 1.84 MB/s | `https://git.yylx.win` | 通用代理 |
| 260 | 504ms | Codeflying | 0.01 MB/s | `https://codeflying.app` | 通用代理 |
| 261 | 506ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 262 | 525ms | Your-domain | 0.08 MB/s | `https://your-domain.com` | 通用代理 |
| 263 | 526ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 264 | 527ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 265 | 528ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 266 | 533ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 267 | 535ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 268 | 541ms | Ccgather | 0.09 MB/s | `https://ccgather.com` | 通用代理 |
| 269 | 550ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 270 | 556ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 271 | 557ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 272 | 557ms | Memstack | 0.01 MB/s | `https://memstack.pro` | 通用代理 |
| 273 | 561ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 274 | 567ms | Ygdj7 | 0.08 MB/s | `https://ygdj7.com` | 通用代理 |
| 275 | 582ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 276 | 589ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 277 | 592ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 278 | 604ms | Patchworkos | 0.23 MB/s | `https://patchworkos.com` | 通用代理 |
| 279 | 607ms | Lucky | 0.36 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 280 | 620ms | Clawbiz | 0.04 MB/s | `https://clawbiz.io` | 通用代理 |
| 281 | 622ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 282 | 626ms | Ednovas Mirror | 0.96 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 283 | 632ms | Github | 0.34 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 284 | 643ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 285 | 662ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 286 | 673ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 287 | 675ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 288 | 676ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 289 | 681ms | Maplecode | - | `https://maplecode.art` | 通用代理 |
| 290 | 694ms | Umami-mcp | 0.62 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 291 | 697ms | Yibiao | 0.18 MB/s | `https://yibiao.pro` | 通用代理 |
| 292 | 699ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 293 | 711ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 294 | 716ms | Gh | 0.63 MB/s | `https://gh.dpik.top` | 通用代理 |
| 295 | 717ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 296 | 721ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 297 | 723ms | Docs | 0.14 MB/s | `https://docs.transifex.com` | 通用代理 |
| 298 | 723ms | Ghproxy | 0.38 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 299 | 728ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 300 | 734ms | GHFile Geekertao | 0.69 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 301 | 735ms | Md | 0.09 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 302 | 743ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 303 | 747ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 304 | 757ms | Honeymeta | 0.02 MB/s | `https://honeymeta.com` | 通用代理 |
| 305 | 757ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 306 | 779ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 307 | 796ms | Invent | 0.01 MB/s | `https://invent.kde.org` | 通用代理 |
| 308 | 807ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 309 | 820ms | GHProxy Net | 0.05 MB/s | `https://ghproxy.net` | 通用代理 |
| 310 | 837ms | Fastfile | 2.23 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 311 | 841ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 312 | 866ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 313 | 879ms | Atomcode | 0.08 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 314 | 895ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 315 | 896ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 316 | 907ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 317 | 927ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 318 | 943ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 319 | 963ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 320 | 965ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 321 | 1003ms | Aif | 0.03 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 322 | 1017ms | Web | - | `https://web.4399.com` | 通用代理 |
| 323 | 1049ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 324 | 1057ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 325 | 1112ms | Agentkey | 0.17 MB/s | `https://agentkey.app` | 通用代理 |
| 326 | 1116ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 327 | 1121ms | Onetwin | 0.01 MB/s | `https://onetwin.cn` | 通用代理 |
| 328 | 1124ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 329 | 1128ms | Aliexpress | 0.02 MB/s | `https://aliexpress.com` | 通用代理 |
| 330 | 1135ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 331 | 1135ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 332 | 1154ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 333 | 1173ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 334 | 1202ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 335 | 1207ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 336 | 1219ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 337 | 1224ms | Ghproxy | 0.34 MB/s | `https://ghproxy.cc` | 通用代理 |
| 338 | 1282ms | Atomgit | 0.01 MB/s | `https://atomgit.com` | 通用代理 |
| 339 | 1297ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 340 | 1426ms | Cf | 0.35 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 341 | 1473ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 342 | 1657ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 343 | 1673ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 344 | 1702ms | Github | 0.12 MB/s | `https://github.chenc.dev` | 通用代理 |
| 345 | 1716ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 346 | 1789ms | V | - | `https://v.douyin.com` | 通用代理 |
| 347 | 1878ms | Kw-aigc | - | `https://kw-aigc.cn` | 通用代理 |
| 348 | 2082ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 349 | 2119ms | Ghproxy | 0.18 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 350 | 2124ms | Img | - | `https://img.ink` | 通用代理 |
| 351 | 2283ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 352 | 2379ms | Mobilevc | - | `https://mobilevc.top` | 通用代理 |
| 353 | 2425ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 354 | 2491ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 355 | 2700ms | G | 0.01 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 356 | 2731ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 357 | 2944ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 358 | 3365ms | Gh | 0.13 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 359 | 3426ms | Wget | - | `https://wget.la` | 通用代理 |
| 360 | 3792ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（8 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Npee Down (`down-npee-cn`) | 17 次 |
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 24 次 |
| Gh (`gh-halonice-com`) | 16 次 |
| Git (`git-669966-xyz`) | 1 次 |
| Git (`git-tangbai-cc`) | 17 次 |
| Proxy (`proxy-yaoyaoling-net`) | 1 次 |
| 5555 (`5555-cab`) | 7 次 |
| Doxygen (`doxygen-org`) | 3 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 361 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **368** | |

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
