from selenium import webdriver
import time
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# 实例化对象

bro.get('https://www.taobao.com/')
# 请求网页

search_input = bro.find_element_by_id("q")
# 标签点位

search_input.send_keys('华为')
# 标签交互

# 执行js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
# 点击搜索按钮
search_button = bro.find_element_by_class_name('btn-search')
search_button.click()

bro.get('https://www.baidu.com')
time.sleep(2)
# 回退
bro.back()
time.sleep(2)
# 前进
bro.forward()

time.sleep(5)

bro.quit()
