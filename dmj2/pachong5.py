import requests
import re
contest = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
# print(contest)

patten = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(patten, contest)
print(results)
for result in results:
    url, name = result
    print(url,re.sub('\s', '', name))

