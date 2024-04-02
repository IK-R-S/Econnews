from flask import Flask, redirect, jsonify
from datetime import datetime
from .app.news.latest.main import Latest # production import
#from app.news.latest.main import Latest # dev import

app = Flask(__name__)
date = datetime.now().strftime("%d/%m/%Y")

sources = {
    "cnn": "cnnbrasil.com.br", 
    "o antagonista": "oantagonista.com.br",
    "o globo": "oglobo.globo.com",
    "infomoney": "infomoney.com.br"
}

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
            "cnn": {"source": sources['cnn'], "recentes": cnn_news}, 
            "o globo": {"source": sources['o globo'], "recentes": oglobo_news}, 
            "o antagonista": {"source": sources['o antagonista'], "recentes": oantagonista_news},
            "infomoney": {"source": sources['infomoney'], "recentes": infomoney_news}
            }
        })


@app.route('/news/recentes/cnn')
def cnn_endoint():
    news = latest.cnn()
    return jsonify({"news": news, "source": sources['cnn'], "date": date})


@app.route('/news/recentes/oantagonista')
def oantagonista_endoint():
    news = latest.oantagonista()
    return jsonify({"news": news, "source": sources['o antagonista'], "date": date})


@app.route('/news/recentes/oglobo')
def oglobo_endoint():
    news = latest.oglobo()
    return jsonify({"news": news, "source": sources['o globo'], "date": date})


@app.route('/news/recentes/infomoney')
def infomoney_endoint():
    news = latest.infomoney()
    return jsonify({"news": news, "source": sources["infomoney"], "date": date})

# Devs run this code:
'''
if __name__ == '__main__':
    app.run(debug=True)
'''
