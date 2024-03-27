from flask import Flask
from api.app import Websites

app = Flask(__name__)

@app.route('/')
def index():
    return {
        "status": 200,
        "endpoints": {
            "/news": ["/uol", "/g1", "/investing", "/infomoney"]
        },
        "info": "Econnews, a API aberta de notícias sobre finanças e economia"
    }


@app.route('/status')
def about():
    return {"status": 200, "message": "Flask server running"}


@app.route('/uol')
def uol_endoint():
    website = Websites()
    news = website.uol()
    return {"status": 200, "uol": news}

app.run(debug=True)
