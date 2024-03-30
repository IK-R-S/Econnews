from flask import Flask, redirect, jsonify
from api.app import Websites
#from app import Websites

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
    uol_news = websites.uol()
    return jsonify({"status": 200, "type": "latest", "news": {"cnn": cnn_news, "uol": uol_news}})

@app.route('/news/uol')
def uol_endoint():
    news = websites.uol()
    return jsonify(news)


@app.route('/news/cnn')
def cnn_endoint():
    news = websites.cnn()
    return jsonify(news)

'''
if __name__ == '__main__':
    app.run(debug=True)
'''