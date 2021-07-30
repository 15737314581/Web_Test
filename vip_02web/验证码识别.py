# coding = utf-8

# encoding:utf-8

import requests
import base64

'''
通用文字识别
'''
'''获取token的接口'''
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=7ECj6hF5ELCXGbOwgncWtZK7&client_secret=d6c6bZecIcXZwOAIr6omARHRNR6y8z8G'
response = requests.get(host)
if response:
    print(response.json())
token = response.json()['access_token']
# 识别图片的接口
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open('./img/code.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = token
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())