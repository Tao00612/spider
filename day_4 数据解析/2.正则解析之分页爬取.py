import re
import requests

if __name__ == '__main__':
    # 设置一个通用的url模板
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    for page_num in range(1,14):
        url = 'https://www.qiushibaike.com/imgrank/page/%d/' % page_num

        ex = r'<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        page_text = requests.get(url=url, headers=headers).text
        img_url_list = re.findall(ex, page_text, re.S)
        for img_url in img_url_list:
            img_name = img_url.split('/')[-1]
            img_url = 'https:' + img_url
            filename = './data/' + img_name
            img_data = requests.get(url=img_url, headers=headers).content
            with open(filename, 'wb') as f:
                f.write(img_data)
