from flask import Flask, redirect, jsonify
from flask_cors import CORS
from datetime import datetime
#from app.news.latest.main import Latest, NewsManager # Dev Imports
from .app.news.latest.main import Latest, NewsManager # Production Imports

app = Flask(__name__)
CORS(app)

date = datetime.now().strftime("%d/%m/%Y")

sources = {
    "cnn": "cnnbrasil.com.br", 
    "o globo": "oglobo.globo.com",
    "infomoney": "infomoney.com.br"
}

# Inicialize a classe NewsManager
news_manager = NewsManager()

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
    all_news = news_manager.get_all_news()
    
    return jsonify({
        "status": 200,
        "type": "latest",
        "date": date, 
        "news": all_news
    })

# Rotas para cada provedor de notícias
@app.route('/news/recentes/cnn')
def cnn_endoint():
    cnn_news = news_manager.latest.cnn()
    return jsonify({"status": 200, "type": "latest", "date": date, "news": cnn_news, "source": sources['cnn']})

@app.route('/news/recentes/oglobo')
def oglobo_endoint():
    oglobo_news = news_manager.latest.oglobo()
    return jsonify({"status": 200, "type": "latest", "date": date, "news": oglobo_news, "source": sources['o globo']})

@app.route('/news/recentes/infomoney')
def infomoney_endoint():
    infomoney_news = news_manager.latest.infomoney()
    return jsonify({"status": 200, "type": "latest", "date": date, "news": infomoney_news, "source": sources['infomoney']})

# Devs run this code:
if __name__ == '__main__':
    app.run(debug=True)
