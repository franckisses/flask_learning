from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>this is my first flask test!</h1>'



# 绑定多个url为一个试图
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# 动态路由, url出事变量
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""