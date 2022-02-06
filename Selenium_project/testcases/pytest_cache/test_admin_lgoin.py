from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from util import util
from selenium import webdriver
import pytest

class TestAdminLogin(object):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.maximize_window()

    #管理员验证码错误
    def test_admin_login_error(self):
        username = 'admin'
        pwd = '123456'
        expected = '验证码不正确，请重新输入'
        captcha = 'asd1'
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected
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
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        assert expected == self.driver.title
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
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        assert  self.driver.switch_to.alert.text == expected
        sleep(2)

if __name__ == '__main__':
    pytest.main(['test_admin_login.py'])