from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://weather.naver.com/today/08230110"

html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")

current_weather = bsObject.find('strong', class_='current')
title = bsObject.find('span', class_='weather')

if current_weather and title:
    weather = current_weather.text.strip()
    title = title.text.strip()