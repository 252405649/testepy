from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.remote.webelement import WebElement


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sahitest.com/demo/clicks.htm')

    # 鼠标
    def test_mouse(self):
        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()

        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()

        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()

    # 键盘
    def test_key(self):
        self.driver.get('http://www.baidu.com')
        # kw = self.driver.find_element(By.ID, 'kw')
        # kw.send_keys('selenium')
        # kw.send_keys(Keys.CONTROL, 'a')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, 'x')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, 'v')
        # e = self.driver.find_element(By.XPATH, '//*[@id="s_tab"]/div/a[1]')
        e = self.driver.find_element_by_link_text('新闻')
        print(e)
        ActionChains(self.driver).move_to_element(e).click().perform()
if __name__ == '__main__':
    case = TestCase()
    # case.test_mouse()
    case.test_key()