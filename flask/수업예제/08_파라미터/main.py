from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html


@app.route('/test1')
def test1():
    data1 = request.args.get("data1")
    data2 = request.args.get("data2")
    data3 = request.args.get("data3")

    print(f'data1 : {data1}')
    print(f'data2 : {data2}')
    print(f'data3 : {data3}')

    html = render_template('test1.html')
    return html


@app.route('/test2', methods=['post'])
def test2():
    value1 = request.form.get("value1")
    value2 = request.form.get("value2")
    value3 = request.form.get("value3")

    print(f'value1 : {value1}')
    print(f'value2 : {value2}')
    print(f'value3 : {value3}')

    html = render_template('test2.html')
    return html


app.run(host='0.0.0.0', port=80, debug=True)