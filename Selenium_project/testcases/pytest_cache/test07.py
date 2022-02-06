import pytest


class TestCase01(object):
    @classmethod
    def setup_class(cls):
        print('setup_class------5555--')
    @classmethod
    def teardown_class(cls):
        print('teardown_class------66666--')
    def setup(self):
        print('setup----777-')
    def teardown(cls):
        print('teardown------888--')
    def test03(self):
        print('----test03')
    def test04(self):
        print('----test04')

TestCase01
def setup_function():
    print('setup_function-----11----')

def teardown_function():
    print('teardown_function-----22----')


def setup_module():
    print('setup_module-----333----')


def teardown_module():
    print('teardown_function----444-----')

def test1():
    print('test1')

def test2():
    print('test2')

if __name__ == '__main__':
    pytest.main(['test07.py', '-vs'])