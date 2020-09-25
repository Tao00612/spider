import scrapy
from xiaohuaPro.items import XiaohuaproItem

class XhSpider(scrapy.Spider):
    name = 'xh'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']

    # 生成一个通用的url模板(不可变)
    url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 2

    def parse(self, response, **kwargs):
        list_li = response.xpath('//div[@class="index_img list_center"]/ul/li')
        for li in list_li:
            title = li.xpath('./a[2]/text() | ./a[1]/img/@alt').extract_first()
            item = XiaohuaproItem()
            item['title'] = title
            yield item

        if self.page_num <= 11:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动请求发送 callback 回调函数是专门用作于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
