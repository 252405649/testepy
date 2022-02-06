#记录12生肖，根据年份来判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# print(chinese_zodiac[0])
# print(chinese_zodiac[-4: chinese_zodiac.__len__()])
# year = int(input('用户请输入出生年份'))
# if(chinese_zodiac[year%12]== '虎'):
#     print('今年是你的本命年')
# else:
#     print('不是当前年份')

# for cz in chinese_zodiac:
#     print(cz)
#
# for i in range(1, 13):
#     print(i)

# for year in range(2000, 2019):
#     print('%s 年的生肖是 %s' %(year,chinese_zodiac[year % 12] ))
import time
num = 5
while True:
    num = num + 1
    if num > 10:
        print('aa__________111')
        break
    print(num)
    time.sleep(1)