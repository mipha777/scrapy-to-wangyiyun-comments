# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from requests_toolbelt import user_agent
from scrapy import signals
import random
import base64
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WangyiyunCommentsSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    async def process_start(self, start):
        # Called with an async iterator over the spider start() method or the
        # maching method of an earlier spider middleware.
        async for item_or_request in start:
            yield item_or_request

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class WangyiyunCommentsDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # request.meta['proxy'] = ''
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



# 自定义请求头中间键

class MyHeadersMiddleware:
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        user_agents = crawler.settings.getlist('USER_AGENTS')  # getlist 获取列表
        return cls(user_agents)

    def process_request(self,request,spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)
        request.headers['referer'] = 'https://music.163.com/',
        request.headers['accept-language'] ='zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',


from .proxy_Pool import ProxyPool
from scrapy.utils.project import get_project_settings
import threading
# zidingyi代理中间件 使用代理 清除被封的代理
class MyProxyMiddleware:
    def __init__(self):
        settings = get_project_settings()
        api_url = settings.get('API_URL')
        if not api_url:
            raise ValueError("请确认settings.py中已配置 API_URL")
        self.Proxy_tool = ProxyPool(api_url)
        self.proxies = []
        self.lock = threading.RLock()
        self.min_size = 3
        self._init_proxies()
        self.fail_counts = {}

    def _init_proxies(self):
        #启动时调用代理池
        self.proxies = self.Proxy_tool.fetch_proxies()

    def _ensure_proxies(self):
        # 代理池数量低时补充代理
        with self.lock:
            if len(self.proxies) < self.min_size:
                print('代理不足 正在补充')
                new_proxies = self.Proxy_tool.fetch_proxies()
                for p in new_proxies:
                    if p not in self.proxies:
                        self.proxies.append(p)

    def get_random_proxy(self):
        # 随机选择一个ip
        with self.lock:
            self._ensure_proxies()
            if not self.proxies:
                return None
            return random.choice(self.proxies)

    def process_request(self,request,spider):
        #请求前设置代理
        proxy = self.get_random_proxy()
        if proxy:
            request.meta['proxy'] = proxy
        else:
            spider.logger.warning("代理q全部被封禁，而且没有进行补充")

    def process_response(self, request, response, spider):
        # 请求后的代理处理
        ban_proxy = request.meta.get('proxy')
        if response.status in [403, 429, 500, 502, 503, 504,404]:
            ban_proxy = request.meta.get('proxy')
            self.fail_counts[ban_proxy] = self.fail_counts.get(ban_proxy, 0) + 1
            if self.fail_counts[ban_proxy] >= 3:
                self.remove_proxy(ban_proxy)
                spider.logger.warning(f"删除封禁代理: {ban_proxy}")
                self.fail_counts.pop(ban_proxy)
            # 重新发起请求（会自动换代理）
            new_request = request.copy()
            new_request.dont_filter = True
            new_request.callback = request.callback
            return new_request
        else:
            # 成功请求，重置失败计数
            if ban_proxy in self.fail_counts:
                self.fail_counts.pop(ban_proxy)
            return response



    def remove_proxy(self, proxy):
        # 删除被封禁的
        with self.lock:
            if proxy in self.proxies:
                self.proxies.remove(proxy)

    def process_exception(self, request, exception, spider):
        # 请求异常时也删除代理
        ban_proxy = request.meta.get('proxy')
        if ban_proxy in self.proxies:
            self.remove_proxy(ban_proxy)
            spider.logger.warning(f"请求异常，删除代理: {ban_proxy}")
        new_request = request.copy()
        new_request.dont_filter = True
        return new_request

