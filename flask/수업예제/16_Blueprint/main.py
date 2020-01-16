# main.py
# 주소만 쳐서 들어왔을때 처리할 건 main.py에다 만들꺼에요.
from flask import Flask, render_template, Blueprint
from blue1 import blue100
from blue2 import blue200

app = Flask(__name__, template_folder='main_view')

# blueprint 등록
app.register_blueprint(blue100)
app.register_blueprint(blue200)

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/test1')
def test1():
    html = render_template('test1.html')
    return html

@app.route('/test2')
def test2():
    html = render_template('test2.html')
    return html


app.run(host='0.0.0.0', port=80, debug=True)