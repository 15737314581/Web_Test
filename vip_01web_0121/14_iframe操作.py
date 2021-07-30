# coding = utf-8

from selenium import  webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://mail.163.com/')

frame_ele = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(frame_ele)
driver.find_element_by_name('email').send_keys('123456')
driver.find_element_by_name('password').send_keys('000000')
driver.switch_to.default_content()
time.sleep(2)
driver.find_element_by_link_text('企业邮箱').click()
time.sleep(2)
driver.quit()

