# coding = utf-8

from selenium import webdriver
import time
from PIL import Image, ImageDraw
from matplotlib import pyplot, pylab

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://passport.ganji.com/register.php?next=/')
driver.maximize_window()
window_path = './img/windowImg'+str(int(time.time()))+'.png'
driver.get_screenshot_as_file(window_path)
code_ele = driver.find_element_by_id('img_phone_checkcode')
left = code_ele.location['x']
top = code_ele.location['y']
right = left + code_ele.size['width']
bottom = top + code_ele.size['height']
print(left, top, right, bottom)
# box=(922,691,1163,758)

window_img = Image.open(window_path)

code_img = window_img.crop((left*2, top*2, right*2, bottom*2))
code_img.save('./img/code'+str(int(time.time()))+'.png')
code_img.show()
# draw_img = ImageDraw.Draw(window_img)
# draw_img.rectangle([left, top, right, bottom], outline='RED')
# window_img.show()

# img_lab = pylab.array(window_img)
# pyplot.imshow(window_img)
#
# X = pyplot.ginput(4)
# print("点击了：",X)