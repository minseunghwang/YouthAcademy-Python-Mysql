from flask import Flask, render_template
from board.BoardBluePrint import board_blue
from user.UserBluePrint import user_blue

app = Flask(__name__)
app.register_blueprint(board_blue)
app.register_blueprint(user_blue)

# 메인 페이지
@app.route('/')
def index():
    html = render_template('index.html')
    return html


app.run(host='0.0.0.0', port=80, debug=True)