from flask import Flask, redirect, jsonify
from .app.news.latest.main import Latest # production import
#from app.news.latest.main import Latest # dev import

app = Flask(__name__)

# News Classes
latest = Latest() # últimas notícias / Mais recentes

@app.route('/')
def index():
    return redirect("https://econnews.info")


@app.route('/status')
def about():
    return jsonify({"status": 200, "message": "Econnews API running"})

@app.route('/news')
def news():
    return redirect("/news/recentes")

@app.route('/news/recentes')
def latest_news():
    cnn_news = latest.cnn()
    oglobo_news = latest.oglobo()
    oantagonista_news = latest.oantagonista()
    infomoney_news = latest.infomoney()

    return jsonify({
        "status": 200, 
        "type": "latest", 
        "news": {
            "cnn": cnn_news, 
            "o globo": oglobo_news, 
            "o antagonista": oantagonista_news,
            "infomoney": infomoney_news
            }
        })

# UOL DESATIVADO
''' 
@app.route('/news/uol')
def uol_endoint():
    news = websites.uol()
    return jsonify(news)
''' 

@app.route('/news/recentes/cnn')
def cnn_endoint():
    news = latest.cnn()
    return jsonify(news)


@app.route('/news/recentes/oantagonista')
def oantagonista_endoint():
    news = latest.oantagonista()
    return jsonify(news)


@app.route('/news/recentes/oglobo')
def oglobo_endoint():
    news = latest.oglobo()
    return jsonify(news)


@app.route('/news/recentes/infomoney')
def infomoney_endoint():
    news = latest.infomoney()
    return jsonify(news)


# Devs run this code:
'''
if __name__ == '__main__':
    app.run(debug=True)
'''