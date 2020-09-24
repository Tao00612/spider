# 爬取三国演义小说
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(page_text, 'lxml')
    l_list = soup.select('.book-mulu > ul > li')
    fp = open('data/三国演义.txt', 'w', encoding='utf-8')
    for l in l_list:
        title = l.a.string
        detail_url = 'https://www.shicimingju.com' + l.a['href']
        # 对详情页发起请求解析章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = soup.find('div', class_='chapter_content')
        content = div_tag.text
        fp.write(title + ":" + content + '\n')
        print(title, '爬取成功')