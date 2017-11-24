from pymongo import MongoClient


class Database(object):

    def __init__(self, database, linkCount, curURL):
        self.Client = MongoClient()
        self.db = self.Client[database]
        self.linkData = self.db["linkData"]
        self.linkList = self.db["linkList"]
        linksD = {"_id": linkCount,
                  "URL": curURL}
        self.linkList.insert_one(linksD)

    def insertDB(self ,linksDetails, texts, curURL, metaData, linkCount):
        for i in linksDetails:
            if (self.linkList.find({"URL": i}).count() == 0) and i != "javascript:void(0)":
                linkCount += 1
                linksD = {"_id": linkCount,
                          "URL": i}
                self.linkList.insert_one(linksD)

        post = {"URL": curURL,
                "Contents": texts,
                "TotaLinks": len(linksDetails),
                "MetaTitle": metaData['title'],
                "MetaUrl": metaData['url'],
                "MetaDesc": metaData['description'],
                "MetaKeywords": metaData['keyword'],
                "Anchors": linksDetails
                }
        self.linkData.insert(post)

        return linkCount

    def getNext(self, curCount):
        l = self.linkList.find_one({"_id": curCount})
        return l["URL"]

    def linksCount(self):
        return self.linkList.find().count()
