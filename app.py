from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello watchlist!'

@app.route('/abc')
def hello2():
    return 'nihao watchlist!22'