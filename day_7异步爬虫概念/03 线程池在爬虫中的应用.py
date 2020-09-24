import requests
from lxml import etree
import re
# 爬取梨视频的视频数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
# 原则: 线程池处理的是阻塞且耗时的操作

# 对下述url发起请求解析视频
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
list_li = tree.xpath('//div[@id="listvideoList"]/ul/li')
for li in list_li:
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    print(detail_url,name)
    # 对详情页发起请求
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    # 网站将MP4放在了ajax里
    print(detail_page_text)
