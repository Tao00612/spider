import requests
import json

if __name__ == '__main__':
    # 1 指定URL
    post_url = "https://fanyi.baidu.com/sug"
    # 2 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    # post 请求参数处理 (同get一致)
    # 3 参数处理
    word = input('enter a word:')
    data = {
        'kw': word
    }
    # 4 进行请求发送
    response = requests.post(url=post_url, data=data, headers=headers)

    # 5 获取响应数据 ; json方法是返回的一个obj(如果确定了是json类型,才能使用json())
    # Content-Type 确认数据类型
    dict_obj = response.json()
    print(dict_obj)

    # 6 持久化存储
    filename = word + '.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dict_obj, f, ensure_ascii=False)
    print('存储成功')
