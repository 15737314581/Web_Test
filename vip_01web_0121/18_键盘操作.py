# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")


driver.find_element_by_id('kw').send_keys('seleniumm')
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.SPACE,'教程')
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.COMMAND,'a')
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)

