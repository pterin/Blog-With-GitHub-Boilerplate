# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "VFxlyAoXejJvRTMb4KX8okfN-MdYXbMMI",
    "appKey": "RH2THTEkeHQFee8QcLPy8l09",
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "pterin/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "PTERIN"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Pterin"
email = ""
author_homepage = ""
description = ""
key_words = ['Maverick', 'Pterin', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "",
        "url": "",
        "brief": ""
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
