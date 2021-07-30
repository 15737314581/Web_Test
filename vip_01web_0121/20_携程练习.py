# coding = utf-8

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()

driver.get("https://passport.ctrip.com/user/reg/home")

driver.find_element_by_link_text('同意并继续').click()
time.sleep(2)
ele = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/dl[2]/dd/div/div[1]/div[2]')
ele1 = driver.find_element_by_id('slideCode')
print(ele1.location)
print(ele1.size)
ActionChains(driver).drag_and_drop_by_offset(ele,ele1.location['x']+ele1.size['width'],ele1.location['y']).perform()

