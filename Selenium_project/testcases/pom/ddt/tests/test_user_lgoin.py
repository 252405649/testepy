from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from testcases.pom.ddt.pages.userLoginPage import UserLoginrPage
from util import util
import pytest

class TestUserLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()
        self.loginPage = UserLoginrPage()
    login_data = {
        ('', '123456', '666', '用户名或密码不正确'),
        ('sunk','213213', '', '用户名或密码不正确'),
        ('sunk', '123456', '', '用户中心')
    }
    #测试登录正确的
    @pytest.mark.dependency(name='user_login')
    @pytest.mark.parametrize('username,pwd,captcha,expected', login_data)
    def test_user_login_ok(self, username, pwd, captcha,expected):
        self.loginPage.input_username(username)
        self.loginPage.input_pwd(pwd)
        if captcha!= '666':
            captcha = util.get_code(self.driver, 'captchaimg')
        self.loginPage.input_captcha(captcha)
        self.loginPage.click_register_btn()
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