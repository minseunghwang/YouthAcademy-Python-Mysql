# main.py
# 주소만 쳐서 들어왔을때 처리할 건 main.py에다 만들꺼에요.
from flask import Flask, render_template, request

app = Flask(__name__)

# 전역변수
# 파이썬 프로그램(웹 서버)가 종료될 때 까지 유지된다.
# 같은 파일 내부라면 자유롭게 사용기 가능하다.
# 현재 파일에서 처리하고 있는 모든 요청에서 똑같은 변수를 사용하게 된다.
# 모든 브라우저 모든 요청에 대해 같은값을 사용하고자 할 때 사용한다.
data1 = 0

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/test1')
def test1():
    # data1은 전역변수임을 명시한다.
    global data1
    data1 = request.values.get('data1')

    # 지역변수
    # 지역변수는 함수 내부에서만 사용이 가능하기 때문에 현재 요청에 대한 처리가 끝나면 소며로딘다.
    # 모든 브라우저, 다른 요청에 대해서는 해당 변수를 사용할 수 없다.
    data2 = request.values.get('data2')

    html = render_template('test1.html')
    return html

@app.route('/test2')
def test2():

    dict1 = {
        'data1' : data1,
        # 'data2' : data2
    }

    html = render_template('test2.html', data_dict = dict1)
    return html


app.run(host='0.0.0.0', port=80, debug=True)