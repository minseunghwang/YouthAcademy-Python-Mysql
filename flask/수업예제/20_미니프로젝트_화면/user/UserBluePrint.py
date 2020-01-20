from flask import Blueprint, render_template,request
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

    chk = user_database.check_user_id(user_id)

    return str(chk)

