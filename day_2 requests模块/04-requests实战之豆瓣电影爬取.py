import requests
import json

if __name__ == '__main__':
    url = "https://movie.douban.com/j/new_search_subjects"
    param = {
        'sort': 'U',
        'range': '0, 20',  # 一次取20个
        'tags': '',
        'start': '0',  # 从库中的第几部电影开始取
        'genres': '喜剧'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)

    list_data = response.json()

    with open('./douban.json','w',encoding='utf-8') as f:
        json.dump(list_data,f,ensure_ascii=False)

    print('over')