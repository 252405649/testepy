from selenium.webdriver.common.by import By
from testcases.pom.ddt.pages.basePage import BasePage


class UserLoginrPage(BasePage):
    username_input = (By.NAME, 'username')
    pwd_input = (By.NAME, 'pwd')
    captcha_input = (By.NAME, 'captcha')
    btn_click = (By.CLASS_NAME, 'btn')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_register_page(self):
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(*self.username_input)
        self.input_text(username, *self.username_input)

    def input_pwd(self, pwd):
        self.clear(*self.pwd_input)
        self.input_text(pwd, *self.pwd_input)

    def input_captcha(self, captcha):
        self.clear(*self.captcha_input)
        self.input_text(captcha, *self.captcha_input)
    def click_admin_login_btn(self):
        self.click(*self.btn_click)
