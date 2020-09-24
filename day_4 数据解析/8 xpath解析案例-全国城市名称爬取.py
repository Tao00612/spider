from lxml import etree
import requests
import json


if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="unstyled"]/li')
    top_list = []
    for li in li_list:
        top_city = li.xpath('./a/text()')[0]
        top_list.append(top_city)
    with open('./热门城市.json', 'w', encoding='utf-8') as f:
        json.dump(top_list,f)

    all_city_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')
    print(all_city_list)