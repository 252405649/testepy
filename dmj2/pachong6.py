import requests
from bs4 import BeautifulSoup
import re
contest = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
# print(contest)
soup = BeautifulSoup(contest, 'lxml')
# print(soup.prettify())

# # 找到title标签
# print(soup.title)
# # 找到title标签内容
# print(soup.title.string)
# #找到p标签
# print(soup.p)
# # 找到P标签class的名字
# print(soup.p('class'))
# # 获取第一个a标签
# print(soup.a)
# # 获取所有的a标签
# print(soup.find_all('a'))
# #获取所有id =Link3的标签
# print(soup.find_all(id ='link3'))
# 找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))
#找到文档所有的文本内容
print(soup.get_text())


