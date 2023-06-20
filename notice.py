from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://computer.deu.ac.kr/computer/sub06_03.do"

html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")

title_elements = bsObject.find_all('td', class_='subject')
titles = []

for element in title_elements:
    title = element.text.strip()
    titles.append(title)

if titles:
    all_titles = '\n'.join(titles)