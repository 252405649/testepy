import pytest

class TestCase05(object):
    #列表
    data = ['123', '456']
    @pytest.mark.parametrize('pwd', data)
    def test01(self,pwd):
        print(pwd)

    # 元组
    data2 = [
        (1, 2, 3),
        (4, 5, 6)
    ]

    @pytest.mark.parametrize('a, b, c', data2)
    def test02(self, a, b , c):
        print( a, b , c)

    #字典
    data3 =(
        {'user': 1, 'pwd': '123'},
        {'age': 4,'email': 'dsadsa@qq.com' }
    )
    @pytest.mark.parametrize('data', data3)
    def test02(self, data):
        print( data)

    data04 = [
        pytest.param(1,2,3, id="前面a+b=c"),
        pytest.param(4,5,91, id="前面a+b=c")
    ]
    def add(self, a, b):
        return a + b

    @pytest.mark.parametrize('a, b, expect', data04)
    def test02(self, a, b, expect):
        assert self.add(a,b) == expect