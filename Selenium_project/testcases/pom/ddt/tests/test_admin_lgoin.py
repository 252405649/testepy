from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from testcases.pom.ddt.pages.adminLoginPage import AdminLoginPage
from util import util
import pytest

class TestAdminLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.maximize_window()
        self.adminLoginPage = AdminLoginPage()
    login_data = {
        ('dsada', '123456', '6666', '用户名或密码不正确'),
        ('admin','213213', '', '用户名或密码不正确'),
        ('admin', '123456', '', '用户中心')
    }
    #d登录成功
    @pytest.mark.dependency(name='admin_login')
    @pytest.mark.parametrize('username,pwd,captcha,expected', login_data)
    def test_admin_login_ok(self, username, pwd, captcha,expected):
        self.adminLoginPage.input_username(username)
        self.adminLoginPage.input_pwd(pwd)
        if captcha!= '6666':
            captcha = util.get_code(self.driver, 'captcha-img')
        if expected == '用户中心':
            self.adminLoginPage.input_captcha(captcha)
            self.adminLoginPage.click_admin_login_btn()
            # 等待最多五秒提示框弹出
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            assert expected == self.driver.title

        else:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == expected
            alert.accept()


if __name__ == '__main__':
    pytest.main(['test_admin_login.py'])