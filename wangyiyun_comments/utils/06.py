# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/8 19:50
@Desc     : 
"""
import requests
import time


target_url = "https://music.163.com/"

proxyHost = "121.205.208.134"
proxyPort = 40012

proxyMeta = "http://%(host)s:%(port)s" % {

"host": proxyHost,
"port": proxyPort,
}
proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}
response = requests.get(target_url, proxies=proxies, timeout=10)
print(response.text)

