from flask import Blueprint, render_template,request, session
from user import user_database

user_blue = Blueprint('user', __name__)


# 로그인 페이지
@user_blue.route('/user_login')
def user_login():
    html = render_template('user/user_login.html')
    return html

# 회원가입 페이지
@user_blue.route('/user_join')
def user_join():
    html = render_template('user/user_join.html')
    return html

# 회원정보수정 페이지
@user_blue.route('/user_modify')
def user_modify():

    data_dic = {
        'user_name' : '늴모리동동',
        'user_id' : 'Neal',
    }

    html = render_template('user/user_modify.html', data_dic=data_dic)
    return html

# 중복확인을 위한 아이디 검사
@user_blue.route('/check_user_id')
def check_user_id():
    # 파라미터로 전달받은 아이디를 추출한다.
    user_id = request.values.get('user_id')

    # 아이디 사용여부를 확인한다.
    chk = user_database.check_user_id(user_id)

    return str(chk)

# 가입 처리
@user_blue.route('/user_join_pro', methods=['post'])
def user_join_pro():
    # 파라미터 데이터를 추출한다.
    user_name = request.values.get('user_name')
    user_id = request.values.get('user_id')
    user_pw = request.values.get('user_pw')

    # 사용자 데이터를 저장한다.
    user_database.add_user(user_name, user_id, user_pw)

    # 응답 결과로 가입 메시지를 보여주고 첫 페이지로 이동하는 자바 스크립트 코드를 전달한다.
    return '''
        <script>
            alert('가입이 완료되었습니다.')
            location.href='/'
        </script>
    '''

# 로그인 처리
@user_blue.route('/user_login_pro', methods=['post'])
def user_login_pro():
    user_id = request.values.get('user_id')
    user_pw = request.values.get('user_pw')

    # 로그인 여부를 확인한다.
    result = user_database.get_user_login_data(user_id, user_pw)
    if result == None:          # 로그인 실패
        str = '''
                <script>
                    alert('로그인에 실패하였습니다.')
                    location.href = 'user_login'
                </script>
        '''
    else :                      # 로그인 성공
        # 세션에다가 사용자 정보를 저장할 겁니다.
        session['login'] = True
        session['user_idx'] = result[0]
        session['user_name'] = result[1]

        str = '''
                <script>
                    alert('로그인 되었습니다')
                    location.href = '/'
                </script>
            '''
    return str

@user_blue.route('/user_logout')
def user_logout():
    session['login'] = False
    return '''
            <script>
                alert('로그아웃 되었습니다.')
                location.href = '/'
            </script>
          '''
