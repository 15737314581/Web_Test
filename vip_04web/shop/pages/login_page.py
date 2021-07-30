# coding = utf-8
from selenium.webdriver.common.by import By

from vip_04web.shop import BasePage


class LoginPage(BasePage):
    # 定义元素定位方式和属性值
    index_login_btn = (By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]')
    user_input = (By.CSS_SELECTOR, '[placeholder="请输入用户名/手机/邮箱"]')
    pwd_input = (By.CSS_SELECTOR, '[placeholder="请输入登录密码"]')
    login_btn = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')
    quit_btn = (By.LINK_TEXT,'退出')
    error_msg = (By.XPATH,'/html/body/div[8]/div/p')
    # 元素操作
    def click_index_login_btn(self):
        self.ele_click(LoginPage.index_login_btn)

    def input_user_input(self, user):
        self.input_text(LoginPage.user_input, user)

    def input_pwd_input(self, pwd):
        self.input_text(LoginPage.pwd_input, pwd)

    def click_login_btn(self):
        self.ele_click(LoginPage.login_btn)

    def find_quit_bin(self):
        return self.ele_wait(LoginPage.quit_btn)

    def find_error_msg(self):
        ele = self.ele_wait(LoginPage.error_msg)
        return ele.text

    # 业务绑定——注册流程
    def login(self, user, pwd):
        self.click_index_login_btn()
        self.input_user_input(user)
        self.input_pwd_input(pwd)
        self.click_login_btn()
