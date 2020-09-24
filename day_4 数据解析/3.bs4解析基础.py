from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    fp = open('./test.html', 'r', encoding='utf-8')
    # 将本地的html文档中的数据加载到对象中
    soup = BeautifulSoup(fp, 'lxml')
    # 返回第一个h1标签内容
    print(soup.h1)

