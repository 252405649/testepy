import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.abspath('test_wait10.html')
        file_path = 'file:///' + path
        self.driver.get(file_path)

    def test_implicitly_wait(self):
        self.driver.find_element(By.ID, 'btn').click()
        # 显示等待
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.text_to_be_present_in_element((By.ID,'id2'), 'id2'))
        print(self.driver.find_element(By.ID, 'id2').text)
        print('ok')
if __name__ == '__main__':
    case = TestCase()
    case.test_implicitly_wait()
