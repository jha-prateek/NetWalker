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

        for i in xrange(1,4):
            d = {}
            for x in chunks:
                d[x] = []
            w = 'P' + str(i)
            # print w
            db = Client[w]
            # ld = db["linkData"]
            # ll = db["linkList"]
            linkData = db["linkData"]
            # for j in linkData.find():
            #     print j["name"]

            for res in linkData.find():
                v=0
                texts = res["Contents"]
                for i in d:
                    for y in texts:
                        if i in y:
                            v=v+1
                            # if res["URL"] not in d[i]:
                            #     d[i].append(res["URL"])
                    if v!=0:
                        d[i].append({res["URL"]:v})
                    #d[i][1].append(v)
            # print d

            for u in d.values()[0]:
                # print u.keys()
                # print ("--------------")
                c=0
                for x in range(1,len(d)):
                    for t in d.values()[x]:
                        if u.keys()==(t.keys()):
                            c=c+1
                if c==(len(d)-1):
                    l.append(u)

        return l
# vp=search()
# q="sharedspace"
# print(vp.cont_search(q))