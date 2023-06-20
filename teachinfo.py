from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://computer.deu.ac.kr/computer/sub02.do"

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
html_class = soup.find(class_="teachList") #class형

# teachlist 분리
row = 0
info=[] 
for tit in html_class:
    title = tit.text.strip()
    info.append(title) #teachClass 0인덱스는 공백, 1인덱스는 교수
teach = info[1].split('More') # 교수님별로 리스트 인덱스에 넣음


teach1 = [item.replace('\xa0', '')for item in teach]
teachlist = [item.replace('\n\n', '')for item in teach1]


teachInfo = {} #딕셔너리로 과목명과 설명을 키와 값으로 분류
# for i in range(0, len(teachlist), 1):
for info in teachlist:
    lines = info.split('님')
    teachname = lines[0]
    teachinfo = '님'.join(lines[1:])
    teachInfo[teachname] = teachinfo
teachInfo.pop('', None)
