import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def Busan():
    url = 'https://www.busan.go.kr/covid19/Travelhist.do'

    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title1 = soup.find('div', {'class': 'scroll-table'})
    title2 = title1.find('tbody')
    locEx = title2.select('tr > td:nth-child(3)')
    timeEx = title2.select('tr > td:nth-child(6)')
    for i in range(0, len(locEx)):
        loc = locEx[i].get_text()
        time = timeEx[i].get_text()
        print(loc, ",", time)


# 함수 실행
Busan()
