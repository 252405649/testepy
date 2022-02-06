import os
from time import sleep, strftime, localtime,time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def test1(self):
        self.driver.find_element(By.ID, "kw").send_keys('selenium')
        self.driver.find_element(By.ID, "su").click()
        sleep(2)
        # self.driver.save_screenshot('baidu.png')

        st = strftime('%Y-%m-%d %H-%M-%S', localtime(time()))
        file_name = st+'.png'

        # self.driver.save_screenshot(file_name)

        path =os.path.abspath('images')
        file_path = path + '\\' + file_name
        print(file_path)
        self.driver.get_screenshot_as_file(file_path)
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    case.test1()