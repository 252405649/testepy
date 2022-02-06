# print("abc",end='\n\n')
# print('vvvv')
#
# def func (a, b,c):
#     print('a= %s' %a)
#     print('b= %s' %b)
#     print('c= %s' %c)
#
#
# func(1,c=4)

# #获取参数的个数
# def howlong(frist, *other):
#     print(other[0])
#     print(1+other[0])
#
# howlong(1,2)

# 作用域
# var1 = 123
# def func():
#     global var1;
#     var1 = 456
#     print(var1)
#
# func()
# print(var1)

# list1 = [1, 2, 4]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) # except

# for i in range(10, 20,0.5):
#     print(i)

# def frange(star, stop, step):
#     x = star
#     while x <= stop:
#          x
#         x += step
#
# for i in frange(1,5,0.5):
#     print(i)

def true(): return True
lambda : True

# lambda x,y: x+y
# from functools import reduce

#reduce1 2 合并成key value形式
# print(reduce(lambda x,y: x+y, [1,2,3],4))
# a = zip((1,2,3),(4,21,3))
# print(dict(zip((1,2,3),(4,21,3))))


# #zip : key 和value互换位子
# dicta = {'a': 'aa', 'b': 'bb'}
# dictb = zip(dicta.values(),dicta.keys())
# print(dict(dictb))

# map

a = [1,2,3]
print(list(map(lambda x:x+1 , a)))
b =[4,5,6]
print(list(map(lambda x,y:x+y , a,b)))

#filter  过滤
print(list(filter(lambda x:x>1, a)))




