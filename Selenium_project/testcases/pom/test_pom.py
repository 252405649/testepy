from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By
import unittest

class BaiduPage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.input_element = (By.ID, 'kw')
        self.btn_element = (By.ID, 'su')
    def goto_baidu(self, url):
        self.driver.get(url)
    def baidu_search(self, url, kw):
        self.driver.get(url)
        self.driver.find_element(*self.input_element).send_keys(kw)
        self.driver.find_element(*self.btn_element).click()
        sleep(2)


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.baiduPage = BaiduPage()

    def test_search(self):
        self.baiduPage.baidu_search('http://baidu.com', 'selenium')

if __name__ == '__main__':
    unittest.main()