from  selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/test_alert.html'
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element(By.ID, 'alert').click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
        self.driver.quit()
    def test_confirm(self):
        self.driver.find_element(By.ID, 'confirm').click()
        confirm =self.driver.switch_to.alert
        print(confirm.text)
        #accept 确定 dismiss 取消
        # confirm.accept()
        confirm.dismiss()

    def test_prompt(self):
        self.driver.find_element(By.ID, 'prompt').click()
        sleep(3)
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        # accept 确定 dismiss 取消
        sleep(3)
        # prompt.accept()



if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()