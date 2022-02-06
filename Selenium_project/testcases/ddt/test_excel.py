import  pytest
import xlrd

def get_data():
    filename = 'test.xls'
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    lst = []

    for row in range(rows):
        for col in range(cols):
            cell_data = sheet.cell_value(row,col)
            print(cell_data)
            lst.append(cell_data)

    return lst

@pytest.mark.parametrize('name', get_data())
def test01(name):
    print(name)

if __name__ == '__main__':
    # get_data()
     pytest.main('-sv', 'test_excel.py')