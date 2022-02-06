from urllib import request
from urllib import parse
import urllib
import socket
# response = request.urlopen('http://httpbin.org/get', timeout=2)
# print(response.read().decode('utf-8'))

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
print(data)
try:
    response2 = request.urlopen('http://httpbin.org/post', data=data, timeout=1)
    print(response2.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('time ot')