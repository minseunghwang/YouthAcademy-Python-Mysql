# blue2.py
from flask import Blueprint, render_template, request

# Blueprint 객체를 생성한다.
# 첫 번째 매개변수 : blueprint이름
# 두 번째 매개변수 : Blueprint를 등록할 Flask 객체 이름
blue200 = Blueprint('blue2', __name__, template_folder='blue200_view')


@blue200.route('/test5')
def test5():
    html = render_template('test5.html')
    return html

@blue200.route('/test6')
def test6():
    html = render_template('test6.html')
    return html