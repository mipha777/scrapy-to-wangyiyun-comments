# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/8 18:34
@Desc     : 代理ip获取与处理
"""

import json
import random

import requests

#
class ProxyPool:
    def __init__(self, api_url):
        self.api_url = api_url
    def fetch_proxies(self):
        response = requests.get(self.api_url,timeout=10)
        if response.status_code == 200:
            proxy_list = []
            res = response.json()
            print('已经获取代理池{}'.format(res))
            for i in res['data']:
                proxyMeta = f'https://{i["ip"]}:{i["port"]}'
                proxy_list.append(proxyMeta)
            print('代理池已经更新')
            return proxy_list
        else:
            print("代理API请求失败", response.status_code)
            return []


if __name__ == '__main__': # 测试入口
    # 测试代理文件这里的返回值 以及代理能不能用
    p = ProxyPool(api_url='http://api.shenlongip.com/ip?key=1m6p9&protocol=2&mr=1&pattern=json&need=1000&count=3&sign=f53ccb4b54')  #自己的api提取连接
    list = p.fetch_proxies()
    print(list) # 以及网站的相应结构  不同的网站的代理 给ip的方式不一样
    proxy = random.choice(list)
    resp = requests.get( url='https://music.163.com/discover/toplist?id=3779629',proxies=proxy,timeout=10)
    print(resp.text)
