from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
# subDic 은 교과목명을 key로 교과목소개를 value로 지정한 딕셔너리 
url = 'https://computer.deu.ac.kr/computer/sub03_02.do'

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
html_class = soup.find_all(class_="li_dot h_li mb40") #html_class 리스트처럼 사용 가능

row = 0
subClass=[] #전공필수, 전공선택을 둘 다 담은 리스트 공백 선언
for tit in html_class:
    title = tit.text.strip() # 1 title은 전공필수 2 title은 전공선택
    subClass.append(title)
subClassLast = subClass[0].split("\xa0\n") + subClass[1].split("\xa0\n") #전공필수, 전공 선택을 하나의 리스트에 저장 및 과목별 분류

sub = []    #sub리스트에 교과목명과 교과목소개를 분리하여 저장
split_subClass =[]
for i in range(len(subClassLast)):
   split_subClass += subClassLast[i].split('\xa0')
for item in split_subClass:
    sub.append(item.strip())

subDic = {} #딕셔너리로 과목명과 설명을 키와 값으로 분류
for i in range(0, len(sub), 2):
    key = sub[i]
    value = sub[i+1]
    subDic[key] = value

keys_to_modify = [] #딕셔너리 키에 (뒤 인덱스들 삭제 = 영어들 삭제
for key in subDic:
    index = key.find('(')
    if index!=-1:
        modified_key = key[:index]
        keys_to_modify.append(key)
    else:
        modified_key = key
for key in keys_to_modify:
    modified_key = key[:key.find('(')]
    subDic[modified_key] = subDic.pop(key)

subjectDic ={}
for key, value in subDic.items():
    if 'I' in key:
        newKey = key.replace('I', '1')
        if 'II' in key:
            newKey = key.replace('II', '2')
    else:
        newKey = key
    subjectDic[newKey] = value

subReplace = {key.replace('1T', 'IT'): value for key, value in subjectDic.items()}
lastsubDic = {key.replace('UN1X', 'UNIX'):value for key, value in subReplace.items()}