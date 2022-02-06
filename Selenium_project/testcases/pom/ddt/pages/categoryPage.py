from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from testcases.pom.ddt.pages.basePage import BasePage


class CategoryPage(BasePage):

    def __init__(self, login):
        BasePage.__init__(self, login.driver)
    #点击文章loc
    click_article_loc = (By.XPATH, '//*[@id="article"]/a')
    #分类loc
    click_category_loc = (By.XPATH, '//*[@id="分类--/admin/article/category"]/a')
    #分类名称loc
    category_name_loc = (By.NAME, 'category.title')
    #父分类loc
    parent_category_loc = (By.NAME, 'category.pid')
    # sulg loc
    sulg_loc = (By.NAME, 'category.sulg')
    # 添加按钮
    add_btn_loc = (By.XPATH, '/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/div/div/button')

    # 点击文章
    def click_article(self):
        self.click(*self.click_article_loc)

    #点击分类
    def click_category(self):
        self.click(*self.click_category_loc)
    #输入分类名称
    def input_category_name(self, name):
        self.input_text(name, *self.category_name_loc)

    # 选择父分类
    def select_parent_category(self, parent_name):
        parent_category_elem = self.find_element(*self.parent_category_loc)
        Select(parent_category_elem).select_by_visible_text(parent_name)

    #输入slug
    def input_slug(self, slug):
        self.input_text(slug, *self.sulg_loc)

    # 点击添加
    def click_add_btn(self):
        self.click(*self.add_btn_loc)