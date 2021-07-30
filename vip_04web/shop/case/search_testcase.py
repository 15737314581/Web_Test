# coding = utf-8
from HTMLTestRunner import HTMLTestRunner

from vip_04web.shop.pages.login_page import LoginPage
from vip_04web.shop.pages.search_page import SearchPage
import unittest


class SearchTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.searchObj = SearchPage(browser='Fopts')
        self.loginObj = LoginPage(browser='no', driver=self.searchObj.driver)
        self.searchObj.url_get('http://shop-xo.hctestedu.com/')

    def tearDown(self) -> None:
        self.searchObj.close()

    def test_01(self):
        '''未登录情况下，进行搜索 '''
        self.searchObj.search('手机')
        goods_name_list = self.searchObj.find_search_goods()
        # print(goods_name_list)
        self.assertIn('MIUI/小米 小米手机4 小米4代 MI4智能4G手机包邮 黑色 D-LTE（4G）/TD-SCD', goods_name_list)

    def test_02(self):
        '''已登录情况下，进行搜索'''
        self.loginObj.login('jijianfeng01', '123456')
        self.searchObj.search('包包')
        goods_name_list = self.searchObj.find_search_goods()
        self.assertIn('纽芝兰包包女士2018新款潮百搭韩版时尚单肩斜挎包少女小挎包链条', goods_name_list)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(SearchTestCase))
    with open('../report/report.html', 'wb') as file:
        runner = HTMLTestRunner(stream=file,
                                verbosity=2,
                                title='shop商场自动化测试报告',
                                description='搜索功能自动化测试报告',
                                tester='jijianfeng')
        runner.run(suite)

