# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/7 20:29
@Desc     : 
"""
import requests

# 代理设置（格式：协议://用户名:密码@IP:端口）
proxies = {
    'http': 'http://d2052301536:65px030u@58.19.54.131:27308',
    'https': 'http://d2052301536:65px030u@58.19.54.131:27308'
}

url = "https://music.163.com/discover/toplist?id=19723756"

headers = {
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'priority': 'u=0, i',
    # 'referer': 'https://music.163.com/',
    # 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'iframe',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'same-origin',
    # 'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
    # 'cookie': '_iuqxldmzr_=32; _ntes_nnid=5c0389f2da175ff1b5a349c3f7dc95e6,1750248409523; _ntes_nuid=5c0389f2da175ff1b5a349c3f7dc95e6; NMTID=00OsWWQT_VfqvjWrkSZvWnu1ukcR0oAAAGXgu9KAQ; WEVNSM=1.0.0; WNMCID=buhkkv.1750248410579.01.0; WM_TID=kjGGF3XcvG9EBBFBUFPHP5QdqLt3WSl%2B; ntes_utid=tid._.gp9K7H2yHtRBB0ABVAaDK4Ecve9nHaDA._.0; sDeviceId=YD-BfELbQuW0t9AVgBABQaHesQJ%2BLtiHbSU; timing_user_id=time_kGg41iMvux; _clck=pmrjc8%7C2%7Cfxx%7C0%7C2033; _ga=GA1.1.1363078823.1753544141; _ga_C6TGHFPQ1H=GS2.1.s1753559512$o3$g0$t1753559512$j60$l0$h0; __snaker__id=r4TUmxvxTbi0BYM7; gdxidpyhxdE=ccL3ZmgI6f6nJwB5m4PmMxoc4oH8oidSC2a4wAAps0PaWqchE31jeNN8BKJn1W2V%2B7W9V%5CBpHTSC%5Cd9%2Fs7%2F0OA5Nil%5CX2shBmStQfBk2ISK4CzqZJtfXBrUME%2BmQYqX6zwm93a9P8x16kBI84elgtXfIWUg5HbEwOt9RqlqK3vEDEkT3%3A1754390802315; WM_NI=KPouUTqQ848bNVJZwqiNKwUZdYeMJxLdSNF3V%2BtdlfWYrh37M%2F8CxAomZ2YJ5S98rgHsEsks1JFSPziuMKgjuBIMu01ZT64tgyQbv5YduQILrnqiCue3thMO6Jk%2BgtXXYlc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed7d640abbaae87ce6e82e78ba6d44b979f8b86d23c8e8aaed4b8499a86ac89c22af0fea7c3b92a8990a196d860b38ff8d5bb6a8e8a86bbf67bab928598d852a887abaec97490bc9dafc53996f5bc85ef6e9587be89b23d8ff1f8a4fb4badb396d3dc42f78df7d9f16d8cad8b94ea79f3968ab4d372abab83ace662b79e87aef83cf3869cd7b780a5a79f83f53f9bbcbbb2cc48b2b2bf8ac27fa7edbc89d045f696a5cce6809c88978de237e2a3; JSESSIONID-WYYY=cmgVowIukrayQHII51HErWkzWv%2FbP6lJ1dKuulcT2BGpNYdBiGUXRpO8%2FgxU2cezB%2BAg3Q8uq4BE%5CAdmR4hBoWAKZkF2aHfIX20la8S%2FSirx4qoB6HsoPk%2BaOCzV%2BC1KHuBNzrM%2BQR1Rl3gzH54j6mhyyOb%2FaxBJZwj8EKs%2BMf6OgFDX%3A1754561852910',
}
res = requests.get(url, headers=headers)
if '此生不' in res.text:
    print('666')
    print(res.text)
