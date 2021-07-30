# coding = utf-8
from selenium.webdriver.common.by import By


class SearchPage(object):
    def __init__(self,driver):
        self.driver = driver

    search_input = (By.ID,'kw')
    search_btn = (By.ID,'su')

    def input_search_input(self,str):
        self.driver.find_element(*SearchPage.search_input).send_keys(str)

    def click_search_btn(self):
        self.driver.find_element(*SearchPage.search_btn).click()
