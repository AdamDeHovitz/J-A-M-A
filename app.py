import random
import re

from flask import Flask, render_template, request
import google

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def start():
    question = None
    answer = None
    if request.method == 'POST':
        question = request.form["question"].strip()
        answer = get_answer(question)
    if (question is not None):
        l = picture(question)
        return render_template("index.html", answer=answer,
                               name=l[0], image=l[1], adjective=l[2])

    return render_template("index.html")


def imgReader():
    filez = open('./Static/namesAndImages.txt', 'r')
    Dict = filez.read()
    Dict = Dict.split('\n')
    Dict = Dict[:len(Dict) - 1]
    filez.close()
    return Dict


def titleReader():
    filezd = open('./Static/Titles.txt', 'r')
    titles = filezd.read()
    titles = titles.split('\n')
    titles = titles[:len(titles) - 2]
    filezd.close()
    return titles


def picture(answer):
    l = []

    imgRepo = imgReader()
    Image = imgRepo[random.randint(0, len(imgRepo) - 1)]
    Image = Image.split(',')
    Name = Image[0]
    image = Image[1]
    l.append(Name)
    l.append(image)
    titles = titleReader()

    l.append(titles[random.randint(0, len(titles) - 1)])

    # get_it.close()

    return l


def get_answer(question):
    corpus = fetch_pages(question)
    corpus = ' '.join(corpus)

    question_word = question.split()[0].lower()
    if question_word == "who":
        data = find_names(corpus)
    elif question_word == "when":
        data = find_dates(corpus)
    else:
        return

    frequency = count_frequency(data)
    answer = max(frequency, key=frequency.get)

    return answer


def fetch_pages(question):
    return [google.get_page(url) for url in google.search(question, stop=10)]


# recognizes dates in format: Month #, #
def find_dates(string):
    count_dict = {}
    for date in re.findall(r"([A-Z][a-z]{1,7}[a-z]+\s\d{,2},\s\d{,4})", string):
        if date in count_dict:
            count_dict[date] = count_dict[date] + 1
        else:
            count_dict[date] = 1

    return count_dict


def find_names(string):
    name_pattern = re.compile("(?:(?:M(?:r|s|rs).?|The) )?(?!The|M(?:r|s|rs).?)[A-Z][a-z]+ (?:(?:Mc|O')?[A-Z][a-z]+)+")
    return re.findall(name_pattern, string)


def count_frequency(data):
    count_dict = {}
    for item in data:
        if item in count_dict:
            count_dict[item] = count_dict[item] + 1
        else:
            count_dict[item] = 1

    return count_dict


if __name__ == "__main__":
    app.debug = True
    app.run()
