from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    list1 = [10,20,30,40,50]

    html = render_template('index.html', a1=10, a2=list1)
    return html



app.run(host='0.0.0.0', port=80, debug=True)