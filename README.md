# MirrorHub

最全 GitHub 加速节点维护仓库。自动发现新节点、自动测速、自动清理失效节点，其他项目远程拉取 JSON 即可接入。

> 📊 数据自动更新于 **2026-11-13T23:23:07Z**，每 6 小时刷新一次。当前 ✅ **515** 在线 / ⚠️ **35** 不稳定 / ⚰️ **64** 已失效归档。

## 核心特性

- **550 个节点**，4 大分类，全部经过测速验证
- **自动发现**：从来源仓库同步 + GitHub Code Search 探索，新节点自动加入待验证
- **自动测速**：每 6 小时全量测速，同时测 raw + release 双 URL，避免误判
- **自动清理**：连续失效的节点自动移入历史档案
- **自动排序**：按平均延迟排序，接入项目直接选最快的
- **飞书推送**：节点状态变化时推送通知（需配置 webhook）
- **语言无关**：纯 JSON 配置，Kotlin/Python/Shell 等任意语言可接入

## 在线节点排行（按延迟）

| # | 延迟 | 名称 | 带宽 | 地址 | 分类 |
|---|------|------|------|------|
| 1 | 57ms | Opencode | 0.1 MB/s | `https://opencode.ai` | 通用代理 |
| 2 | 72ms | jsDelivr CDN | - | `cdn.jsdelivr.net` | CDN Raw |
| 3 | 76ms | App | 1.42 MB/s | `https://app.snowflake.com` | 通用代理 |
| 4 | 82ms | Linkedin | 0.16 MB/s | `https://linkedin.com` | 通用代理 |
| 5 | 87ms | Microsoftedge | 0.62 MB/s | `https://microsoftedge.microsoft.com` | 通用代理 |
| 6 | 97ms | Vmflow | - | `https://vmflow.xyz` | 通用代理 |
| 7 | 102ms | Docs | 0.07 MB/s | `https://docs.tibco.com` | 通用代理 |
| 8 | 102ms | Xjtu-nyxf-study-material | 0.15 MB/s | `https://xjtu-nyxf-study-material.pages.dev` | 通用代理 |
| 9 | 103ms | Freegrid-web | - | `https://freegrid-web.pages.dev` | 通用代理 |
| 10 | 104ms | X | 1.22 MB/s | `https://x.com` | 通用代理 |
| 11 | 105ms | Dilo-d14 | 0.17 MB/s | `https://dilo-d14.pages.dev` | 通用代理 |
| 12 | 106ms | Deno | 0.75 MB/s | `https://deno.com` | 通用代理 |
| 13 | 106ms | Kighelper-cloud | 0.06 MB/s | `https://kighelper-cloud.pages.dev` | 通用代理 |
| 14 | 108ms | Crypto-funding-arbitrage | 1.26 MB/s | `https://crypto-funding-arbitrage.pages.dev` | 通用代理 |
| 15 | 110ms | Opresume | 0.36 MB/s | `https://opresume.pages.dev` | 通用代理 |
| 16 | 111ms | Huly-mcp | 0.15 MB/s | `https://huly-mcp.dearlordylord.com` | 通用代理 |
| 17 | 111ms | Vibeholding | - | `https://vibeholding.pages.dev` | 通用代理 |
| 18 | 112ms | Bee-vs-hornets | - | `https://bee-vs-hornets.pages.dev` | 通用代理 |
| 19 | 113ms | Wordpaper | 0.25 MB/s | `https://wordpaper.pages.dev` | 通用代理 |
| 20 | 115ms | Getorigin | - | `https://getorigin.io` | 通用代理 |
| 21 | 115ms | Tools | 1.54 MB/s | `https://tools.realtime-ai.chat` | 通用代理 |
| 22 | 117ms | Img | - | `https://img.shields.io` | 通用代理 |
| 23 | 118ms | jsDelivr TestingCF | - | `testingcf.jsdelivr.net` | CDN Raw |
| 24 | 123ms | Impeccable | 1.03 MB/s | `https://impeccable.style` | 通用代理 |
| 25 | 124ms | Docs | 1.79 MB/s | `https://docs.uxway.app` | 通用代理 |
| 26 | 127ms | Earth | - | `https://earth.jaxa.jp` | 通用代理 |
| 27 | 127ms | Githubstatus | 1.12 MB/s | `https://githubstatus.com` | 通用代理 |
| 28 | 127ms | Zen-ai-pentest | - | `https://zen-ai-pentest.pages.dev` | 通用代理 |
| 29 | 132ms | App | 0.04 MB/s | `https://app.codecov.io` | 通用代理 |
| 30 | 134ms | Repsy | 0.09 MB/s | `https://repsy.io` | 通用代理 |
| 31 | 134ms | Shields | - | `https://shields.io` | 通用代理 |
| 32 | 136ms | My-portfolio-6d703 | 0.12 MB/s | `https://my-portfolio-6d703.web.app` | 通用代理 |
| 33 | 136ms | Shiguredo | 0.52 MB/s | `https://shiguredo.jp` | 通用代理 |
| 34 | 136ms | jsDelivr GCore | - | `gcore.jsdelivr.net` | CDN Raw |
| 35 | 137ms | App | 0.13 MB/s | `https://app.netlify.com` | 通用代理 |
| 36 | 137ms | Dsh | - | `https://dsh.jiangjiangze.icu` | 通用代理 |
| 37 | 138ms | Anh | 0.25 MB/s | `https://anh.sirrus.cc` | 通用代理 |
| 38 | 138ms | Cloud | 0.31 MB/s | `https://cloud.google.com` | 通用代理 |
| 39 | 138ms | Ghproxy | 0.31 MB/s | `https://ghproxy.cfd` | 通用代理 |
| 40 | 139ms | Eng-3385e | 0.02 MB/s | `https://eng-3385e.web.app` | 通用代理 |
| 41 | 139ms | Openpua | 0.29 MB/s | `https://openpua.ai` | 通用代理 |
| 42 | 139ms | Resume-5lv | 0.17 MB/s | `https://resume-5lv.pages.dev` | 通用代理 |
| 43 | 140ms | Freeport | 0.03 MB/s | `https://freeport.network` | 通用代理 |
| 44 | 142ms | Agentlimb | 0.17 MB/s | `https://agentlimb.com` | 通用代理 |
| 45 | 142ms | Codeeraser | 0.07 MB/s | `https://codeeraser.dev` | 通用代理 |
| 46 | 142ms | Twitch | 0.7 MB/s | `https://twitch.tv` | 通用代理 |
| 47 | 143ms | Eng-3385e | 0.04 MB/s | `https://eng-3385e.firebaseapp.com` | 通用代理 |
| 48 | 143ms | Serac | 0.06 MB/s | `https://serac.build` | 通用代理 |
| 49 | 144ms | Caw | 0.05 MB/s | `https://caw.rocks` | 通用代理 |
| 50 | 144ms | Clayrune | 0.14 MB/s | `https://clayrune.io` | 通用代理 |
| 51 | 144ms | Gpui | 0.22 MB/s | `https://gpui.rs` | 通用代理 |
| 52 | 145ms | App | 0.03 MB/s | `https://app.openpencil.dev` | 通用代理 |
| 53 | 145ms | L4d2 | 0.13 MB/s | `https://l4d2.laoyutang.cn` | 通用代理 |
| 54 | 145ms | Polgarand | 0.07 MB/s | `https://polgarand.org` | 通用代理 |
| 55 | 147ms | Fxin | 0.05 MB/s | `https://fxin.cc` | 通用代理 |
| 56 | 147ms | Gitea-mirror | 0.49 MB/s | `https://gitea-mirror.raylabs.io` | 通用代理 |
| 57 | 147ms | Openchamber | 1.75 MB/s | `https://openchamber.dev` | 通用代理 |
| 58 | 150ms | Goreportcard | 0.02 MB/s | `https://goreportcard.com` | 通用代理 |
| 59 | 151ms | Vidocq | 0.14 MB/s | `https://vidocq.dev` | 通用代理 |
| 60 | 152ms | Search | - | `https://search.nixos.org` | 通用代理 |
| 61 | 153ms | Cumora | 0.3 MB/s | `https://cumora.ai` | 通用代理 |
| 62 | 154ms | Chops | 0.03 MB/s | `https://chops.md` | 通用代理 |
| 63 | 154ms | Cpfly | - | `https://cpfly.top` | 通用代理 |
| 64 | 154ms | Datamelt | 0.07 MB/s | `https://datamelt.org` | 通用代理 |
| 65 | 154ms | Nezha | - | `https://nezha.hanshutx.com` | 通用代理 |
| 66 | 155ms | App | 0.03 MB/s | `https://app.opencastor.com` | 通用代理 |
| 67 | 155ms | Ireasoning | 0.06 MB/s | `https://ireasoning.com` | 通用代理 |
| 68 | 155ms | Music-cli | 0.21 MB/s | `https://music-cli.luongnv.com` | 通用代理 |
| 69 | 155ms | Oreports | - | `https://oreports.com` | 通用代理 |
| 70 | 156ms | Play | 0.03 MB/s | `https://play.templatical.com` | 通用代理 |
| 71 | 158ms | Caiji | - | `https://caiji.cyou` | 通用代理 |
| 72 | 158ms | Nextclaw | - | `https://nextclaw.io` | 通用代理 |
| 73 | 158ms | Vibesql | 0.1 MB/s | `https://vibesql.org` | 通用代理 |
| 74 | 159ms | Opencovibe | 0.28 MB/s | `https://opencovibe.com` | 通用代理 |
| 75 | 159ms | Smith | - | `https://smith.attck.com` | 通用代理 |
| 76 | 160ms | Github | 1.62 MB/s | `https://github.788787.xyz` | 通用代理 |
| 77 | 162ms | Miaozitie | 0.07 MB/s | `https://miaozitie.80wdb.com` | 通用代理 |
| 78 | 163ms | Agents | - | `https://agents.hyper.space` | 通用代理 |
| 79 | 163ms | Github | 1.47 MB/s | `https://github.zzrbk.xyz` | 通用代理 |
| 80 | 163ms | Opentakeoff | 0.04 MB/s | `https://opentakeoff.kentucky-ai.com` | 通用代理 |
| 81 | 163ms | Tokei | 0.41 MB/s | `https://tokei.lanshuagent.com` | 通用代理 |
| 82 | 163ms | Zebrunner | 1.46 MB/s | `https://zebrunner.com` | 通用代理 |
| 83 | 164ms | Glass | 0.08 MB/s | `https://glass.goose.cc.cd` | 通用代理 |
| 84 | 167ms | Git | 1.93 MB/s | `https://git.951959483.xyz` | 通用代理 |
| 85 | 167ms | Gp | 0.9 MB/s | `https://gp.871201.xyz` | 通用代理 |
| 86 | 168ms | Alas | 0.64 MB/s | `https://alas.nanoda.work` | 通用代理 |
| 87 | 168ms | Cognitum | 0.12 MB/s | `https://cognitum.one` | 通用代理 |
| 88 | 169ms | Bestdori | 0.06 MB/s | `https://bestdori.com` | 通用代理 |
| 89 | 169ms | Console | - | `https://console.kubestellar.io` | 通用代理 |
| 90 | 170ms | Discord | 0.09 MB/s | `https://discord.gg` | 通用代理 |
| 91 | 171ms | Dockerproxy | - | `https://dockerproxy.link` | 通用代理 |
| 92 | 171ms | Gh | 1.67 MB/s | `https://gh.198962.xyz` | 通用代理 |
| 93 | 171ms | Osf | 0.02 MB/s | `https://osf.io` | 通用代理 |
| 94 | 172ms | Ghproxy | 1.48 MB/s | `https://ghproxy.xzhouqd.com` | 通用代理 |
| 95 | 172ms | Github | 1.93 MB/s | `https://github.880824.xyz` | 通用代理 |
| 96 | 172ms | Tvv | 1.47 MB/s | `https://tvv.tw` | 通用代理 |
| 97 | 173ms | Tmt | - | `https://tmt.tencentcloudapi.com` | 通用代理 |
| 98 | 173ms | Tubawinui3 | 0.02 MB/s | `https://tubawinui3.cn` | 通用代理 |
| 99 | 174ms | Wiki | - | `https://wiki.mozilla.org` | 通用代理 |
| 100 | 175ms | Cherryai | 0.04 MB/s | `https://cherryai.com` | 通用代理 |
| 101 | 175ms | Codevibeforyou | - | `https://codevibeforyou.netlify.app` | 通用代理 |
| 102 | 176ms | GH-Proxy Org | 1.02 MB/s | `https://gh-proxy.org` | 通用代理 |
| 103 | 178ms | Cody | 0.22 MB/s | `https://cody.todyle.com` | 通用代理 |
| 104 | 178ms | GH Con | - | `https://gh.con.sh` | 通用代理 |
| 105 | 179ms | Thumb | 1.13 MB/s | `https://thumb.wikimedia.org` | 通用代理 |
| 106 | 182ms | Ghproxy | 1.74 MB/s | `https://ghproxy.imciel.com` | 通用代理 |
| 107 | 182ms | Lawyer-yu | 0.06 MB/s | `https://lawyer-yu.netlify.app` | 通用代理 |
| 108 | 182ms | Readsync | 0.05 MB/s | `https://readsync.org` | 通用代理 |
| 109 | 183ms | Git | 1.48 MB/s | `https://git.820828.xyz` | 通用代理 |
| 110 | 184ms | GH-Proxy | 1.11 MB/s | `https://gh-proxy.com` | 通用代理 |
| 111 | 185ms | Blitzos | - | `https://blitzos.com` | 通用代理 |
| 112 | 185ms | Bolt2github | 0.03 MB/s | `https://bolt2github.com` | 通用代理 |
| 113 | 185ms | Gh | 1.61 MB/s | `https://gh.996986.xyz` | 通用代理 |
| 114 | 186ms | Github | 1.58 MB/s | `https://github.ihnic.com` | 通用代理 |
| 115 | 188ms | App | - | `https://app.catgo-ucsd.org` | 通用代理 |
| 116 | 188ms | Capitalcompanion | - | `https://capitalcompanion.ai` | 通用代理 |
| 117 | 188ms | Status | - | `https://status.leez.tech` | 通用代理 |
| 118 | 188ms | Vhs | - | `https://vhs.charm.sh` | 通用代理 |
| 119 | 189ms | GH Monlor | 1.32 MB/s | `https://gh.monlor.com` | 通用代理 |
| 120 | 191ms | Nextup-resource | 0.02 MB/s | `https://nextup-resource.vercel.app` | 通用代理 |
| 121 | 194ms | Components | 0.09 MB/s | `https://components.dereekb.com` | 通用代理 |
| 122 | 196ms | Dandiarchive | - | `https://dandiarchive.org` | 通用代理 |
| 123 | 200ms | Game | 0.09 MB/s | `https://game.chozo.net` | 通用代理 |
| 124 | 200ms | Lrclib | - | `https://lrclib.net` | 通用代理 |
| 125 | 201ms | Openttd | 0.05 MB/s | `https://openttd.org` | 通用代理 |
| 126 | 201ms | Tms | 0.09 MB/s | `https://tms.logisticsx.app` | 通用代理 |
| 127 | 204ms | Agoramarket | 0.04 MB/s | `https://agoramarket.purrtechllc.com` | 通用代理 |
| 128 | 204ms | Aiblackboxfc | 0.27 MB/s | `https://aiblackboxfc.com` | 通用代理 |
| 129 | 205ms | Bananaslides | 0.26 MB/s | `https://bananaslides.online` | 通用代理 |
| 130 | 208ms | Megacrit | 0.12 MB/s | `https://megacrit.com` | 通用代理 |
| 131 | 210ms | Gh | 1.36 MB/s | `https://gh.404cafe.fun` | 通用代理 |
| 132 | 213ms | Boxento | - | `https://boxento.app` | 通用代理 |
| 133 | 213ms | Hopp | 0.02 MB/s | `https://hopp.sh` | 通用代理 |
| 134 | 214ms | Pidash | - | `https://pidash.airepublic.com` | 通用代理 |
| 135 | 215ms | Contrib | 0.21 MB/s | `https://contrib.rocks` | 通用代理 |
| 136 | 215ms | Shiori-v1 | 0.01 MB/s | `https://shiori-v1.vercel.app` | 通用代理 |
| 137 | 216ms | Weibo-archiver | - | `https://weibo-archiver.chilfish.top` | 通用代理 |
| 138 | 220ms | Agent-assistant-ten | - | `https://agent-assistant-ten.vercel.app` | 通用代理 |
| 139 | 220ms | Tjf | 0.09 MB/s | `https://tjf.totvs.com.br` | 通用代理 |
| 140 | 221ms | Kenyu | 1.74 MB/s | `https://kenyu.ggff.net` | 通用代理 |
| 141 | 222ms | Ghproxy | 0.66 MB/s | `https://ghproxy.sakuramoe.dev` | 通用代理 |
| 142 | 223ms | Sink | - | `https://sink.gamas.workers.dev` | 通用代理 |
| 143 | 225ms | Demo-public | - | `https://demo-public.dev.scalebase.io` | 通用代理 |
| 144 | 225ms | Pnfsoftware | 0.04 MB/s | `https://pnfsoftware.com` | 通用代理 |
| 145 | 226ms | Chatgpt | 2.59 MB/s | `https://chatgpt.com` | 通用代理 |
| 146 | 230ms | FastGit CC | 1.12 MB/s | `https://fastgit.cc` | 通用代理 |
| 147 | 230ms | Training | 1.03 MB/s | `https://training.ti.com` | 通用代理 |
| 148 | 231ms | Sina | 0.87 MB/s | `https://sina.dev` | 通用代理 |
| 149 | 232ms | Gitnexus | - | `https://gitnexus.vercel.app` | 通用代理 |
| 150 | 232ms | Tools | 0.06 MB/s | `https://tools.ietf.org` | 通用代理 |
| 151 | 236ms | jsDelivr Fastly | - | `fastly.jsdelivr.net` | CDN Raw |
| 152 | 237ms | Tomcat1235 | 0.58 MB/s | `https://tomcat1235.nyc.mn` | 通用代理 |
| 153 | 237ms | Xm | - | `https://xm.solov.cc` | 通用代理 |
| 154 | 239ms | Demo | - | `https://demo.mcphub.app` | 通用代理 |
| 155 | 240ms | Ode | - | `https://ode.fun` | 通用代理 |
| 156 | 242ms | Cdn | 0.75 MB/s | `https://cdn.gh-proxy.org` | 通用代理 |
| 157 | 242ms | Savannah | 0.04 MB/s | `https://savannah.gnu.org` | 通用代理 |
| 158 | 244ms | Api | 0.06 MB/s | `https://api.solov.cc` | 通用代理 |
| 159 | 244ms | Microcoreos | 0.18 MB/s | `https://microcoreos.com` | 通用代理 |
| 160 | 245ms | Misaligned | 0.72 MB/s | `https://misaligned.top` | 通用代理 |
| 161 | 246ms | Peer-learning-liart | - | `https://peer-learning-liart.vercel.app` | 通用代理 |
| 162 | 247ms | Meetonmemory | - | `https://meetonmemory.vercel.app` | 通用代理 |
| 163 | 247ms | Slack | 0.09 MB/s | `https://slack.kubernetes.io` | 通用代理 |
| 164 | 248ms | Twitter | 0.86 MB/s | `https://twitter.com` | 通用代理 |
| 165 | 249ms | Gsd | 0.25 MB/s | `https://gsd.vinny.dev` | 通用代理 |
| 166 | 249ms | Nisar | 0.28 MB/s | `https://nisar.jpl.nasa.gov` | 通用代理 |
| 167 | 251ms | Jolli | - | `https://jolli.ai` | 通用代理 |
| 168 | 252ms | Taigi-life-islands | 1.01 MB/s | `https://taigi-life-islands.cjs-1359.chatgpt.site` | 通用代理 |
| 169 | 253ms | Gvsu | - | `https://gvsu.edu` | 通用代理 |
| 170 | 254ms | Clypra | 0.05 MB/s | `https://clypra.abdulkabirmusa.com` | 通用代理 |
| 171 | 254ms | Trysquash | - | `https://trysquash.dev` | 通用代理 |
| 172 | 255ms | Aka | 0.26 MB/s | `https://aka.ms` | 通用代理 |
| 173 | 258ms | Sprite | - | `https://sprite.gorest.ai` | 通用代理 |
| 174 | 259ms | Anyplot | 0.05 MB/s | `https://anyplot.ai` | 通用代理 |
| 175 | 259ms | Axios-http | 0.3 MB/s | `https://axios-http.com` | 通用代理 |
| 176 | 259ms | Fastgpt | - | `https://fastgpt.leez.tech` | 通用代理 |
| 177 | 261ms | Green-wells-connect | - | `https://green-wells-connect.vercel.app` | 通用代理 |
| 178 | 261ms | Paypal | 0.03 MB/s | `https://paypal.com` | 通用代理 |
| 179 | 262ms | App | - | `https://app.agent-swarm.dev` | 通用代理 |
| 180 | 262ms | Ginlix | 0.46 MB/s | `https://ginlix.ai` | 通用代理 |
| 181 | 262ms | SciProxy Down | - | `https://down.sciproxy.com` | 通用代理 |
| 182 | 264ms | Cinegen-kappa | - | `https://cinegen-kappa.vercel.app` | 通用代理 |
| 183 | 264ms | Zuckerbot | 0.02 MB/s | `https://zuckerbot.ai` | 通用代理 |
| 184 | 266ms | Ai-trend-publish | 0.02 MB/s | `https://ai-trend-publish.vercel.app` | 通用代理 |
| 185 | 266ms | Help | - | `https://help.obsidian.md` | 通用代理 |
| 186 | 266ms | Market-tracker-khaki | - | `https://market-tracker-khaki.vercel.app` | 通用代理 |
| 187 | 267ms | Binance-alpha-ten | - | `https://binance-alpha-ten.vercel.app` | 通用代理 |
| 188 | 267ms | Github | 0.65 MB/s | `https://github.cnxiaobai.com` | 通用代理 |
| 189 | 267ms | Wings | 0.03 MB/s | `https://wings.nopejs.me` | 通用代理 |
| 190 | 267ms | Yoyo | - | `https://yoyo.yolog.dev` | 通用代理 |
| 191 | 268ms | Open-prep-ai | - | `https://open-prep-ai.vercel.app` | 通用代理 |
| 192 | 268ms | Phabricator | 0.05 MB/s | `https://phabricator.wikimedia.org` | 通用代理 |
| 193 | 269ms | Open | 0.02 MB/s | `https://open.bigmodel.cn` | 通用代理 |
| 194 | 269ms | Themolt | 0.03 MB/s | `https://themolt.net` | 通用代理 |
| 195 | 269ms | Travis-ci | 0.16 MB/s | `https://travis-ci.org` | 通用代理 |
| 196 | 270ms | I | - | `https://i.imgur.com` | 通用代理 |
| 197 | 270ms | Radio-browser | 0.02 MB/s | `https://radio-browser.info` | 通用代理 |
| 198 | 273ms | Ggg | 1.52 MB/s | `https://ggg.clwap.dpdns.org` | 通用代理 |
| 199 | 279ms | Fx4 | - | `https://fx4.cn` | 通用代理 |
| 200 | 280ms | CrashMC CDN | 1.18 MB/s | `https://cdn.crashmc.com` | 通用代理 |
| 201 | 280ms | Hub | - | `https://hub.decision.ai` | 通用代理 |
| 202 | 283ms | Datomic | 0.04 MB/s | `https://datomic.com` | 通用代理 |
| 203 | 284ms | Ai-watch | 0.02 MB/s | `https://ai-watch.dev` | 通用代理 |
| 204 | 284ms | Cursor | 0.52 MB/s | `https://cursor.com` | 通用代理 |
| 205 | 284ms | Ngrok | 0.93 MB/s | `https://ngrok.com` | 通用代理 |
| 206 | 286ms | Pulse-commerce | 0.17 MB/s | `https://pulse-commerce.com` | 通用代理 |
| 207 | 287ms | Coreos | 1.34 MB/s | `https://coreos.com` | 通用代理 |
| 208 | 291ms | Vibe | - | `https://vibe.demonrain.top` | 通用代理 |
| 209 | 291ms | Visionmemorymcp | 0.23 MB/s | `https://visionmemorymcp.com` | 通用代理 |
| 210 | 292ms | Builders-gate | - | `https://builders-gate.com` | 通用代理 |
| 211 | 293ms | Space-track | - | `https://space-track.org` | 通用代理 |
| 212 | 296ms | Congressmcp | 0.02 MB/s | `https://congressmcp.lawgiver.ai` | 通用代理 |
| 213 | 299ms | Gradle | - | `https://gradle.org` | 通用代理 |
| 214 | 301ms | Godocs | 0.07 MB/s | `https://godocs.io` | 通用代理 |
| 215 | 302ms | Demo | 0.01 MB/s | `https://demo.edgeever.org` | 通用代理 |
| 216 | 304ms | Kalix | 0.33 MB/s | `https://kalix.io` | 通用代理 |
| 217 | 305ms | Web4j | - | `https://web4j.com` | 通用代理 |
| 218 | 306ms | GH-Proxy Net | - | `https://gh-proxy.net` | 通用代理 |
| 219 | 309ms | Getgit | 1.6 MB/s | `https://getgit.love8yun.eu.org` | 通用代理 |
| 220 | 313ms | Aistudio | 1.46 MB/s | `https://aistudio.google.com` | 通用代理 |
| 221 | 318ms | Gh | 0.55 MB/s | `https://gh.padao.fun` | 通用代理 |
| 222 | 319ms | Gitproxy | - | `https://gitproxy.click` | 通用代理 |
| 223 | 319ms | Sonarcloud | 0.12 MB/s | `https://sonarcloud.io` | 通用代理 |
| 224 | 320ms | Jbg53qui | - | `https://jbg53qui.tolink.pro` | 通用代理 |
| 225 | 322ms | Edgeone | 1.76 MB/s | `https://edgeone.gh-proxy.org` | 通用代理 |
| 226 | 326ms | Data | 0.03 MB/s | `https://data.openecon.ai` | 通用代理 |
| 227 | 327ms | Bisguard | - | `https://bisguard.com` | 通用代理 |
| 228 | 327ms | Github | 1.65 MB/s | `https://github.crdz.eu.org` | 通用代理 |
| 229 | 328ms | Youtu | 1.21 MB/s | `https://youtu.be` | 通用代理 |
| 230 | 330ms | 30006000 | 0.73 MB/s | `https://30006000.xyz` | 通用代理 |
| 231 | 332ms | jsDelivr OriginFastly | - | `originfastly.jsdelivr.net` | CDN Raw |
| 232 | 333ms | Agentkey | 0.61 MB/s | `https://agentkey.app` | 通用代理 |
| 233 | 333ms | B23 | - | `https://b23.tv` | 通用代理 |
| 234 | 334ms | Gh | 1.06 MB/s | `https://gh.223456.xyz` | 通用代理 |
| 235 | 339ms | Oem | 0.02 MB/s | `https://oem.re` | 通用代理 |
| 236 | 340ms | Code | 1.29 MB/s | `https://code.claude.com` | 通用代理 |
| 237 | 340ms | Erp | 0.01 MB/s | `https://erp.kacon.ai` | 通用代理 |
| 238 | 341ms | Beta | - | `https://beta.durieux.me` | 通用代理 |
| 239 | 342ms | Wandoukj | - | `https://wandoukj.eu.org` | 通用代理 |
| 240 | 347ms | Agenticcorporation | 0.02 MB/s | `https://agenticcorporation.net` | 通用代理 |
| 241 | 347ms | GHFast | 0.66 MB/s | `https://ghfast.top` | 通用代理 |
| 242 | 347ms | Wpt | - | `https://wpt.fyi` | 通用代理 |
| 243 | 352ms | Claude | 0.24 MB/s | `https://claude.megabyte.space` | 通用代理 |
| 244 | 352ms | Github | 1.7 MB/s | `https://github.1ms.xx.kg` | 通用代理 |
| 245 | 362ms | GH Nxnow | 0.41 MB/s | `https://gh.nxnow.top` | 通用代理 |
| 246 | 363ms | Code | - | `https://code.leez.tech` | 通用代理 |
| 247 | 363ms | Ghproxy | 0.57 MB/s | `https://ghproxy.vip` | 通用代理 |
| 248 | 371ms | Props | - | `https://props.jodd.org` | 通用代理 |
| 249 | 372ms | Demo | - | `https://demo.whodb.com` | 通用代理 |
| 250 | 372ms | Vatrasoft | - | `https://vatrasoft.de` | 通用代理 |
| 251 | 374ms | Agitar | 0.03 MB/s | `https://agitar.com` | 通用代理 |
| 252 | 377ms | Docs | - | `https://docs.chartsql.com` | 通用代理 |
| 253 | 377ms | Gh | 0.76 MB/s | `https://gh.noki.eu.org` | 通用代理 |
| 254 | 377ms | V4 | 1.55 MB/s | `https://v4.gh-proxy.org` | 通用代理 |
| 255 | 377ms | Wesight | - | `https://wesight.ai` | 通用代理 |
| 256 | 379ms | Ipradar | - | `https://ipradar.huxiao0207.dpdns.org` | 通用代理 |
| 257 | 381ms | Nanobananaeditor | - | `https://nanobananaeditor.dev` | 通用代理 |
| 258 | 382ms | Certbot | - | `https://certbot.eff.org` | 通用代理 |
| 259 | 382ms | Cloddsbot | - | `https://cloddsbot.com` | 通用代理 |
| 260 | 382ms | Docs | 0.03 MB/s | `https://docs.scriptcat.org` | 通用代理 |
| 261 | 385ms | Db | - | `https://db.jodd.org` | 通用代理 |
| 262 | 386ms | Bailian | 0.08 MB/s | `https://bailian.console.aliyun.com` | 通用代理 |
| 263 | 386ms | Github | 1.57 MB/s | `https://github.lsdfxdk.nyc.mn` | 通用代理 |
| 264 | 388ms | Lagarto | - | `https://lagarto.jodd.org` | 通用代理 |
| 265 | 389ms | Electronforge | - | `https://electronforge.io` | 通用代理 |
| 266 | 393ms | Proxetta | - | `https://proxetta.jodd.org` | 通用代理 |
| 267 | 396ms | Ghproxy | 0.54 MB/s | `https://ghproxy.mirror.skybyte.me` | 通用代理 |
| 268 | 397ms | App | 0.01 MB/s | `https://app.verifywise.ai` | 通用代理 |
| 269 | 399ms | Agent-room | 0.02 MB/s | `https://agent-room.com` | 通用代理 |
| 270 | 399ms | Appdynamics | 0.53 MB/s | `https://appdynamics.com` | 通用代理 |
| 271 | 399ms | Dreamgraph | - | `https://dreamgraph.nofs.ai` | 通用代理 |
| 272 | 399ms | Steamcommunity | 0.11 MB/s | `https://steamcommunity.com` | 通用代理 |
| 273 | 401ms | Core | 0.01 MB/s | `https://core.telegram.org` | 通用代理 |
| 274 | 404ms | Manual | - | `https://manual.getsurfboard.com` | 通用代理 |
| 275 | 407ms | Docs | 0.56 MB/s | `https://docs.anthropic.com` | 通用代理 |
| 276 | 407ms | Serverkit | 0.02 MB/s | `https://serverkit.ai` | 通用代理 |
| 277 | 408ms | App | - | `https://app.baro.jigjoy.ai` | 通用代理 |
| 278 | 412ms | Gdcvault | 0.14 MB/s | `https://gdcvault.com` | 通用代理 |
| 279 | 413ms | Mantishack | - | `https://mantishack.com` | 通用代理 |
| 280 | 414ms | Forklaunch | - | `https://forklaunch.com` | 通用代理 |
| 281 | 416ms | Hk | 0.6 MB/s | `https://hk.gh-proxy.com` | 通用代理 |
| 282 | 417ms | Codeflying | 0.01 MB/s | `https://codeflying.app` | 通用代理 |
| 283 | 421ms | Api | 0.01 MB/s | `https://api.everyapi.ai` | 通用代理 |
| 284 | 422ms | Cabinet | 0.02 MB/s | `https://cabinet.xgate.online` | 通用代理 |
| 285 | 422ms | Hub | 0.33 MB/s | `https://hub.glowp.xyz` | 通用代理 |
| 286 | 424ms | Your-domain | 0.06 MB/s | `https://your-domain.com` | 通用代理 |
| 287 | 427ms | GHProxy Net | - | `https://ghproxy.net` | 通用代理 |
| 288 | 429ms | Store | 1.08 MB/s | `https://store.steampowered.com` | 通用代理 |
| 289 | 430ms | Petite | - | `https://petite.jodd.org` | 通用代理 |
| 290 | 435ms | Ipaslogo | - | `https://ipaslogo.com` | 通用代理 |
| 291 | 436ms | Git | - | `https://git.drupalcode.org` | 通用代理 |
| 292 | 439ms | Jonas | - | `https://jonas.ow2.org` | 通用代理 |
| 293 | 441ms | Ednovas Mirror | 0.56 MB/s | `https://github.ednovas.xyz` | 通用代理 |
| 294 | 441ms | Rmfkb6yg | - | `https://rmfkb6yg.mikasa.cloud` | 通用代理 |
| 295 | 442ms | Labas | - | `https://labas.rogasper.com` | 通用代理 |
| 296 | 446ms | Drupal | 0.2 MB/s | `https://drupal.com` | 通用代理 |
| 297 | 447ms | Mh | - | `https://mh.site19.ddns.net` | 通用代理 |
| 298 | 449ms | Open | 0.01 MB/s | `https://open.feishu.cn` | 通用代理 |
| 299 | 453ms | Muggletest | - | `https://muggletest.com` | 通用代理 |
| 300 | 453ms | Tiktok | 0.11 MB/s | `https://tiktok.com` | 通用代理 |
| 301 | 456ms | Aicoin | - | `https://aicoin.com` | 通用代理 |
| 302 | 458ms | Miu2d | - | `https://miu2d.com` | 通用代理 |
| 303 | 460ms | Lucky | 0.52 MB/s | `https://lucky.appinn.com` | 通用代理 |
| 304 | 463ms | Wl | - | `https://wl.do` | 通用代理 |
| 305 | 465ms | Cfkua | 0.97 MB/s | `https://cfkua.wokaotianshi.eu.org` | 通用代理 |
| 306 | 467ms | Ghproxy | 0.47 MB/s | `https://ghproxy.it` | 通用代理 |
| 307 | 470ms | Neudrive | - | `https://neudrive.ai` | 通用代理 |
| 308 | 481ms | Visual-paradigm | 0.57 MB/s | `https://visual-paradigm.com` | 通用代理 |
| 309 | 486ms | Bible-ai-explorer | 0.07 MB/s | `https://bible-ai-explorer.vercel.app` | 通用代理 |
| 310 | 486ms | Projects | - | `https://projects.ow2.org` | 通用代理 |
| 311 | 486ms | Unhaut | - | `https://unhaut.epizy.com` | 通用代理 |
| 312 | 487ms | Autonomi | 0.02 MB/s | `https://autonomi.dev` | 通用代理 |
| 313 | 489ms | Threadmine | 0.2 MB/s | `https://threadmine.dev` | 通用代理 |
| 314 | 491ms | Axonivy | 0.4 MB/s | `https://axonivy.com` | 通用代理 |
| 315 | 491ms | Memstack | 0.02 MB/s | `https://memstack.pro` | 通用代理 |
| 316 | 495ms | Forgerock | 0.29 MB/s | `https://forgerock.com` | 通用代理 |
| 317 | 496ms | Libusb-java | 0.02 MB/s | `https://libusb-java.ch` | 通用代理 |
| 318 | 500ms | Bseindia | 0.03 MB/s | `https://bseindia.com` | 通用代理 |
| 319 | 503ms | Gitlab | 0.02 MB/s | `https://gitlab.ow2.org` | 通用代理 |
| 320 | 506ms | Turborepo-starter-kit-web | 0.05 MB/s | `https://turborepo-starter-kit-web.vercel.app` | 通用代理 |
| 321 | 509ms | Datastax | 0.39 MB/s | `https://datastax.com` | 通用代理 |
| 322 | 510ms | Lecvdemarius | 0.07 MB/s | `https://lecvdemarius.netlify.app` | 通用代理 |
| 323 | 514ms | SLink | 0.05 MB/s | `https://slink.ltd` | 通用代理 |
| 324 | 515ms | So | - | `https://so.252035.xyz` | 通用代理 |
| 325 | 518ms | Doc | 0.02 MB/s | `https://doc.sibvisions.com` | 通用代理 |
| 326 | 524ms | YYLX Git | 1.09 MB/s | `https://git.yylx.win` | 通用代理 |
| 327 | 530ms | Stockapp | - | `https://stockapp.finance.qq.com` | 通用代理 |
| 328 | 531ms | Isi | 0.18 MB/s | `https://isi.edu` | 通用代理 |
| 329 | 535ms | Patchworkos | 0.27 MB/s | `https://patchworkos.com` | 通用代理 |
| 330 | 536ms | Ygdj7 | 0.04 MB/s | `https://ygdj7.com` | 通用代理 |
| 331 | 537ms | Luna | 0.04 MB/s | `https://luna.diamondfsd.com` | 通用代理 |
| 332 | 540ms | Mxnet | 0.03 MB/s | `https://mxnet.apache.org` | 通用代理 |
| 333 | 545ms | Tridium | 0.12 MB/s | `https://tridium.com` | 通用代理 |
| 334 | 551ms | Msdn | 0.04 MB/s | `https://msdn.microsoft.com` | 通用代理 |
| 335 | 553ms | Hubp | 0.01 MB/s | `https://hubp.org` | 通用代理 |
| 336 | 555ms | Analytics | - | `https://analytics.geekertao.top` | 通用代理 |
| 337 | 559ms | App | 0.02 MB/s | `https://app.fossa.com` | 通用代理 |
| 338 | 559ms | Umami-mcp | 0.87 MB/s | `https://umami-mcp.macawls.dev` | 通用代理 |
| 339 | 560ms | Easyxls | 0.12 MB/s | `https://easyxls.com` | 通用代理 |
| 340 | 564ms | Easyboardgame | 0.01 MB/s | `https://easyboardgame.top` | 通用代理 |
| 341 | 565ms | Api | - | `https://api.river.ai` | 通用代理 |
| 342 | 569ms | Taozhiyy | - | `https://taozhiyy.top` | 通用代理 |
| 343 | 576ms | App | - | `https://app.flashcards-open-source-app.com` | 通用代理 |
| 344 | 578ms | Yourdomain | - | `https://yourdomain.com` | 通用代理 |
| 345 | 581ms | Mt4j | 0.01 MB/s | `https://mt4j.org` | 通用代理 |
| 346 | 585ms | Company | - | `https://company.g0v.ronny.tw` | 通用代理 |
| 347 | 586ms | Oci-pronghorn | - | `https://oci-pronghorn.gitbook.io` | 通用代理 |
| 348 | 591ms | Kuroutoshikou | 0.63 MB/s | `https://kuroutoshikou.com` | 通用代理 |
| 349 | 599ms | Oapi | - | `https://oapi.dingtalk.com` | 通用代理 |
| 350 | 605ms | Nyx | 0.03 MB/s | `https://nyx.chrono-ai.fun` | 通用代理 |
| 351 | 606ms | Local-mcp | - | `https://local-mcp.com` | 通用代理 |
| 352 | 606ms | Paymentcomponents | 0.47 MB/s | `https://paymentcomponents.com` | 通用代理 |
| 353 | 607ms | Ark | 0.32 MB/s | `https://ark.intel.com` | 通用代理 |
| 354 | 609ms | Vaultproject | 0.18 MB/s | `https://vaultproject.io` | 通用代理 |
| 355 | 613ms | Aps | 0.02 MB/s | `https://aps.com` | 通用代理 |
| 356 | 621ms | Github | 0.18 MB/s | `https://github.xxlab.tech` | 通用代理 |
| 357 | 624ms | Console | - | `https://console.tencentcloud.com` | 通用代理 |
| 358 | 633ms | Chinamnos | 0.01 MB/s | `https://chinamnos.ftac.dpdns.org` | 通用代理 |
| 359 | 640ms | Gh | 0.68 MB/s | `https://gh.sixyin.com` | 通用代理 |
| 360 | 644ms | KKGitHub | - | `https://kkgithub.com` | 网页镜像 |
| 361 | 658ms | Costrict | - | `https://costrict.ai` | 通用代理 |
| 362 | 659ms | Semantic-release | - | `https://semantic-release.gitbook.io` | 通用代理 |
| 363 | 661ms | Demo | - | `https://demo.nocobase.com` | 通用代理 |
| 364 | 665ms | Data | - | `https://data.ntpc.gov.tw` | 通用代理 |
| 365 | 668ms | Support | 0.16 MB/s | `https://support.apple.com` | 通用代理 |
| 366 | 674ms | Demo | - | `https://demo.welink.click` | 通用代理 |
| 367 | 678ms | Aosmd | 0.14 MB/s | `https://aosmd.com` | 通用代理 |
| 368 | 678ms | Safedocx | 0.1 MB/s | `https://safedocx.com` | 通用代理 |
| 369 | 690ms | Fastfile | 0.9 MB/s | `https://fastfile.asfd.cn` | 通用代理 |
| 370 | 693ms | Groovy-lang | 0.02 MB/s | `https://groovy-lang.org` | 通用代理 |
| 371 | 702ms | Agoracitizen | 0.02 MB/s | `https://agoracitizen.app` | 通用代理 |
| 372 | 703ms | Jpro | - | `https://jpro.one` | 通用代理 |
| 373 | 718ms | Qm | - | `https://qm.qq.com` | 通用代理 |
| 374 | 721ms | Git | 0.24 MB/s | `https://git.tangbai.cc` | 通用代理 |
| 375 | 722ms | Eclipse | 0.01 MB/s | `https://eclipse.dev` | 通用代理 |
| 376 | 722ms | Os | 0.05 MB/s | `https://os.ryo.lu` | 通用代理 |
| 377 | 727ms | T | 0.03 MB/s | `https://t.me` | 通用代理 |
| 378 | 727ms | Tracely-studio | 0.02 MB/s | `https://tracely-studio.xyz` | 通用代理 |
| 379 | 735ms | Gh | 0.72 MB/s | `https://gh.39.al` | 通用代理 |
| 380 | 738ms | Aixt | - | `https://aixt.llingfei.com` | 通用代理 |
| 381 | 738ms | Tsukuyomi | 0.02 MB/s | `https://tsukuyomi.rozx.moe` | 通用代理 |
| 382 | 739ms | Ghproxy | 0.26 MB/s | `https://ghproxy.053000.xyz` | 通用代理 |
| 383 | 742ms | Proxylist | 0.47 MB/s | `https://proxylist.geonode.com` | 通用代理 |
| 384 | 746ms | 3d-set-visualizer | 0.02 MB/s | `https://3d-set-visualizer.vercel.app` | 通用代理 |
| 385 | 778ms | Aif | 0.05 MB/s | `https://aif.cutcode.dev` | 通用代理 |
| 386 | 778ms | Structure101 | 0.28 MB/s | `https://structure101.com` | 通用代理 |
| 387 | 784ms | Axibase | - | `https://axibase.com` | 通用代理 |
| 388 | 787ms | App | - | `https://app.happy-next.com` | 通用代理 |
| 389 | 806ms | Ghproxy | 0.01 MB/s | `https://ghproxy.cn` | 通用代理 |
| 390 | 808ms | Framagit | 0.01 MB/s | `https://framagit.org` | 通用代理 |
| 391 | 810ms | Api | - | `https://api.niutrans.com` | 通用代理 |
| 392 | 824ms | Community | 0.58 MB/s | `https://community.snowflake.com` | 通用代理 |
| 393 | 826ms | Agentrouter | 0.02 MB/s | `https://agentrouter.org` | 通用代理 |
| 394 | 828ms | Onetwin | 0.02 MB/s | `https://onetwin.cn` | 通用代理 |
| 395 | 830ms | Springboot-generator | 0.05 MB/s | `https://springboot-generator.com` | 通用代理 |
| 396 | 833ms | Docs | 0.19 MB/s | `https://docs.transifex.com` | 通用代理 |
| 397 | 835ms | Code | 0.02 MB/s | `https://code.videolan.org` | 通用代理 |
| 398 | 849ms | Drjava | 0.07 MB/s | `https://drjava.org` | 通用代理 |
| 399 | 849ms | Zhuanlan | 0.04 MB/s | `https://zhuanlan.zhihu.com` | 通用代理 |
| 400 | 875ms | Bugs | 0.02 MB/s | `https://bugs.freebsd.org` | 通用代理 |
| 401 | 880ms | Invent | 0.02 MB/s | `https://invent.kde.org` | 通用代理 |
| 402 | 880ms | Vulnetix | 0.03 MB/s | `https://vulnetix.com` | 通用代理 |
| 403 | 884ms | Sencha | 0.31 MB/s | `https://sencha.com` | 通用代理 |
| 404 | 888ms | Dbgate | 0.13 MB/s | `https://dbgate.org` | 通用代理 |
| 405 | 896ms | Reminder | - | `https://reminder.dev` | 通用代理 |
| 406 | 902ms | Lkkushan | - | `https://lkkushan.gitbook.io` | 通用代理 |
| 407 | 903ms | Support | - | `https://support.iluvatar.com` | 通用代理 |
| 408 | 909ms | Kw-aigc | 0.01 MB/s | `https://kw-aigc.cn` | 通用代理 |
| 409 | 909ms | Vt | 0.19 MB/s | `https://vt.tiktok.com` | 通用代理 |
| 410 | 915ms | Clawbiz | 0.03 MB/s | `https://clawbiz.io` | 通用代理 |
| 411 | 915ms | Fund | - | `https://fund.eastmoney.com` | 通用代理 |
| 412 | 918ms | Gh | 0.7 MB/s | `https://gh.noki.icu` | 通用代理 |
| 413 | 923ms | Kece | - | `https://kece.zheco68.asia` | 通用代理 |
| 414 | 924ms | Build | - | `https://build.cloudflare.dev` | 通用代理 |
| 415 | 928ms | Ccgather | 0.07 MB/s | `https://ccgather.com` | 通用代理 |
| 416 | 928ms | Sct | - | `https://sct.ftqq.com` | 通用代理 |
| 417 | 943ms | Task | 0.03 MB/s | `https://task.sarwarxsami.me` | 通用代理 |
| 418 | 952ms | Ihk | - | `https://ihk.de` | 通用代理 |
| 419 | 952ms | Mimo | 0.18 MB/s | `https://mimo.mi.com` | 通用代理 |
| 420 | 954ms | Geohao | - | `https://geohao.com` | 通用代理 |
| 421 | 955ms | Mirror | - | `https://mirror.houlang.cloud` | 通用代理 |
| 422 | 972ms | Console | 0.01 MB/s | `https://console.cloud.tencent.com` | 通用代理 |
| 423 | 980ms | Md | 0.07 MB/s | `https://md.yhsun.cn` | 通用代理 |
| 424 | 1011ms | Gbs | - | `https://gbs.wanzij.cn` | 通用代理 |
| 425 | 1021ms | Naiveadmin | 0.01 MB/s | `https://naiveadmin.com` | 通用代理 |
| 426 | 1021ms | Romaframework | 0.02 MB/s | `https://romaframework.org` | 通用代理 |
| 427 | 1022ms | Dbschema | - | `https://dbschema.com` | 通用代理 |
| 428 | 1030ms | Jfxstore | 0.02 MB/s | `https://jfxstore.com` | 通用代理 |
| 429 | 1038ms | Web | - | `https://web.4399.com` | 通用代理 |
| 430 | 1039ms | Npmmirror | 0.01 MB/s | `https://npmmirror.com` | 通用代理 |
| 431 | 1040ms | Agentic | - | `https://agentic.iloveagile.me` | 通用代理 |
| 432 | 1046ms | Gleanapp | - | `https://gleanapp.cn` | 通用代理 |
| 433 | 1050ms | Maplesoft | 0.04 MB/s | `https://maplesoft.com` | 通用代理 |
| 434 | 1051ms | Bks | 0.01 MB/s | `https://bks.indevs.in` | 通用代理 |
| 435 | 1052ms | Axislab | - | `https://axislab.top` | 通用代理 |
| 436 | 1058ms | Aistack | 0.01 MB/s | `https://aistack.to` | 通用代理 |
| 437 | 1062ms | Dimagent | 0.37 MB/s | `https://dimagent.com` | 通用代理 |
| 438 | 1064ms | Paper | - | `https://paper.mulanai.com` | 通用代理 |
| 439 | 1068ms | Mdma | 0.05 MB/s | `https://mdma.dev` | 通用代理 |
| 440 | 1072ms | Honeymeta | 0.04 MB/s | `https://honeymeta.com` | 通用代理 |
| 441 | 1085ms | Ghproxy | - | `https://ghproxy.cc` | 通用代理 |
| 442 | 1096ms | Internhack | 0.03 MB/s | `https://internhack.xyz` | 通用代理 |
| 443 | 1105ms | Akiroio | 0.02 MB/s | `https://akiroio.com` | 通用代理 |
| 444 | 1126ms | Doubao | 0.17 MB/s | `https://doubao.com` | 通用代理 |
| 445 | 1141ms | Matroska | 0.01 MB/s | `https://matroska.org` | 通用代理 |
| 446 | 1154ms | Nikkigallery | - | `https://nikkigallery.vip` | 通用代理 |
| 447 | 1159ms | Douyin | - | `https://douyin.com` | 通用代理 |
| 448 | 1161ms | Gitlab | 0.01 MB/s | `https://gitlab.heigit.org` | 通用代理 |
| 449 | 1162ms | Doc | - | `https://doc.libsodium.org` | 通用代理 |
| 450 | 1166ms | Jahia | 0.07 MB/s | `https://jahia.com` | 通用代理 |
| 451 | 1168ms | Fbfh | - | `https://fbfh.trade.gov.tw` | 通用代理 |
| 452 | 1184ms | Im | 0.78 MB/s | `https://im.codes` | 通用代理 |
| 453 | 1221ms | Aliexpress | 0.01 MB/s | `https://aliexpress.com` | 通用代理 |
| 454 | 1222ms | Gitcode | - | `https://gitcode.com` | 通用代理 |
| 455 | 1226ms | Sanguinesoftwares | 0.12 MB/s | `https://sanguinesoftwares.com` | 通用代理 |
| 456 | 1231ms | Github | 0.17 MB/s | `https://github.chenc.dev` | 通用代理 |
| 457 | 1232ms | Caiji | - | `https://caiji.maotaizy.cc` | 通用代理 |
| 458 | 1237ms | Hevolve | 0.07 MB/s | `https://hevolve.ai` | 通用代理 |
| 459 | 1253ms | V | - | `https://v.douyin.com` | 通用代理 |
| 460 | 1271ms | Comfyit | - | `https://comfyit.cn` | 通用代理 |
| 461 | 1283ms | Quant | 0.01 MB/s | `https://quant.zizizaizai.com` | 通用代理 |
| 462 | 1288ms | Pew | 0.01 MB/s | `https://pew.md` | 通用代理 |
| 463 | 1292ms | Github | 0.02 MB/s | `https://github.zjzzy.cloudns.org` | 通用代理 |
| 464 | 1322ms | Git | 0.25 MB/s | `https://git.669966.xyz` | 通用代理 |
| 465 | 1325ms | Terranor | - | `https://terranor.no` | 通用代理 |
| 466 | 1342ms | Atomgit | - | `https://atomgit.com` | 通用代理 |
| 467 | 1359ms | Docs | 0.01 MB/s | `https://docs.waveshare.net` | 通用代理 |
| 468 | 1367ms | Esa | 0.01 MB/s | `https://esa.console.aliyun.com` | 通用代理 |
| 469 | 1372ms | Jadasite | 0.1 MB/s | `https://jadasite.com` | 通用代理 |
| 470 | 1373ms | Atomcode | 0.07 MB/s | `https://atomcode.atomgit.com` | 通用代理 |
| 471 | 1403ms | Gitlab | 0.01 MB/s | `https://gitlab.phaidra.org` | 通用代理 |
| 472 | 1419ms | Jboltai | 0.05 MB/s | `https://jboltai.com` | 通用代理 |
| 473 | 1439ms | E-stat | 0.1 MB/s | `https://e-stat.go.jp` | 通用代理 |
| 474 | 1447ms | Jinguyuan | - | `https://jinguyuan.cloud` | 通用代理 |
| 475 | 1496ms | Yibiao | 0.08 MB/s | `https://yibiao.pro` | 通用代理 |
| 476 | 1510ms | Teambition | 0.1 MB/s | `https://teambition.com` | 通用代理 |
| 477 | 1511ms | 4kf9kfxujfhg2 | 0.01 MB/s | `https://4kf9kfxujfhg2.space.mcode.cn` | 通用代理 |
| 478 | 1550ms | Tech | - | `https://tech.meituan.com` | 通用代理 |
| 479 | 1608ms | Docs | 0.01 MB/s | `https://docs.cloudbase.net` | 通用代理 |
| 480 | 1612ms | Gitproxy | 0.25 MB/s | `https://gitproxy.127731.xyz` | 通用代理 |
| 481 | 1648ms | I-qps | 0.03 MB/s | `https://i-qps.net` | 通用代理 |
| 482 | 1657ms | Wget | 0.02 MB/s | `https://wget.la` | 通用代理 |
| 483 | 1678ms | Dplayer | 0.04 MB/s | `https://dplayer.diandian.com` | 通用代理 |
| 484 | 1722ms | Tmaxsoft | - | `https://tmaxsoft.com` | 通用代理 |
| 485 | 1735ms | Docs | 0.01 MB/s | `https://docs.volcengine.com` | 通用代理 |
| 486 | 1817ms | GitClone | - | `https://gitclone.com` | Clone 专用 |
| 487 | 2055ms | Adv | 0.01 MB/s | `https://adv.co.jp` | 通用代理 |
| 488 | 2105ms | G | 0.19 MB/s | `https://g.blfrp.cn` | 通用代理 |
| 489 | 2107ms | Clougence | 0.01 MB/s | `https://clougence.com` | 通用代理 |
| 490 | 2148ms | Grafana | - | `https://grafana.nav.cloud.nais.io` | 通用代理 |
| 491 | 2156ms | Infoq | - | `https://infoq.cn` | 通用代理 |
| 492 | 2173ms | Tieba | - | `https://tieba.baidu.com` | 通用代理 |
| 493 | 2254ms | F2bpm | - | `https://f2bpm.com` | 通用代理 |
| 494 | 2254ms | Modelscope | - | `https://modelscope.cn` | 通用代理 |
| 495 | 2275ms | Img | - | `https://img.ink` | 通用代理 |
| 496 | 2321ms | Primeton | 0.02 MB/s | `https://primeton.com` | 通用代理 |
| 497 | 2369ms | Provider | - | `https://provider.com` | 通用代理 |
| 498 | 2399ms | Code | 0.02 MB/s | `https://code.usgs.gov` | 通用代理 |
| 499 | 2419ms | Visionx | 0.02 MB/s | `https://visionx.sibvisions.com` | 通用代理 |
| 500 | 2518ms | Cs | 0.09 MB/s | `https://cs.waikato.ac.nz` | 通用代理 |
| 501 | 2645ms | Gh | 0.28 MB/s | `https://gh.dpik.top` | 通用代理 |
| 502 | 2735ms | Testfather | - | `https://testfather.cn` | 通用代理 |
| 503 | 2760ms | Upyun | - | `https://upyun.com` | 通用代理 |
| 504 | 2874ms | Web | - | `https://web.archive.org` | 通用代理 |
| 505 | 2878ms | Tcl | 0.02 MB/s | `https://tcl.tk` | 通用代理 |
| 506 | 2977ms | Wiki | - | `https://wiki.wocommunity.org` | 通用代理 |
| 507 | 3016ms | Lightlycode | - | `https://lightlycode.com` | 通用代理 |
| 508 | 3035ms | Developer | 0.04 MB/s | `https://developer.jdcloud.com` | 通用代理 |
| 509 | 3065ms | My | - | `https://my.oschina.net` | 通用代理 |
| 510 | 3071ms | Pan | - | `https://pan.quark.cn` | 通用代理 |
| 511 | 3121ms | Informat | 0.01 MB/s | `https://informat.cn` | 通用代理 |
| 512 | 3175ms | Leankg | - | `https://leankg.onrender.com` | 通用代理 |
| 513 | 3568ms | GHProxy MonkeyRay | 0.12 MB/s | `https://ghproxy.monkeyray.net` | 通用代理 |
| 514 | 4479ms | Tongtech | - | `https://tongtech.com` | 通用代理 |
| 515 | 4782ms | Kuaishou | - | `https://kuaishou.com` | 通用代理 |


