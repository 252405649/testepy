# i = j

# print(})

# a = '123'
# print(a[3 ])

# d = { 'a': 1, 'b': 2}
# print(d['c'])

# year = int(input('输入年份'))
# try:
#     year = int(input('输入年份'))
# except ValueError:
#     print('输入的年份不是数字')

#属性异常
# a = 123
# a.append()

# except(ValueError, AttributeError, KeyError)

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print('0不能做除数 %s' %e)

# #自定义异常
# try:
#     raise  NameError('helloError')
# except NameError as e:
#     print(e)

try:
    a = open('namSe.txt')
except IOError as e:
    print('------ %s ----' %e)
finally:
    a.close()

