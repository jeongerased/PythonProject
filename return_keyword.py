import pandas as pd
import random

chatbot_data = pd.read_excel("chatbot_data.xlsx")

chat_dic = {}
random_dic = {}

row = 0
for rule in chatbot_data['rule']:
    chat_dic[row] = rule.split('|')
    row += 1

for request in chatbot_data['request']:
    random_dic[request] = request.split(" ")

def get_random_question():
    random_question = random.choice(list(random_dic.keys()))
    return random_question

def recommend_response(request):
    recommended_responses = []
    for k, v in chat_dic.items():
        for word in v:
            if word in request:
                recommended_responses.append(chatbot_data['request'][k])
    return recommended_responses