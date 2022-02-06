from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from testcases.ddt.test_admin_lgoin import TestAdminLogin
from testcases.pom.ddt.pages.categoryPage import CategoryPage
import pytest
from util import util

class TestCategory(object):
    def setup_class(self):
        self.login = TestAdminLogin
        self.logger = util.get_logger()
        self.categoryPage = CategoryPage(self.login)
    category_data = [
        ('','python','test','分类名称不能为空'),
        ('test','python','test','文章分类保存成功')
    ]

    # 测试文章分类成功
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    @pytest.mark.parametrize('name,parent,slug,expected', category_data)
    def test_add_category_ok(self, name, parent, slug, expected):
            if name == '':
                # 点击文章
                self.categoryPage.click_article()
                # 点击分类
                self.categoryPage.click_category()
            sleep(1)
            # 输入分类名称
            self.categoryPage.input_category_name(name)
            self.categoryPage.select_parent_category(parent)
            # 输入slug
            self.categoryPage.input_slug(slug)
            # 点击添加
            self.categoryPage.click_add_btn()
            if name == '':
                loc = (By.CLASS_NAME, 'toast-container').text
                # 等待最多五秒提示框弹出
                WebDriverWait(self.login.driver, 5).until(EC.visibility_of_all_elements_located(loc))
                msg = self.login.driver.find_element(*loc).text
                assert msg == expected
            else:
                assert 1==1

if __name__ == '__main__':
    pytest.main(['test_category.py'])