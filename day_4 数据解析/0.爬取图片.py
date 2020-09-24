import requests
import json


if __name__ == '__main__':
    url = 'https://pic.qiushibaike.com/system/pictures/12355/123558286/medium/TTHJKYA6G7F528HM.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    data = requests.get(url=url).content
    with open('./qiutu.jpg','wb') as f:
        f.write(data)