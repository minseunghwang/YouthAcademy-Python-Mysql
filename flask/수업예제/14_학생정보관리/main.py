from flask import Flask, render_template, request
import database as db
                        # 우리가 방금 만든거 그 왼쪽에 보면 database.py 있는거 이거

# 1. 화면작업
# 2. 만든 화면에서 변할 수 있는 부븐을 변수 출력으로 변경한다.
# 3. 변수에 담길 값들을 어떻게 가져올 것인가를 결정.(DB or 처리)

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html

# 학생 정보 입력 페이지
@app.route('/add_info')
def add_info():
    html = render_template('add_info.html')
    return html

# 학생 정보 입력 완료 페이지
@app.route('/add_info_pro', methods=['post'])       # post방식으로 넘어올때는 이렇게 받아줘야 되는구만!
def add_info_pro():
    # 클라이언트가 전달한 파라미터 데이터를 추출한다.
    student_name = request.values.get('student_name')
    student_age = request.values.get('student_age')
    student_kor = request.values.get('student_kor')

    # 데이터를 저장한다.
    db.add_student_info(student_name, student_age, student_kor)

    html = render_template('add_info_pro.html')
    return html

# 학생 정보 검색 페이지
@app.route('/search_info')
def search_info():
    html = render_template('search_info.html')
    return html

# 학생 정보 검색 결과 페이지
@app.route('/search_info_result', methods=['post'])
def search_info_result():
    # 파라미터 데이터 추출
    student_name = request.values.get('student_name')

    # 검색된 학생정보를 가져온다.
    student_list = db.get_search_info(student_name)

    html = render_template('search_info_result.html', student_list=student_list)
    return html

@app.route('/show_total_info')
def show_total_info():

    total_info = db.get_total_info()

    html = render_template('show_total_info.html', total_info=total_info)
    return html

app.run(host='0.0.0.0', port=80, debug=True)