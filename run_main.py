# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/7 16:16
@Desc     : 主程序文件
"""
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from wangyiyun_comments.spiders.wangyi import WangyiSpider  



#   主运行文件
def run():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(WangyiSpider)
    process.start()

if __name__ == '__main__':
    run()
