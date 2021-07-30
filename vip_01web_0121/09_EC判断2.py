# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")
search_ele = EC.presence_of_element_located((By.ID, 'kw'))(driver)
search_ele.send_keys("华测教育")
driver.find_element_by_id('su').click()