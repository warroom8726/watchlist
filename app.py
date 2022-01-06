from flask import Flask
from flask import url_for
from werkzeug.utils import escape
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello watchlist!'

@app.route('/cn')
def hello2():
    return u'你好 watchlist!'

@app.route('/gif')
def hello_html():
    return '<h1>hello totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user-<name>')
def hello4(name):
    return 'user is: %s' % escape(name)

@app.route('/test')
def hello_test():
    print(url_for('hello_html'))
    print('url-is:%s' % escape(('hello4')))
    return '<h2>testfdddd督导费</h2>'
