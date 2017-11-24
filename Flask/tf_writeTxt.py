from pymongo import MongoClient
Client = MongoClient()
db=Client["IDF"]
Coll=db["Fri"]
x =""
c=0
file = open("testfile.txt","w")
for res in Coll.find():
    text=res["ARM"]
    for i in text:
        if c<11:
            x=x+i[1]+" "
            c=c+1

    file.write(x+'\n')
    x=""
    c=0
file.close()
f=open("testfile.txt","r")
print f.read()