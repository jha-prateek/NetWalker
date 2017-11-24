from flask import Flask
from flask import request
from flask import render_template
from tfVecor_search import search
from meta_presence import search1
import operator
# import webbrowser
x=search()
y=search1()

class FlaskIgnite:

    app = Flask(__name__)

    @app.route('/')
    def my_form():
        return render_template("home.html")

    @app.route('/', methods=['POST'])
    def my_form_post():
        p={}
        query=""
        text = request.form['text']
        query = text
        y.process(query)

        l = x.cont_search(query)
        for a in l:
            print(a)
            c=0
            m = y.link_MetaDescription(a)
            n = y.link_MetaKeyword(a)
            if m:
                c = c + 200
            if n:
                c = c + 100
            # print a.keys().pop(0)
            # print p[a.keys()]
            p[a]=c

        sorted_d = sorted(p.items(), key=operator.itemgetter(1), reverse=True)
        print('Dictionary in descending order by value : ', sorted_d)
        for ak in sorted_d:
            print ak[0]

        return render_template("new_resultList.html",tfr=sorted_d)

    if __name__ == '__main__':
        app.run()


Ignite=FlaskIgnite()
Ignite.my_form()
Ignite.my_form_post()