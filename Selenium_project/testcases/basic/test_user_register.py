from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from util import util

class TestUserRegister(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()

    #测试登录验证码错误
    def test_ragister_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = '666'
        expected = '验证码不正确'

        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.NAME, 'confirmPwd').send_keys(confirmPwd)
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print('--------------------')
        print(alert.text)
        assert alert.text == expected
        alert.accept()

    #测试登录验证码错误
    def test_ragister_code_ok(self):
        username = util.gen_random_str()
        email = username +'@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        expected = '注册成功，点击确定进行登录.'
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'email').clear()
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'confirmPwd').clear()
        self.driver.find_element(By.NAME, 'captcha').clear()

        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.NAME, 'confirmPwd').send_keys(confirmPwd)
        #自动识别验证码
        captcha = util.get_code(self.driver, 'captchaimg')
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected
        alert.accept()
        sleep(2)
