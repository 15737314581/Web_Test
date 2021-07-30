# coding = utf-8
from HTMLTestRunner import HTMLTestRunner
from vip_04web.shop.pages.register_page import RegisterPage
import unittest
import time


class RegisterTestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     global register
    #     register = RegisterPage()
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     register.close()

    def setUp(self) -> None:
        self.registerObj = RegisterPage(browser='Fopts')
        self.registerObj.url_get('http://shop-xo.hctestedu.com/index.php?s=/index/user/reginfo.html')

    def tearDown(self) -> None:
        self.registerObj.close()

    def test_01(self):
        '''已注册过用户，进行注册'''

        self.registerObj.register('jijianfeng01', '123456')
        time.sleep(3)
        msg = self.registerObj.find_error_msg()
        self.assertEqual(msg,'账号已存在')

    def test_02(self):
        '''注册密码不符合规范'''
        self.registerObj.register('jijianfeng01', '12345')
        time.sleep(3)
        msg = self.registerObj.find_error_msg()
        self.assertEqual(msg, '密码格式 6~18 个字符之间')




if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(RegisterTestCase))
    with open('../report/report.html', 'wb') as file:
        runner = HTMLTestRunner(stream=file,
                                verbosity=2,
                                title='shop商场自动化测试报告',
                                description='注册功能自动化测试报告',
                                tester='jijianfeng')
        runner.run(suite)
