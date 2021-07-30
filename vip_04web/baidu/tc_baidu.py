# coding = utf-8

from selenium import webdriver
import time
import unittest
import ddt


@ddt.ddt()
class BaiduTestCase(unittest.TestCase):

    # @ddt.data('自动化测试','自动化','测试')
    # @ddt.data(*['自动化测试','自动化','测试'])
    # def test_01(self,data):
    #     driver = webdriver.Firefox()
    #     driver.get('https://www.baidu.com')
    #     baidu = SearchPage(driver)
    #     baidu.input_search_input(data)
    #     baidu.click_search_btn()
    #     time.sleep(2)
    #     driver.quit()

    # @ddt.data(('jijianfeng01','123456'),('jijianfeng02','123456'))
    # # @ddt.data({'username':'jijianfeng01','password':'123456'},{'username':'jijianfeng02','password':'123456'})
    # @ddt.unpack

    @ddt.file_data('../shop/config/login.yaml')
    @ddt.unpack
    def test_01(self, username,password):
        driver = webdriver.Firefox()
        driver.get('http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html')
        driver.find_element_by_css_selector('[placeholder="请输入用户名/手机/邮箱"]').send_keys(username)
        driver.find_element_by_css_selector('[placeholder="请输入登录密码"]').send_keys(password)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()
        time.sleep(2)
        driver.quit()
        print(111)


if __name__ == '__main__':
    unittest.main()
