# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By

from vip_01web_0121.web_api import Web_api
import time

# 打开浏览器
# driver = webdriver.Firefox()


# # 输入用户名
# # driver.find_element_by_id('name').send_keys('test123456')
# # # 输入密码
# # driver.find_element_by_id('pass').send_keys('123456')
# # # 点击提交
# # driver.find_element_by_class_name('span-primary').click()
# 退出

web_api = Web_api()
# web_api.url_get('http://shop-xo.hctestedu.com/index.php?s=/index/user/reginfo.html')
# web_api.input_text((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[1]/input'), '111')
# web_api.input_text((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div/input'), '111')
# web_api.ele_click((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/button'))

# driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[1]/input').send_keys('111')
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div/input').send_keys('222')
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/button').click()

web_api.url_get('http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html')
web_api.input_text((By.CSS_SELECTOR, '[placeholder="请输入用户名/手机/邮箱"]'),"jijianfeng01")
web_api.input_text((By.CSS_SELECTOR, '[placeholder="请输入登录密码"]'),"1234567")
web_api.ele_click((By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button'))

ele = web_api.ele_wait((By.XPATH,'/html/body/div[8]/div/p'))
print(ele.text)
