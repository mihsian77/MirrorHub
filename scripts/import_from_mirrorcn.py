#!/usr/bin/env python3
"""从 AClon314/mirror-cn 导入节点，分类整理为 MirrorHub 格式"""
import json
import re
import urllib.request

# 拉取 mirror-cn 的节点配置
url = "https://raw.githubusercontent.com/AClon314/mirror-cn/refs/heads/main/src/mirror_cn/mirror_cn.py"
content = urllib.request.urlopen(url, timeout=15).read().decode("utf-8")

# 提取所有 GitHub 相关的代理 URL
raw_urls = re.findall(r'"(https?://[^\"]+)"', content)
github_urls = []
seen = set()
for u in raw_urls:
    if any(k in u.lower() for k in ['github', 'ghproxy', 'gh-proxy', 'fastgit', 'gitclone',
                                       'jsdelivr', 'kkgithub', 'bgithub', 'cnpmjs', 'moeyy',
                                       'ghfast', 'gitmirror', 'slink', 'sciproxy', 'isteed',
                                       'crashmc', 'muran', 'idayer', 'monkeyray', 'nxnow',
                                       'zwy', 'xx9527', 'chenby', 'ednovas', 'geekertao',
                                       'keleyaa', 'wuzhij', 'chjina', 'hwinzniej', 'yylx',
                                       'mrhjx', 'cxkpro', 'xxooo', 'xiaopa', '944446',
                                       'limoruirui', 'zwnes', 'npee', 'ygxz', 'linioi',
                                       'lxstd', 'jasonzeng', 'monlor', '862510', 'h233',
                                       '1888866', 'ddlc', 'fangkuai', 'dpik', '3x25',
                                       'akams', 'acmsz', 'cmsz', 'class3', 'lixxing',
                                       'tbedu', 'whrstudio', 'boki', 'cfd', 'ihtw']):
        # 清理 URL：去掉路径部分，只保留域名
        clean = re.sub(r'/(https?://github\.com.*)$', '', u)
        clean = re.sub(r'/\?https?://github\.com.*$', '', clean)
        clean = clean.rstrip('/')
        if clean not in seen and 'github.com' not in clean.split('/')[2] if len(clean.split('/')) > 2 else True:
            seen.add(clean)
            github_urls.append(clean)

print(f"提取到 {len(github_urls)} 个节点域名")
for u in sorted(github_urls):
    print(f"  {u}")
