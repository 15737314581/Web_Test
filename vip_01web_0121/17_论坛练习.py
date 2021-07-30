# coding = utf-8
from selenium.webdriver.common.by import By

from vip_01web_0121.web_api import Web_api

web_api = Web_api()

web_api.url_get('http://bbs.hctestedu.com/signin')
web_api.input_text((By.ID,'name'),'test123456')
web_api.input_text((By.ID,'pass'),'123456')
web_api.ele_click((By.XPATH,'//*[@value="登录"]'))
print(web_api.driver.current_url)
print(web_api.driver.title)
web_api.ele_click((By.PARTIAL_LINK_TEXT,'发布话题'),3)
web_api.ele_click((By.XPATH,'//*[@id="tab-value"]'))
web_api.ele_click((By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/form/fieldset/select/option[3]"]'))

web_api.close()
