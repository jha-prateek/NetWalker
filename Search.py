from pymongo import MongoClient
import webbrowser

query = ["LARGE"]
#queryString = query[0]
stringCount = []

Client = MongoClient()
db = Client["W3"]
linkData = db["linkData"]

i = 0
for res in linkData.find():
    texts = res["Contents"]
    #print len(filter(lambda x: queryString in x, texts))
    matching = [s for s in texts if any(xs in s for xs in query)]
    i+=1
    stringCount.append({
        'URL': res["URL"],
        'Count': len(matching)
        })

maxx = max([i['Count'] for i in stringCount])

for link in stringCount:
    if link['Count']==maxx:
        #print link['URL']
        webbrowser.open_new_tab(link['URL'])
