zodiac_name = (u'摩羯座', u'水平座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
# print(zodiac_name)
zodiac_days = (
(1, 20), (2, 19), (3, 1), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
(month, day) = (3, 14)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
print(zodiac_day)
# 获取星座下标
zodiac_len = len(list(zodiac_day))
zodiac_list = list(zodiac_day)
print(zodiac_list)
print(zodiac_name[zodiac_len])
print(zodiac_len)


# a_list = ['abc', 'xyz']
# a_list.append('x')
# print(a_list)
# a_list.remove('xyz')
# print(a_list)