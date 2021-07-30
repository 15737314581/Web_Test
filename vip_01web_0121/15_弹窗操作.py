# coding = utf-8
from selenium import  webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('file:///Users/jijianfeng/Desktop/Alter(1).html')

driver.find_element_by_id('alert').click()
a = driver.switch_to.alert
print(a.text)
time.sleep(2)
a.accept()
time.sleep(2)
driver.quit()