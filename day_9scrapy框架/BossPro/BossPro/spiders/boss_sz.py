import scrapy
from BossPro.items import BossproItem

class BossSzSpider(scrapy.Spider):
    name = 'boss_sz'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101280600']
    url = 'xx.com  %d'
    page_num = 1
    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        for li in li_list:
            item = BossproItem()
            job_name = li.xpath('.//span[@class="job-name"]/text()').extract_first()
            print(job_name)
            item['job_name'] = job_name
            deltail_url = 'https://www.zhipin.com/' + li.xpath('.//span[@class="job-name"]/@href').extract_first()
            # 对详情页发请求,获取详细页的页面数据
            # 手动请求的发送
            # 请求传参  meta = {} 可以将meta字典传递给对应的回调函数
            yield scrapy.Request(deltail_url, callback=self.parse_det,meta={'item':item})
            break

        # 分页操作
        if self.page_num <= 11:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)

    # 会调函数接收item
    def parse_det(self, response, **kwargs):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        print(job_desc)
        item['job_desc'] = job_desc

        yield item