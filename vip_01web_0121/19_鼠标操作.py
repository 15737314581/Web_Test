# coding = utf-8

from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

# driver.find_element_by_id('kw').send_keys('hello')
# ele = driver.find_element_by_id('su')
# action = ActionChains(driver)
# action.click(ele).perform()

# 悬停操作
# ele = driver.find_element_by_link_text('更多')
# ActionChains(driver).move_to_element(ele).perform()
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div[1]/a[2]/div').click()

# 双击和右击
ele = driver.find_element_by_id('kw')
ele.send_keys('你好')

ActionChains(driver).double_click(ele).perform()
ActionChains(driver).context_click(ele).perform()
time.sleep(5)
driver.quit()