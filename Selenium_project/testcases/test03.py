# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from lib.ShowapiRequest  import ShowapiRequest
import requests
r = ShowapiRequest("http://route.showapi.com/2360-1","898187","5ccaec5f4852482dbd50e088fd1c42a5" )
r.addFilePara("img_url", "123.jpg")
res = r.post()
print(res.text) # 返回信息
body = res.json()['showapi_res_body']
print(body['Result'])