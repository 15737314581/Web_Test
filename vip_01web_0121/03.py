# coding = utf-8

from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
# driver.find_element_by_link_text('hao123').click()
# driver.find_element_by_partial_link_text('hao').click()

url = driver.current_url
title = driver.title
if url == "https://www.baidu.com/":
    print("打开成功")
else:
    print("打开失败")

if title == "百度一下，你就知道":
    print("打开成功")
else:
    print("打开失败")

ele_search = driver.find_element_by_id("kw")
print(ele_search.size)
print(ele_search.location)
print(ele_search.get_attribute('class'))
time.sleep(2)
driver.quit()
