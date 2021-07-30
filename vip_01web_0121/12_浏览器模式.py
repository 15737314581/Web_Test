# coding = utf-8

from selenium import  webdriver

opts = webdriver.ChromeOptions()
opts.headless = True

driver = webdriver.Chrome(chrome_options=opts)
driver.get('https://www.baidu.com')
if driver.title == "百度一下，你就知道":
    print("成功")
else:
    print("失败")