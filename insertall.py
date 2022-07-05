from pymongo import MongoClient
import json
client = MongoClient('mongodb://172.17.0.2:27017')
db = client.test
col = db.celiaco
with open("MOOCforum.json","r", encoding='utf-8') as  f:
        for line in f :
                data =json.loads(line)
                col.insert_one(data)
client.close()
