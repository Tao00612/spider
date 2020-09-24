import requests
import json

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    id_list = []  # 存储企业id
    all_data_list = []  # 存储所有的企业详情数据
    for page in range(1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for i in json_ids['list']:
            id_list.append(i['ID'])

    # 获取企业详情数据
    url_3 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        data_json = requests.post(url=url_3, data=data, headers=headers).json()
        all_data_list.append(data_json)

    with open('./化妆品.json', 'w', encoding='utf-8') as f:
        json.dump(all_data_list, f, ensure_ascii=False)
