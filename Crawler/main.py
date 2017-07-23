from Spider import spider
from Mongo import Database
from threading import Thread

"""
        Developed by: Prateek Jha, 15 May 2017
"""

linkCount = curCount = 0
i=0
url = "https://www.ubisoft.com/"
mongoData = Database("Ubisoft",linkCount,url)
while(i<mongoData.linksCount()):
    try:
        spiderLeg = spider(mongoData.getNext(curCount))
        curCount += 1
        spiderLeg.crawl()
        linkCount = mongoData.insertDB(spiderLeg.linkURI, spiderLeg.headings, spiderLeg.CurLink, spiderLeg.Meta, linkCount)
        print "Link ", i, " Done!!"
    except:
        print "Dropped!!"
    i+=1