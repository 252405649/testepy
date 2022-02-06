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
    login_data = {
        ('', '123456', '6666', '用户名或密码不正确'),
        ('sunk','213213', '', '用户名或密码不正确'),
        ('sunk', '123456', '', '用户中心')
    }
    #测试登录正确的
    @pytest.mark.dependency(name='user_login')
    @pytest.mark.parametrize('username,pwd,captcha,expected', login_data)
    def test_user_login_ok(self, username, pwd, captcha,expected):
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'pwd').clear()

        self.driver.find_element(By.NAME, 'captcha').clear()
        self.driver.find_element(By.NAME, 'username').send_keys(username)

        self.driver.find_element(By.NAME, 'pwd').send_keys(pwd)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        if captcha!= '6666':
            captcha = util.get_code(self.driver, 'captchaimg')
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        if expected == '用户中心':
            # 等待最多五秒提示框弹出
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            assert expected == self.driver.title
        else:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == expected
            alert.accept()
        sleep(2)

if __name__ == '__main__':
    pytest.main(['test_user_login.py'])