from flask import Flask, render_template, request
import pymysql as db

app = Flask(__name__)

# 데이터베이스 접속 함수
def get_connection():
    conn = db.connect(host='127.0.0.1', user='root', password='1234', db='flaskdb1', charset='utf8')
    return conn

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/insert_data')
def insert_data():
    # 데이터 베이스 접속
    conn = get_connection()

    # 쿼리문
    sql = '''
            insert into flasktable(data1, data2, data3)
            values (%s, %s, %s)
          '''

    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(sql, (100, 200, 300))
    cursor.execute(sql, (1000, 2000, 3000))
    conn.commit()
    conn.close()


    return '저장완료'


@app.route('/show_data')
def show_data():
    conn = get_connection()

    sql = 'select data1, data2, data3 from flasktable'

    cursor = conn.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()

    # 모든 로우의 데이터를 담을 리스트
    result_list = []

    for row in result:
        # 로우 하나의 데이터를 담을 딕셔너리
        row_dict ={
            'data1' : row[0],
            'data2' : row[1],
            'data3' : row[2],
        }
        result_list.append(row_dict)

    conn.close()

    html = render_template('show_data.html', data_list=result_list)
    return html


app.run(host='0.0.0.0', port=80, debug=True)