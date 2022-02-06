from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from util import util
import pytest

class TestAdminLogin(object):

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.maximize_window()
        self.logger = util.get_logger()
        self.logger.info("管理员登录日志开始")
    #管理员验证码错误
    def test_admin_login_error(self):
        username = 'admin'
        pwd = '123456'
        expected = '验证码不正确，请重新输入'
        captcha = 'asd1'
        print('111111111111')
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
        try:
            assert alert.text == expected
        except AssertionError as ae:
            self.logger.error("验证码输入错误，报异常", exc_info =1)
        alert.accept()

    #d登录成功
    @pytest.mark.dependency(name='admin_login')
    def test_admin_login_ok(self):
        username = 'admin'
        pwd = '123456'
        expected = 'JPress后台'
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        captcha = util.get_code(self.driver, 'captcha-img')
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        self.logger.debug('用户输入名称： %s', username)
        self.logger.debug('用户输入密码： %s', pwd)
        self.logger.debug('用户输入验证码： %s', captcha)
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        try:
            assert expected == self.driver.title
        except AssertionError as ae:
            self.logger.error("验证码输入错误，报异常", exc_info =1)
        sleep(3)

    #测试登录密码错误
    def test_admin_login_pwd_error(self):
        username = 'admin'
        pwd = '312123'
        expected = '用户名或密码不正确.'
        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'captcha').clear()

        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        #自动识别验证码
        captcha = util.get_code(self.driver, 'captcha-img')
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        self.logger.debug('用户输入名称： %s', username)
        self.logger.debug('用户输入密码： %s', pwd)
        self.logger.debug('用户输入验证码： %s', captcha)
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        try:
            assert self.driver.switch_to.alert.text == expected
        except AssertionError as ae:
            self.logger.error("验证码输入错误，报异常", exc_info=1)
        sleep(2)

if __name__ == '__main__':
    pytest.main(['test_admin_login.py'])