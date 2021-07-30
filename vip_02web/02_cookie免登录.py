# coding = utf-8

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('https://pan.baidu.com/')

# 手动做一个登录操作，获取cookies
# time.sleep(60)
# cookies = driver.get_cookies()
# print(cookies)

cookies = [{'name': 'BAIDUID', 'value': '175C86ED687DCF26773FFE6D77AC1E0E:FG=1', 'path': '/', 'domain': '.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 1658305875}, {'name': 'BDUSS', 'value': 'mtwNVFna0ppclBLaG5mcElzU09JbFo3NFhselhFRXZRRjFiS3BXamwzfmZGaDVoSVFBQUFBJCQAAAAAAAAAAAEAAAAa-42oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN-J9mDfifZgN', 'path': '/', 'domain': '.baidu.com', 'secure': False, 'httpOnly': True, 'expiry': 1885969888}, {'name': 'pan_login_way', 'value': '1', 'path': '/', 'domain': 'pan.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 4218769889}, {'name': 'csrfToken', 'value': '683PXGsk-mNh55bYW9JLWL-I', 'path': '/', 'domain': 'pan.baidu.com', 'secure': False, 'httpOnly': False}, {'name': 'STOKEN', 'value': '0444f22e1cda199bc8c7390ba07bdeb6c78a657139cc6efd73f089adcb642c17', 'path': '/', 'domain': '.pan.baidu.com', 'secure': False, 'httpOnly': True, 'expiry': 1629448289}, {'name': 'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', 'value': '1626769890', 'path': '/', 'domain': '.pan.baidu.com', 'secure': False, 'httpOnly': False, 'expiry': 1658305889}, {'name': 'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', 'value': '1626769890', 'path': '/', 'domain': '.pan.baidu.com', 'secure': False, 'httpOnly': False}, {'name': 'PANPSC', 'value': '16598740064202809019%3AHSTAF2XekfrGVlXIeiN%2BE3libiKzYuqj1cOxG%2BadPe4gW%2FcF1mpNt0ci2O0YbEjp2%2F4VCsSoEpyNS0fevMTvAKKK%2FFH5WUxXYzQxFe2ZxZXEHd8Y8cGAwXZNBoZ8i0CTW8pfgMw2m%2FoeGDMyMjs7itnzWX47O8AWDB1fJR5h5SrRS1QGHwZcOH1t8VXlRfZV', 'path': '/', 'domain': '.pan.baidu.com', 'secure': False, 'httpOnly': True, 'expiry': 1626856289}]
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(3)
driver.get('https://pan.baidu.com/')
