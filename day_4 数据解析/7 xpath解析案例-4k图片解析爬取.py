from lxml import etree
import requests

if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    url_upload = 'http://pic.netbian.com/'
    li_list = tree.xpath('//div[@class="slist"]/ul[@class="clearfix"]/li')
    for li in li_list:
        img_src = url_upload + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 通用处理中文乱码的问题
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        path = './img/' + img_name
        img_data = requests.get(url=img_src,headers=headers).content
        with open(path, 'wb') as f:
            f.write(img_data)
            print(img_name,'下载完毕')