
from flask import Flask,request

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name','Flask')
    return '<h1>hello,%s</h1>'%name



@app.route('/hi', methods=['GET','POST'])
def hi():
  return 'hi'


@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d</p>'%(2020-year)
