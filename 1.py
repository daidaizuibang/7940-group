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
t = "���ݳ�������Ϊ2000��9��19�յ��ˣ����ݰ��������ķ��������Եõ����µķ����ͽ��顣��ע�⣬�����һ�������������������ֺͲο�����Ӧ��Ϊ���ߵ�Ψһ���ݡ����ݰ���������2000��9��19�ճ������˵���������Ϊ�������ꡢ�����¡������ա�����ʱ������������֣����ǿ��Եó����µķ�����1. ������������ˣ����Լ�ǿ���о�����������������ѣ�����ʱ���Ե���Į�͹�ִ��2. �����³������ˣ����л��������飬�����罻�ͽ��ʣ�����ʱҲ���׳嶯������������3. �����ճ������ˣ����мᶨ����־�;��ģ�����ֱǰ����Ҳ���׹�����������͹�ִ��4. ����ʱ�������ˣ����Ի����ֹۣ����д������ͱ������������ʱҲ���Եü����ȱ�����ԡ��������ϵķ���������2000��9��19�ճ������ˣ���Ҫע��ļɻ����£�1. �ɹ�ִ����Į����Ϊ�����������Ե���Į�͹�ִ������Ҫѧ��������Ϳ��ŵش��������Ҫ���ڹ����Լ��Ĺ۵㡣2. �ɳ嶯������������������ʱ�����׳嶯����������������Ҫѧ������Լ��������������侲�����ǡ�3. �ɹ����������壺�����мᶨ����־�;��ģ���ʱ������������壬����Ҫѧ���ע���˵���������棬�Լ��ŶӺ�������Ҫ�ԡ�4. �ɼ����ȱ�����ԣ����ڸ��������׼����ȱ�����ԣ�����Ҫѧ�����ĵȴ��ʹ������飬��Ҫ������ɡ����ס����ֻ��һ�������������޷�Ԥ���������˺�δ����չ��ÿ���˵������Ǹ��Ӷ����ģ�����Ҫ�����������ص�Ӱ�졣����Ҫ���ǣ�Ҫ�����Լ���������Ŭ������������������ս��"
message = fp.ProtocolMessage(role="user", content="���Ҿ�����λ�:"+t+"��ֻ��Ҫ�ش𾫼�����")
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
