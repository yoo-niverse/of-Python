"""import requests
from bs4 import BeautifulSoup

url='https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y'
html=requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')
soup.find_all('div.list_body.newsflash_body > ul >5 a.nclicks\(cnt_flashart\)')
title = soup.select('a')
print (title)
"""


import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y')

soup = BeautifulSoup(res.content, 'html.parser')

# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
title = soup.select("#main_content > div.list_body.newsflash_body > ul > li > a > strong")
                         #depth4Tab0Content > div > table > tbody > tr > td.align_l.name > div > a.sale_title")


"""for num in range(2):"""
print(title)
