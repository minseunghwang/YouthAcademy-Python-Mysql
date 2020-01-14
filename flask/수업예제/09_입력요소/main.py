from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html


@app.route('/test1')
def test1():
    html = render_template('test1.html')
    return html


@app.route('/test2', methods=['post'])
def test2():

    html = render_template('test2.html')
    return html


@app.route('/result2', methods=['post'])
def result2():

    data1 = request.form.get('data1')
    data2 = request.form.get('data2')
    data3 = request.form.get('data3')

    print(f'data1 : {data1}')
    print(f'data2 : {data2}')
    print(f'data3 : {data3}')

    html = render_template('result2.html')
    return html



app.run(host='0.0.0.0', port=80, debug=True)