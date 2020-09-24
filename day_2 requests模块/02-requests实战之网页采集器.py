import requests

# UA伪装 门户网站的服务器会检测对应请求的载体身份标识,如果检测到请求的载体身份标识为
# 某一款浏览器 说明该请求是一个正常的请求,但是,如果检测到身份标识不是某一款浏览器的,则
# 不是正常的请求(爬虫) 服务器会拒绝该次请求
# UA: User-Agent ()
# 让爬虫对应的爬虫身份标识伪装成某一款浏览器

if __name__ == '__main__':
    # UA伪装 : 将对应的user-agent 封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    # 指定url
    url = "https://www.sogou.com/web"
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 发起请求
    # 对指定的url发起的请求对应的url是携带参数的,并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)
    # 获取响应数据
    page_text = response.text
    # 存储
    file_name = kw + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(page_text)
    print(file_name, '保存成功')
