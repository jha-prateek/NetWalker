from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
import time

dbs = []
Client = MongoClient()
for i in xrange(1,4):
    name = "P" + str(i)
    dbs.append(Client[name])

data = []
for con in dbs:
    linkData = con["linkData"]
    for x in linkData.find():
        data.append({x["URL"]: x["Contents"]})

datalist = []
for val in data:
    string = ""
    for xval in val.values()[0]:
        string = string + " " + xval
    datalist.append(string)

cv = TfidfVectorizer(min_df=1, stop_words='english')
train = cv.fit_transform(datalist)

tokens = cv.get_feature_names()
out_matrix = train.toarray()

def token_sort(i):
    ve = list(zip(out_matrix[i].tolist(),tokens))
    freq = lambda f:f[0]
    new_list = sorted(ve,key=freq,reverse=True)
    return new_list[:300]

Push = MongoClient()
document = Push["IDF"]
coll = document[str(time.asctime()[:3])]

final_out = []
for fx in range(len(data)):
    break
    # final_out.append(
    #     {
    #         "URL": data[fx].keys()[0],
    #         "Representatives": cv.inverse_transform(out_matrix[fx])[0].tolist(),
    #         "ARM": token_sort(fx)
    #     }
    # )
    # coll.insert_one({
    #         "URL": data[fx].keys()[0],
    #         "Representatives": cv.inverse_transform(out_matrix[fx])[0].tolist(),
    #         "ARM": token_sort(fx)
    #     })