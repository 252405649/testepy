from  selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/form3.html'
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element(By.ID, 'provise')
        select = Select(se)
        # select.select_by_index(2)
        # sleep(2)
        # select.select_by_value('sz')
        # select.select_by_visible_text('BeiJing')
        # sleep(2)

        for i in range(4):
            select.select_by_index(i)
            sleep(1)
        select.deselect_all()
        for option in select.options:
            print(option.text)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_select()