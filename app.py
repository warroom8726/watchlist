from flask import Flask
from flask import url_for, request
from flask.templating import render_template
from werkzeug.utils import escape, redirect
app = Flask(__name__)

name_value = 'wenjie chen'
movies_value = [
    {'title':'my first movie', 'year': '2011'},
    {'title':'my second movie', 'year': '2012'},
    {'title':'my third movie', 'year': '2013'},
    {'title':'my forth movie', 'year': '2014'},
    {'title':'my fifth movie', 'year': '2015'},
    {'title':'my sixth movie', 'year': '2016'},
    {'title':'my seventh movie', 'year': '2017'},
    {'title':'my eighth movie', 'year': '2018'},
]

@app.route('/')
def hello():
    return 'hello watchlist!'

@app.route('/redirect')
def hello2():
    return redirect('https://www.baidu.com')

@app.route('/gif')
def hello_html():
    return '<h1>hello totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/re2')
def hello2_2():
    return redirect(url_for('hello_html'))

@app.route('/user-<name>')
def hello4(name):
    return 'user is: %s' % escape(name)

@app.route('/test')
def hello_test():
    print(url_for('hello_html'))
    print('url-is:%s' % escape(('hello4')))
    return '<h2>testfdddd督导费</h2>'

@app.route("/test2")
def hello_test2():
    name = request.args.get('name', 'Flask')
    return '<h1> hello: %s!' % name

@app.route("/movie")
def movie():
    return render_template('index.html', name=name_value, movies=movies_value)