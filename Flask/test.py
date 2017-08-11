from pymongo import MongoClient
client=MongoClient()
db=client.bank
test_collection=db.users
cursor=test_collection.find()
for document in cursor:
    print document