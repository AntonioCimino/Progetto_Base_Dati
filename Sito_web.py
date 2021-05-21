from flask import Flask, render_template, make_response, request
import Query

app = Flask(__name__)

@app.route('/')
def main():
    list = Query.query_six_recent()
    resp = make_response(render_template('Home.html', name = list[0]["author"]))
    return resp


@app.route('/Ricerca', methods=['GET', 'POST'])
def ricerca():
    titolo = request.form['titolo']
    resp = make_response(render_template('Ricerca.html', name = titolo))
    return resp


@app.route('/Team', methods=['GET', 'POST'])
def team():
    return render_template('Team.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
