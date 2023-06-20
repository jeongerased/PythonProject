from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import lxml
import re

def search():
    url = f'https://terms.naver.com/entry.naver?docId=917867&cid=44346&categoryId=44346'
    response= requests.get(url)

    if response.status_code==200:
        html = response.text
        soup=BeautifulSoup(html,'lxml')
        html_class = soup.find_all('div','size_ct_v2')
        s=str(html_class).split('<h3 class="stress" id="TABLE_OF_CONTENT8">관련직업</h3>')
        s1=s[1].split('<h3 class="stress" id="TABLE_OF_CONTENT9">관련자격</h3>')
        s2=s1[0]
        s3=re.sub(r"<[^>]*>","",s2).strip('\n')
        jobs=s3.split(', ')
    return jobs