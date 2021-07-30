# coding = utf-8
import unittest

from selenium.webdriver.common.by import By

from vip_02web.hc_shop import HcShop
import time


class SearchTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        global hc_shop
        hc_shop = HcShop()
        print("类开始")

    @classmethod
    def tearDownClass(cls) -> None:
        hc_shop.close()
        print("类结束")

    def setUp(self) -> None:
        print('方法开始')
        # 访问页面
        hc_shop.web_api.url_get('http://shop-xo.hctestedu.com/')

    def test_01(self):
        '''未登录情况下搜索包包'''
        hc_shop.search('包包')

    def test_02(self):
        '''登录情况下搜索手机'''
        # 点击登录按钮
        hc_shop.web_api.ele_click((By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]'))
        hc_shop.login('jijianfeng01', '123456')
        hc_shop.search('手机')


if __name__ == '__main__':
    unittest.main()
