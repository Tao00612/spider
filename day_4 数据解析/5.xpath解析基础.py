from lxml import etree
import requests

if __name__ == '__main__':
    # 实例化一个对象 将页面源码记载到对象中
    response = requests.get('http://www.baidu.com').text
    tree = etree.HTML(response)

    r = tree.xpath('//a')
    print(r)