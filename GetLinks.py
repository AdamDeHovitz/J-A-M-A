import google
question = "Who played spiderman?" 
urls = []
def getLinks(question):
    from google import search
    for url in search(question, stop = 10): ##might also use get_urls()
        urls.append(url)
    print urls

getLinks(question)
