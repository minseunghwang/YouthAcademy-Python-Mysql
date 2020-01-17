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

@app.route('/02_Grid')
def grid():
    html = render_template('02_Grid.html')
    return html

@app.route('/03_button')
def button():
    html = render_template('03_button.html')
    return html


app.run(host='0.0.0.0', port=80, debug=True)