# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/9 01:42
@Desc     : 
"""
import requests

cookies = {
    '_iuqxldmzr_': '32',
    '_ntes_nnid': '5c0389f2da175ff1b5a349c3f7dc95e6,1750248409523',
    '_ntes_nuid': '5c0389f2da175ff1b5a349c3f7dc95e6',
    'NMTID': '00OsWWQT_VfqvjWrkSZvWnu1ukcR0oAAAGXgu9KAQ',
    'WEVNSM': '1.0.0',
    'WNMCID': 'buhkkv.1750248410579.01.0',
    'WM_TID': 'kjGGF3XcvG9EBBFBUFPHP5QdqLt3WSl%2B',
    'ntes_utid': 'tid._.gp9K7H2yHtRBB0ABVAaDK4Ecve9nHaDA._.0',
    'sDeviceId': 'YD-BfELbQuW0t9AVgBABQaHesQJ%2BLtiHbSU',
    'timing_user_id': 'time_kGg41iMvux',
    '_clck': 'pmrjc8%7C2%7Cfxx%7C0%7C2033',
    '_ga': 'GA1.1.1363078823.1753544141',
    '_ga_C6TGHFPQ1H': 'GS2.1.s1753559512$o3$g0$t1753559512$j60$l0$h0',
    '__snaker__id': 'r4TUmxvxTbi0BYM7',
    'gdxidpyhxdE': 'ccL3ZmgI6f6nJwB5m4PmMxoc4oH8oidSC2a4wAAps0PaWqchE31jeNN8BKJn1W2V%2B7W9V%5CBpHTSC%5Cd9%2Fs7%2F0OA5Nil%5CX2shBmStQfBk2ISK4CzqZJtfXBrUME%2BmQYqX6zwm93a9P8x16kBI84elgtXfIWUg5HbEwOt9RqlqK3vEDEkT3%3A1754390802315',
    'WM_NI': 'CGPhdRngh%2Fj%2FLDvPPq2OZJbjm1sTukSrKbL4pABOTSzze8wACz9j6wGC66%2Bs8DpU%2FARanhKQ9lDDE1daYzx%2FruklFjorVDKSBPuwKvIbHkYoagi9yvm19ksz6833PrWgVk0%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeabbc7e989e8aabed43b28e8ab6d14a929a9aacdb648e889a97d67095b6afaaf92af0fea7c3b92a8199a089e75aaeb9a8d0e925909cbab1d37bf29196abe162afefbdb5f86191ae8583cf40b49f8eb0d759baa6abd9f64b81a6f78bb57d859dfad7aa79fc9cc0b6ae4b92bfa289ca5bfbb48ca5c83ba8bf979bfb25b2aba58dc562adae9aa5ca598290bb98ca7e8bbe888cdc65a3b9a7dafc7eafeff78cf272f6e8fdd4d37a95b99a8cb337e2a3',
    'JSESSIONID-WYYY': '5oXCBzltwfaBgAAjmKJhRvk%2BVobTjYP8BrrnQzxCYqzaXnQY5CFK5r%5C9a%2BdNU4ZglGkn1CmtDWWxfc7ePoH2DpwwcoudEmF7Z31s6JKJ5jCdFx5K25Tn7idvjSpJXHJ5D02Nts4OVvnBDf%2BjKlE92s%5Cv9GxC7I6vCrayDcOa0QAArahm%3A1754676030558',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'priority': 'u=0, i',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
    # 'cookie': '_iuqxldmzr_=32; _ntes_nnid=5c0389f2da175ff1b5a349c3f7dc95e6,1750248409523; _ntes_nuid=5c0389f2da175ff1b5a349c3f7dc95e6; NMTID=00OsWWQT_VfqvjWrkSZvWnu1ukcR0oAAAGXgu9KAQ; WEVNSM=1.0.0; WNMCID=buhkkv.1750248410579.01.0; WM_TID=kjGGF3XcvG9EBBFBUFPHP5QdqLt3WSl%2B; ntes_utid=tid._.gp9K7H2yHtRBB0ABVAaDK4Ecve9nHaDA._.0; sDeviceId=YD-BfELbQuW0t9AVgBABQaHesQJ%2BLtiHbSU; timing_user_id=time_kGg41iMvux; _clck=pmrjc8%7C2%7Cfxx%7C0%7C2033; _ga=GA1.1.1363078823.1753544141; _ga_C6TGHFPQ1H=GS2.1.s1753559512$o3$g0$t1753559512$j60$l0$h0; __snaker__id=r4TUmxvxTbi0BYM7; gdxidpyhxdE=ccL3ZmgI6f6nJwB5m4PmMxoc4oH8oidSC2a4wAAps0PaWqchE31jeNN8BKJn1W2V%2B7W9V%5CBpHTSC%5Cd9%2Fs7%2F0OA5Nil%5CX2shBmStQfBk2ISK4CzqZJtfXBrUME%2BmQYqX6zwm93a9P8x16kBI84elgtXfIWUg5HbEwOt9RqlqK3vEDEkT3%3A1754390802315; WM_NI=CGPhdRngh%2Fj%2FLDvPPq2OZJbjm1sTukSrKbL4pABOTSzze8wACz9j6wGC66%2Bs8DpU%2FARanhKQ9lDDE1daYzx%2FruklFjorVDKSBPuwKvIbHkYoagi9yvm19ksz6833PrWgVk0%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeabbc7e989e8aabed43b28e8ab6d14a929a9aacdb648e889a97d67095b6afaaf92af0fea7c3b92a8199a089e75aaeb9a8d0e925909cbab1d37bf29196abe162afefbdb5f86191ae8583cf40b49f8eb0d759baa6abd9f64b81a6f78bb57d859dfad7aa79fc9cc0b6ae4b92bfa289ca5bfbb48ca5c83ba8bf979bfb25b2aba58dc562adae9aa5ca598290bb98ca7e8bbe888cdc65a3b9a7dafc7eafeff78cf272f6e8fdd4d37a95b99a8cb337e2a3; JSESSIONID-WYYY=5oXCBzltwfaBgAAjmKJhRvk%2BVobTjYP8BrrnQzxCYqzaXnQY5CFK5r%5C9a%2BdNU4ZglGkn1CmtDWWxfc7ePoH2DpwwcoudEmF7Z31s6JKJ5jCdFx5K25Tn7idvjSpJXHJ5D02Nts4OVvnBDf%2BjKlE92s%5Cv9GxC7I6vCrayDcOa0QAArahm%3A1754676030558',
}

params = {
    'id': '991319590',
}

response = requests.get('https://music.163.com/discover/toplist', params=params, cookies=cookies, headers=headers)

print(response.text)