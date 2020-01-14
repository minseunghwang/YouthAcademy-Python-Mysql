from flask import Flask, render_template, request

# 웹 에서의 요청방식
# 클라이언트 웹 브라우저가 서버에 요청을 할 때 사용하는 방식들
# get : 주소창에 주소를 직접 입력한 경우
#       링크를 클릭한 경우
#       form 태그의 method가 get인 경우
#       클라이언트가 서버로 데이터를 보낼 때 문자열 데이터만 보낼 수 있으며
#       전체 길이가 255글자에 한정되어 있다
#       띄어쓰기와 유니코드(한글 등) 문자는 포함할 수 없다.

# post : form 태그의 method가 post인 경우
#       클라이언트가 서버로 데이터를 보낼 때 문자열 뿐만 아니라 파일 데이터 등 다양한 형태의 데이터를 보낼 수 있다.
#       데이터의 총량은 제한이 없으며 띄어쓰기, 유니코드 등과 같은 문자도 포함할 수 있다.
#       서버로 보내는 데이터가 숨겨져서 전달된다.


app = Flask(__name__)


@app.route('/')
def index():
    html = render_template('index.html')
    return html



@app.route('/second')
def second():
    # 요청 방식
    print(f'요청 방식 : {request.method}')

    html = render_template('second.html')
    return html


# 요청방식을 post로 세팅. GET요청시 405 에러가 발생한다.
@app.route('/third', methods=['POST'])
def third():
    # 요청방식
    print(f'요청 방식 : {request.method}')
    html = render_template('third.html')
    return html


# fourth를 요청할때 get과 post모두 처리될 수 있도록 한다.
# 이 때, get 방식으로 요청했을때와 post방식으로 요청했을 때의 처리가 다르다면
# request.post를 가지고 if문을 사용하거나 함수를 따로 만들어 사용하면 된다.
@app.route('/fourth')
def fourth_get():
    print(f'fourth를 get 방식으로 요청하였습니다.')
    html = render_template('fourth.html')
    return html


@app.route('/fourth', methods=['POST'])
def fourth_post():
    print(f'fourth를 post 방식으로 요청하였습니다.')
    html = render_template('fourth.html')
    return html


# get, post 일때의 처리가 대부분이 일치한다면 하나로 통합해서 만들고 달라지는 부분만 if문으로 분기해서 처리한다.
@app.route('/fifth', methods=['get','post'])
def fifth():
    print(f'get 또는 post 방식으로 요청하였습니다.')
    
    if request.method == 'GET':
        print('GET 방식일때의 처리')
    else:
        print('POST 방식일때의 처리')

    html = render_template('fifth.html')
    return html



app.run(host='0.0.0.0', port=80, debug=True)