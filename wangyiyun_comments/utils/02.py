import requests

cookies = {
    '_ntes_nnid': 'b9929e671a0c5d00f0f0ef8475f86e73,1753785264977',
    '_ntes_nuid': 'b9929e671a0c5d00f0f0ef8475f86e73',
    'NMTID': '00OGB0USzNOd0QxHEtAgpN8v2UW5q8AAAGYVb9osA',
    'WEVNSM': '1.0.0',
    'WNMCID': 'pkalun.1753785266103.01.0',
    'WM_TID': 'TYeaEZKe%2FsBBAEUBUALXkSJznu556ARO',
    'sDeviceId': 'YD-%2BqhUC3P6%2F4NFQkRUEBfCkTJzjr8%2FCMDT',
    '__snaker__id': 'Jq562J2MhXS7dlLc',
    'ntes_kaola_ad': '1',
    '_iuqxldmzr_': '32',
    'ntes_utid': 'tid._.H5VVJc8vUABERwVBEUeClWd2jus7HSlZ._.0.%2C.edd._.._.0',
    'gdxidpyhxdE': 'rgXw1cERY8dygI5zG17XD4z1owtqTe4oyY9zTs8SLLguNx%2BbcX%2F1N7K7EDDl5%2Fa9GTGlBIe0zEy51CtI7%2BRdX0c0IQLZu2DvDAS4ipLzjr%5Cgz0YVrruzyVXWeMUjPsJUVpxX7yo%2BJodzm7QL93JpVUbkOZH%5CpjXUE1T8O%2FARNcQ91oHj%3A1754503667593',
    'WM_NI': 'V1DPZn5xEUw8BISWAtJIgG5DW%2Ba5FyogFhnTZjK5fmWCDL7A0mtfAg4v0ysPKHcqewpjSeaU1Z8akV39gRMl7sXsBUDgRuU5jr4TPGv7kM4aC93D9pleAQi41RZyzv%2FkY2c%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eea2ec5cbc9b8fa9c27eb0968eb2c85e838a8e83d6648e8f818dee5fadbe96aee62af0fea7c3b92a96ef8cb1d966f7a88bb6f63482979db8c4808a97a9a8b85095f5afd6c573adb98a89ed609ab685d6e567959d8cadb64bf4b3bc87c46df8aa009af25c8998ad92e87db4b69d86e45ff386f882ea5ef1e7a9b3d068f5ad9894c15f88b99e96d83faaaefcb5d34db6e9a5aeb76b81e7fda5bc7cb0bb8fb2ec40f38e969af97eedb597d3e237e2a3',
    'JSESSIONID-WYYY': 'yylcRP%2BlGYyqsZORhhZFBKhz56De8F%2BCgXIvjOaDYyo6a4ICYStUHSykgdsCEPItB%5C7FbJmlmSnGxBX5ZepN34%2FigC6g7VNHJhTfj0nQMoDNVIAXpD9ioOEc7oWU2AqQustbYlwme42t7E01m5XGX2McBnw4GRqSyyNxM4%5Ci9N%5CaJlxe%3A1754582415012',
}

headers = {
    # 'accept': '*/*',
    # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'content-type': 'application/x-www-form-urlencoded',
    # 'origin': 'https://music.163.com',
    # 'priority': 'u=1, i',
    # 'referer': 'https://music.163.com/song?id=2731384240',
    # 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '_ntes_nnid=b9929e671a0c5d00f0f0ef8475f86e73,1753785264977; _ntes_nuid=b9929e671a0c5d00f0f0ef8475f86e73; NMTID=00OGB0USzNOd0QxHEtAgpN8v2UW5q8AAAGYVb9osA; WEVNSM=1.0.0; WNMCID=pkalun.1753785266103.01.0; WM_TID=TYeaEZKe%2FsBBAEUBUALXkSJznu556ARO; sDeviceId=YD-%2BqhUC3P6%2F4NFQkRUEBfCkTJzjr8%2FCMDT; __snaker__id=Jq562J2MhXS7dlLc; ntes_kaola_ad=1; _iuqxldmzr_=32; ntes_utid=tid._.H5VVJc8vUABERwVBEUeClWd2jus7HSlZ._.0.%2C.edd._.._.0; gdxidpyhxdE=rgXw1cERY8dygI5zG17XD4z1owtqTe4oyY9zTs8SLLguNx%2BbcX%2F1N7K7EDDl5%2Fa9GTGlBIe0zEy51CtI7%2BRdX0c0IQLZu2DvDAS4ipLzjr%5Cgz0YVrruzyVXWeMUjPsJUVpxX7yo%2BJodzm7QL93JpVUbkOZH%5CpjXUE1T8O%2FARNcQ91oHj%3A1754503667593; WM_NI=V1DPZn5xEUw8BISWAtJIgG5DW%2Ba5FyogFhnTZjK5fmWCDL7A0mtfAg4v0ysPKHcqewpjSeaU1Z8akV39gRMl7sXsBUDgRuU5jr4TPGv7kM4aC93D9pleAQi41RZyzv%2FkY2c%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea2ec5cbc9b8fa9c27eb0968eb2c85e838a8e83d6648e8f818dee5fadbe96aee62af0fea7c3b92a96ef8cb1d966f7a88bb6f63482979db8c4808a97a9a8b85095f5afd6c573adb98a89ed609ab685d6e567959d8cadb64bf4b3bc87c46df8aa009af25c8998ad92e87db4b69d86e45ff386f882ea5ef1e7a9b3d068f5ad9894c15f88b99e96d83faaaefcb5d34db6e9a5aeb76b81e7fda5bc7cb0bb8fb2ec40f38e969af97eedb597d3e237e2a3; JSESSIONID-WYYY=yylcRP%2BlGYyqsZORhhZFBKhz56De8F%2BCgXIvjOaDYyo6a4ICYStUHSykgdsCEPItB%5C7FbJmlmSnGxBX5ZepN34%2FigC6g7VNHJhTfj0nQMoDNVIAXpD9ioOEc7oWU2AqQustbYlwme42t7E01m5XGX2McBnw4GRqSyyNxM4%5Ci9N%5CaJlxe%3A1754582415012',
}


data = {
    'params': 'ZClivKqu+2l/iir8mWde9Uzls4grZf9K9IerBPsQhf1yIJM6KzceiHvmKO4IZbCs3U+Q+GY7cPvHoBDwsSXolyJHilBQ/gok5x8E7KDFJhBvajeV7Abg+CWqTGe1CXiiJwmuqJj2nYNhhGAhcSGxFghjFiJ/oXunMW+JD4JxxQrAVZNJ3xAePWkcRDVYBaMsJv+ADPlCqwjkDnKrmz0HxMj/vl2BsO/Zl+fQ6ZyqF40EqCx30vo9FpfWJVcnoQlGsyWorZQnUDkEH7ZXHAd+pQkyx06KSJcKo6KWHonszmw=',
    'encSecKey': '116c3a94ea5c2f91e580371af8ee84c0a6808caf291941b781903a3055f77b5e5bf95bfea1917776106c8eff10594a1e8a50120fffa7cded62539a63bc013095e1b081731151946380c42826ad09bd69ea1ce0779a069aa27f1a249ed12974b6a120e28efc5fbbdf94be068ef833d79d8d4c0b701942a14773e013d699f83d5c',
}

response = requests.post(
    'https://music.163.com/weapi/comment/resource/comments/get',
    cookies=cookies,
    headers=headers,
    data=data,
)
print(len(response.text))
print(response.text)