from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['W3']
collection = db['linkData']
db.linkData.ensure_index([
      ('Contents', 'text'),
      ('MetaDesc', 'text'),
  ],
  name="search_index",
  weights={
      'MetaDesc':100,
      'Contents':25
  }
)
# db.linkData.runCommand("text", {search :"\"W3\" \"Schools\""})
#print(db.linkData.index_information())
print(db.linkData.find( {"$search_index": { "$regex": "W3Schools Online Web Tutorials" } } ))
# # peeps=collection.find( {'Contents':{'$regex': 'W3Schools Online Web Tutorials'}})
# for person in peeps:
#     print person
