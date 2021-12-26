from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h3>Flaskr</h3>'
@app.route('/child')
def child():
    return '<h3>Child Branch</h3>'