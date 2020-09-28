from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')

zhanghao = bro.find_element_by_id('switcher_plogin')
zhanghao.click()
name_input = bro.find_element_by_id('u')
name_input.send_keys('1521927397')
pwd_input = bro.find_element_by_id('p')
pwd_input.send_keys('zhang.0612')

btn_input = bro.find_element_by_id('login_button')
btn_input.click()

sleep(5)

bro.quit()

