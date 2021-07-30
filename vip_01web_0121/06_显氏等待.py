# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys("华测教育")
driver.find_element_by_id('su').click()
wait = WebDriverWait(driver, 10, 0.2)
wait.until(lambda x:x.find_element_by_partial_link_text('腾讯课堂官网').is_displayed())
driver.find_element_by_partial_link_text('腾讯课堂官网').click()
driver.quit()