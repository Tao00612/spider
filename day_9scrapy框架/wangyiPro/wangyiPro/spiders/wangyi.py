import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_urls = []  # 存储5个板块的详情页url

    # 实例化一个浏览器对象
    def __init__(self):
        # super(scrapy.Spider,self).__init__()
        self.bro = webdriver.Chrome(executable_path='F:\爬虫日记\day_9scrapy框架\chromedriver.exe')

    # 解析五大板块对应的详情页的url
    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        a_list = [3, 4, 6, 7, 8]
        for index in a_list:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            print(model_url)
            self.models_urls.append(model_url)
        for url in self.models_urls:
            yield scrapy.Request(url=url, callback=self.parse_model)

    # 每一个板块的新闻都是动态加载的
    def parse_model(self, response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href | ./a/@href').extract_first()
            item = WangyiproItem()
            item['title'] = title
            # 对新闻详情页的url发起请求
            print(new_detail_url)
            yield scrapy.Request(url=new_detail_url, callback=self.parse_detail, meta={'item': item})

    # 解析详情页的内容
    def parse_detail(self,response):
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content

        yield item

    def close(spider, reason):
        spider.bro.quit()