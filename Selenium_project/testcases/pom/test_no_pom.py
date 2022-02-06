from time import sleep

from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_baidu(self):
        self.driver.get('http://baidu.com')
        self.driver.find_element(By.ID, 'kw').send_keys('dsadas')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

TestBaidu