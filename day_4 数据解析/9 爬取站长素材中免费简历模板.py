from lxml import etree
import requests

#     get   data headers url
if __name__ == '__main__':
    url = 'http://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&issale=&classID=864&page=3'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@id="main"]/div/div')
    down_list = []
    for div in div_list:
        url = div.xpath('./a/@href')[0]
        name = div.xpath('./p/a/text()')[0]
        path = './data/' + name + '.rar'
        page_text = requests.get(url=url, headers=headers).text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="clearfix mt20 downlist"]/ul[@class="clearfix"]/li[1]')
        if li_list:
            href = li_list[0].xpath('./a/@href')[0]
            data = requests.get(url=href,headers=headers).content
            with open(path,'wb') as f:
                f.write(data)
                print(path,'下载完毕')
