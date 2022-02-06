from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from testcases.ddt.test_admin_lgoin import TestAdminLogin
from testcases.pom.ddt.pages.articlePage import ArticlePage
import unittest
import pytest
from util import util

class TestArticle(unittest.TestCase):
    def setup_class(self):
        self.login = TestAdminLogin
        self.logger = util.get_logger()
        self.articlePage = ArticlePage(self.login)
    article_data = [
        ('我的文章','我的文章32342342','test','文章保存成功')
    ]
    #测试文章分类失败，名称为空
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    @pytest.mark.parametrize('title,content,expected', article_data)
    def test_add_ok(self, title,content,expected):
       #点击文章分类
        self.articlePage.click_article_loc()
        #点击写文章
        self.articlePage.click_write_article()
        #输入文章名称
        self.articlePage.input_article_title(title)
        # 输入文章内容
        self.articlePage.select_parent_category(content)
        # 点击发布按钮
        self.articlePage.click_add_btn()

        loc = (By.CLASS_NAME, 'toast-container').text
        #等待最多五秒提示框弹出
        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_all_elements_located(loc))
        msg = self.login.driver.find_element(*loc).text
        try:
            assert msg == expected
        except AssertionError as ae:
            self.logger.error("文章保存错误，报异常", exc_info =1)

    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_del_one_article_ok(self):

            # 点击文章            ''
            self.articlePage.click_article_list()
            sleep(1)
            # 选中第一个文章
            self.articlePage.click_first_article()
            #删除当前文章
            self.articlePage.del_single_article()
            self.logger.debug('用户删除文章')
            sleep(1)
if __name__ == '__main__':
    pytest.main(['test_article.py'])