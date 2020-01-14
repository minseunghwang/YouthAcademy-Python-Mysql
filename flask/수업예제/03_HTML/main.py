from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/01_basic')
def basic():
    html = render_template('01_basic.html')
    return html

@app.route('/02_header')
def header():
    html = render_template('02_header.html')
    return html

@app.route('/03_paragraphs')
def paragraphs():
    html = render_template('03_paragraphs.html')
    return html

@app.route('/04_link')
def link():
    html = render_template('04_link.html')
    return html

@app.route('/05_table')
def table():
    html = render_template('05_table.html')
    return html

@app.route('/06_list')
def list():
    html = render_template('06_list.html')
    return html


app.run(host='0.0.0.0', port=80, debug=True)
