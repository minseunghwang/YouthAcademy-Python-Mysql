from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html


@app.route('/test1')
def test1():
    return 'test1'


@app.route('/test1/sub1')
def test1sub1():
    return 'test1/sub1'


@app.route('/test1/sub2')
def test1sub2():
    return 'test1/sub2'


# test2를 요청할때 두번째 하위 주소가 있는 경우 호출
# 두번째 하위 주소는 데이터를 취급하여 변수에 담아준다.
@app.route('/test1/<data1>')
def test2(data1):
    return f'test2 data1 : {data1}'


# 요청 주소는 같고 데이터의 개수가 다를 경우 처리할 코드가 너무 많이 다르다면 함수를 나누어서 구현해 준다.
@app.route('/test2/<data1>/<data2>')
def test22(data1, data2):
    return f'test2 data1 : {data1}, data2 : {data2}'


# 서로 다른 요청 주소에 대해 처리할 코드가 똑같다면 같이 등록한다.
@app.route('/test3')
@app.route('/test4')
def test3_test4():
    return 'test3 or test4'


@app.route('/test5', defaults = {'data1' : 1, 'data2' : 2})
@app.route('/test5/<data1>', defaults={'data2' : 20})
@app.route('/test5/<data1>/<data2>')
def test5(data1, data2):
    return f'test5 data1 : {data1}, data2 : {data2}'


app.run(host='0.0.0.0', port=80, debug=True)