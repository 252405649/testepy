import pytest

class TestCase02(object):
    @pytest.mark.do
    def test01(self):
        print('test01-----------')
        assert 1==1
        self.add()
    @pytest.mark.do
    def test02(self):
        print('test02-----------')
        assert 2==2
    @pytest.mark.undo
    def test03(self):
        print('test03-----------')
        assert 2==2

    def add(self):
        print('-----add')
