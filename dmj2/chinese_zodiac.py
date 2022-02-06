#记录12生肖，根据年份来判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# print(chinese_zodiac[0])
# print(chinese_zodiac[-4: chinese_zodiac.__len__()])
year = 2022
print(year %12)
print(chinese_zodiac[year %12])

print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)
print(chinese_zodiac * 2)