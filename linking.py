import pymongo

mongoDB_conn = "mongodb://daiyuheng:nr4D7LDTfX83PiajBtAEBJ0FAaoDztOxpNQLf5ZpFHJmUBqfw26IwcRV82sUvve0C5NYZpM28BU6ACDbXvfHaQ%3D%3D@daiyuheng.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@daiyuheng@"
myclient = pymongo.MongoClient(mongoDB_conn)
db = myclient['7940_group']
col = db['chat_bot']
c = col.find({'userid':'1'})
h=h = len(list(c))
c1 = col.find_one({'userid':'1','count':h})
# myclient = pymongo.MongoClient('localhost',27017)
# h = len(list(c1))
# c2 = col.findone({'userid':'1','count':1})
m1 = "ProtocolMessage(role='user', content='你好', content_type='text/markdown', timestamp=0, message_id='', feedback=[], attachments=[])"
msg = c1['messages'].append(m1)
print(c1['messages'])