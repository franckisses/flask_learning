# ----
import os
from flask import Flask,request,redirect,abort,make_response,json,jsonify,url_for,session

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'this is stupid!')

# @app.route('/hello')
# def hello():
#     name = request.args.get('name','Flask')
#     return '<h1>hello,%s</h1>'%name



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



# make response
@app.route('/foo777')
def foo777():
    response = make_response('hello,world!')
    response.mimetype = 'text\plain'
    return response

# text

@app.route('/foo1')
def foo1():
    note =  '''
    Note
    to : peter
    from : Jane
    heading: Reminder
    body:Dont't forger the party!
    ''' 
    response = make_response(note)
    response.mimetype = 'text\plain'
    return response


# html 

@app.route('/foo2')
def foo2():
    note =  '''
    <! DOCTYPE html>
    <html>    
        <body>
            <h1>Note</h1>
            <p>to:Peter</p>
            <p>from:Jane</p>
            <p>heading:Reminder</p>
            <p>body:<strong>Dont't forget the party!</strong></p>
        </body>
    </html>
    ''' 
    response = make_response(note)
    response.mimetype = 'text\html'
    return response


# return json
@app.route('/foo3')
def foo3():
    data = {
        'name':'franck',
        'gender':'male'
    }
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response


@app.route('/foo4')
def foo4():
    return jsonify(name='franck', age=20)


@app.route('/foo5')
def foo5():
    return jsonify({'name':'franck', 'age':19})


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


# get name value from query string and cookie
@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
    response = '<h1>Hello, %s!</h1>' % (name)  # escape name to avoid XSS
    # return different response according to the user's authentication status
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))


# protect view
@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page.'


# log out user
@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))



@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href="%s">Do something and redirect</a>' \
           % url_for('do_something', next=request.full_path)


@app.route('/bar')
def bar():
    
    return '<h1>Bar page</h1><a href="%s">Do something and redirect</a>' \
           % url_for('do_something', next=request.full_path)



@app.route('/do_something')
def do_something():
    print('where am i come from:',request.referrer)

    print('get request next:',request.args.get('next'))
    return redirect(url_for('hello'))




# 获取上一个页面的url
# 1 HTTP Referer
#  通过request.referer


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def redirect_back(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))
