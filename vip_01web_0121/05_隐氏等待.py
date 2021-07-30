# coding = utf-8

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(20)
driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys("华测教育")
driver.find_element_by_id('su').click()
driver.find_element_by_partial_link_text('腾讯课堂官网').click()
driver.quit()