from NLP import nlp
from pymongo import MongoClient

Client = MongoClient()
db = Client["W3"]
linkData = db["linkData"]

n=nlp()
linkk = "https://www.w3schools.com/xml/xpath_examples.asp"
que = "Web CSS"

class search(object):

    def __init__(self):
        self.s = []
        self.p = []
        # self.f = []
        # self.k = []

    def process(self,query):
        d={}
        e={}
        chunks = n.process_content(query)
        # print chunks
        for x in chunks:
            d[x]=[]
            e[x]=[]

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


            # print text
            for i in d:
                for y in texts:
                    if i in y:
                        if res["URL"] not in d[i]:
                            d[i].append(res["URL"])
            for i in e:
                for y in text:
                    if i in y:
                        if res["URL"] not in e[i]:
                            e[i].append(res["URL"])
        # print self.k
        # print e
        # print (d.values())

        for u in d.values()[0]:
            c=0
            for x in range(1,len(d)):
                if u in d.values()[x]:
                    c = c+1
            if c==(len(d)-1):
                # print u
                self.s.append(u)
        # print self.s

        for w in e.values()[0]:
            b=0
            for x in range(1,len(e)):
                if w in e.values()[x]:
                    b = b+1
            if b==(len(e)-1):
                # print u
                self.p.append(w)
        # print self.p

    def link_present(self,link):
        flag = "false"
        if link in self.s:
            flag = "true"
        if link in self.p:
            flag = "true"
        return flag

b = search()
b.process(que)
l = b.link_present(linkk)
print l