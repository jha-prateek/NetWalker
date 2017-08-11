from flask import Flask
from flask import request
from flask import render_template
from NLP import nlp
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['W3']
collection = db['linkData']
db.linkData.ensure_index([
      ('Contents', 'text'),
      ('MetaDesc', 'text'),
  ],
  name="search_index",
  weights={
      'MetaDesc':100,
      'Contents':25
  }
)
# db.linkData.runCommand("text", {search :"\"W3\" \"Schools\""})
db.linkData.index_information()

n=nlp()
class FlaskIgnite:

    app = Flask(__name__)

    @app.route('/')
    def my_form():

        return render_template("Flaskhtml.html")

    @app.route('/', methods=['POST'])
    def my_form_post():

        query=""
        text = request.form['text']
        chunks = n.process_content(text)
        # return render_template("search.html", chunks=chunks)
        query=chunks
        x=db.linkData.find({"$search_index": {"$search": query}})
        return render_template("search.html", x=x)
        #text_results = db.command('text', 'linkData', search=query, limit=SEARCH_LIMIT)
        #doc_matches = (res['obj'] for res in text_results['results'])
        #return render_template("search.html", results=results)
        #fo = open("tr.txt", "w")
        # fo.write(chunks);
        # fo.close()

    if __name__ == '__main__':
        app.run()


Ignite=FlaskIgnite()
Ignite.my_form()
Ignite.my_form_post()
