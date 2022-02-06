import base64
import os

import pickle
import random
import string
import time
import json
import logging
import logging.handlers
from time import strftime, localtime
import datetime
from urllib import parse
from urllib import request as urllib2
from selenium.webdriver.common.by import By
from PIL import Image
from lib.ShowapiRequest import ShowapiRequest


def get_code(driver, id):
    # 获取验证码图片
    t = time.time()
    #获取当前项目路径，拼接制定位置下存放图片
    path = os.path.dirname(os.path.dirname(__file__))+"\\screenshots"
    picture_name1 = path + '\\'+ str(t) + '.png'
    # 截屏
    driver.save_screenshot(picture_name1)

    ce = driver.find_element(By.ID, id)
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top
    im = Image.open(picture_name1)
    #如果屏幕像素过高可能错位，所以获取下像素比例
    dpr = driver.execute_script(' return window.devicePixelRatio')
    # 抠图 ：验证码的图片
    img = im.crop((left*dpr, top*dpr, right*dpr, height*dpr))
    #存放截图的验证码图片
    t = time.time()
    picture_name2 = path + '\\' + str(t) + '.png'
    img.save(picture_name2)

    with open(picture_name2, 'rb') as f:
        image = f.read()
        image_base64 = str(base64.b64encode(image), encoding='utf-8')
    print('----------------------')
    print(image_base64)
    print(picture_name2)
    #调用第三方验证码识别

    host = 'http://yzmplus.market.alicloudapi.com'
    path = '/fzyzm'
    method = 'POST'
    appcode = 'a2420eb580894ec997e19000c9118a41'
    bodys = {}
    url = host + path

    bodys['v_pic'] = image_base64
    bodys['v_type'] = 'cn'
    post_data = parse.urlencode(bodys).encode('utf-8')
    request = urllib2.Request(url, post_data)
    print(post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    # 根据API的要求，定义相对应的Content - Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    rep = json.loads(content)
    if (rep):
        print(rep)
    return rep['v_code']

def get_code2(driver, id):
    # 获取验证码图片
    t = time.time()
    picture_name1 = str(t) + '.png'
    #获取当前项目路径，拼接制定位置下存放图片
    path = os.path.dirname(os.path.dirname(__file__))+"\\screenshots"
    picture_name1 = path + '\\'+ str(t) + '.png'
    # 截屏
    driver.save_screenshot(picture_name1)

    ce = driver.find_element(By.ID, id)
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top
    im = Image.open(picture_name1)
    # 抠图 ：验证码的图片
    img = im.crop((left, top, right, height))
    #存放截图的验证码图片
    t = time.time()
    picture_name2 = path + '\\' + str(t) + '.png'
    img.save(picture_name2)
    #调用第三方验证码识别
    r = ShowapiRequest("http://route.showapi.com/2360-1", "898187", "5ccaec5f4852482dbd50e088fd1c42a5")
    r.addFilePara("img_url", picture_name2)
    res = r.post()
    print(res.json())  # 返回信息
    body = res.json()['showapi_res_body']
    print('----------')
    print(body)
    code = body['Result']
    return code

#生成随机字符串
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters+string.digits, 8))
    print(rand_str)
    return rand_str

# cookie的存储
def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookies)

# 定义日志格
def get_logger():
     path = os.path.dirname(os.path.dirname(__file__)) + "\\logs\\"
     print('path---'+path)
     logger = logging.getLogger('mylogger')
     logger.setLevel(logging.DEBUG)
     date = strftime('%Y-%m-%d', localtime(time.time()))
     rf_handler = logging.handlers.TimedRotatingFileHandler(path+date+'all.log', when='midnight', interval=1, backupCount=7,
                                                            encoding='utf-8', atTime=datetime.time(0, 0, 0, 0), errors=None)
     rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))

     f_handler = logging.FileHandler(path+date+'error.log', encoding='utf-8')
     f_handler.setLevel(logging.ERROR)
     f_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s"))
     logger.addHandler(rf_handler)
     logger.addHandler(f_handler)
     return logger
