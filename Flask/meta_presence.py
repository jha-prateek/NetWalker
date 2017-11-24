from NLP import nlp
from pymongo import MongoClient

meaningful=nlp()
Client = MongoClient()
linkk = "http://w3schools.com/css/default.asp"
# lin = "https://youtube.com/"
que = "HTML java"

class search1(object):

    def __init__(self):
        self.s = []
        self.p = []

    def process(self,query):

        chunks = meaningful.process_content(query)
        # print chunks

        for cnt in xrange(1,4):
            d = {}
            e = {}
            for x in chunks:
                d[x]=[]
                e[x]=[]

            w = "P" + str(cnt)
            # print w
            db = Client[w]
            linkData = db["linkData"]
            # linkList = db["linkList"]

            for res in linkData.find():
                texts = res["MetaKeywords"]
                text = res["MetaDesc"]
                # for co in text:
                #     self.f.append(co.split(","))
                #     # print self.f
                # for cc in self.f:
                #     for dd in cc:
                #         if dd not in self.k:
                #             self.k.append(dd)
                for i in d:
                    for y in texts:
                        if i in y:
                            if res["URL"] not in d[i]:
                                d[i].append(res["URL"])
                                self.s.append(res["URL"])

                for i in e:
                    for y in text:
                        if i in y:
                            if res["URL"] not in e[i]:
                                e[i].append(res["URL"])
                                self.p.append(res["URL"])


    def link_MetaKeyword(self,link):
        flag = "false"
        if link in self.s:
            flag = "true"
        return flag

    def link_MetaDescription(self,link):
        flag = "false"
        if link in self.p:
            flag = "true"
        return flag

# b=search1()
# b.process(que)
# l = b.link_MetaKeyword(linkk)
# print l
# o = b.link_MetaDescription(linkk)
# print o
