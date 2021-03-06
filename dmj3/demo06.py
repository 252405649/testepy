from  selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/form2.html'
        self.driver.get(file_path)

    def test_checkbox(self):
        swimming = self.driver.find_element(By.NAME, 'swimming')
        if not swimming.is_selected():
            swimming.click()
        reading = self.driver.find_element(By.NAME, 'reading')
        if not reading.is_selected():
            reading.click()
        sleep(2)
        self.driver.quit()

    def test_radio(self):
        lst = self.driver.find_elements(By.NAME, 'gender')
        lst[1].click()

if __name__ == '__main__':
    case = TestCase()
    # case.test_checkbox()
    case.test_radio()