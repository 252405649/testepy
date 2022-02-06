from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
    def test_sllep(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
        self.driver.quit()

    def test_implicitly_wait(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        self.driver.quit()
    def test_implicitly_wait(self):
        wait = WebDriverWait(self.driver,2)
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    # case.test_sllep()
    # case.test_implicitly_wait()
    case.test_implicitly_wait()
