# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 封装等待方法
def wait(type, value, time=10):
    WebDriverWait(driver, time).until(lambda x: len(x.find_elements(type, value)) > 0, message='没有找到元素')


# 封装EC判断
def ele_isdisplay(locator):
    search_ele = EC.presence_of_element_located(locator)(driver)
    return search_ele


# 同时封装等待方法和EC判断
def wait_ele(locator, time=10):
    ele = WebDriverWait(driver, time).until(EC.presence_of_element_located(locator), message='没有找到元素')
    return ele


driver = webdriver.Firefox()

driver.get("https://www.baidu.com")
wait_ele((By.ID,'kw')).send_keys("华测教育")
wait_ele((By.ID,'su')).click()
wait_ele((By.PARTIAL_LINK_TEXT, '腾讯课堂官网')).click()

