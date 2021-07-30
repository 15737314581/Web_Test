# coding = utf-8
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5000/signin")

driver.find_element_by_name("username").send_keys('15902127953')
driver.find_element_by_name("password").send_keys('123456')
driver.find_element_by_xpath("/html/body/form/p[3]/button").click()
driver.find_element_by_xpath('//*[@id="testtable"]/tbody/tr[1]/td[2]/input').send_keys(r'/Users/jijianfeng/Pictures/a.jpeg')