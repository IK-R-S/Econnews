from flask import Flask, redirect, jsonify
from api.app import Websites # production imports
#from app import Websites # dev imports

app = Flask(__name__)
websites = Websites()

@app.route('/')
def index():
    return redirect("https://econnews.info")


@app.route('/status')
def about():
    return jsonify({"status": 200, "message": "Econnews API running"})

@app.route('/news')
def news():
    cnn_news = websites.cnn()
    oantagonista_news = websites.oantagonista()
    return jsonify({"status": 200, "type": "latest", "news": {"cnn": cnn_news, "o antagonista": oantagonista_news}})

# UOL DESATIVADO
''' 
@app.route('/news/uol')
def uol_endoint():
    news = websites.uol()
    return jsonify(news)
''' 

@app.route('/news/cnn')
def cnn_endoint():
    news = websites.cnn()
    return jsonify(news)


@app.route('/news/oantagonista')
def oantagonista_endoint():
    news = websites.oantagonista()
    return jsonify(news)

# Devs run this code:

if __name__ == '__main__':
    app.run(debug=True)
