# mongodb
import pymongo

db = pymongo.MongoClient("mongodb://root:aA123456@localhost:27017/admin")

dblist = db.list_database_names()
print(dblist)

test = db['test']
print(test.list_collection_names())

collection = test['person']
# list
print(list(collection.find({'name': '李四'})))




