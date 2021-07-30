# coding = utf-8
from HTMLTestRunner import HTMLTestRunner

from vip_04web.shop import LoginPage
import unittest
import time


class LoginTestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     global register
    #     register = RegisterPage()
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     register.close()

    def setUp(self) -> None:
        self.loginObj = LoginPage(browser='Fopts')
        self.loginObj.url_get('http://shop-xo.hctestedu.com/')

    def tearDown(self) -> None:
        self.loginObj.close()

    def test_01(self):
        '''登录失败'''
        self.loginObj.login('jijianfeng01', '1234567')
        # time.sleep(3)
        # exp_url = 'http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html'
        # act_url = self.loginObj.driver.current_url
        # self.assertTrue(exp_url,act_url)
        msg = self.loginObj.find_error_msg()
        self.assertEqual(msg, '密码错误')
        # print(msg)

    def test_02(self):
        '''登录成功'''
        self.loginObj.login('jijianfeng02', '123456')
        time.sleep(5)
        # exp_url = 'http://shop-xo.hctestedu.com/'
        # act_url = self.loginObj.driver.current_url
        # self.assertTrue(exp_url, act_url)
        quit_ele = self.loginObj.find_quit_bin()
        self.assertIsNotNone(quit_ele)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(LoginTestCase))
    with open('../report/report.html', 'wb') as file:
        runner = HTMLTestRunner(stream=file,
                                verbosity=2,
                                title='shop商场自动化测试报告',
                                description='登录功能自动化测试报告',
                                tester='jijianfeng')
        runner.run(suite)
