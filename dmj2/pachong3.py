from urllib import request
from urllib import parse
import urllib
import socket

headers = {
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
  }
data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
print(data)
try:
    req = request.Request('http://httpbin.org/post', data=data, headers = headers, method='POST')
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('time ot')