# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-10-24T10:24:26Z**，每 6 小时刷新一次。当前 ✅ **357** 在线 / ⚠️ **12** 不稳定 / ⚰️ **48** 已失效归档。

## 核心特性

- **369 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 54ms | Microsoftedge | 0.6 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 2 | 55ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 3 | 62ms | Kighelper-cloud | 0.12 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 4 | 68ms | Linkedin | 0.14 MB/s | `https://linkedin.com` | 通用代理 |
| 5 | 69ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 6 | 70ms | Huly-mcp | 0.21 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 7 | 74ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 8 | 75ms | Deno | 0.87 MB/s | `https://deno.com` | 通用代理 |
| 9 | 80ms | Dilo-d14 | 0.22 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 10 | 83ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 11 | 84ms | Alas | 1.01 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 12 | 85ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 13 | 86ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 14 | 86ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 15 | 88ms | Xjtu-nyxf-study-material | 0.18 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 16 | 91ms | Tools | 2.08 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 17 | 95ms | Caw | 0.1 MB/s | `https://caw.rocks` | 通用代理 |
| 18 | 95ms | X | 1.37 MB/s | `https://x.com` | 通用代理 |
| 19 | 96ms | Glass | 0.23 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 20 | 96ms | Vibesql | 0.13 MB/s | `https://vibesql.org` | 通用代理 |
| 21 | 98ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 22 | 98ms | Opresume | 0.73 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 23 | 99ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 24 | 99ms | Freeport | 0.04 MB/s | `https://freeport.network` | 通用代理 |
| 25 | 99ms | Githubstatus | 0.8 MB/s | `https://githubstatus.com` | 通用代理 |
| 26 | 102ms | App | 0.09 MB/s | `https://app.netlify.com` | 通用代理 |
| 27 | 102ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 28 | 102ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 29 | 103ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 30 | 103ms | Serac | 0.1 MB/s | `https://serac.build` | 通用代理 |
| 31 | 105ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 32 | 108ms | Bananaslides | 0.64 MB/s | `https://bananaslides.online` | 通用代理 |
| 33 | 108ms | Impeccable | 1.12 MB/s | `https://impeccable.style` | 通用代理 |
| 34 | 108ms | L4d2 | 0.18 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 35 | 110ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 36 | 111ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 37 | 112ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 38 | 114ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 39 | 114ms | Clayrune | 0.18 MB/s | `https://clayrune.io` | 通用代理 |
| 40 | 114ms | Codeeraser | 0.13 MB/s | `https://codeeraser.dev` | 通用代理 |
| 41 | 114ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 42 | 114ms | Wordpaper | 0.44 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 43 | 115ms | Coffeecli | 0.13 MB/s | `https://coffeecli.com` | 通用代理 |
| 44 | 115ms | Impro | 2.41 MB/s | `https://impro.social` | 通用代理 |
| 45 | 116ms | Anh | 0.29 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 46 | 116ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 47 | 117ms | Polgarand | 0.1 MB/s | `https://polgarand.org` | 通用代理 |
| 48 | 118ms | Discord | 0.1 MB/s | `https://discord.gg` | 通用代理 |
| 49 | 118ms | Thumb | 1.1 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 50 | 119ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 51 | 119ms | Lawyer-yu | 0.08 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 52 | 120ms | Crypto-funding-arbitrage | 0.09 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 53 | 121ms | Game | - | `https://game.chozo.net` | 通用代理 |
| 54 | 121ms | Zebrunner | 1.65 MB/s | `https://zebrunner.com` | 通用代理 |
| 55 | 122ms | Opencovibe | 0.58 MB/s | `https://opencovibe.com` | 通用代理 |
| 56 | 124ms | Agentlimb | 0.26 MB/s | `https://agentlimb.com` | 通用代理 |
| 57 | 124ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 58 | 126ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 59 | 126ms | Resume-5lv | 0.26 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 60 | 126ms | Tokei | 0.64 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 61 | 126ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 62 | 130ms | Play | 0.07 MB/s | `https://play.templatical.com` | 通用代理 |
| 63 | 131ms | Gitea-mirror | 1.12 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 64 | 132ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 65 | 132ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 66 | 133ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 67 | 133ms | Img | - | `https://img.shields.io` | 通用代理 |
| 68 | 134ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 69 | 136ms | App | 0.06 MB/s | `https://app.opencastor.com` | 通用代理 |
| 70 | 138ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 71 | 138ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 72 | 142ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 73 | 144ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 74 | 145ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 75 | 148ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 76 | 149ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 77 | 149ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 78 | 150ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 79 | 152ms | Opensunsama | 0.04 MB/s | `https://opensunsama.com` | 通用代理 |
| 80 | 153ms | Music-cli | 0.19 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 81 | 154ms | Cognitum | 0.22 MB/s | `https://cognitum.one` | 通用代理 |
| 82 | 154ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 83 | 158ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 84 | 159ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 85 | 160ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 86 | 160ms | Microcoreos | 0.4 MB/s | `https://microcoreos.com` | 通用代理 |
| 87 | 160ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 88 | 164ms | App | 0.05 MB/s | `https://app.codecov.io` | 通用代理 |
| 89 | 164ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 90 | 166ms | Cody | 0.26 MB/s | `https://cody.todyle.com` | 通用代理 |
| 91 | 166ms | Openpua | 0.83 MB/s | `https://openpua.ai` | 通用代理 |
| 92 | 168ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 93 | 168ms | Nssurge | - | `https://nssurge.com` | 通用代理 |
| 94 | 170ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 95 | 170ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 96 | 170ms | GH-Proxy | 1.35 MB/s | `https://gh-proxy.com` | 通用代理 |
| 97 | 172ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 98 | 180ms | Ode | - | `https://ode.fun` | 通用代理 |
| 99 | 181ms | Gh | 2.82 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 100 | 182ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 101 | 182ms | Visionmemorymcp | 0.21 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 102 | 183ms | Git | 3.76 MB/s | `https://git.820828.xyz` | 通用代理 |
| 103 | 184ms | GH Monlor | 1.07 MB/s | `https://gh.monlor.com` | 通用代理 |
| 104 | 184ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 105 | 186ms | Github | 3.64 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 106 | 186ms | Holyclaude | 0.17 MB/s | `https://holyclaude.coderluii.dev` | 通用代理 |
| 107 | 187ms | Congressmcp | 0.04 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 108 | 188ms | Gh | 1.33 MB/s | `https://gh.llkk.cc` | 通用代理 |
| 109 | 188ms | Git | 2.72 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 110 | 190ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 111 | 190ms | Cbrowser | 2.44 MB/s | `https://cbrowser.ai` | 通用代理 |
| 112 | 190ms | Ginlix | 0.76 MB/s | `https://ginlix.ai` | 通用代理 |
| 113 | 193ms | Github | 2.75 MB/s | `https://github.788787.xyz` | 通用代理 |
| 114 | 194ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 115 | 195ms | Twitter | 0.8 MB/s | `https://twitter.com` | 通用代理 |
| 116 | 196ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 117 | 196ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 118 | 197ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 119 | 198ms | Ghproxy | 2.99 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 120 | 198ms | Gp | 3.04 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 121 | 200ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 122 | 200ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 123 | 201ms | Gh | 2.28 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 124 | 202ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 125 | 204ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 126 | 205ms | Claude | 0.43 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 127 | 205ms | Github | 3.23 MB/s | `https://github.880824.xyz` | 通用代理 |
| 128 | 206ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 129 | 206ms | Axios-http | 0.39 MB/s | `https://axios-http.com` | 通用代理 |
| 130 | 206ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 131 | 208ms | Ampcode | 0.18 MB/s | `https://ampcode.com` | 通用代理 |
| 132 | 208ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 133 | 209ms | Openttd | 0.06 MB/s | `https://openttd.org` | 通用代理 |
| 134 | 212ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 135 | 213ms | Sub | 0.14 MB/s | `https://sub.ikar.eu.org` | 通用代理 |
| 136 | 214ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 137 | 217ms | Cursor | 0.51 MB/s | `https://cursor.com` | 通用代理 |
| 138 | 217ms | Github | 2.79 MB/s | `https://github.ihnic.com` | 通用代理 |
| 139 | 218ms | GH-Proxy Org | 1.34 MB/s | `https://gh-proxy.org` | 通用代理 |
| 140 | 218ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 141 | 220ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 142 | 224ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 143 | 230ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 144 | 230ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 145 | 231ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 146 | 232ms | Clypra | 0.04 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 147 | 239ms | Ghproxy | 2.17 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 148 | 240ms | FastGit CC | 1.3 MB/s | `https://fastgit.cc` | 通用代理 |
| 149 | 241ms | Tvv | 2.41 MB/s | `https://tvv.tw` | 通用代理 |
| 150 | 242ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 151 | 242ms | Tms | 0.17 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 152 | 244ms | Aka | 0.44 MB/s | `https://aka.ms` | 通用代理 |
| 153 | 245ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 154 | 245ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 155 | 246ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 156 | 247ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 157 | 249ms | Training | 0.16 MB/s | `https://training.ti.com` | 通用代理 |
| 158 | 251ms | Contrib | 0.44 MB/s | `https://contrib.rocks` | 通用代理 |
| 159 | 252ms | Aomedia | 0.21 MB/s | `https://aomedia.issues.chromium.org` | 通用代理 |
| 160 | 254ms | Code | 1.89 MB/s | `https://code.claude.com` | 通用代理 |
| 161 | 254ms | Components | 0.08 MB/s | `https://components.dereekb.com` | 通用代理 |
| 162 | 254ms | Ghproxy | 0.76 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 163 | 254ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 164 | 255ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 165 | 257ms | Im | 1.58 MB/s | `https://im.codes` | 通用代理 |
| 166 | 259ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 167 | 260ms | Nisar | 0.79 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 168 | 262ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 169 | 262ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 170 | 264ms | Coreos | 1.06 MB/s | `https://coreos.com` | 通用代理 |
| 171 | 266ms | Gh | 2.53 MB/s | `https://gh.1k.ink` | 通用代理 |
| 172 | 266ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 173 | 268ms | Themolt | 0.04 MB/s | `https://themolt.net` | 通用代理 |
| 174 | 269ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 175 | 270ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 176 | 272ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 177 | 280ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 178 | 281ms | Gh | 0.47 MB/s | `https://gh.padao.fun` | 通用代理 |
| 179 | 292ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 180 | 292ms | Kenyu | 2.98 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 181 | 292ms | Weaverse | 0.58 MB/s | `https://weaverse.io` | 通用代理 |
| 182 | 296ms | Flashtype | 0.11 MB/s | `https://flashtype.com` | 通用代理 |
| 183 | 297ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 184 | 298ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 185 | 302ms | Kuroutoshikou | 0.78 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 186 | 303ms | Agoramarket | 0.81 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 187 | 303ms | Ggg | 2.73 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 188 | 304ms | Github | 0.72 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 189 | 307ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 190 | 308ms | Api | 0.12 MB/s | `https://api.solov.cc` | 通用代理 |
| 191 | 308ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 192 | 310ms | Support | 0.56 MB/s | `https://support.apple.com` | 通用代理 |
| 193 | 312ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 194 | 312ms | Gsd | 0.21 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 195 | 316ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 196 | 317ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 197 | 323ms | CrashMC CDN | 1.08 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 198 | 327ms | Aiblackboxfc | 0.19 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 199 | 328ms | B23 | - | `https://b23.tv` | 通用代理 |
| 200 | 330ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 201 | 333ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 202 | 336ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 203 | 337ms | Steamcommunity | 0.09 MB/s | `https://steamcommunity.com` | 通用代理 |
| 204 | 339ms | 30006000 | 0.71 MB/s | `https://30006000.xyz` | 通用代理 |
| 205 | 339ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 206 | 340ms | Tiktok | 0.08 MB/s | `https://tiktok.com` | 通用代理 |
| 207 | 347ms | Youtu | 1.17 MB/s | `https://youtu.be` | 通用代理 |
| 208 | 352ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 209 | 358ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 210 | 360ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 211 | 367ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 212 | 369ms | Gh | 0.75 MB/s | `https://gh.noki.icu` | 通用代理 |
| 213 | 370ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 214 | 371ms | Store | 0.89 MB/s | `https://store.steampowered.com` | 通用代理 |
| 215 | 376ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 216 | 378ms | Safedocx | 0.1 MB/s | `https://safedocx.com` | 通用代理 |
| 217 | 383ms | Aps | 0.05 MB/s | `https://aps.com` | 通用代理 |
| 218 | 385ms | Bailian | 0.1 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 219 | 386ms | Github | 2.46 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 220 | 387ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 221 | 388ms | GHFast | 0.6 MB/s | `https://ghfast.top` | 通用代理 |
| 222 | 392ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 223 | 393ms | GH Zwnes | - | `https://gh.zwnes.xyz` | 通用代理 |
| 224 | 393ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 225 | 395ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 226 | 397ms | Bseindia | 0.04 MB/s | `https://bseindia.com` | 通用代理 |
| 227 | 400ms | Github | 2.56 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 228 | 409ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 229 | 413ms | GH Nxnow | 0.78 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 230 | 416ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 231 | 418ms | Wl | - | `https://wl.do` | 通用代理 |
| 232 | 419ms | Hk | 0.94 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 233 | 422ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 234 | 436ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 235 | 436ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 236 | 436ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 237 | 441ms | Msdn | 0.05 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 238 | 442ms | Bible-ai-explorer | 0.05 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 239 | 451ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 240 | 452ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 241 | 464ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 242 | 465ms | Getgit | 2.58 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 243 | 470ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 244 | 471ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 245 | 474ms | Github | 2.92 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 246 | 488ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 247 | 490ms | Aosmd | 0.18 MB/s | `https://aosmd.com` | 通用代理 |
| 248 | 491ms | Gh | 1.07 MB/s | `https://gh.39.al` | 通用代理 |
| 249 | 492ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 250 | 495ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 251 | 506ms | Ark | 0.34 MB/s | `https://ark.intel.com` | 通用代理 |
| 252 | 510ms | Lecvdemarius | 0.05 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 253 | 511ms | YYLX Git | 0.3 MB/s | `https://git.yylx.win` | 通用代理 |
| 254 | 512ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 255 | 519ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 256 | 524ms | Umami-mcp | 0.4 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 257 | 526ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 258 | 527ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 259 | 530ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 260 | 541ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 261 | 542ms | Patchworkos | 0.28 MB/s | `https://patchworkos.com` | 通用代理 |
| 262 | 543ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 263 | 550ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 264 | 555ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 265 | 558ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 266 | 560ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 267 | 569ms | Os | 0.11 MB/s | `https://os.ryo.lu` | 通用代理 |
| 268 | 572ms | Nyx | 0.07 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 269 | 576ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 270 | 584ms | GHFile Geekertao | 0.26 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 271 | 590ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 272 | 598ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 273 | 599ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 274 | 600ms | Lucky | 0.41 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 275 | 604ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 276 | 607ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 277 | 618ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 278 | 623ms | Ednovas Mirror | 0.78 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 279 | 629ms | Github | 0.31 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 280 | 638ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 281 | 640ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 282 | 656ms | Memstack | 0.01 MB/s | `https://memstack.pro` | 通用代理 |
| 283 | 670ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 284 | 690ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 285 | 691ms | Ghproxy | 0.24 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 286 | 698ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 287 | 712ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 288 | 734ms | Gh | 0.51 MB/s | `https://gh.dpik.top` | 通用代理 |
| 289 | 742ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 290 | 748ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 291 | 752ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 292 | 754ms | Docs | 0.18 MB/s | `https://docs.transifex.com` | 通用代理 |
| 293 | 760ms | Maplecode | - | `https://maplecode.art` | 通用代理 |
| 294 | 768ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 295 | 778ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 296 | 786ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 297 | 793ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 298 | 796ms | Clawbiz | 0.02 MB/s | `https://clawbiz.io` | 通用代理 |
| 299 | 813ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 300 | 814ms | GHProxy Net | 0.05 MB/s | `https://ghproxy.net` | 通用代理 |
| 301 | 814ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 302 | 827ms | Fastfile | 2.01 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 303 | 830ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 304 | 852ms | Yibiao | 0.11 MB/s | `https://yibiao.pro` | 通用代理 |
| 305 | 873ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 306 | 892ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 307 | 896ms | Aif | 0.03 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 308 | 902ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 309 | 916ms | Md | 0.07 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 310 | 923ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 311 | 924ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 312 | 924ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 313 | 935ms | Sct | 0.01 MB/s | `https://sct.ftqq.com` | 通用代理 |
| 314 | 936ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 315 | 938ms | Mimo | 0.17 MB/s | `https://mimo.mi.com` | 通用代理 |
| 316 | 956ms | Web | - | `https://web.4399.com` | 通用代理 |
| 317 | 988ms | Tsukuyomi | 0.01 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 318 | 1033ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 319 | 1050ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 320 | 1061ms | Atomcode | 0.07 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 321 | 1082ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 322 | 1114ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 323 | 1124ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 324 | 1129ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 325 | 1137ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 326 | 1138ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 327 | 1153ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 328 | 1158ms | Agentkey | 0.14 MB/s | `https://agentkey.app` | 通用代理 |
| 329 | 1175ms | Hevolve | 0.08 MB/s | `https://hevolve.ai` | 通用代理 |
| 330 | 1186ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 331 | 1214ms | Ghproxy | 0.26 MB/s | `https://ghproxy.cc` | 通用代理 |
| 332 | 1218ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 333 | 1235ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 334 | 1287ms | Docs | - | `https://docs.waveshare.net` | 通用代理 |
| 335 | 1288ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 336 | 1295ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 337 | 1333ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 338 | 1420ms | V | 0.05 MB/s | `https://v.douyin.com` | 通用代理 |
| 339 | 1427ms | Cf | 0.25 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 340 | 1542ms | Github | 0.13 MB/s | `https://github.chenc.dev` | 通用代理 |
| 341 | 1590ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 342 | 1600ms | Git | 0.45 MB/s | `https://git.669966.xyz` | 通用代理 |
| 343 | 1667ms | Docs | - | `https://docs.volcengine.com` | 通用代理 |
| 344 | 1667ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 345 | 1711ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 346 | 2069ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 347 | 2114ms | Img | - | `https://img.ink` | 通用代理 |
| 348 | 2228ms | Ghproxy | 0.15 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 349 | 2228ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 350 | 2362ms | G | 0.19 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 351 | 2381ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 352 | 2749ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 353 | 2776ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 354 | 2955ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 355 | 3156ms | Wget | - | `https://wget.la` | 通用代理 |
| 356 | 3299ms | Gh | 0.1 MB/s | `https://gh.b52m.cn` | 通用代理 |
| 357 | 3983ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |


### ⚠️ 不稳定节点（12 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| Npee Down (`down-npee-cn`) | 18 次 |
| GH-Proxy YGXZ (`gh-proxy-ygxz-in`) | 25 次 |
| Gh (`gh-idayer-com`) | 1 次 |
| Gh (`gh-halonice-com`) | 17 次 |
| Git (`git-tangbai-cc`) | 18 次 |
| Proxy (`proxy-yaoyaoling-net`) | 2 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |
| 5555 (`5555-cab`) | 8 次 |
| Code (`code-leez-tech`) | 1 次 |
| Status (`status-leez-tech`) | 1 次 |
| Doxygen (`doxygen-org`) | 4 次 |
| Mobilevc (`mobilevc-top`) | 1 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 362 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **369** | |

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
