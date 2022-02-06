import  re
def find_item(name):
    with open('home.txt', encoding= 'utf-8') as f:
        data  = f.read().replace('\n', '')
        name_num = re.findall(name, data)
        # print('家庭成员 %s 出现 %s 次' %(name, name_num))
    return  len(name_num)

#读取家庭成员名称
name_dict = {}
with open('name.txt') as f:
    for line in f:
        name = line.strip('\n')
        name_num = find_item(name)
        name_dict[name] = name_num

name_sorted = sorted(name_dict.items(), key= lambda  item: item[1], reverse=True)
print(name_dict)
print(name_sorted[0:10])