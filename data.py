# import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

cookies = {
    "__ddg1_": "h0qF7E0Xn9BghTzrYPHH",
    "PHPSESSID": "M6S8dFIMQSLDiVCEyerwJuyQdP7HXxL9",
    "_ym_uid": "1699804556468980057",
    "_ym_d": "1699804556",
    "_ym_isad": "1",
}

headers = {
    "authority": "spvb.ru",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    # 'cookie': '__ddg1_=h0qF7E0Xn9BghTzrYPHH; PHPSESSID=M6S8dFIMQSLDiVCEyerwJuyQdP7HXxL9; _ym_uid=1699804556468980057; _ym_d=1699804556; _ym_isad=1',
    "referer": "https://spvb.ru/rynki/fondovyy-rynok/",
    "sec-ch-ua": '"Chromium";v="118", "Opera";v="104", "Not=A?Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0",
}
s = requests.Session()
response = s.get('https://spvb.ru/rynki/denezhnyy-rynok/uchastniki/', cookies=cookies, headers=headers).text

soup = bs(response, "lxml")
table = soup.find_all("td")
data_arr = []
for i in table:
    data_arr.append(i.text)
index = 2
inns = []
for z in range(int(len(data_arr)/6)):
    inns.append(data_arr[index])
    index = index + 6

