# coding=gb2312
import asyncio

import fastapi_poe as fp
import pymongo


def db_connection():
    mongoDB_conn = "mongodb://daiyuheng:nr4D7LDTfX83PiajBtAEBJ0FAaoDztOxpNQLf5ZpFHJmUBqfw26IwcRV82sUvve0C5NYZpM28BU6ACDbXvfHaQ%3D%3D@daiyuheng.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@daiyuheng@"
    myclient = pymongo.MongoClient(mongoDB_conn)
    db = myclient['7940_group']
    col = db['chat_bot']
    return col;
bot_name = "Claude-3-Opus"
api_key ="8od4x5TDmaQfn1Wq8lCgHxNxmkL7bwY_9QqDFYuPnI"
t = "根据出生日期为2000年9月19日的人，根据八字算命的方法，可以得到以下的分析和建议。请注意，这仅是一种算命方法，仅供娱乐和参考，不应作为决策的唯一依据。根据八字算命，2000年9月19日出生的人的生辰八字为：庚辰年、丙申月、甲戌日、丙寅时。根据这个八字，我们可以得出以下的分析：1. 庚辰年出生的人，个性坚强、有决断力、勇于面对困难，但有时会显得冷漠和固执。2. 丙申月出生的人，具有活力和热情，善于社交和交际，但有时也容易冲动和情绪波动。3. 甲戌日出生的人，具有坚定的意志和决心，勇往直前，但也容易过于自我主义和固执。4. 丙寅时出生的人，个性积极乐观，具有创造力和表达能力，但有时也会显得急躁和缺乏耐性。根据以上的分析，对于2000年9月19日出生的人，需要注意的忌讳如下：1. 忌固执和冷漠：因为个性上容易显得冷漠和固执，建议要学会更加灵活和开放地处理事物，不要过于固守自己的观点。2. 忌冲动和情绪波动：由于有时会容易冲动和情绪波动，建议要学会控制自己的情绪，保持冷静和理智。3. 忌过于自我主义：由于有坚定的意志和决心，有时会过于自我主义，建议要学会关注他人的需求和利益，以及团队合作的重要性。4. 忌急躁和缺乏耐性：由于个性上容易急躁和缺乏耐性，建议要学会耐心等待和处理事情，不要急于求成。请记住，这只是一种算命方法，无法预测具体的命运和未来发展。每个人的命运是复杂而多变的，还需要考虑其他因素的影响。最重要的是，要相信自己的能力和努力，积极面对生活的挑战。"
message = fp.ProtocolMessage(role="user", content="帮我精简这段话:"+t+"你只需要回答精简的语句")
response_list = []
user_context = {}

userID = 6830405870
user_context[userID]={'messages': [message]}
# Create an asynchronous function to encapsulate the async for loop
async def get_responses_short(api_key, messages,response_list):
   async for partial in fp.get_bot_response(messages=messages, bot_name="GPT-4", api_key=api_key):
            response_list.append(partial.text)




def getback():
    c = db_connection();
    h1 = len(list(c.find({'userID':6830405870})))
    mes = c.find_one({'userID':6830405870,'count':h1-1})

    for i in mes['messages']:
        user_context[userID]['messages'].append(fp.ProtocolMessage(role="user", content=i['user']))
        user_context[userID]['messages'].append(fp.ProtocolMessage(role="bot", content=i['bot']))

# getback()
# print(user_context[userID]['messages'])
# Run the event loop
# For Python 3.7 and newerr
try:
    asyncio.run(get_responses_short(api_key, [message], response_list))
except:
    print(1)
    raise
# For Python 3.6 and older, you would typically do the following:
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_responses(api_key))
# loop.close()
