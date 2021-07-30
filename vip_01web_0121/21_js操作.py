# coding = utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

js1 = 'window.open("https://www.jd.com")'
driver.execute_script(js1)
time.sleep(2)
driver.quit()
