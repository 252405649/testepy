# #讲董明姣名字插入在文件中
# file1 = open('name.txt','w')
# file1.write('董明姣'+"\n")
# file1.close()
#
# file2 = open('name.txt')
# print(file2.readline())
# file2.close()
#
# file3 = open('name.txt','a')
# file3.write('孙林夕'+'\n')
# file3.close()

# file4 = open('name.txt')
# for line in file4.readlines():
#     print(line)
#     print('----------------')
# file4.close()

file5 = open('name.txt')
print(file5.tell())
print(file5.read(1))
print('当前文件指针的位置 %s' %file5.tell())
print(file5.read(1))
print('当前文件指针的位置 %s' %file5.tell())
file5.seek(0)
print('当前文件指针的位置 %s' %file5.tell())
print(file5.read(1))
print(file5.read(1))
print('当前文件指针的位置 %s' %file5.tell())