# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc')
# 同时封装等待方法和EC判断
def wait_ele(locator, time=10):
    ele = WebDriverWait(driver, time).until(EC.presence_of_element_located(locator), message='没有找到元素')
    return ele


wait_ele((By.ID, 'qd_closeDefaultWarningWindowDialog_id')).click()

wait_ele((By.NAME,'leftTicketDTO.from_station_name')).click()

wait_ele((By.NAME,'leftTicketDTO.from_station_name')).send_keys('北京')
wait_ele((By.XPATH,'//*[@id="citem_2"]')).click()

wait_ele((By.NAME,'leftTicketDTO.to_station_name')).click()

wait_ele((By.NAME,'leftTicketDTO.to_station_name')).send_keys('上海\n')

wait_ele((By.XPATH,'//*[@id="date_icon_1"]')).click()
wait_ele((By.XPATH,'/html/body/div[37]/div[1]/div[2]/div[14]/div')).click()
wait_ele((By.XPATH,'//*[@id="cc_start_time"]')).click()
wait_ele((By.XPATH,'/html/body/div[7]/div[5]/div[2]/div[1]/select/option[4]')).click()
wait_ele((By.XPATH,'//*[@id="cc_start_time"]')).click()
wait_ele((By.LINK_TEXT,'查询')).click()





