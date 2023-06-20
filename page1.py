from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import lxml

def search():
    url = f'https://www.work.go.kr/consltJobCarpa/srch/schdpt/schdptSrchDtl05.do?empCurtState1Id=5&empCurtState2Id=22'
    response= requests.get(url)

    jobs=[]
    tmp2=[]
    if response.status_code==200:
        html = response.text
        soup=BeautifulSoup(html,'lxml')
        html_class = soup.find(class_="dpt-jobList dpt5")
        tmp=str(html_class).split('\n')
        for i in tmp:
            if i[0:4]=='<li>':
                tmp2.append(i)
        for i in tmp2:
            a=str(i).split('Code=')
            jobs.append(a[1].split('"')[0].strip())

    return jobs