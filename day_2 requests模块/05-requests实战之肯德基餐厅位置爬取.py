import requests
import json

if __name__ == '__main__':
    post_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    kw = input('请输入城市名:')
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

    response = requests.post(url=post_url, data=data, headers=headers)
    # print(response.text)

    list_json = json.loads(response.text)

    filename = kw + '.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(list_json, f, ensure_ascii=False)
    print('over')
