from flask import Flask, render_template
from api.app import Websites

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/status')
def about():
    return {"status": 200, "message": "Flask server running"}


@app.route('/uol')
def uol_endoint():
    website = Websites()
    news = website.uol()
    return {"status": 200, "uol": news}

#app.run(debug=True)
