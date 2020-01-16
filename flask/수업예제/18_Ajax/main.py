from flask import Flask, render_template, request, session, make_response
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/get_time')
def get_time():
    # 현재 시간을 구한다.
    now = datetime.now()

    return f'{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}:{now.microsecond}'

@app.route('/test1')
def test1():
    html = render_template('test1.html')
    return html

@app.route('/test2')
def test2():
    html = render_template('test2.html')
    return html





app.run(host='0.0.0.0', port=80, debug=True)