from flask import Blueprint, render_template, request

# Blueprint 객체를 생성한다.
# 첫 번째 매개변수 : blueprint이름
# 두 번째 매개변수 : Blueprint를 등록할 Flask 객체 이름
blue100 = Blueprint('blue1', __name__, template_folder='blue100_view')


@blue100.route('/test3')
def test3():
    html = render_template('test3.html')
    return html

@blue100.route('/test4')
def test4():
    html = render_template('test4.html')
    return html