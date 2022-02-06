import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# plt.plot((1,3,5),(4,8,10))
# #plt.show()

import numpy as np
#线性图
# x = np.linspace(-np.pi*2, np.pi*2, 100) # 定义域为： -2pi到2pi
# plt.figure(1, dpi=50) #创建图表2
# for i in range(1,5): #画四条线
#     plt.plot(x,np.sin(x/i))
# plt.show()

#树状图
# plt.figure(1, dpi = 60) #创建图表1，dpi代表图片的精细度， dpi越大文件越大，杂志要300以上
# data = [1,1,1,2,2,2,3,3,4,5,5,6,4]
# plt.hist(data) #z只要传入数据，直方图就会统计数据出现的次数
# plt.show()


# #散点图
# x = np.arange(1,10)
# y = x
# fig = plt.figure()
# plt.scatter(x, y, c = 'r', marker= 'o') #c ='r' 代表散点为红色 marker表示散点形状为圆形
# plt.show()

# #seaborn库实现的散点图
# iris = pd.read_csv('./irdsda.crv')
# #设置样式
# sns.set(style='white', color_codes=True)
# #设置绘制格式为散点图
# sns.jointplot(x="120", y ="4", data=iris, size=5)
# #distplot绘制曲线
# sns.distplot(iris['120'])
# #没啥用，只是让pandas的plot（）方法在pyCharm上显示
# plt.show()

#seaborn库实现多个颜色的散点图
iris = pd.read_csv('./irdsda.crv')
#设置样式
sns.set(style='white', color_codes=True)
# FacetGrid 一般绘图函数
# hue 彩色显示分类0/1/2
#add_legend() 显示分类的描述信息
sns.FacetGrid(iris, hue= "virginica", size=5).map(plt.scatter, "120", "4").add_legend()