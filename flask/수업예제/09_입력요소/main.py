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

    # values를 사용하면 요청 방식에 관계없이 파라미터 데이터 추출이 가능하다.
    data4 = request.values.get('data4')

    # 동일 이름으로 여러 데이터가 전달될 경우 getlist 함수를 이용한다.
    data5 = request.values.getlist('data5')

    data6 = request.values.getlist('data6')


    print(f'data1 : {data1}')
    print(f'data2 : {data2}')
    print(f'data3 : {data3}')
    print(f'data4 : {data4}')
    print(f'data5 : {data5}')
    print(f'data6 : {data6}')


    html = render_template('result2.html')
    return html



app.run(host='0.0.0.0', port=80, debug=True)