### ⚠️ 不稳定节点（35 个）

连续失败 1-2 次，暂时不可用，后续测速成功将自动恢复。

| 节点 | 连续失败 |
|------|---------|
| GHFile Geekertao (`ghfile-geekertao-top`) | 2 次 |
| Gh (`gh-idayer-com`) | 2 次 |
| Cf (`cf-ghproxy-cc`) | 10 次 |
| Gh (`gh-1k-ink`) | 17 次 |
| Proxy (`proxy-yaoyaoling-net`) | 3 次 |
| Ampcode (`ampcode-com`) | 19 次 |
| Proxy (`proxy-vvvv-ee`) | 4 次 |
| Axonhub (`axonhub-onrender-com`) | 11 次 |
| Cbrowser (`cbrowser-ai`) | 15 次 |
| Coffeecli (`coffeecli-com`) | 5 次 |
| Demo (`demo-confabulous-dev`) | 8 次 |
| Flashtype (`flashtype-com`) | 22 次 |
| Heycall-e (`heycall-e-com`) | 10 次 |
| Impro (`impro-social`) | 4 次 |
| Mcp-x (`mcp-x-com`) | 1 次 |
| Mobilevc (`mobilevc-top`) | 1 次 |
| Opensunsama (`opensunsama-com`) | 25 次 |
| Vibetrading (`vibetrading-wiki`) | 23 次 |
| Weaverse (`weaverse-io`) | 7 次 |
| Weishucdn (`weishucdn-jiangjiangze-icu`) | 14 次 |
| You (`you-piccalc-com`) | 12 次 |
| Adult (`adult-contents-fc2-com`) | 8 次 |
| Git (`git-net2o-de`) | 25 次 |
| Proxy (`proxy-scdn-io`) | 3 次 |
| Gh (`gh-ddlc-top`) | 5 次 |
| Github (`github-dpik-top`) | 5 次 |
| 5555 (`5555-cab`) | 5 次 |
| Bestofbi (`bestofbi-com`) | 12 次 |
| Gitlab (`gitlab-pasteur-fr`) | 25 次 |
| Shopjsp (`shopjsp-com`) | 2 次 |
| Jwebmp (`jwebmp-com`) | 1 次 |
| 104 (`104-com-tw`) | 21 次 |
| Bsr (`bsr-twse-com-tw`) | 17 次 |
| Mopsov (`mopsov-twse-com-tw`) | 17 次 |
| Wiki (`wiki-easyrpg-org`) | 12 次 |

## 节点分类

| 分类 | 数量 | 用途 |
|------|------|------|
| `universal_proxy` | 543 | 通用，支持 release/archive/blob/raw/clone |
| `web_mirror` | 1 | GitHub 网页完整镜像，可直接浏览 |
| `clone_specialized` | 1 | 仅 git clone 加速 |
| `cdn_raw` | 5 | CDN 加速，仅 raw/blob 小文件 |
| **合计** | **550** | |

已失效节点历史档案见 [graveyard.json](graveyard.json)（64 个）。

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
