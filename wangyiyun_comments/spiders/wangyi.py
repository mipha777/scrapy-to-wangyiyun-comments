
import scrapy
import json
import random
from bs4 import BeautifulSoup
from ..items import WangyiyunTOPItem,WangyiyunSONGItem,WangyiyunCOMMENTSItem
from ..js.crypto_js import get_p_e


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    allowed_domains = ["music.163.com"]
    start_urls = ["https://music.163.com/discover/toplist"]
    fk_list_url=[
        'https://music.163.com/artist?id=3684',
        'https://music.163.com/artist?id=10559',
        'https://music.163.com/artist?id=2116',
        'https://music.163.com/artist?id=6460',
        'https://music.163.com/artist?id=5346',
        'https://music.163.com/artist?id=6452',
        'https://music.163.com/artist?id=5771',
        'https://music.163.com/artist?id=1091',
        'https://music.163.com/album?id=75097',
        'https://music.163.com/album?id=35534',
        'https://music.163.com/album?id=81590',
        'https://music.163.com/album?id=123456',
        'https://music.163.com/album?id=456789'

    ]
    # 对应榜单的类型映射 # 这个倒是可以写进setting
    list_map = {
        '3778678': '热歌榜',
        '3779629': '新歌榜',
        '2884035': '原创榜',
        '19723756': '飙升榜',
        '1978921795':'电音榜',
        '71384707':'古典榜'
    }
    def start_requests(self):

        for toplist_id,toplist_name in self.list_map.items():
            url = "https://music.163.com/discover/toplist?id={}".format(toplist_id)
            print(f"数据库即将写入{toplist_id}")
            yield WangyiyunTOPItem(toplist_name=toplist_name, toplist_id=toplist_id)

            # 模拟随机访问其他路径
            if random.random() < 0.3:  # 本分之30概率插入一个假的访问
                fake_url = random.choice(self.fk_list_url)
                self.logger.info(f"模拟用户顺便访问: {fake_url}")
                yield scrapy.Request(fake_url, callback=self.fake_parse,errback=self.errback)
            print('即将访问歌单内的歌曲')
            yield scrapy.Request(url=url, callback=self.parse,errback=self.errback,meta={"toplist_id": toplist_id},dont_filter=True)

    def errback(self, failure):
        self.logger.error(f"请求失败：{repr(failure)}")

    def parse(self, response,**kwargs):
        # 歌曲解析方法
        toplist_id = response.meta["toplist_id"]
        self.logger.info(f"parse回调: {toplist_id}")
        soup = BeautifulSoup(response.text, 'html.parser')
        json_text = soup.find(id="song-list-pre-data").text.strip()
            # 真歌曲解析方法
        all_song_json = json.loads(json_text)
        for song in all_song_json:
            songid = song['id']
            songname = song['name']
            song_commentThreadId = song['commentThreadId'] # 评论的id
            songs_url = f'https://music.163.com/song?id={songid}' # 不用访问这个
            singer = " / ".join([artist['name'] for artist in song['artists']])
            # 送入管道 保存到数据库
            yield WangyiyunSONGItem(songid=songid, songname=songname, songs_url=songs_url,singer=singer,toplist_id=toplist_id)

            # 模拟随机访问其他路径
            if random.random() < 0.3:  # 30概率插入一个假的访问
                fake_url = random.choice(self.fk_list_url)
                self.logger.info(f"模拟用户顺便访问: {fake_url}")
                yield scrapy.Request(fake_url, callback=self.fake_parse)

            # 获取加密参数
            params_key,encSecKey = get_p_e(song_commentThreadId)
            # 评论链接
            comment_url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
            yield scrapy.FormRequest(url=comment_url,
                                     callback=self.comments_parse,
                                     formdata={'params': params_key,'encSecKey': encSecKey},
                                     meta={"songid": songid} # 参数=给下一个函数使用
                                     )

    def comments_parse(self,response,**kwargs):
        # 评论解析方法
        songid = response.meta["songid"]
        res = json.loads(response.text)
        comments = res.get('data', {}).get('comments', [])
        # hot_comments = res.get('data', {}).get('hotComments', [])
        for i in comments:
            comment_name = i.get("user", {}).get("nickname", "None") # 瑞平人
            comment_ip = i.get("ipLocation", {}).get("location", "None") # 地址
            comment_content = i.get("content", "None") # 发言内容

            yield WangyiyunCOMMENTSItem(comment_name= comment_name, comment_ip=comment_ip, comment_content=comment_content,songid=songid)

    def fake_parse(self, response):
        pass