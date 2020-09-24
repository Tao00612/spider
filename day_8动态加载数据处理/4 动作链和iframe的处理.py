from selenium import webdriver
from time import sleep
# 导入动作链的类
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-draggable')

# 如何定位的标签存在iframe标签之中的必须进行如下操作定位
bro.switch_to.frame('iframeResult')
# 切换浏览器标签定位的作用域

div = bro.find_element_by_id('draggable')

# 动作链
action = ActionChains(bro)
# 点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    # perform 立即执行
    # move_by_offset(x,y) x 表示水平方向  y 表示竖直方向
    action.move_by_offset(17, 0).perform()
    sleep(0.3)

# 释放动作链
action.release()
bro.quit()