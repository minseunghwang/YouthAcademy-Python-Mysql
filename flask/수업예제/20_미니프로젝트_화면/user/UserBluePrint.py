from flask import Blueprint, render_template

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
    html = render_template('user/user_modify.html')
    return html