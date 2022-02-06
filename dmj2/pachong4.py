import requests
url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc': 'xyz'}
# .get 是使用get方法请求url，字典类型的data不需要额外进行处理
response = requests.get(url, data)
print(response.text)

# post请求
url = 'http://httpbin.org/post'
data = {'key': 'value', 'abc': 'xyz'}
# .post 是使用post方法请求url，字典类型的data不需要额外进行处理
response = requests.post(url, data)
print(response.json())