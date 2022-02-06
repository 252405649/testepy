from testcases import testcase, testcase2
from testcases.basic.test_user_register import TestUserRegister
from testcases.basic.test_user_lgoin import TestUserLogin
from testcases.basic.test_admin_lgoin import TestAdminLogin
from testcases.basic.test_category import TestCategory
from testcases.basic.test_article import TestArticle
from util import util
if __name__ == '__main__':
    # testcase.test1()
    # testcase.test2()
    # testcase2.test1()
    # testcase2.test2()
    # util.gen_random_str()
    # case = TestUserRegister()
    # case.test_ragister_code_error()

    # case2 = TestUserLogin()
    # case2.test_user_login_error()
    # case3.test_admin_login_pwd_error()
    #每个界面都要有登录信息
    login = TestAdminLogin()
    login.test_admin_login_ok()
    #测试创建分类
    case4 = TestCategory(login)
    # case4.test_add_category_error()
    case4.test_add_category_ok()

    #测试删除
    case5 = TestArticle(login)
    case5.test_add_ok()
    case5.test_del_one_article_ok()