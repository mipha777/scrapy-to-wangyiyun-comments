# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiyunTOPItem(scrapy.Item):
    toplist_name = scrapy.Field()
    toplist_id = scrapy.Field()


class WangyiyunSONGItem(scrapy.Item):
    # define the fields for your item here like:
    songname = scrapy.Field()
    songid = scrapy.Field()
    songs_url = scrapy.Field()
    singer = scrapy.Field()
    toplist_id = scrapy.Field() # 外键链接榜单名

class WangyiyunCOMMENTSItem(scrapy.Item):
    comment_name = scrapy.Field()
    comment_ip = scrapy.Field()
    comment_content = scrapy.Field()
    songid = scrapy.Field()# 外键链接歌曲id
