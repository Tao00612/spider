import scrapy
from qiushibaike.items import QiushibaikeItem

class TextSpider(scrapy.Spider):
    name = 'text'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response, **kwargs):
    #     # 解析作者的名称和段子的内容
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = [] # 存储所有解析的数据
    #     for div in div_list:
    #         # xpath 返回的是列表,但是列表元素一定是Selector类型的对象
    #         # extract可以将Selector对象中的data参数存储的字符串提取出来
    #         # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         # 列表调用了extract之后,则表示将列表中每一个Selector对象中data对应的字符串提取
    #         content = div.xpath('./a[1]/div/span[1]//text()').extract()
    #         content = ''.join(content)
    #
    #         dic = {
    #             'author':author,
    #             'content':content
    #         }
    #         all_data.append(dic)
    #     return all_data
    def parse(self, response, **kwargs):
        # 解析作者的名称和段子的内容
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = [] # 存储所有解析的数据
        for div in div_list:
            # xpath 返回的是列表,但是列表元素一定是Selector类型的对象
            # extract可以将Selector对象中的data参数存储的字符串提取出来
            # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            # 列表调用了extract之后,则表示将列表中每一个Selector对象中data对应的字符串提取
            content = div.xpath('./a[1]/div/span[1]//text()').extract()
            content = ''.join(content)

            item = QiushibaikeItem()
            item['author'] = author
            item['content'] = content

            yield item # 将item提交给管道