from lxml import etree
import requests

if __name__ == '__main__':
    url = 'https://sz.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('./58.txt', 'w', encoding='utf-8')
    for li in li_list:
        # 局部解析
        title = li.xpath('./div[2]/h2/a/text()')[0]
        price = ''.join(li.xpath('./div[3]/p//text()'))
        fp.write(title + price + '\n')
