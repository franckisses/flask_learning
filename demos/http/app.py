
from flask import Flask,request,redirect,abort

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


@app.route('/colors/<any(blue,white,red):color>')
def three_color(color):
    return '<p>Love is paitent and kind,Love is not jealous or boastful or proud of rude.</p>'


@app.before_request
def do_something():
    print('test')



# response 
@app.route('/resp')
def resp():
    return '<h1>Hello,Flask</h1>',201

# redirect 
@app.route('/red')
def myred():
    return redirect('https:google.com')


# error response
@app.route('/404')
def not_found():
    abort(status=404)