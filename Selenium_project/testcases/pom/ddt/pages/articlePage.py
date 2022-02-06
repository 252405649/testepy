from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from testcases.pom.ddt.pages.basePage import BasePage


class ArticlePage(BasePage):
    # 点击文章loc
    click_article_loc = (By.XPATH, '//*[@id="article"]/a')
    #点击文章管理loc
    click_article_list_loc = (By.XPATH, '//*[@id="文章管理--/admin/article/list"]/a')
    # 写文章loc
    click_write_article_loc = (By.XPATH, '//*[@id="写文章--/admin/article/write"]/a')
    #点击第一个文章
    click_first_article_loc = (By.XPATH, '/html/body/div/div[1]/section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/strong/a')
    # 文章名称loc
    article_title_loc = (By.ID, 'article-title')
    #富文本名称loc
    iframe_loc = (By.XPATH, '//*[@id="editor"]/iframe')
    # 富文本输入内容loc
    content_loc =(By.XPATH, '/html/body')
    # 发布文章loc
    add_btn_loc =(By.XPATH, '//*[@id="form"]/div/div[2]/div[1]/div/button[1]')
    #删除单个文章
    del_bt_loc = (By.XPATH, '/html/body/div/div[1]/section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/div/div/a[3]')
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 点击文章
    def click_article_btn(self):
        self.click(*self.click_article_loc)

    #点击写文章
    def click_write_article(self):
        self.click(*self.click_category_loc)
    # 点击文章管理
    def click_article_list(self):
        self.click(*self.click_article_list_loc)

    # 选中第一个文章
    def click_first_article(self):
        link = self.click(*self.click_first_article_loc)
        # 移动鼠标到第一个文章上面
        ActionChains(self.driver).move_to_element(link).perform()
    #输入文章名称
    def input_article_title(self, title):
        self.input_text(title, *self.category_name_loc)

    # 输入文章内容
    def select_parent_category(self, content):
        # 因为数富文本要选择 iframe
        frame1 = self.get_element(*self.iframe_loc)
        # 切入到富文本
        self.switch_to.frame(frame1)
        # 输如富文本内容
        self.input_text(content, *self.content_loc)
        # 跳出富文本
        self.switch_to.default_content()


    # 点击添加
    def click_add_btn(self):
        self.click(*self.add_btn_loc)

    def del_single_article(self):
        self.click(*self.del_bt_loc)
