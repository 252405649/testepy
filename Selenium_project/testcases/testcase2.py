import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract

def test1():
    #打开浏览器
    driver = webdriver.Chrome()
    #打开首页
    driver.get('http://localhost:8080/jpress/user/register')
    driver.maximize_window()
    #获取验证码图片
    t = time.time()
    picture_name1 = str(t)+'.png'
    #截屏
    driver.save_screenshot(picture_name1)

    ce = driver.find_element(By.ID, 'captcha-img')
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top
    im = Image.open(picture_name1)
    # 抠图 ：验证码的图片
    img = im.crop((left, top, right, height))
    t = time.time()
    picture_name2 = str(t)+'.png'
    img.save(picture_name2)
    driver.close()

def test2():
    image1 = Image.open('123.jpg')
    str = pytesseract.image_to_string(image1)
    print('111111')
    print(str)