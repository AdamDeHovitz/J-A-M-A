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



#f = open('dates', 'r') #data will be the stuff from web pages
#data = f.read()
#f.close()

#def findnames(data):
#    print re.findall(r"([A-Z][a-z]{1,7}[a-z]+\s\d{,2},\s\d{,4})" , data) #recognizes dates in format: Month #, #

#findnames(data)
