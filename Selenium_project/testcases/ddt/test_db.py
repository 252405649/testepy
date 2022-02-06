import MySQLdb
import pytest

conn = MySQLdb.connect(
    user = 'root',
    password='123456',
    host='localhost',
    port=3306,
    db='testing_db'
)

def get_data():
    query_sql = 'select id, username, pwd from user_tbl'
    lst = []
    try:
        cursor = conn.cursor()
        cursor.execute(query_sql)
        r = cursor.fetchall()
        for x in r:
            u = (x[0], x[1], x[2])
            lst.append(u)
        return lst
    except ConnectionError as e:
        print('error:' + e)
    finally:
        cursor.close()
@pytest.mark.parametrize('id, name, pwd', get_data())
def test01(id, name, pwd):
    print(id, name, pwd)

if __name__ == '__main__':
    # get_data()
     pytest.main('-sv', 'test_db.py')