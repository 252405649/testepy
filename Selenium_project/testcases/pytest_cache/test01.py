import pytest

class TestLoginCase(object):

    def test01(self):
        print('test01-----------')
        assert 1==1
    def test02(self):
        print('test02-----------')
        assert 2==2

if __name__ == '__main__':
    pytest,map('-s','-v', 'test01.py')