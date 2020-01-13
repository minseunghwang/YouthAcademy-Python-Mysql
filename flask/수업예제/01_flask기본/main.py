# flask 모듈
# pip insall flask

from flask import Flask

# flask 객체를 생성한다.
# 첫 번째 매개 변수 : 아무 문자열이나 넣어주면 된다. 파이썬쪽에서 운영중인 서버들을 구분하기 위한 이름.
app = Flask(__name__)

# 요청 주소에 따라 호출되는 함수들을 구현한다.
@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def test():
    return 'Hello Test'

# 서버 가동
# 컴퓨터에서 도메인 등록
# 경로 : C:\Windows\System32\drivers\etc\hosts
app.run(host='0.0.0.0', port=80)     # 외부에서의 접속이 가능하게한다!

