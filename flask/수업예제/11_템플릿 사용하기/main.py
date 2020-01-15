from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    dict1 ={
        'v1' : 100,
        'v2' : 200
    }

    list1 = [10, 20, 30, 40, 50]

    html = render_template('index.html', a1=100, a2=11.11, a3='안녕하세요', a4=dict1, a5=list1)
    return html



app.run(host='0.0.0.0', port=80, debug=True)