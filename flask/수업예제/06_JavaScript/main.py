from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/01_JavaScriptBasic')
def JavascriptBasic():
    html = render_template('01_JavaScriptBasic.html')
    return html

@app.route('/02_jQueryBasic')
def jQueryBasic():
    html = render_template('02_jQueryBasic.html')
    return html

app.run(host='0.0.0.0', port=80, debug=True)
