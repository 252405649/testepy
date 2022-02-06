import pytest

@pytest.fixture(scope='session')
def init():
    print('init----------')
    return 1

def test1(init):
    print('test1')

def test2(init):
    print('test2')

if __name__ == '__main__':
    pytest.main(['-sv', 'test06.py'])