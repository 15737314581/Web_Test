# coding = utf-8
from selenium.webdriver.common.by import By

from vip_04web.shop import BasePage


class RegisterPage(BasePage):
    # 定义元素定位方式和属性值
    user_input = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[1]/input')
    pwd_input = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div/input')
    register_btn = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/button')
    error_msg = (By.XPATH,'/html/body/div[8]/div/p')

    # 元素操作
    def input_user_input(self, user):
        # print(RegisterPage.user_input)
        # print(user)
        self.input_text(RegisterPage.user_input, user)

    def input_pwd_input(self, pwd):
        self.input_text(RegisterPage.pwd_input, pwd)

    def click_register_btn(self):
        self.ele_click(RegisterPage.register_btn)

    def find_error_msg(self):
        ele = self.ele_wait(RegisterPage.error_msg)
        return ele.text

    # 业务绑定——注册流程
    def register(self, user, pwd):
        self.input_user_input(user)
        self.input_pwd_input(pwd)
        self.click_register_btn()
