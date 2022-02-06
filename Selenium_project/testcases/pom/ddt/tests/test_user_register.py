from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from testcases.pom.ddt.pages.userRegisterPage import UserRegisterPage
from util import util
import pytest

class TestUserRegister(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()
        self.logger = util.get_logger()
        self.registerPage = UserRegisterPage()
    register_data = [
        ('test001', 'test001@qq.com', '123456', '666', '验证码不正确'),
        ('test002', 'test002@qq.com', '123456', '', '注册成功，点击确定进行登录')
    ]
    #测试登录验证码错误
    @pytest.mark.parametrize('username, email, pwd, confirmPwd, captcha, expected', register_data)
    def test_ragister_code_ok(self, username, email, pwd, confirmPwd, captcha, expected):
        self.registerPage.input_username(username)
        self.registerPage.input_email(email)
        self.registerPage.input_pwd(pwd)
        self.registerPage.input_confirm_pwd(confirmPwd)
        if captcha != '666':
            #自动识别验证码
            captcha = util.get_code(self.driver, 'captchaimg')
        self.registerPage.input_captcha(captcha)
        self.registerPage.click_register_btn()
        #等待最多五秒提示框弹出
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        try:
            assert alert.text == expected
        except AssertionError as ae:
            self.logger.error("注册失败", exc_info=1)
        alert.accept()
        sleep(2)

if __name__ == '__main__':
    pytest.main(['test_user_register.py'])