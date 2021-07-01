from flask import Flask, render_template, make_response, request, json
import matplotlib.pylab as plt
import numpy as np


import Query

class News():
  def __init__(self, i, news):
        self.id = i
        #self.id_dataset = news["_id"]
        #self.ord_in_thread = news["ord_in_thread"]
        self.author = news["author"]
        self.published = news["published"]

        self.title = ""
        if len(news["title"])<=60 : self.title = news["title"]
        else : self.title = news["title"][0:60]+"..."

        self.text = ""
        if len(news["text"]) <= 300 : self.text = news["text"]
        else : self.text = news["text"][0:300] + "..."

        self.language = news["language"]
        #self.crawled = news["crawled"]
        self.site_url = news["site_url"]
        self.country = news["country"]
        #self.domain_rank = news["domain_rank"]
        #self.thread_title = news["thread_title"]
        #self.spam_score = news["spam_score"]
        self.main_img_url = news["main_img_url"]
        #self.replies_count = news["replies_count"]
        #self.participants_count = news["participants_count"]
        #self.likes = news["likes"]
        #self.comments =news["comments"]
        #self.shares = news["shares"]
        #self.type = news["type"]

  def dump(self):
      return {"_id": self.id, "title": self.title, "author" : self.author, "published": self.published, "language" : self.language,
            "text": self.text, "site_url" : self.site_url,  "country" : self.country, "main_img_url" : self.main_img_url}
            #"ord_in_thread": self.ord_in_thread,  "crawled" : self.crawled, "domain_rank" : self.domain_rank,
            #"thread_title" : self.thread_title, "spam_score" : self.spam_score, "replies_count" : self.replies_count,
            #"participants_count" : self.participants_count, "likes" : self.likes, "comments" : self.comments,
            #"shares" : self.shares, "type" : self.type}

app = Flask(__name__)

@app.route('/')
def main():
    list = Query.query_six_recent()
    print(list)
    news = []
    i = 0
    for x in list:
        news.append(News(i,x))
        i = i + 1
    print(news)
    resp = make_response(render_template('Home.html', list_news = news))
    return resp

@app.route('/Home')
def home():
    list = Query.query_six_recent()
    news = []
    i = 0
    for x in list:
        news.append(News(i,x))
        i = i + 1
    resp = make_response(render_template('Home.html', list_news = news))
    return resp

@app.route('/Ricerca', methods=['GET', 'POST'])
def ricerca():

    i = 0
    list_author = Query.query_all_author()
    json_author = "{ \"Author\" :["
    for x in list_author:
        json_author = json_author + "{\"_id\" : \"" + x["_id"] + "\"},"
        i = i + 1
        if i == 30: break
    json_author = json_author[0:(len(json_author)-1)] + "]}"

    j = 0
    list_country = Query.query_all_country()
    json_country = "{ \"Country\" :["
    for x in list_country:
        json_country = json_country + "{\"_id\" : \"" + x["_id"] + "\"},"
        j = j + 1
    json_country = json_country[0:(len(json_country) - 1)] + "]}"

    m = 0
    list_site = Query.query_all_site()
    json_site = "{ \"Site\" :["
    for x in list_site:
        json_site = json_site + "{\"_id\" : \"" + x["_id"] + "\"},"
        m = m + 1
    json_site = json_site[0:(len(json_site) - 1)] + "]}"

    n = 0
    list_len = Query.query_all_leng()
    json_len = "{ \"Len\" :["
    for x in list_len:
        json_len = json_len + "{\"_id\" : \"" + x["_id"] + "\"},"
        n = n + 1
    json_len = json_len[0:(len(json_len) - 1)] + "]}"


    resp = make_response(render_template('Ricerca.html',list_author = json_author, len_author = i ,
                                         list_country = json_country, len_country = j,
                                         list_site = json_site, len_site = m,
                                         list_len = json_len, len_len = n))
    return resp


@app.route('/Ricerca_risultato', methods=['GET', 'POST'])
def ricerca_risultato():
    news = []
    i = 0

    tipo_ricerca = request.form['tipo_ricerca']

    if(tipo_ricerca == "ricerca_text"):
        testo = request.form['titolo']
        list_title, list_text = Query.query_for_text(testo)
    if(tipo_ricerca == "ricerca_date"):
        testo = request.form['date2']
        list_title, list_text = Query.query_for_date(testo)
    if(tipo_ricerca == "ricerca_author"):
        testo = request.form['author']
        list_title, list_text = Query.query_for_author(testo)
    if(tipo_ricerca == "ricerca_len"):
        testo = request.form['len']
        list_title, list_text = Query.query_for_leng(testo)
    if(tipo_ricerca == "ricerca_country"):
        testo = request.form['country']
        list_title, list_text = Query.query_for_country(testo)
    if(tipo_ricerca == "ricerca_site"):
        testo = request.form['site']
        list_title, list_text = Query.query_for_site(testo)

    for x in list_text:
        news.append(News(i,x))
        i = i + 1
    for x in list_title:
        news.append(News(i,x))
        i = i + 1
    jsonN = "{ \"News\" :" + json.dumps([z.dump() for z in news]) + "}"
    resp = make_response(render_template('Risultati_ricerca.html',list_news = jsonN, len = len(news)))
    return resp

@app.route('/Statistica', methods=['GET', 'POST'])
def stat():
   Query.query_all_country_count()
   Query.query_all_len_count()
   return render_template('Statistiche.html')


@app.route('/Team', methods=['GET', 'POST'])
def team():
    return render_template('Team.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
