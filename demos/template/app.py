
import os
from flask import Flask,render_template,Markup

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

user = {
    'username': 'Franck',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html',user=user,movies=movies)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/hello')
def hello():
    text = Markup('<h1>Hello,Flask</h1>')
    return render_template('index.html',text=text)