import pandas as pd
import subject as sj
import teachinfo as ti
import return_keyword as rk
import notice as nt
import weather as wt
import career as cr

def chatbotfn(s):
    chatbot_data = pd.read_excel("chatbot_data.xlsx")
    chat_dic={}
    row = 0
    for rule in chatbot_data['rule']:
        chat_dic[row] = rule.split('|')
        row +=1

    if '공지사항' in s:
        return '다음은 컴퓨터공학과 홈페이지 공지사항입니다.\n\n'+"Subject Notices:\n" + nt.all_titles
    
    if '날씨' in s:
        return '동의대학교가 위치한 가야동의 날씨입니다.\n\n'+ wt.weather +'\n'+wt.title

    if '직업' in s or '진로' in s:
        return '다음은 두 사이트에서 취득한 직업 정보입니다.\n\n' + cr.s

    for key in sj.lastsubDic:
        if key == s:
            return sj.lastsubDic[key] 
            break
    
    for key in ti.teachInfo:
        if key == s:
            return ti.teachInfo[key]
            break
            
    
    for k, v in chat_dic.items():
        index = -1
        for word in v:
            try:
                if index == -1:
                    index=s.index(word)
                else:
                    if index<s.index(word, index):
                        index=s.index(word, index)
                    else:
                        index = -1
                        break
            except ValueError:
                index = -1
                break
        if index>-1:
            return chatbot_data['response'][k]
    return random_response(s)
    
def random_response(s1):  #입력받은 s를 통해 죄송합니다. 문구 출력.
    recommended = rk.recommend_response(s1)
    if recommended:
        resp1 =''
        for resp in recommended:
            resp1 += resp +'\n'
        return '죄송합니다. 아래 목록은 "'+s1 +'" 라는 질문속에 있는 키워드가 포함된 질문들입니다.\n아래 질문 목록 중에 하나를 선택하여 다시 질문해주세요.\n\n'+ resp1
    else:
        return '죄송합니다. 무슨 말인지 모르겠어요. ' + rk.get_random_question()+' 와(과) 같은 질문은 어떠신가요?'
            