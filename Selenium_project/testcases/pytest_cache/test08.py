import pytest
import allure

@pytest.fixture(scope='session')
def login():
    print('用户登录，保存信息')

@allure.step('步骤1：点击XXX')
def step_1():
    print('1111')

@allure.step('步骤2：点击XXX')
def step_2():
    print('222222')

@allure.feature('编辑页面')
class TestEditPage(object):
    @allure.story("这是一个xx的用例")
    def test_1(self, login):
        '''用例描述：先登录,在执行XX'''
        step_1()
        step_2()
        print('xxxx')

    @allure.story("打开a页面")
    def test_2(self, login):
        '''用例描述：先登录,在执行yyyy'''

        print('yyyyy')

if __name__ == '__main__':
    #注意生产测试报告 必须在命令行执行
    # pytest --alluredir ./report test08.py
    # allure serve ./report 启动allure 查看报告
    pytest.main(['alluredir', './reports', 'test08.py'])
    pytest.main(['alluredir', './reports', 'test08.py'])
