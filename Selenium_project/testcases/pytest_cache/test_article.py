from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from testcases.pytest_cache.test_admin_lgoin import TestAdminLogin
import unittest
import pytest

class TestArticle(object):
    def setup_class(self):
        self.login = TestAdminLogin

    #测试文章分类失败，名称为空
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_add_ok(self):
        title = '我的文章'
        content = '我的文章内容'
        expected = '文章保存成功'
       #点击文章分类
        self.login.driver.find_element(By.XPATH, '//*[@id="article"]/a').click()
        sleep(1)
        #点击写文章
        self.login.driver.find_element(By.XPATH, '//*[@id="写文章--/admin/article/write"]/a').click()
        sleep(1)
        #输入文章名称
        self.login.driver.find_element(By.ID, 'article-title').send_keys(title)
        #因为数富文本要选择 iframe
        frame1 = self.login.driver.find_element(By.XPATH, '//*[@id="editor"]/iframe')
        #切入到富文本
        self.login.driver.switch_to.frame(frame1)
        sleep(1)
        #输如富文本内容
        self.login.driver.find_element(By.XPATH, '/html/body').send_keys(content)
        #跳出富文本
        self.login.driver.switch_to.default_content()

        # 点击发布按钮
        self.login.driver.find_element(By.XPATH, '//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()
        loc = (By.CLASS_NAME, 'toast-container').text
        #等待最多五秒提示框弹出
        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_all_elements_located(loc))
        msg = self.login.driver.find_element(*loc).text
        assert msg == expected

    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_del_one_article_ok(self):

            # 点击文章            ''
            self.login.driver.find_element(By.XPATH, '//*[@id="文章管理--/admin/article/list"]/a').click()
            sleep(1)
            # 选中第一个文章
            link = self.login.driver.find_element(By.XPATH, '/html/body/div/div[1]/section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/strong/a')
            #移动鼠标到第一个文章上面
            ActionChains(self.login.driver).move_to_element(link).perform()
            #删除当前文章
            del_elem = self.login.driver.find_element(By.XPATH,'/html/body/div/div[1]/section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/div/div/a[3]')
            del_elem.click()
            sleep(1)
if __name__ == '__main__':
    pytest.main(['test_article.py'])