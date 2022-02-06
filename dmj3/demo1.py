from selenium.webdriver.common.by import By
from selenium import webdriver

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()

if __name__ == '__main__':
    case = TestCase()
    case.test()



