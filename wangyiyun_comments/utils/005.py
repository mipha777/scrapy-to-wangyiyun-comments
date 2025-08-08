# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/8 19:38
@Desc     : 
"""
import requests
import json
url = 'http://api.shenlongip.com/ip?key=1mq6p9&protocol=2&mr=1&pattern=json&need=1001&count=2&sign=9dcb467e7'

response = requests.get(url)
res = json.loads(response.text)
for i in res['data']:
    print(i['ip'])
    print(i['port'])