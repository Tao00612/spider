# coding:utf-8

import requests
from hashlib import md5
from lxml import etree


class Chaojiying_Client(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json().get('pic_str')

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

    def get_img(self):
        # 将验证码下载到本地
        url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
        page_text = requests.get(url=url, headers=self.headers).text
        # 解析验证码中图片img中src属性值
        tree = etree.HTML(page_text)
        code_img_src = 'https://so.gushiwen.cn' + tree.xpath('//img[@id="imgCode"]/@src')[0]
        img_data = requests.get(url=code_img_src, headers=self.headers).content
        path = 'code_img.jpg'
        # 将验证码保存在本地
        with open(path, 'wb') as f:
            f.write(img_data)
        return path


if __name__ == '__main__':
    chaojiying = Chaojiying_Client('zhangTao', 'zhang0612',
                                   '1082a5c5e46df4be738cd6f9190a237b')
    path = chaojiying.get_img()
    im = open(path, 'rb').read()  # 本地图片文件路径 来替换 a.jpg
    code_img_data = chaojiying.PostPic(im, 1004)  # 1902 验证码类型
    print(code_img_data)