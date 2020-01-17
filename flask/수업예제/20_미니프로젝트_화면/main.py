from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html


app.run(host='0.0.0.0', port=80, debug=True)