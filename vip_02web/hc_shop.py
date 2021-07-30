# coding = utf-8

from selenium.webdriver.common.by import By

from vip_01web_0121.web_api import Web_api


class HcShop(object):
    def __init__(self):
        self.web_api = Web_api()

    def login(self, user, password):
        # 输入用户名
        self.web_api.input_text((By.CSS_SELECTOR, '[placeholder="请输入用户名/手机/邮箱"]'), user)
        # 输入密码
        self.web_api.input_text((By.CSS_SELECTOR, '[placeholder="请输入登录密码"]'), password)
        # 点击登录
        self.web_api.ele_click((By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button'))

    def search(self, searchName):
        # 输入商品名
        self.web_api.input_text((By.ID, 'search-input'), searchName)
        # 点击搜索
        self.web_api.ele_click((By.XPATH, '//*[@id="ai-topsearch"]'))

    def close(self):
        self.web_api.close()
