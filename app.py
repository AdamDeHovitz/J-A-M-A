from flask import Flask,render_template, request
import random, google

app = Flask(__name__)



@app.route("/", methods = ["POST", "GET"])
def start():
    question = None;
    answer = None;
    if request.method == 'POST':
        question = request.form["question"]
        #Operate on question using google stuff here
    if (question != None):
        l = picture(question);
        return render_template("index.html", answer = question, name = l[0], image = l[1], adjective = l[2]  )




    return render_template("index.html")

def imgReader():
  filez = open('./Static/namesAndImages.txt', 'r')
  Dict=filez.read()
  Dict=Dict.split('\n')
  Dict=Dict[:len(Dict)-1]
  filez.close()
  return Dict
def titleReader ():
  filezd = open('./Static/Titles.txt', 'r')
  titles=filezd.read()
  titles=titles.split('\n')
  titles=titles[:len(titles)-2]
  filezd.close()
  return titles


def picture(answer):

    l = []







    imgRepo = imgReader()
    Image=imgRepo[random.randint(0, len(imgRepo)-1)]
    Image=Image.split(',')
    Name = Image[0]
    image = Image[1]
    l.append(Name);
    l.append(image);
    titles=titleReader()

    l.append(titles[random.randint(0, len(titles)-1)])


    #get_it.close()



    return l




if __name__=="__main__":
    app.debug=True
    app.run()




#f = open('dates', 'r') #data will be the stuff from web pages
#data = f.read()
#f.close()

#def findnames(data):
#    print re.findall(r"([A-Z][a-z]{1,7}[a-z]+\s\d{,2},\s\d{,4})" , data) #recognizes dates in format: Month #, #

#findnames(data)

#def find_names(string):
#    pattern = re.compile("(?:(?:M(?:r|s|rs).?|The) )?(?!The|M(?:r|s|rs).?)[A-Z][a-z]+ (?:(?:Mc|O')?[A-Z][a-z]+)+")
#    return re.findall(pattern, string)

# from flask import Flask, render_template, request

# app = Flask(__name__)


# @app.route("/", methods=["POST", "GET"])
# def start():
#     question = None

#     if request.method == 'POST':
#         question = request.form["question"].strip()
#         answer = find_answer(question)

#     return render_template("index.html", answer=answer)


#urls = []

#def getLinks(question):
 #   from google import search
  #  for url in search(question, stop = 10): ##might also use get_urls()
   #     urls.append(url)
    #return urls

# def find_answer(question):
#   getLinks(question)
#     # fetch all documents and load here

#     question_word = question.split()[0].lower()
#     if question_word == "who":
#         # look for names
#         pass
#     elif question_word == "when":
#         # look for dates
#         pass

#     return None


# if __name__ == "__main__":
#     app.debug = True
#     app.run()
