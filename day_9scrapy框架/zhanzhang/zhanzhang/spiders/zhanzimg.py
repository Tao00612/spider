import scrapy
from zhanzhang.items import ZhanzhangItem

class ZhanzimgSpider(scrapy.Spider):
    name = 'zhanzimg'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response, **kwargs):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            item = ZhanzhangItem()
            # 在解析的时候要使用伪属性
            src = div.xpath('./div/a/img/@src2').extract_first()
            item['src'] = src

            yield item
