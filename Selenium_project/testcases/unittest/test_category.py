from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from util import util

class TestCategory(object):
    def __init__(self, login):
        self.login = login

    #测试文章分类失败，名称为空
    def test_add_category_error(self):
        name = ''
        #前置条件
        parent= 'python'
        slug = 'test'
        expected = '分类名称不能为空'
       #点击文章            ''
        self.login.driver.find_element(By.XPATH, '//*[@id="article"]/a').click()
        sleep(1)
        #点击分类
        self.login.driver.find_element(By.XPATH, '//*[@id="分类--/admin/article/category"]/a').click()
        sleep(1)
        #输入分类名称
        self.login.driver.find_element(By.NAME, 'category.title').send_keys(name)
        #选择父分类
        parent_category_elem = self.login.driver.find_element(By.NAME, 'category.pid')
        #Select
        Select(parent_category_elem).select_by_visible_text(parent)
        #输入slug
        self.login.driver.find_element(By.NAME, 'category.slug').send_keys(slug)
        # 点击添加
        self.login.driver.find_element(By.XPATH, '/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()
        loc = (By.CLASS_NAME, 'toast-container').text
        #等待最多五秒提示框弹出
        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_all_elements_located(loc))
        msg = self.login.driver.find_element(*loc).text
        assert msg == expected
        # 测试文章分类失败，名称为空
    def test_add_category_ok(self):
            name = 'dmj'
            # 前置条件
            parent = 'python'
            slug = 'test'
            expected = '文章分类保存成功'
            # 点击文章            ''
            self.login.driver.find_element(By.XPATH, '//*[@id="article"]/a').click()
            sleep(1)
            # 点击分类
            self.login.driver.find_element(By.XPATH, '//*[@id="分类--/admin/article/category"]/a').click()
            sleep(1)
            # 输入分类名称
            self.login.driver.find_element(By.NAME, 'category.title').send_keys(name)
            # 选择父分类
            parent_category_elem = self.login.driver.find_element(By.NAME, 'category.pid')
            # Select
            Select(parent_category_elem).select_by_visible_text(parent)
            # 输入slug
            self.login.driver.find_element(By.NAME, 'category.slug').send_keys(slug)
            # 点击添加
            self.login.driver.find_element(By.XPATH,
                                     '/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()
            sleep(5)
            # loc = (By.CLASS_NAME, 'toast-container').text
            # # 等待最多五秒提示框弹出
            # WebDriverWait(self.login.driver, 5).until(EC.visibility_of_all_elements_located(loc))
            # msg = self.login.driver.find_element(*loc).text
