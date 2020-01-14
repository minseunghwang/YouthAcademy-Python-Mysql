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

@app.route('/03_Ready')
def ready():
    html = render_template('03_Ready.html')
    return html

@app.route('/04_SelectorBasic')
def selectorBasic():
    html = render_template('04_SelectorBasic.html')
    return html

@app.route('/05_Selector2')
def selector2():
    html = render_template('05_Selector2.html')
    return html

app.run(host='0.0.0.0', port=80, debug=True)
