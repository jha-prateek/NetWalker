# from associate import d,da
# q="html"
# for i in d:
#     if q in i:
#         h=d.index(i)
#         break
#
# print h



from NLP import nlp
from pymongo import MongoClient
Client = MongoClient()
n=nlp()

class search(object):

    def cont_search(self,query):
        l=[]
        n = nlp()
        chunks = n.process_content(query)
        print chunks
        db = Client["IDF"]
        coll = db["Fri"]
        d = {}
        for x in chunks:
            d[x] = []


        for res in coll.find():
            v=0
            texts = res["Representatives"]
            for i in d:
                for y in texts:
                    if i in y:
                        v=v+1
                        if v!=0:
                            d[i].append(res["URL"])

        for u in d.values()[0]:
            c=0
            for x in range(1,len(d)):
                for t in d.values()[x]:
                    if u==t:
                        c=c+1
            if c==(len(d)-1):
                if u not in l:
                    l.append(u)
        print len(l)
        return l
# vp=search()
# q="mdn"
# print vp.cont_search(q)