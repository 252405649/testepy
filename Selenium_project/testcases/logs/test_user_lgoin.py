from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from util import util
import pytest

class TestUserLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

    #测试登录验证码错误self.logger = util.get_logger()
    def test_user_login_error(self):
        username = 'admin'
        pwd = '123456'
        expected = '验证码不正确'
        captcha = 'asd1'
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        self.logger.debug('用户输入名称： %s', username)
        self.logger.debug('用户输入密码： %s', pwd)
        self.logger.debug('用户输入验证码： %s', captcha)
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print(alert.text)
        try:
            assert alert.text == expected
        except AssertionError as ae:
            self.logger.error("用户登陆错误", exc_info=1)
        alert.accept()

    #测试登录正确的
    def test_user_login_ok(self):
        username = 'admin'
        pwd = '123456'
        expected = '用户中心.'
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'captcha').clear()

        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        #自动识别验证码
        captcha = util.get_code(self.driver, 'captchaimg')
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        self.logger.debug('用户输入名称： %s', username)
        self.logger.debug('用户输入密码： %s', pwd)
        self.logger.debug('用户输入验证码： %s', captcha)
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver,5).until(EC.alert_is_present())

        try:
            assert self.driver.text == expected
        except AssertionError as ae:
            self.logger.error("用户登陆错误", exc_info =1)
        sleep(2)

if __name__ == '__main__':
    pytest.main(['test_user_login.py'])