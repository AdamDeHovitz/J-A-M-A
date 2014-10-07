from flask import Flask,render_template, request
import random

app = Flask(__name__)



@app.route("/", methods = ["POST", "GET"])
def start():
    question = None;
    if request.method == 'POST':
        question = request.form["question"]
        #Operate on question using google stuff here
        




    return render_template("index.html", answer = question)


if __name__=="__main__":
    app.debug=True
    app.run()
