import page1
import page2

s=""

t1=page1.search()
t2=page2.search()

s=s+'1. 워크넷\n'
for i in t1:
    if i==t1[-1]:
        s=s+i
        continue
    s=s+i+','
s=s+'\n\n'

s=s+'2. 네이버 지식백과\n'
for i in t2:
    if i==t2[-1]:
        s=s+i
        continue
    s=s+i+','

s=s+'\n\n'