# coding = utf-8
from selenium.webdriver.common.by import By

from vip_01web_0121.web_api import Web_api

web_api = Web_api()
# 1.访问页面1
web_api.url_get('http://shop-xo.hctestedu.com/')
# 2.登录
# 点击登录按钮
web_api.ele_click((By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]'))
# 输入用户名
web_api.input_text((By.CSS_SELECTOR, '[placeholder="请输入用户名/手机/邮箱"]'), 'jijianfeng01')
# 输入密码
web_api.input_text((By.CSS_SELECTOR, '[placeholder="请输入登录密码"]'), '123456')
# 点击登录
web_api.ele_click((By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button'))
# 3.搜索商品
# 输入商品名
web_api.input_text((By.ID,'search-input'),'包包')
# 点击搜索
web_api.ele_click((By.XPATH,'//*[@id="ai-topsearch"]'))
# 4.加入购物车
# 点击商品
web_api.ele_click((By.XPATH,'/html/body/div[4]/div/ul/li/div/a/img'))
# 切换窗口句柄
web_api.switch_to_window()
# 点击加入购物车
web_api.ele_click((By.CSS_SELECTOR,'[title="加入购物车"]'))
# 5.提交订单
# 刷新页面
web_api.driver.refresh()
# 点击购物车
web_api.ele_click((By.XPATH,'/html/body/div[1]/div/ul[2]/div[5]/div/a/span'))
# 选择结算商品
web_api.ele_click((By.CLASS_NAME,'am-icon-checked'),flag=False,index=0)
# 点击结算
web_api.ele_click((By.XPATH,'/html/body/div[5]/div/div[2]/form/button'))


