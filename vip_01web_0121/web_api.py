# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Web_api(object):
    def __init__(self, browser='Firefox'):
        if browser == 'Firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

    # 封装打开网页方法
    def url_get(self, url):
        self.driver.get(url)

    # 封装判断网页标题方法
    def ele_title(self, tltle):
        res = EC.title_is(tltle).__call__(self.driver)
        if res:
            print('页面打开成功')
        else:
            print('页面打开失败')

    # 封装判断网页网址方法
    def ele_url(self, url):
        res = EC.url_contains(url).__call__(self.driver)
        if res:
            print('页面打开成功')
        else:
            print('页面打开失败')

    # 封装显示等待方法
    def ele_wait(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        ele = wait.until(EC.presence_of_element_located(locator), message='元素没有找到')
        return ele

    # 封装显示等待方法（通过元素组查找元素）
    def ele_list_wait(self, locator, index, time=10):
        wait = WebDriverWait(self.driver, time)
        ele = wait.until(EC.presence_of_all_elements_located(locator), message='元素没有找到')
        return ele[index]

    # 封装输入框填写方法
    def input_text(self, locator, str, time=10, flag=True, index=0):
        if flag:
            self.ele_wait(locator, time).send_keys(str)
        else:
            self.ele_list_wait(locator, index, time).send_keys(str)

    # 封装按钮点击方法
    def ele_click(self, locator, time=10, flag=True, index=0):
        if flag:
            self.ele_wait(locator, time).click()
        else:
            self.ele_list_wait(locator, index, time).click()

    # 切换句柄
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # 关闭弹窗
    def close(self):
        self.driver.quit()
