# coding:utf-8
import requests
from hashlib import md5


class Chaojiying_Client(object):

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

    def get_url(self):
        bro = webdriver.Chrome(executable_path='chromedriver.exe')
        bro.get('https://kyfw.12306.cn/otn/resources/login.html')


# if __name__ == '__main__':
#     chaojiying = Chaojiying_Client('zhangTao', 'zhang0612',
#                                '1082a5c5e46df4be738cd6f9190a237b')  # 用户中心>>软件ID 生成一个替换 96001
#     im = open('a.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
#     print(chaojiying.PostPic(im, 1902))  # 1902 验证码类型

# 使用selenium打开登录页面
from selenium import webdriver
from time import sleep
from PIL import Image
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
bro = webdriver.Chrome(executable_path='chromedriver.exe', options=option)

bro.get('https://kyfw.12306.cn/otn/login/init')
bro.execute_script('document.body.style.zoom="0.5"')
sleep(2)
# 需要截图   将当前页面对象截面且保存
bro.save_screenshot('a.png')
sleep(2)
# 确定验证码图片对应左上和右下的坐标 (裁剪的区域确定)
code_img_ele = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
left = code_img_ele.location['x']  # 区块截图左上角在网页中的x坐标
top = code_img_ele.location['y']  # 区块截图左上角在网页中的y坐标
right = left + code_img_ele.size['width']  # 区块截图右下角在网页中的x坐标
bottom = top + code_img_ele.size['height']  # 区块截图右下角在网页中的y坐标
rangle = (left, top, right, bottom)
# 至此验证码的图片的坐标就确定下来了

picture = Image.open(r'a.png')
picture = picture.crop(rangle)  # 二次截图：形成区块截图
picture.save(r'code.png')

# 提交 图片给超级鹰识别

chaojiying = Chaojiying_Client('zhangTao', 'zhang0612', '1082a5c5e46df4be738cd6f9190a237b')  # 用户中心>>软件ID 生成一个替换 96001
im = open('code.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
result = chaojiying.PostPic(im, 9004)  # 1902 验证码类型
all_list = []  # 要存储即将被点击的点的坐标  [[],[]]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    xy_list = []
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)

# 便利列表,使用动作链对每一个列表元素对应的x,y指定操作
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()
    sleep(1)

# 录入用户名和密码

bro.find_element_by_id('username').send_keys('15616122577')
sleep(2)
bro.find_element_by_id('password').send_keys('zhang0612')
sleep(2)
login_btn = bro.find_element_by_id('loginSub')
bro.execute_script("arguments[0].click();", login_btn)
