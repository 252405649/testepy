import requests
from bs4 import BeautifulSoup
import shutil
import os
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9Accept-Encoding: gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.infoq.cn",
    "If-Modified-Since": "Thu, 13 Jan 2022 11:08:55 GMT",
    "Referer": 'https://www.infoq.cn/',
    "sec-ch-ua": "Not;A Brand;v=99, Google Chrome;v=97, Chromium;v=97",
    "sec-ch-ua-mobile": "0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "1",
    'Upgrade-Insecure-Requests': "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

url = 'https://www.infoq.com/cn/talk'

def download_jpg(image_url, image_localpath):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_localpath,'wb') as f:
            response.raw.deconde_content = True

def craw(url):
    response = requests.get(url, headers= headers)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)
    for pic_href in soup.find_all('div', class_='theme-list'):
        for pic in pic_href.find_all('img'):
            imgurl = pic.get('src')
            dir = os.path.abspath('.')
            filename = os.path.basename(imgurl)
            imgpath = os.path.join(dir, filename)
            print('开始下载 %s' %imgurl)
            download_jpg(imgurl, imgpath)

#单页
craw(url)
#翻页
j=0
for i in range(12,37,12):
    url = url = 'https://www.infoq.com/cn/talk'+str(i)
    j+=1
    print('第 %d 页' %j)
    craw(url)

