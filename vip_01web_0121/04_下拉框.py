# coding = utf-8

from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/signin")

driver.find_element_by_name("username").send_keys('15902127953')
driver.find_element_by_name("password").send_keys('123456')
driver.find_element_by_xpath("/html/body/form/p[3]/button").click()

driver.find_element_by_xpath('//*[@value="peach"]').click()
time.sleep(2)
ele_select = driver.find_element_by_id('Selector')
obj_selsect = Select(ele_select)
obj_selsect.select_by_value("apple")
time.sleep(2)
obj_selsect.select_by_index(3)
time.sleep(2)
obj_selsect.select_by_visible_text("芒果")

