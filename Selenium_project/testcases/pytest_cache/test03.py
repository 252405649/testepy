import pytest

class TestCase02(object):

    def test01(self):
        print('test01-----------')
        assert 1==1
        self.add()
    def test02(self):
        print('test02-----------')
        assert 2==2
    def add(self):
        print('-----add')

if __name__ == '__main__':
    pytest,map('-s','-v', 'test02.py')