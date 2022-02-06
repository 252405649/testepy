from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.remote.webelement import WebElement


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')


    # 键盘
    def test1(self):
        self.driver.execute_script("alert('text')")
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test3(self):
        js = 'var q = document.getElementById("kw"); q.style.border= "2px solid red"'
        self.driver.execute_script(js)

    def test4(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        title = self.driver.execute_script(js)
        sleep(2)
if __name__ == '__main__':
    case = TestCase()
    # case.test1()
    # case.test2()
    case.test3()
    # case.test4()