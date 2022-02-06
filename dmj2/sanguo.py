
# try:
#     # 读取人物名称
#     f = open('name.txt')
#     data = f.read().strip('\n')
#     print(data.split('\n'))
#
#     # 读取个人爱好
#     f2 = open('like.txt', encoding= 'utf-8')
#     # data = f2.read().strip('\n')
#     # print(data.split('\n'))
#     print(f2.readlines())
#     i = 1
#     for line in f2.readlines():
#         print(line.strip('\n'))
#         i += 1
#
#     f3 = open('home.txt', encoding='utf-8')
#     print(f3.read().replace('\n', ''))
# except IOError as e:
#     print(e)
# finally:
#     f.close()
#     f2.close()
#     f3.close()


def func(filename):
    print(open(filename).read())
    print('test func')
func('name.txt')
