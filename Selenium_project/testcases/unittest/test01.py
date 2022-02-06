import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        #初始化driver
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
        cls.driver.maximize_window()
        print('setUpClass--------')
    def setUp(self):
        super().setUp()
        print('setup---------------')
    def tearDown(self):
        #关闭数据库
        print('tearDown-----------------')
    #打开数据库
    def test01(self):
        print('test01')
        self.driver.find_element(By.ID, 'kw').send_keys('dsadsada')
        self.assertEqual(1+2, 3)
    def test02(self):
        print('test02')
        # self.assertGreaterEqual(5,4)
        self.assertEqual(1,1)
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        print('tearDownClass--------')
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main

MyTestCase