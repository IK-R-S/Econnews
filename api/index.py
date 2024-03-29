from flask import Flask, redirect
from api.app import Websites

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://econnews.info")


@app.route('/status')
def about():
    return {"status": 200, "message": "Econnews API running"}


@app.route('/uol')
def uol_endoint():
    website = Websites()
    news = website.uol()
    return {"status": 200, "uol": news}

#app.run(debug=True)
