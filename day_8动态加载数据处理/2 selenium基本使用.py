from selenium import webdriver
from lxml import etree
from time import sleep
# 选择下载好的驱动程序
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# 实例化好了一个浏览器对象

# 让浏览器发起请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')

# 获取浏览器当前页面源码数据
page_text = bro.page_source

# 解析企业名称
tree = etree.HTML(page_text)

list_li = tree.xpath('//ul[@id="gzlist"]/li')
for li in list_li:
    title = li.xpath('./dl/@title')[0]
    print(title)

sleep(5)
# 关闭浏览器
bro.quit()