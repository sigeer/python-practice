from flask import Flask, request, render_template
from waitress import serve

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

@app.route('/getName')
def getName():
    return request.args.get("name")

@app.route('/user/name/update')
def updateUserName():
    print(request.form['name'])

app.run(host="0.0.0.0", port=8555)
# serve(app, host="0.0.0.0", port=8555)