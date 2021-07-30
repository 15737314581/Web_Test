# coding = utf-8

from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome()
url = ['https://www.baidu.com','https://www.jd.com']
img_name=['百度','京东']
for i in range(len(url)):
    driver.get(url[i])
    driver.get_screenshot_as_file("./img/{}.png".format(img_name[i]))

# 后退
driver.back()
time.sleep(2)
# 前进
driver.forward()
time.sleep(2)
# 刷新
driver.refresh()
time.sleep(2)
driver.quit()




# driver.quit()