from Spider import spider
from Mongo import Database
from threading import Thread

"""
        Developed by: Prateek Jha, 15 May 2017
"""

linkCount = curCount = 0
i=0
url = "https://www.w3schools.com"
mongoData = Database("W3",linkCount,url)
while(i<mongoData.linksCount()):
    try:
        spiderLeg = spider(mongoData.getNext(curCount))
        curCount += 1
        spiderLeg.crawl()
        linkCount = mongoData.insertDB(spiderLeg.linkURI, spiderLeg.texts, spiderLeg.CurLink, spiderLeg.Meta, linkCount)
        print "Link ", i, " Done!!"
    except:
        print "Dropped!!"
    i+=1