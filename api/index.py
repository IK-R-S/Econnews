from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/status')
def about():
    return {"status": 200, "message": "Flask server running"}