import pytest
import csv
from time import sleep

def get_data():
    sleep(2)
    with open('test.csv') as f:
        lst = csv.reader(f)
        my_data = []
        for row in lst:
            my_data.extend(row)
        return my_data

@pytest.mark.parametrize('name', get_data())
def test01(name):
    print(name)

if __name__ == '__main__':
    get_data()
    # pytest.main('-sv', 'test_csv.py')
