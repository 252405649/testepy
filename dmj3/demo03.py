from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(1)
        self.driver.back() # 后退
        sleep(1)
        self.driver.refresh() #刷新
        sleep(1)
        self.driver.forward()   #前进

        self.driver.close()  #只关闭当前tab
        self.driver.quit()  #关闭浏览器

    def test_windos(self):
        self.driver.find_element_by_link_text('新闻')
        windows = self.driver.window_handles
        while 1:
            for w in windows:
                print(w)
                self.driver.switch_to.window(w)
                sleep(2)

if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    # case.test_method()
    case.test_windos()