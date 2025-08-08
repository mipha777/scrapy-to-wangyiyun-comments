# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/5 20:35
@Desc     : 使用 execjs 调用 JS 加密函数
"""
import os
import execjs
import json
def get_p_e(song_commentThreadId):
    js_dict = {
        "rid": song_commentThreadId,
        "threadId": song_commentThreadId,
        "pageNo": "1",
        "pageSize": "700", # 这里设置每首歌爬取多少条评论  如果歌曲评论数量少于这个值 也不会异常
        "cursor": "-1",
        "offset": "0",
        "orderType": "1",
        "csrf_token": ""
    }
    json_str = json.dumps(js_dict)
    base_dir = os.path.dirname(os.path.abspath(__file__)) # 获取当前目录
    js_path = os.path.join(base_dir, 'encrypt.js')

    with open(js_path, 'r', encoding='utf-8') as f:
        js_code = f.read()

    p_e = execjs.compile(js_code)
    params = p_e.call('get_params_encSecKey',json_str)
    params_key = params[0]
    encSecKey = params[1]
    return params_key, encSecKey

