# coding = utf-8

from selenium import  webdriver
import time
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

# driver.set_window_size(600,800)
# time.sleep(2)
# driver.minimize_window()
# time.sleep(2)
# driver.maximize_window()
# time.sleep(2)
# driver.quit()
print(driver.current_window_handle)
driver.find_element_by_partial_link_text('新闻').click()
print(driver.current_window_handle)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])
print(driver.current_window_handle)
# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/ul/li[2]/strong/a[1]/b').click()
time.sleep(3)
driver.find_element_by_partial_link_text('奥林匹克').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_partial_link_text('hao123').click()
time.sleep(2)
driver.quit()
