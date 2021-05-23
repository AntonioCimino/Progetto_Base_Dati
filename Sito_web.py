from flask import Flask, render_template, make_response, request, json
from pymongo.cursor import Cursor

import Query

class News():
  def __init__(self, i, news):
        self.id = i
        self.id_dataset = news["_id"]
        self.ord_in_thread = news["ord_in_thread"]
        self.author = news["author"]
        self.published = news["published"]
        self.title = news["title"]
        self.text = news["text"][0:300]
        self.language = news["language"]
        self.crawled = news["crawled"]
        self.site_url = news["site_url"]
        self.country = news["country"]
        self.domain_rank = news["domain_rank"]
        self.thread_title = news["thread_title"]
        self.spam_score = news["spam_score"]
        self.main_img_url = news["main_img_url"]
        self.replies_count = news["replies_count"]
        self.participants_count = news["participants_count"]
        self.likes = news["likes"]
        self.comments =news["comments"]
        self.shares = news["shares"]
        self.type = news["type"]

  def dump(self):
      return {"_id": self.id, "ord_in_thread": self.ord_in_thread,  "author" : self.author, "published": self.published,
        "title": self.title, "text": self.text, "language" : self.language, "crawled" : self.crawled, "site_url" : self.site_url,
        "country" : self.country, "domain_rank" : self.domain_rank, "thread_title" : self.thread_title, "spam_score" : self.spam_score,
        "main_img_url" : self.main_img_url, "replies_count" : self.replies_count, "participants_count" : self.participants_count,
        "likes" : self.likes, "comments" : self.comments, "shares" : self.shares, "type" : self.type}

app = Flask(__name__)

@app.route('/')
def main():
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
    resp = make_response(render_template('Ricerca.html'))
    return resp


@app.route('/Ricerca_risultato', methods=['GET', 'POST'])
def ricerca_risultato():
    news = []
    i = 0
    testo = request.form['titolo']
    tipo_ricerca = request.form['tipo_ricerca']

    if(tipo_ricerca == "ricerca_text"): list_title, list_text = Query.query_for_text(testo)
    if(tipo_ricerca == "ricerca_date"): list_title, list_text = Query.query_for_date(testo)
    if(tipo_ricerca == "ricerca_author"): list_title, list_text = Query.query_for_author(testo)
    if(tipo_ricerca == "ricerca_lenguage"): list_title, list_text = Query.query_for_leng(testo)
    if(tipo_ricerca == "ricerca_country"): list_title, list_text = Query.query_for_country(testo)
    if(tipo_ricerca == "ricerca_site"): list_title, list_text = Query.query_for_site(testo)

    for x in list_text:
        news.append(News(i,x))
        i = i + 1
    for x in list_title:
        news.append(News(i,x))
        i = i + 1
    jsonN = "{ \"News\" :" + json.dumps([z.dump() for z in news]) + "}"
    print(jsonN)
    resp = make_response(render_template('Risultati_ricerca.html',list_news = jsonN, len = len(news)))
    return resp



@app.route('/Team', methods=['GET', 'POST'])
def team():
    return render_template('Team.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
