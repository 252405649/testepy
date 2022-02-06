import requests
from bs4 import BeautifulSoup
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
    U'pgrade-Insecure-Requests': "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

url = 'https://www.infoq.cn/public/v1/topic/get_hot_list'

def craw2(url):
    response = requests.get(url, headers= headers)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)
    for title_href in soup.find_all('div', class_='theme-list'):
        print(title_href.get_text())
        print([title.get('title')
               for title in title_href.find_all('a') if title.get('title')])

craw2(url)

