import os, base64, re, logging
from elasticsearch import Elasticsearch

# Log transport details (optional):
logging.basicConfig(level=logging.INFO)

print("\n\nIndexing data...\n\n")

import pymongo
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.DATA6

l = db.linkData.find()

total = db.linkData.count()
count = 0
prv = -1

while count<total:
    try:
        # Instantiate the new Elasticsearch connection
        es = Elasticsearch("AWS Elasticsearch cluster API Endpoint")
        count = 0
        for item in xrange(0,total):
            if count > prv:
                prv = count

                es.index('hnb', 'docb', {'url': l[item]['URL'],
                                              'TotalLinks': l[item]['TotalLinks'],
                                        })

                count = count + 1
                print count, item+1
            else:
                count = count + 1

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    res = es.search(index='hnb' , doc_type='docb', body={"query": {"match": {"TotalLinks": 576}}})
    print("%d documents found:" % res['hits']['total'])
    for doc in res['hits']['hits']:
        print("%s) %s" % (doc['_id']))