'''
- 需求: 爬取网站首页页面
'''

import requests

if __name__ == '__main__':
    #     - 指定url
    url = "https://www.sogou.com/"
    #     - 发起请求
    # get 方法会返回一个响应对象
    response = requests.get(url=url)
    #     - 获取响应数据.text 返回的是字符串响应数据
    page_text = response.text
    print(page_text)
    #     - 持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as f:
        f.write(page_text)
    print('结束')
