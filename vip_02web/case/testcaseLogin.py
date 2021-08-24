# coding = utf-8
import unittest

from selenium.webdriver.common.by import By
from HTMLTestRunner import HTMLTestRunner

from vip_02web.hc_shop import HcShop
import time


class LoginTestCase(unittest.TestCase):
    '''
    登录模块测试用例
    '''

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
        # 1.访问页面
        hc_shop.web_api.url_get('http://shop-xo.hctestedu.com/')
        # 2.点击登录按钮
        hc_shop.web_api.ele_click((By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]'))

    def tearDown(self) -> None:
        print('方法结束')
        time.sleep(3)
        if hc_shop.web_api.driver.current_url == 'http://shop-xo.hctestedu.com/':
            hc_shop.web_api.ele_click((By.LINK_TEXT, '退出'))
        else:
            hc_shop.web_api.driver.refresh()

    def test_01_moke(self):
        '''登录成功，url断言'''
        hc_shop.login('jijianfeng01', '123456')
        # 断言
        time.sleep(3)
        exp_url = 'http://shop-xo.hctestedu.com/'
        act_url = hc_shop.web_api.driver.current_url
        self.assertEqual(exp_url, act_url)

    def test_02(self):
        '''登录成功，退出按钮断言'''
        hc_shop.login('jijianfeng02', '123456')
        # 断言
        time.sleep(3)
        ele_quit_list = hc_shop.web_api.driver.find_elements_by_link_text('退出')
        self.assertTrue(len(ele_quit_list) > 0)


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

    def test_02_moke(self):
        '''登录情况下搜索手机'''
        # 点击登录按钮
        hc_shop.web_api.ele_click((By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]'))
        hc_shop.login('jijianfeng01', '123456')
        hc_shop.search('手机')


if __name__ == '__main__':
    # 执行全部用了
    # unittest.main()

    # 1.创建一个测试套件
    suite = unittest.TestSuite()
    # 2.在测试套件中加入测试用例
    # 方式一
    # suite.addTest(LoginTestCase('test_01'))
    # suite.addTest(SearchTestCase('test_01'))
    # 方式二
    # suite.addTests([SearchTestCase('test_01'),LoginTestCase('test_01')])
    # 方式三
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(LoginTestCase))

    # 3.执行测试套件
    # 创建一个执行器---文本执行
    # runner = unittest.TextTestRunner()

    # 创建一个执行器---HTML执行
    with open('../report/report.html', 'wb') as file:
        runner = HTMLTestRunner(stream=file,
                                verbosity=2,
                                title='shop商场自动化测试报告',
                                description='登录功能自动化测试报告',
                                tester='jijianfeng')

        # 执行器执行测试套件
        runner.run(suite)
