from pandas import Series, DataFrame
# import pandas as pd

# obj =Series([4,5,6,-7])
# print(obj)
# print(obj.index)
# print(obj.values)

# obj2 = Series([4,7,-5,3],index=['a','c','b','d'])
# print(obj2)
# obj2['c'] = 7
# print(obj2)
# print('c' in obj2)

# sdata = {'beijing': 1100, 'shanghai': 2100, 'wuhan': 6100, 'shenzhen': 5000}
# obj3 = Series(sdata)
# print(obj3)
# obj3.index = ['bi', 'sh', 'wh', 'sz']
# print(obj3)

data = {'city': ['sh','bj', 'sz', 'gz'],
        'year': [2015,2016,2017,2018],
        'pop': [1.5,2.1,2.6, 3.5]}
frame = DataFrame(data)
frame2 = DataFrame(data, columns=['year', 'pop', 'city'])
# print(frame)
# print(frame2)
#
# print(frame2['city'])
# print(frame2.year)


# frame2['new'] = 100
# print(frame2)
#
# frame2['cap'] = frame2.city == 'bj'
# print(frame2)

pop = {'bj': {2012: 1.8, 2009: 2.0},
       'sh': {2012: 2.5, 2009: 4.1}
       }
frame3 = DataFrame(pop)
print(frame3)
print(frame3.T)

obj4 = Series([4.5, 7.2, -5.3,3.6], index=['a','d','c','b'])
obj5 = obj4.reindex(['a','b','c','d','e'], fill_value=0)
print(obj5)

obj6 = Series(['a','b', 'c'], index=[0,2,4])
# 如果索引位子没有数据：ffill取前一个的值 bfill 取下一个的值
print(obj6.reindex(range(6), method='bfill'))

from numpy import nan as NA
data = Series([1,NA,2])
print(data.dropna())

data2 = DataFrame([[1,2,3], [2,NA,NA], [NA,NA,NA]])
data2[4] = NA
print(data2.dropna())
# how=all 删除一行都是NA
# print(dara2.dropna(how='all'))
# axis =1 删除列是NA
print(data2.dropna(axis=1, how='all'))

data2.fillna(0)
# fillna修改的data2副本， 如果想对data2直接修改可以使用： inplace=True
print(data2.fillna(0, inplace=True))
print(data2)

import numpy as np
data3 = Series(np.random.rand(10),
               index=[['a','a','a','b','b','b','c','c','d','d'],
                      [1,2,3,1,2,3,1,2,2,3]])
print(data3.unstack().stack())

print(data3['b':'c'])
