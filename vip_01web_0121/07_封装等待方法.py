# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def wait(type, value, time=10):
    WebDriverWait(driver, time).until(lambda x: len(x.find_elements(type, value)) > 0, message='没有找到元素')


driver = webdriver.Firefox()

driver.get("https://www.baidu.com")
# driver.find_element_by_id('kw').send_keys("华测教育")
# driver.find_element_by_id('su').click()
# wait(By.PARTIAL_LINK_TEXT,'腾讯课堂官网')
# driver.find_element_by_partial_link_text('腾讯课堂官网').click()
print(driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/a[3]').text)
