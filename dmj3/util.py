from selenium.webdriver.common.by import By
from selenium import webdriver

def get_element(driver, *loc):
    element = driver.find_element(*loc)
    return element


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    get_element(driver, By.ID, 'kw').send_keys('selenium')
    get_element(driver, By.ID, 'su').click()