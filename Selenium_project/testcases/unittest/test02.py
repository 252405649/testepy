import unittest
import os

class MyTestCase3(unittest.TestCase):
    #打开数据库
    def test01(self):
        print('test01')
        self.assertEqual(1+2, 3)
    def test02(self):
        print('test02')
        # self.assertGreaterEqual(5,4)
        self.assertEqual(1,1)
class MyTestCase4(unittest.TestCase):
    def test03(self):
        print('test03')
        self.assertEqual(1+2, 3)
    def test04(self):
        print('test04')
        self.assertEqual(1,1)

if __name__ == '__main__':
    #实例化
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    #方法一：通过测试用例类进行加载
    # suite.addTest(loader.loadTestsFromTestCase(MyTestCase3))
    # suite.addTest(loader.loadTestsFromTestCase(MyTestCase4))

    # #方法二：通过测试用例模块加载
    # suite.addTest(loader.loadTestsFromModule(MyTestCase3))
    # suite.addTest(loader.loadTestsFromModule(MyTestCase4))

    #方法三： 通过路径加载
    path = os.path.abspath(os.path.abspath(__file__))
    suite.addTest(loader.discover(path))
    # #方法四
    # case4 = MyTestCase4()
    # suite.addTest(case4)

    runner = unittest.TextTestRunner()
    runner.run()
