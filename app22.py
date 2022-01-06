from flask import Flask
app = Flask(__name__)

@app.route('/abc/')
def hello22():
    return 'hello2 switch a py file.'