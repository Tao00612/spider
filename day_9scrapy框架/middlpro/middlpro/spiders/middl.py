import scrapy


class MiddlSpider(scrapy.Spider):
    # 爬取百度
    name = 'middl'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.baidu.com/s?wd=ip&tn=78040160_5_pg&ch=8']

    def parse(self, response,**kwargs):
        page_text = response.text()
        with open('ip.html','w',encoding='utf-8') as f:
            f.write(page_text)