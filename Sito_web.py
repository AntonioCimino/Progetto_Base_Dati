from flask import Flask, render_template, make_response, request
from pymongo.cursor import Cursor

import Query

class News():
  def __init__(self, news):
        self.id = news["_id"]
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


app = Flask(__name__)

@app.route('/')
def main():
    list = Query.query_six_recent()
    news = []
    for x in list:
        news.append(News(x))
    resp = make_response(render_template('Home.html', list_news = news))
    return resp


@app.route('/Ricerca', methods=['GET', 'POST'])
def ricerca():
    testo = request.form['titolo']
    list_title, list_text = Query.query_for_text(testo)
    news = []
    for x in list_text:
        news.append(News(x))
    for x in list_title:
        news.append(News(x))
    resp = make_response(render_template('Ricerca.html', list_news = news))
    return resp


@app.route('/Team', methods=['GET', 'POST'])
def team():
    return render_template('Team.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
