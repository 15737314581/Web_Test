# coding = utf-8
from selenium.webdriver.common.by import By

from vip_04web.baidu.shop import BasePage


class SearchPage(BasePage):
    # 定义元素定位方式和属性值
    search_input = (By.ID, 'search-input')
    search_btn = (By.XPATH, '//*[@id="ai-topsearch"]')
    search_goods = (By.CLASS_NAME, 'goods-images')

    # 元素操作
    def input_search_input(self, search_name):
        self.input_text(SearchPage.search_input, search_name)

    def click_search_btn(self):
        self.ele_click(SearchPage.search_btn)

    def find_search_goods(self):
        ele_list = self.eles_list_wait(SearchPage.search_goods)
        ele_list_goods_name = []
        for i in ele_list:
            ele_goods_name = i.get_attribute('alt')
            ele_list_goods_name.append(ele_goods_name)
        return ele_list_goods_name

    # 业务绑定——搜索流程
    def search(self, search_name):
        self.input_search_input(search_name)
        self.click_search_btn()
