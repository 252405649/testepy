
# # 从1到10 所有偶数的平分
# list1 = []
# for i in range(1,11):
#     if (i % 2 ==0):
#         list1.append( i*i )
# print(list1)
#
# list1 = [i*i for i in range(1,11) if(i % 2) == 0]
# print(list1)

zodiac_name = ('摩羯座', u'水平座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
z_num = {}
#疏导式
z_num = { i:0 for i in zodiac_name}
print(z_num)