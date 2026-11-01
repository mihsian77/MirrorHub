# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-11-01T04:37:01Z**，每 6 小时刷新一次。当前 ✅ **397** 在线 / ⚠️ **17** 不稳定 / ⚰️ **53** 已失效归档。

## 核心特性

- **414 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 72ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 2 | 74ms | Microsoftedge | 0.64 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 83ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 4 | 89ms | Linkedin | 0.24 MB/s | `https://linkedin.com` | 通用代理 |
| 5 | 92ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 6 | 95ms | Game | 0.15 MB/s | `https://game.chozo.net` | 通用代理 |
| 7 | 97ms | Githubstatus | 1.47 MB/s | `https://githubstatus.com` | 通用代理 |
| 8 | 99ms | Wordpaper | 0.51 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 9 | 100ms | Resume-5lv | 0.21 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 10 | 100ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 11 | 100ms | Xjtu-nyxf-study-material | 0.18 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 12 | 101ms | Crypto-funding-arbitrage | 0.1 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 13 | 102ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 14 | 103ms | Huly-mcp | 0.21 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 15 | 104ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 16 | 105ms | X | 1.47 MB/s | `https://x.com` | 通用代理 |
| 17 | 108ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 18 | 110ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 19 | 110ms | Tools | 1.68 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 20 | 111ms | Kighelper-cloud | 0.1 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 21 | 112ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 22 | 115ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 23 | 116ms | Deno | 0.69 MB/s | `https://deno.com` | 通用代理 |
| 24 | 116ms | Zebrunner | 1.16 MB/s | `https://zebrunner.com` | 通用代理 |
| 25 | 117ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 26 | 117ms | Img | - | `https://img.shields.io` | 通用代理 |
| 27 | 118ms | App | 0.11 MB/s | `https://app.netlify.com` | 通用代理 |
| 28 | 119ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 29 | 119ms | Opresume | 0.77 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 30 | 120ms | Impeccable | 1.18 MB/s | `https://impeccable.style` | 通用代理 |
| 31 | 121ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 32 | 122ms | Dilo-d14 | 0.18 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 33 | 126ms | Lawyer-yu | 0.08 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 34 | 126ms | Serac | 0.08 MB/s | `https://serac.build` | 通用代理 |
| 35 | 126ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 36 | 127ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 37 | 128ms | Megacrit | 0.11 MB/s | `https://megacrit.com` | 通用代理 |
| 38 | 129ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 39 | 130ms | Caiji | - | `https://caiji.cyou` | 通用代理 |
| 40 | 132ms | Cumora | 0.3 MB/s | `https://cumora.ai` | 通用代理 |
| 41 | 132ms | Git | 2.89 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 42 | 133ms | Impro | 1.73 MB/s | `https://impro.social` | 通用代理 |
| 43 | 134ms | Git | 2.87 MB/s | `https://git.820828.xyz` | 通用代理 |
| 44 | 136ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 45 | 136ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 46 | 137ms | Bestdori | 0.08 MB/s | `https://bestdori.com` | 通用代理 |
| 47 | 137ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 48 | 138ms | Codeeraser | 0.13 MB/s | `https://codeeraser.dev` | 通用代理 |
| 49 | 139ms | Gp | 3.29 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 50 | 139ms | Misaligned | - | `https://misaligned.top` | 通用代理 |
| 51 | 141ms | Github | 2.74 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 52 | 142ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 53 | 143ms | Gh | 2.56 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 54 | 144ms | Gitea-mirror | 0.76 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 55 | 144ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 56 | 145ms | Anh | 0.3 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 57 | 145ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 58 | 146ms | Openpua | 0.63 MB/s | `https://openpua.ai` | 通用代理 |
| 59 | 146ms | Opentakeoff | 0.05 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 60 | 147ms | Agentlimb | 0.23 MB/s | `https://agentlimb.com` | 通用代理 |
| 61 | 147ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 62 | 147ms | Components | 0.12 MB/s | `https://components.dereekb.com` | 通用代理 |
| 63 | 147ms | Vibesql | 0.12 MB/s | `https://vibesql.org` | 通用代理 |
| 64 | 149ms | Agoramarket | 0.04 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 65 | 149ms | Gh | 2.67 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 66 | 150ms | Github | 2.93 MB/s | `https://github.788787.xyz` | 通用代理 |
| 67 | 151ms | Ghproxy | 3.54 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 68 | 151ms | Github | 2.62 MB/s | `https://github.880824.xyz` | 通用代理 |
| 69 | 151ms | Gpui | 0.2 MB/s | `https://gpui.rs` | 通用代理 |
| 70 | 151ms | Polgarand | 0.09 MB/s | `https://polgarand.org` | 通用代理 |
| 71 | 151ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 72 | 152ms | Caw | 0.07 MB/s | `https://caw.rocks` | 通用代理 |
| 73 | 152ms | Cody | 0.29 MB/s | `https://cody.todyle.com` | 通用代理 |
| 74 | 152ms | L4d2 | 0.17 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 75 | 153ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 76 | 153ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 77 | 153ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 78 | 153ms | Play | 0.06 MB/s | `https://play.templatical.com` | 通用代理 |
| 79 | 153ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 80 | 154ms | Alas | 0.9 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 81 | 154ms | Discord | 0.07 MB/s | `https://discord.gg` | 通用代理 |
| 82 | 155ms | Clayrune | 0.14 MB/s | `https://clayrune.io` | 通用代理 |
| 83 | 155ms | Training | 0.16 MB/s | `https://training.ti.com` | 通用代理 |
| 84 | 156ms | Demo | 0.04 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 85 | 156ms | Tokei | 0.69 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 86 | 158ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 87 | 158ms | Music-cli | 0.2 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 88 | 158ms | Opensunsama | 0.04 MB/s | `https://opensunsama.com` | 通用代理 |
| 89 | 159ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 90 | 159ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 91 | 159ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 92 | 161ms | Cherryai | 0.07 MB/s | `https://cherryai.com` | 通用代理 |
| 93 | 163ms | GH-Proxy | 1.17 MB/s | `https://gh-proxy.com` | 通用代理 |
| 94 | 164ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 95 | 165ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 96 | 166ms | Glass | 0.25 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 97 | 167ms | Tomcat1235 | 0.72 MB/s | `https://tomcat1235.nyc.mn` | 通用代理 |
| 98 | 168ms | Bolt2github | 0.04 MB/s | `https://bolt2github.com` | 通用代理 |
| 99 | 171ms | Api | 0.12 MB/s | `https://api.solov.cc` | 通用代理 |
| 100 | 171ms | Miaozitie | 0.08 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 101 | 172ms | Osf | 0.04 MB/s | `https://osf.io` | 通用代理 |
| 102 | 173ms | Coffeecli | 0.14 MB/s | `https://coffeecli.com` | 通用代理 |
| 103 | 173ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 104 | 175ms | Ghproxy | 3.0 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 105 | 178ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 106 | 179ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 107 | 180ms | Opencovibe | 0.28 MB/s | `https://opencovibe.com` | 通用代理 |
| 108 | 180ms | Tvv | 3.83 MB/s | `https://tvv.tw` | 通用代理 |
| 109 | 184ms | Cognitum | 0.26 MB/s | `https://cognitum.one` | 通用代理 |
| 110 | 185ms | Pidash | 0.03 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 111 | 186ms | Gh | 3.48 MB/s | `https://gh.1k.ink` | 通用代理 |
| 112 | 187ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 113 | 187ms | Github | 2.79 MB/s | `https://github.ihnic.com` | 通用代理 |
| 114 | 187ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 115 | 188ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 116 | 188ms | Openchamber | 0.68 MB/s | `https://openchamber.dev` | 通用代理 |
| 117 | 189ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 118 | 189ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 119 | 195ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 120 | 195ms | Tms | 0.15 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 121 | 196ms | GH-Proxy Org | 1.22 MB/s | `https://gh-proxy.org` | 通用代理 |
| 122 | 198ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 123 | 198ms | Thumb | 1.08 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 124 | 199ms | Twitter | 0.9 MB/s | `https://twitter.com` | 通用代理 |
| 125 | 204ms | Bananaslides | 0.62 MB/s | `https://bananaslides.online` | 通用代理 |
| 126 | 205ms | Aiblackboxfc | 0.23 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 127 | 209ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 128 | 211ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 129 | 212ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 130 | 212ms | Microcoreos | 0.49 MB/s | `https://microcoreos.com` | 通用代理 |
| 131 | 213ms | Clypra | 0.05 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 132 | 214ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 133 | 214ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 134 | 215ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 135 | 215ms | Shiori-v1 | 0.02 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 136 | 216ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 137 | 216ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 138 | 216ms | Ghproxy | 0.81 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 139 | 218ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 140 | 218ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 141 | 221ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 142 | 221ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 143 | 222ms | Ggg | 2.88 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 144 | 222ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 145 | 222ms | Tools | 0.09 MB/s | `https://tools.ietf.org` | 通用代理 |
| 146 | 223ms | Github | 0.84 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 147 | 223ms | Sina | 0.45 MB/s | `https://sina.dev` | 通用代理 |
| 148 | 224ms | Ode | - | `https://ode.fun` | 通用代理 |
| 149 | 226ms | Ampcode | 0.23 MB/s | `https://ampcode.com` | 通用代理 |
| 150 | 226ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 151 | 227ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 152 | 229ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 153 | 229ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 154 | 229ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 155 | 230ms | Ai-trend-publish | 0.01 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 156 | 230ms | Axios-http | 0.33 MB/s | `https://axios-http.com` | 通用代理 |
| 157 | 230ms | Cbrowser | 1.47 MB/s | `https://cbrowser.ai` | 通用代理 |
| 158 | 231ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 159 | 235ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 160 | 236ms | Contrib | 0.4 MB/s | `https://contrib.rocks` | 通用代理 |
| 161 | 236ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 162 | 236ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 163 | 238ms | CrashMC CDN | 1.1 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 164 | 238ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 165 | 241ms | Ginlix | 0.44 MB/s | `https://ginlix.ai` | 通用代理 |
| 166 | 241ms | Kenyu | 2.83 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 167 | 241ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 168 | 243ms | GH Monlor | 1.05 MB/s | `https://gh.monlor.com` | 通用代理 |
| 169 | 247ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 170 | 248ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 171 | 250ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 172 | 254ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 173 | 258ms | Travis-ci | 0.18 MB/s | `https://travis-ci.org` | 通用代理 |
| 174 | 261ms | Visionmemorymcp | 0.27 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 175 | 262ms | Gsd | 0.26 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 176 | 263ms | Gh | 0.68 MB/s | `https://gh.padao.fun` | 通用代理 |
| 177 | 264ms | Wandoukj | - | `https://wandoukj.eu.org` | 通用代理 |
| 178 | 265ms | Savannah | 0.05 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 179 | 268ms | Kuroutoshikou | 0.67 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 180 | 270ms | Claude | 0.42 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 181 | 270ms | Getgit | 2.96 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 182 | 273ms | Wings | 0.02 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 183 | 276ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 184 | 277ms | Hk | 1.09 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 185 | 278ms | Code | 0.95 MB/s | `https://code.claude.com` | 通用代理 |
| 186 | 279ms | Cursor | 0.48 MB/s | `https://cursor.com` | 通用代理 |
| 187 | 279ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 188 | 280ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 189 | 281ms | Nisar | 0.8 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 190 | 282ms | FastGit CC | 0.62 MB/s | `https://fastgit.cc` | 通用代理 |
| 191 | 283ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 192 | 284ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 193 | 285ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 194 | 288ms | GHFast | 0.59 MB/s | `https://ghfast.top` | 通用代理 |
| 195 | 293ms | Coreos | 1.25 MB/s | `https://coreos.com` | 通用代理 |
| 196 | 295ms | Aka | 0.53 MB/s | `https://aka.ms` | 通用代理 |
| 197 | 295ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 198 | 295ms | Youtu | 1.2 MB/s | `https://youtu.be` | 通用代理 |
| 199 | 298ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 200 | 301ms | Docs | 0.06 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 201 | 303ms | Github | 2.27 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 202 | 305ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 203 | 307ms | Github | 3.48 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 204 | 308ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 205 | 308ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 206 | 308ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 207 | 318ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 208 | 318ms | Oem | 0.03 MB/s | `https://oem.re` | 通用代理 |
| 209 | 318ms | Steamcommunity | 0.11 MB/s | `https://steamcommunity.com` | 通用代理 |
| 210 | 319ms | B23 | - | `https://b23.tv` | 通用代理 |
| 211 | 325ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 212 | 327ms | Cfkua | 1.55 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 213 | 331ms | 30006000 | 0.73 MB/s | `https://30006000.xyz` | 通用代理 |
| 214 | 332ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 215 | 337ms | Tiktok | 0.08 MB/s | `https://tiktok.com` | 通用代理 |
| 216 | 337ms | V4 | 1.77 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 217 | 340ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 218 | 340ms | Docs | 0.67 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 219 | 340ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 220 | 344ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 221 | 345ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 222 | 348ms | Store | 1.14 MB/s | `https://store.steampowered.com` | 通用代理 |
| 223 | 349ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 224 | 351ms | Sonarcloud | 1.12 MB/s | `https://sonarcloud.io` | 通用代理 |
| 225 | 352ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 226 | 359ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 227 | 370ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 228 | 383ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 229 | 391ms | Autonomi | 0.01 MB/s | `https://autonomi.dev` | 通用代理 |
| 230 | 392ms | Bailian | 0.06 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 231 | 393ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 232 | 393ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 233 | 393ms | Nyx | 0.07 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 234 | 394ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 235 | 395ms | Im | 1.58 MB/s | `https://im.codes` | 通用代理 |
| 236 | 399ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 237 | 402ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 238 | 403ms | Weaverse | 0.76 MB/s | `https://weaverse.io` | 通用代理 |
| 239 | 413ms | Serverkit | 0.04 MB/s | `https://serverkit.ai` | 通用代理 |
| 240 | 417ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 241 | 417ms | Your-domain | 0.05 MB/s | `https://your-domain.com` | 通用代理 |
| 242 | 423ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 243 | 425ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 244 | 426ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 245 | 429ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 246 | 433ms | Aps | 0.06 MB/s | `https://aps.com` | 通用代理 |
| 247 | 437ms | Codeflying | 0.02 MB/s | `https://codeflying.app` | 通用代理 |
| 248 | 437ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 249 | 438ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 250 | 440ms | GH Nxnow | 0.52 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 251 | 440ms | You | 1.03 MB/s | `https://you.piccalc.com` | 通用代理 |
| 252 | 444ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 253 | 448ms | Readsync | 0.02 MB/s | `https://readsync.org` | 通用代理 |
| 254 | 451ms | Agentkey | 0.72 MB/s | `https://agentkey.app` | 通用代理 |
| 255 | 454ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 256 | 454ms | YYLX Git | 1.09 MB/s | `https://git.yylx.win` | 通用代理 |
| 257 | 462ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 258 | 463ms | SLink | 0.04 MB/s | `https://slink.ltd` | 通用代理 |
| 259 | 463ms | Wl | - | `https://wl.do` | 通用代理 |
| 260 | 466ms | Lucky | 0.21 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 261 | 470ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 262 | 470ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 263 | 471ms | Bible-ai-explorer | 0.05 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 264 | 482ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 265 | 483ms | Gh | 0.59 MB/s | `https://gh.noki.icu` | 通用代理 |
| 266 | 488ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 267 | 495ms | Ark | 0.53 MB/s | `https://ark.intel.com` | 通用代理 |
| 268 | 495ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 269 | 497ms | Github | 2.92 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 270 | 506ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 271 | 515ms | Lecvdemarius | 0.06 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 272 | 516ms | Gh | 3.39 MB/s | `https://gh.idayer.com` | 通用代理 |
| 273 | 518ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 274 | 519ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 275 | 524ms | Safedocx | 0.13 MB/s | `https://safedocx.com` | 通用代理 |
| 276 | 531ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 277 | 535ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 278 | 536ms | Support | 0.48 MB/s | `https://support.apple.com` | 通用代理 |
| 279 | 538ms | Api | - | `https://api.river.ai` | 通用代理 |
| 280 | 538ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 281 | 545ms | Patchworkos | 0.32 MB/s | `https://patchworkos.com` | 通用代理 |
| 282 | 574ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 283 | 576ms | Tsukuyomi | 0.15 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 284 | 577ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 285 | 596ms | Github | 0.27 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 286 | 598ms | Fastfile | 2.06 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 287 | 598ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 288 | 604ms | 3d-set-visualizer | 0.03 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 289 | 605ms | Umami-mcp | 1.38 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 290 | 609ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 291 | 611ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 292 | 614ms | Aosmd | 0.16 MB/s | `https://aosmd.com` | 通用代理 |
| 293 | 622ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 294 | 642ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 295 | 646ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 296 | 646ms | Ghproxy | 0.26 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 297 | 655ms | Proxy | - | `https://proxy.scdn.io` | 通用代理 |
| 298 | 669ms | Bseindia | 0.02 MB/s | `https://bseindia.com` | 通用代理 |
| 299 | 672ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 300 | 673ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 301 | 687ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 302 | 688ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 303 | 699ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 304 | 706ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 305 | 708ms | Os | 0.05 MB/s | `https://os.ryo.lu` | 通用代理 |
| 306 | 713ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 307 | 719ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 308 | 721ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 309 | 727ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 310 | 760ms | Ccgather | 0.06 MB/s | `https://ccgather.com` | 通用代理 |
| 311 | 767ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 312 | 785ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 313 | 795ms | Gh | 0.83 MB/s | `https://gh.39.al` | 通用代理 |
| 314 | 800ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 315 | 803ms | Gh | 0.86 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 316 | 816ms | Md | 0.07 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 317 | 826ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 318 | 835ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 319 | 846ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 320 | 847ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 321 | 849ms | Aif | 0.05 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 322 | 859ms | Docs | 0.19 MB/s | `https://docs.transifex.com` | 通用代理 |
| 323 | 869ms | Internhack | 0.02 MB/s | `https://internhack.xyz` | 通用代理 |
| 324 | 872ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 325 | 890ms | Dbgate | 0.15 MB/s | `https://dbgate.org` | 通用代理 |
| 326 | 898ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 327 | 898ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 328 | 905ms | Yibiao | 0.12 MB/s | `https://yibiao.pro` | 通用代理 |
| 329 | 912ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 330 | 914ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 331 | 935ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 332 | 936ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 333 | 937ms | GHFile Geekertao | 2.66 MB/s | `https://ghfile.geekertao.top` | 通用代理 |
| 334 | 943ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 335 | 947ms | Ednovas Mirror | 0.74 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 336 | 962ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 337 | 963ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 338 | 966ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 339 | 974ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 340 | 978ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 341 | 995ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 342 | 1004ms | Mcp-x | - | `https://mcp-x.com` | 通用代理 |
| 343 | 1024ms | Dimagent | 0.57 MB/s | `https://dimagent.com` | 通用代理 |
| 344 | 1027ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 345 | 1029ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 346 | 1067ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 347 | 1079ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 348 | 1087ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 349 | 1094ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 350 | 1105ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 351 | 1107ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 352 | 1112ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 353 | 1133ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 354 | 1133ms | Web | - | `https://web.4399.com` | 通用代理 |
| 355 | 1143ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 356 | 1146ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 357 | 1154ms | V | - | `https://v.douyin.com` | 通用代理 |
| 358 | 1169ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 359 | 1173ms | Ghproxy | 0.31 MB/s | `https://ghproxy.cc` | 通用代理 |
| 360 | 1181ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 361 | 1187ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 362 | 1196ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 363 | 1198ms | Hevolve | 0.07 MB/s | `https://hevolve.ai` | 通用代理 |
| 364 | 1224ms | Atomcode | 0.05 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 365 | 1229ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 366 | 1257ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 367 | 1259ms | Github | 0.15 MB/s | `https://github.chenc.dev` | 通用代理 |
| 368 | 1287ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 369 | 1289ms | Web | 0.12 MB/s | `https://web.archive.org` | 通用代理 |
| 370 | 1309ms | Cf | 0.28 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 371 | 1415ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 372 | 1451ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 373 | 1468ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 374 | 1484ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 375 | 1606ms | GHProxy Net | 0.08 MB/s | `https://ghproxy.net` | 通用代理 |
| 376 | 1607ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 377 | 1611ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 378 | 1614ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 379 | 1632ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 380 | 1665ms | Heycall-e | 0.11 MB/s | `https://heycall-e.com` | 通用代理 |
| 381 | 1763ms | Git | 0.12 MB/s | `https://git.669966.xyz` | 通用代理 |
| 382 | 2050ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 383 | 2068ms | G | 0.03 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 384 | 2131ms | Img | - | `https://img.ink` | 通用代理 |
| 385 | 2170ms | Gh | 0.95 MB/s | `https://gh.dpik.top` | 通用代理 |
| 386 | 2174ms | Wget | 0.15 MB/s | `https://wget.la` | 通用代理 |
| 387 | 2338ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 388 | 2354ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 389 | 2479ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 390 | 2480ms | Provider | 0.01 MB/s | `https://provider.com` | 通用代理 |
| 391 | 2537ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 392 | 2735ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 393 | 2756ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 394 | 2865ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 395 | 2888ms | Ghproxy | 0.54 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 396 | 3461ms | GHProxy MonkeyRay | 0.06 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 397 | 6309ms | Proxy | 0.02 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（17 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GH Zwnes (`gh-zwnes-xyz`) | 23 次 |
| GitClone (`gitclone-com`) | 2 次 |
| Gh (`gh-llkk-cc`) | 7 次 |
| Git (`git-tangbai-cc`) | 6 次 |
| Gh (`gh-b52m-cn`) | 10 次 |
| Proxy (`proxy-vvvv-ee`) | 1 次 |
| Sub (`sub-ikar-eu-org`) | 5 次 |
| Nssurge (`nssurge-com`) | 9 次 |
| Fastgpt (`fastgpt-leez-tech`) | 1 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 9 次 |
| Flashtype (`flashtype-com`) | 1 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 14 次 |
| Maplecode (`maplecode-art`) | 24 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 20 次 |
| Adult (`adult-contents-fc2-com`) | 6 次 |
| Git (`git-net2o-de`) | 2 次 |
| Free (`free-cn-eu-org`) | 2 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 407 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **414** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（53 个）。

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
