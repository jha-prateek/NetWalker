from flask import Flask
from flask import request
from flask import render_template
from NLP import nlp
from pymongo import MongoClient
import webbrowser

client = MongoClient('mongodb://localhost:27017/')
db = client['Hack']
collection = db['linkData']
# db.linkData.ensure_index([
#       ('Contents', 'text'),
#       ('MetaDesc', 'text'),
#   ],
#   name="search_index",
#   weights={
#       'MetaDesc':100,
#       'Contents':25
#   }
# )

# db.linkData.runCommand("text", {search :"\"W3\" \"Schools\""})
# db.linkData.index_information()
n=nlp()
stringCount = []

class FlaskIgnite:

    app = Flask(__name__)

    @app.route('/')
    def my_form():
        return render_template("fp.html")

    @app.route('/', methods=['POST'])
    def my_form_post():

        query=""
        text = request.form['text']
        chunks = n.process_content(text)
        # return render_template("search.html", chunks=chunks)
        query=chunks

        i = 0
        for res in collection.find():
            texts = res["Contents"]
            # print len(filter(lambda x: queryString in x, texts))
            matching = [s for s in texts if any(xs in s for xs in query)]
            print(matching)
            i += 1
            stringCount.append({
                'URL': res["URL"],
                'Count': len(matching)
            })
        maxx = max([i['Count'] for i in stringCount])

        for link in stringCount:
            if link['Count'] == maxx:
                # print link['URL']
                webbrowser.open(link['URL'],new=0,autoraise=True)

    if __name__ == '__main__':
        app.run()


Ignite=FlaskIgnite()
Ignite.my_form()
Ignite.my_form_post()