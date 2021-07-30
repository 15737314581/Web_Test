# coding = utf-8

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
res = EC.title_is('百度一下，你就知道').__call__(driver)
print(res)
res1 = EC.title_contains('百度')(driver)
print(res1)