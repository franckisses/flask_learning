
from flask import Flask,request,redirect,abort,make_response,json,jsonify

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



# make response
@app.route('/foo')
def foo():
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