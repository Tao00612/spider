# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep
class WangyiproDownloaderMiddleware:

    def process_request(self, request, spider):

        return None

    # 通过该方法拦截5大板块对应的响应对象,进行篡改
    def process_response(self, request, response, spider):# spider 爬虫对象
        bro = spider.bro # 获取了在爬虫类中的定义的浏览器对象
        # 挑选出指定的响应对象进行篡改
        # 通过url来指定request
        # 通过request指定response
        if request.url in spider.models_urls:
            bro.get(request.url) # 对5个板块对应的url进行请求发送
            sleep(3)
            page_text = bro.page_source # 包含了动态加载的新闻数据
            # response # 5大板块的对应
            # 针对定位到的response进行篡改
            # 实例化一个新的响应对象(符合需求:包含动态加载的新闻数据),替代原来响应对象
            # 如何获取动态加载出的新闻数据
                # 基于selenium便捷的获取动态加载数据
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)

            return new_response
        else:
            # response
            return response

    def process_exception(self, request, exception, spider):

        pass


