from selenium.webdriver.common.by import By


def test1():
    print('test1')

from selenium import webdriver
from time import sleep
import pyautogui
def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.jpress.io/user/register')
    driver.maximize_window()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys('董明姣')
    elem = driver.find_element(By.ID, 'agree')
    rect = elem.rect
    pyautogui.click(rect['x']+10, rect['y']+130)
    sleep(5)