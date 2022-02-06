from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep



class TestCase(object):
    def __init__(self):
        # from .chrome.webdriver import WebDriver as Chrome  # noqa
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        # self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        element = self.driver.find_element(By.ID, 'kw')
        element.send_keys('selenium')
        print(type(element))
        self.driver.find_element(By.ID, 'su').click()
        sleep(1)
        # self.driver.quit()

    def test_name(self):
        element = self.driver.find_element(By.NAME,'wd')
        element.send_keys('selenium')
        print(type(element))
        self.driver.find_element(By.ID, 'su').click()
        sleep(1)
        self.driver.quit()

    def test_linktext(self):
        self.test_id()
        self.driver.find_element_by_link_text( '首页').click()
        sleep(3)

    def test_partial_linktext(self):
        self.test_id()
        self.driver.find_element_by_partial_link_text('百度首页').click()
        sleep(3)
    def test_xath(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('sadas')
        self.driver.find_element(By.ID, 'su').click()
    def text_tag(self):
        input = self.driver.find_element(By.TAG_NAME,'input')
        print(input)
    def test_css_selector(self):
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('董明姣')
        self.driver.find_element(By.ID, 'su').click()

    def test_calss_name(self):
        self.driver.find_element(By.CLASS_NAME, 's_ipt').send_keys('董明姣')
        self.driver.find_element(By.ID, 'su').click()
    def test_all(self):
        element = self.driver.find_element(value='kw').send_keys('董小胖')
        self.driver.find_element(By.ID, 'su').click()
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    # case.test_id()
    # case.test_name()
    # case.test_partial_linktext()
    # case.test_xath()
    # case.text_tag()
    # case.test_css_selector()
    # case.test_calss_name()
    case.test_all()