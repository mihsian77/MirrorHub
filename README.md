# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-11-01T21:48:05Z**，每 6 小时刷新一次。当前 ✅ **398** 在线 / ⚠️ **18** 不稳定 / ⚰️ **53** 已失效归档。

## 核心特性

- **416 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 68ms | Leereilly | - | `https://leereilly.net` | 通用代理 |
| 2 | 86ms | Microsoftedge | 0.37 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 3 | 87ms | Opencode | - | `https://opencode.ai` | 通用代理 |
| 4 | 90ms | Githubstatus | 3.21 MB/s | `https://githubstatus.com` | 通用代理 |
| 5 | 90ms | Xjtu-nyxf-study-material | 0.24 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 6 | 91ms | Wordpaper | 0.74 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 7 | 93ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 8 | 94ms | Resume-5lv | 0.05 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 9 | 95ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 10 | 95ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 11 | 97ms | Huly-mcp | 0.18 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 12 | 98ms | Crypto-funding-arbitrage | 0.11 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 13 | 98ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 14 | 98ms | Kighelper-cloud | 0.12 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 15 | 100ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 16 | 101ms | Game | 0.18 MB/s | `https://game.chozo.net` | 通用代理 |
| 17 | 102ms | Opresume | 0.78 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 18 | 102ms | Tools | 2.64 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 19 | 105ms | Demo | - | `https://demo.confabulous.dev` | 通用代理 |
| 20 | 105ms | Linkedin | 0.13 MB/s | `https://linkedin.com` | 通用代理 |
| 21 | 105ms | X | 1.62 MB/s | `https://x.com` | 通用代理 |
| 22 | 110ms | Megacrit | 0.43 MB/s | `https://megacrit.com` | 通用代理 |
| 23 | 111ms | Zebrunner | 2.44 MB/s | `https://zebrunner.com` | 通用代理 |
| 24 | 111ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 25 | 113ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 26 | 114ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 27 | 115ms | Bestdori | 0.16 MB/s | `https://bestdori.com` | 通用代理 |
| 28 | 117ms | Dilo-d14 | 0.24 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 29 | 118ms | Serac | 0.1 MB/s | `https://serac.build` | 通用代理 |
| 30 | 119ms | Caiji | - | `https://caiji.cyou` | 通用代理 |
| 31 | 119ms | Git | 3.91 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 32 | 119ms | Impeccable | 0.32 MB/s | `https://impeccable.style` | 通用代理 |
| 33 | 119ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 34 | 122ms | Img | - | `https://img.shields.io` | 通用代理 |
| 35 | 122ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 36 | 123ms | Git | 4.9 MB/s | `https://git.820828.xyz` | 通用代理 |
| 37 | 124ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 38 | 124ms | Gh | 3.77 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 39 | 124ms | Godocs | 0.04 MB/s | `https://godocs.io` | 通用代理 |
| 40 | 125ms | Impro | 2.8 MB/s | `https://impro.social` | 通用代理 |
| 41 | 127ms | Api | 0.18 MB/s | `https://api.solov.cc` | 通用代理 |
| 42 | 127ms | App | 0.16 MB/s | `https://app.netlify.com` | 通用代理 |
| 43 | 127ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 44 | 128ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 45 | 128ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 46 | 129ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 47 | 129ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 48 | 129ms | Github | 2.37 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 49 | 131ms | Agentlimb | 0.27 MB/s | `https://agentlimb.com` | 通用代理 |
| 50 | 131ms | Alas | 1.24 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 51 | 131ms | Codeeraser | 0.14 MB/s | `https://codeeraser.dev` | 通用代理 |
| 52 | 132ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 53 | 132ms | Cumora | 0.42 MB/s | `https://cumora.ai` | 通用代理 |
| 54 | 132ms | Gp | 4.62 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 55 | 133ms | Axonhub | - | `https://axonhub.onrender.com` | 通用代理 |
| 56 | 133ms | Github | 4.65 MB/s | `https://github.880824.xyz` | 通用代理 |
| 57 | 135ms | Miaozitie | 0.04 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 58 | 135ms | Openpua | 0.9 MB/s | `https://openpua.ai` | 通用代理 |
| 59 | 136ms | Anh | 0.18 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 60 | 136ms | Lawyer-yu | 0.11 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 61 | 137ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 62 | 138ms | Gitea-mirror | 1.24 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 63 | 138ms | Github | 1.93 MB/s | `https://github.788787.xyz` | 通用代理 |
| 64 | 138ms | Vibesql | 0.16 MB/s | `https://vibesql.org` | 通用代理 |
| 65 | 141ms | Gh | 3.93 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 66 | 141ms | Polgarand | 0.04 MB/s | `https://polgarand.org` | 通用代理 |
| 67 | 142ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 68 | 142ms | App | 0.04 MB/s | `https://app.opencastor.com` | 通用代理 |
| 69 | 142ms | Fxin | - | `https://fxin.cc` | 通用代理 |
| 70 | 143ms | Clayrune | 0.18 MB/s | `https://clayrune.io` | 通用代理 |
| 71 | 144ms | Cody | 0.3 MB/s | `https://cody.todyle.com` | 通用代理 |
| 72 | 144ms | Demo | 0.06 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 73 | 144ms | Deno | 0.23 MB/s | `https://deno.com` | 通用代理 |
| 74 | 144ms | Freeport | 0.05 MB/s | `https://freeport.network` | 通用代理 |
| 75 | 144ms | Gpui | 0.19 MB/s | `https://gpui.rs` | 通用代理 |
| 76 | 144ms | L4d2 | 0.15 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 77 | 145ms | Agoramarket | 0.09 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 78 | 145ms | Components | 0.15 MB/s | `https://components.dereekb.com` | 通用代理 |
| 79 | 145ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 80 | 146ms | App | 0.04 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 81 | 146ms | Opensunsama | 0.1 MB/s | `https://opensunsama.com` | 通用代理 |
| 82 | 146ms | Training | 0.2 MB/s | `https://training.ti.com` | 通用代理 |
| 83 | 147ms | Discord | 0.09 MB/s | `https://discord.gg` | 通用代理 |
| 84 | 148ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 85 | 148ms | Coffeecli | 0.2 MB/s | `https://coffeecli.com` | 通用代理 |
| 86 | 148ms | Ghproxy | 4.43 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 87 | 149ms | Chops | 0.04 MB/s | `https://chops.md` | 通用代理 |
| 88 | 149ms | Glass | 0.35 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 89 | 150ms | Cherryai | 0.06 MB/s | `https://cherryai.com` | 通用代理 |
| 90 | 150ms | Play | 0.05 MB/s | `https://play.templatical.com` | 通用代理 |
| 91 | 151ms | Opencovibe | 0.57 MB/s | `https://opencovibe.com` | 通用代理 |
| 92 | 151ms | Tokei | 0.66 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 93 | 152ms | Vibetrading | - | `https://vibetrading.wiki` | 通用代理 |
| 94 | 153ms | Caw | 0.1 MB/s | `https://caw.rocks` | 通用代理 |
| 95 | 154ms | Goreportcard | 0.04 MB/s | `https://goreportcard.com` | 通用代理 |
| 96 | 155ms | Openchamber | 0.32 MB/s | `https://openchamber.dev` | 通用代理 |
| 97 | 155ms | Pidash | 0.06 MB/s | `https://pidash.airepublic.com` | 通用代理 |
| 98 | 156ms | Bananaslides | 1.01 MB/s | `https://bananaslides.online` | 通用代理 |
| 99 | 157ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 100 | 158ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 101 | 160ms | Music-cli | 0.3 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 102 | 166ms | Ghproxy | 4.62 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 103 | 166ms | Hopp | 0.08 MB/s | `https://hopp.sh` | 通用代理 |
| 104 | 168ms | GH-Proxy | 0.95 MB/s | `https://gh-proxy.com` | 通用代理 |
| 105 | 168ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 106 | 168ms | Misaligned | 0.73 MB/s | `https://misaligned.top` | 通用代理 |
| 107 | 170ms | Thumb | 4.89 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 108 | 172ms | Gh | 5.7 MB/s | `https://gh.1k.ink` | 通用代理 |
| 109 | 173ms | Bolt2github | 0.05 MB/s | `https://bolt2github.com` | 通用代理 |
| 110 | 173ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 111 | 174ms | Tvv | 4.5 MB/s | `https://tvv.tw` | 通用代理 |
| 112 | 175ms | Ghproxy | 2.42 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 113 | 175ms | Github | 4.3 MB/s | `https://github.ihnic.com` | 通用代理 |
| 114 | 176ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 115 | 179ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 116 | 183ms | Openttd | 0.08 MB/s | `https://openttd.org` | 通用代理 |
| 117 | 184ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 118 | 186ms | Cognitum | 0.14 MB/s | `https://cognitum.one` | 通用代理 |
| 119 | 186ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 120 | 191ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 121 | 191ms | Tomcat1235 | 0.52 MB/s | `https://tomcat1235.nyc.mn` | 通用代理 |
| 122 | 193ms | Twitter | 1.02 MB/s | `https://twitter.com` | 通用代理 |
| 123 | 194ms | Osf | 0.01 MB/s | `https://osf.io` | 通用代理 |
| 124 | 195ms | Nextup-resource | 0.05 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 125 | 196ms | GH-Proxy Org | 0.92 MB/s | `https://gh-proxy.org` | 通用代理 |
| 126 | 196ms | Nisar | 1.13 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 127 | 200ms | Clypra | 0.14 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 128 | 201ms | Aiblackboxfc | 0.19 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 129 | 201ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 130 | 201ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 131 | 202ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 132 | 202ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 133 | 203ms | Shiori-v1 | 0.04 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 134 | 205ms | Contrib | 0.51 MB/s | `https://contrib.rocks` | 通用代理 |
| 135 | 205ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 136 | 206ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 137 | 208ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 138 | 208ms | Gh | 1.64 MB/s | `https://gh.padao.fun` | 通用代理 |
| 139 | 209ms | Ai-watch | 0.03 MB/s | `https://ai-watch.dev` | 通用代理 |
| 140 | 211ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 141 | 211ms | Tms | 0.1 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 142 | 211ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 143 | 212ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 144 | 213ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 145 | 213ms | Paypal | 0.04 MB/s | `https://paypal.com` | 通用代理 |
| 146 | 214ms | Kenyu | 4.91 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 147 | 215ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 148 | 217ms | Ai-trend-publish | 0.1 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 149 | 217ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 150 | 219ms | Congressmcp | 0.03 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 151 | 220ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 152 | 220ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 153 | 220ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 154 | 222ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 155 | 225ms | CrashMC CDN | 0.81 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 156 | 225ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 157 | 225ms | Ode | - | `https://ode.fun` | 通用代理 |
| 158 | 227ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 159 | 229ms | Sina | 1.03 MB/s | `https://sina.dev` | 通用代理 |
| 160 | 230ms | Github | 1.34 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 161 | 231ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 162 | 232ms | GH Monlor | 0.77 MB/s | `https://gh.monlor.com` | 通用代理 |
| 163 | 233ms | Ggg | 3.09 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 164 | 236ms | Ampcode | 0.21 MB/s | `https://ampcode.com` | 通用代理 |
| 165 | 239ms | Microcoreos | 0.43 MB/s | `https://microcoreos.com` | 通用代理 |
| 166 | 241ms | Cbrowser | 0.58 MB/s | `https://cbrowser.ai` | 通用代理 |
| 167 | 243ms | Axios-http | 0.75 MB/s | `https://axios-http.com` | 通用代理 |
| 168 | 243ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 169 | 247ms | Ginlix | 0.44 MB/s | `https://ginlix.ai` | 通用代理 |
| 170 | 248ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 171 | 250ms | Visionmemorymcp | 0.78 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 172 | 250ms | Wandoukj | - | `https://wandoukj.eu.org` | 通用代理 |
| 173 | 254ms | Getgit | 4.19 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 174 | 255ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 175 | 256ms | Radio-browser | 0.03 MB/s | `https://radio-browser.info` | 通用代理 |
| 176 | 256ms | Tools | 0.06 MB/s | `https://tools.ietf.org` | 通用代理 |
| 177 | 256ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 178 | 260ms | Kuroutoshikou | 1.19 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 179 | 263ms | Wings | 0.12 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 180 | 265ms | FastGit CC | 0.86 MB/s | `https://fastgit.cc` | 通用代理 |
| 181 | 265ms | Open | 0.03 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 182 | 266ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 183 | 266ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 184 | 270ms | Code | 0.68 MB/s | `https://code.claude.com` | 通用代理 |
| 185 | 275ms | Aka | 0.6 MB/s | `https://aka.ms` | 通用代理 |
| 186 | 276ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 187 | 277ms | Github | 3.64 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 188 | 279ms | Docs | 0.05 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 189 | 280ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 190 | 280ms | Travis-ci | 0.12 MB/s | `https://travis-ci.org` | 通用代理 |
| 191 | 282ms | Hk | 1.13 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 192 | 282ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 193 | 284ms | GHFast | 1.59 MB/s | `https://ghfast.top` | 通用代理 |
| 194 | 286ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 195 | 287ms | 30006000 | 1.77 MB/s | `https://30006000.xyz` | 通用代理 |
| 196 | 291ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 197 | 293ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 198 | 295ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 199 | 296ms | Cursor | 0.59 MB/s | `https://cursor.com` | 通用代理 |
| 200 | 300ms | Savannah | 0.02 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 201 | 300ms | Steamcommunity | 0.19 MB/s | `https://steamcommunity.com` | 通用代理 |
| 202 | 300ms | Youtu | 1.59 MB/s | `https://youtu.be` | 通用代理 |
| 203 | 302ms | Coreos | 1.55 MB/s | `https://coreos.com` | 通用代理 |
| 204 | 304ms | B23 | - | `https://b23.tv` | 通用代理 |
| 205 | 304ms | Claude | 0.41 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 206 | 306ms | Tiktok | 0.09 MB/s | `https://tiktok.com` | 通用代理 |
| 207 | 312ms | Github | 1.09 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 208 | 313ms | Zuckerbot | 0.03 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 209 | 314ms | Phabricator | 0.04 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 210 | 316ms | Gsd | 0.08 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 211 | 321ms | V4 | 3.73 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 212 | 322ms | Cfkua | 2.24 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 213 | 323ms | Erp | - | `https://erp.kacon.ai` | 通用代理 |
| 214 | 325ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 215 | 328ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 216 | 330ms | Oem | 0.04 MB/s | `https://oem.re` | 通用代理 |
| 217 | 335ms | Store | 2.3 MB/s | `https://store.steampowered.com` | 通用代理 |
| 218 | 339ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 219 | 340ms | Aps | 0.22 MB/s | `https://aps.com` | 通用代理 |
| 220 | 340ms | Gh | 0.62 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 221 | 342ms | Agenticcorporation | 0.03 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 222 | 343ms | Bailian | 0.11 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 223 | 346ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 224 | 350ms | Docs | 0.61 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 225 | 350ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 226 | 353ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 227 | 359ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 228 | 366ms | Autonomi | 0.04 MB/s | `https://autonomi.dev` | 通用代理 |
| 229 | 366ms | Turborepo-starter-kit-web | 0.17 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 230 | 368ms | Data | 0.02 MB/s | `https://data.openecon.ai` | 通用代理 |
| 231 | 368ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 232 | 368ms | Your-domain | 0.09 MB/s | `https://your-domain.com` | 通用代理 |
| 233 | 370ms | You | 1.15 MB/s | `https://you.piccalc.com` | 通用代理 |
| 234 | 372ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 235 | 372ms | Serverkit | 0.05 MB/s | `https://serverkit.ai` | 通用代理 |
| 236 | 372ms | YYLX Git | 0.98 MB/s | `https://git.yylx.win` | 通用代理 |
| 237 | 377ms | Weishucdn | - | `https://weishucdn.jiangjiangze.icu` | 通用代理 |
| 238 | 379ms | Agentkey | 0.58 MB/s | `https://agentkey.app` | 通用代理 |
| 239 | 379ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 240 | 387ms | Agent-room | 0.07 MB/s | `https://agent-room.com` | 通用代理 |
| 241 | 390ms | Github | 2.12 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 242 | 392ms | Api | 0.03 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 243 | 400ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 244 | 402ms | Im | 0.2 MB/s | `https://im.codes` | 通用代理 |
| 245 | 404ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 246 | 410ms | Sonarcloud | 0.09 MB/s | `https://sonarcloud.io` | 通用代理 |
| 247 | 414ms | Open | 0.02 MB/s | `https://open.feishu.cn` | 通用代理 |
| 248 | 415ms | GH Nxnow | 0.7 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 249 | 432ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 250 | 435ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 251 | 437ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 252 | 439ms | Weaverse | 0.82 MB/s | `https://weaverse.io` | 通用代理 |
| 253 | 440ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 254 | 441ms | Proxy | - | `https://proxy.vvvv.ee` | 通用代理 |
| 255 | 442ms | SLink | 0.06 MB/s | `https://slink.ltd` | 通用代理 |
| 256 | 443ms | Bible-ai-explorer | 0.14 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 257 | 445ms | Hubp | 0.02 MB/s | `https://hubp.org` | 通用代理 |
| 258 | 446ms | Gh | 0.59 MB/s | `https://gh.noki.icu` | 通用代理 |
| 259 | 446ms | Wl | - | `https://wl.do` | 通用代理 |
| 260 | 447ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 261 | 454ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 262 | 457ms | Codeflying | 0.01 MB/s | `https://codeflying.app` | 通用代理 |
| 263 | 460ms | Ark | 0.75 MB/s | `https://ark.intel.com` | 通用代理 |
| 264 | 462ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 265 | 466ms | Ygdj7 | 0.06 MB/s | `https://ygdj7.com` | 通用代理 |
| 266 | 467ms | Readsync | 0.03 MB/s | `https://readsync.org` | 通用代理 |
| 267 | 471ms | Msdn | 0.07 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 268 | 477ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 269 | 477ms | Lucky | 0.46 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 270 | 480ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 271 | 480ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 272 | 497ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 273 | 500ms | Easyboardgame | - | `https://easyboardgame.top` | 通用代理 |
| 274 | 502ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 275 | 512ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 276 | 513ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 277 | 518ms | Support | 0.17 MB/s | `https://support.apple.com` | 通用代理 |
| 278 | 523ms | Bseindia | 0.05 MB/s | `https://bseindia.com` | 通用代理 |
| 279 | 537ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 280 | 540ms | Safedocx | 0.17 MB/s | `https://safedocx.com` | 通用代理 |
| 281 | 541ms | Lecvdemarius | 0.07 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 282 | 549ms | Api | - | `https://api.river.ai` | 通用代理 |
| 283 | 549ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 284 | 552ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 285 | 552ms | Tsukuyomi | 0.09 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 286 | 564ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 287 | 565ms | Github | 0.31 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 288 | 568ms | Patchworkos | 0.24 MB/s | `https://patchworkos.com` | 通用代理 |
| 289 | 585ms | Luna | 0.03 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 290 | 592ms | Fastfile | 1.44 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 291 | 598ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 292 | 600ms | 3d-set-visualizer | 0.07 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 293 | 607ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 294 | 607ms | Tracely-studio | 0.04 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 295 | 612ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 296 | 615ms | Umami-mcp | 0.34 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 297 | 617ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 298 | 624ms | Vaultproject | 0.69 MB/s | `https://vaultproject.io` | 通用代理 |
| 299 | 627ms | Ghproxy | 0.37 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 300 | 652ms | Aosmd | 0.12 MB/s | `https://aosmd.com` | 通用代理 |
| 301 | 673ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 302 | 674ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 303 | 708ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 304 | 709ms | Clawbiz | 0.04 MB/s | `https://clawbiz.io` | 通用代理 |
| 305 | 710ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 306 | 712ms | Memstack | 0.01 MB/s | `https://memstack.pro` | 通用代理 |
| 307 | 719ms | Gh | 0.97 MB/s | `https://gh.39.al` | 通用代理 |
| 308 | 719ms | Onetwin | 0.03 MB/s | `https://onetwin.cn` | 通用代理 |
| 309 | 723ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 310 | 728ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 311 | 728ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 312 | 735ms | Os | 0.02 MB/s | `https://os.ryo.lu` | 通用代理 |
| 313 | 748ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 314 | 772ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 315 | 774ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 316 | 774ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 317 | 814ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 318 | 814ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 319 | 815ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 320 | 817ms | T | 0.02 MB/s | `https://t.me` | 通用代理 |
| 321 | 836ms | Framagit | - | `https://framagit.org` | 通用代理 |
| 322 | 846ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 323 | 846ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 324 | 852ms | Md | 0.08 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 325 | 866ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 326 | 883ms | Ccgather | 0.1 MB/s | `https://ccgather.com` | 通用代理 |
| 327 | 888ms | Aif | 0.04 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 328 | 892ms | Yibiao | 0.14 MB/s | `https://yibiao.pro` | 通用代理 |
| 329 | 900ms | Mimo | 0.2 MB/s | `https://mimo.mi.com` | 通用代理 |
| 330 | 902ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 331 | 915ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 332 | 922ms | Internhack | 0.11 MB/s | `https://internhack.xyz` | 通用代理 |
| 333 | 927ms | Ednovas Mirror | 0.64 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 334 | 931ms | Docs | 0.13 MB/s | `https://docs.transifex.com` | 通用代理 |
| 335 | 933ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 336 | 934ms | Honeymeta | 0.01 MB/s | `https://honeymeta.com` | 通用代理 |
| 337 | 937ms | Dbgate | 0.14 MB/s | `https://dbgate.org` | 通用代理 |
| 338 | 944ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 339 | 953ms | Invent | 0.01 MB/s | `https://invent.kde.org` | 通用代理 |
| 340 | 956ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 341 | 956ms | Dimagent | 0.16 MB/s | `https://dimagent.com` | 通用代理 |
| 342 | 956ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 343 | 959ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 344 | 964ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 345 | 965ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 346 | 1016ms | Mcp-x | 0.01 MB/s | `https://mcp-x.com` | 通用代理 |
| 347 | 1081ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 348 | 1085ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 349 | 1086ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 350 | 1088ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 351 | 1108ms | Mobilevc | 0.01 MB/s | `https://mobilevc.top` | 通用代理 |
| 352 | 1118ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 353 | 1130ms | Console | - | `https://console.cloud.tencent.com` | 通用代理 |
| 354 | 1132ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 355 | 1137ms | Ghproxy | 0.41 MB/s | `https://ghproxy.cc` | 通用代理 |
| 356 | 1138ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 357 | 1149ms | Gitcode | 0.01 MB/s | `https://gitcode.com` | 通用代理 |
| 358 | 1152ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 359 | 1165ms | Atomcode | 0.07 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 360 | 1203ms | Hevolve | 0.09 MB/s | `https://hevolve.ai` | 通用代理 |
| 361 | 1203ms | V | - | `https://v.douyin.com` | 通用代理 |
| 362 | 1206ms | Web | - | `https://web.4399.com` | 通用代理 |
| 363 | 1207ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 364 | 1216ms | Pew | 0.02 MB/s | `https://pew.md` | 通用代理 |
| 365 | 1226ms | Matroska | - | `https://matroska.org` | 通用代理 |
| 366 | 1252ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 367 | 1268ms | Code | 0.01 MB/s | `https://code.videolan.org` | 通用代理 |
| 368 | 1283ms | Cf | 0.37 MB/s | `https://cf.ghproxy.cc` | 通用代理 |
| 369 | 1306ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 370 | 1320ms | Github | 0.2 MB/s | `https://github.chenc.dev` | 通用代理 |
| 371 | 1367ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 372 | 1415ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 373 | 1449ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 374 | 1516ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 375 | 1563ms | Github | 0.01 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 376 | 1568ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 377 | 1617ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 378 | 1623ms | Heycall-e | 0.13 MB/s | `https://heycall-e.com` | 通用代理 |
| 379 | 1653ms | GHProxy Net | 0.28 MB/s | `https://ghproxy.net` | 通用代理 |
| 380 | 1668ms | Web | 0.17 MB/s | `https://web.archive.org` | 通用代理 |
| 381 | 1677ms | Gh | 1.02 MB/s | `https://gh.dpik.top` | 通用代理 |
| 382 | 1691ms | Git | 0.12 MB/s | `https://git.669966.xyz` | 通用代理 |
| 383 | 1720ms | Ghproxy | 0.96 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 384 | 2059ms | G | 0.16 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 385 | 2117ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 386 | 2119ms | Img | - | `https://img.ink` | 通用代理 |
| 387 | 2166ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 388 | 2207ms | Dplayer | 0.03 MB/s | `https://dplayer.diandian.com` | 通用代理 |
| 389 | 2269ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 390 | 2494ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 391 | 2586ms | Upyun | 0.01 MB/s | `https://upyun.com` | 通用代理 |
| 392 | 2595ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 393 | 2656ms | Provider | - | `https://provider.com` | 通用代理 |
| 394 | 2807ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 395 | 2813ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 396 | 3017ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 397 | 3378ms | GHProxy MonkeyRay | 0.07 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 398 | 6301ms | Proxy | 0.04 MB/s | `https://proxy.yaoyaoling.net` | 通用代理 |


### ⚠️ 不稳定节点（18 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| GH Zwnes (`gh-zwnes-xyz`) | 25 次 |
| GitClone (`gitclone-com`) | 4 次 |
| Gh (`gh-llkk-cc`) | 9 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Git (`git-tangbai-cc`) | 8 次 |
| Gh (`gh-b52m-cn`) | 12 次 |
| Sub (`sub-ikar-eu-org`) | 7 次 |
| Nssurge (`nssurge-com`) | 11 次 |
| Aomedia (`aomedia-issues-chromium-org`) | 11 次 |
| Flashtype (`flashtype-com`) | 3 次 |
| Holyclaude (`holyclaude-coderluii-dev`) | 16 次 |
| Maplecode (`maplecode-art`) | 26 次 |
| Worldofclaudecraft (`worldofclaudecraft-com`) | 22 次 |
| Adult (`adult-contents-fc2-com`) | 8 次 |
| Git (`git-net2o-de`) | 1 次 |
| Free (`free-cn-eu-org`) | 4 次 |
| Proxy (`proxy-scdn-io`) | 2 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 409 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **416** | |

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
