from flask import Blueprint, render_template

board_blue = Blueprint('board', __name__)

# 게시판 목록 페이지
@board_blue.route('/board_list')
def board_list():
    html = render_template('board/board_list.html')
    return html

# 게시글 보는 페이지
@board_blue.route('/borad_read')
def borad_read():

    html = render_template('board/borad_read.html')
    return html

# 게시글 작정 페이지
@board_blue.route('/board_write')
def borad_write():
    html = render_template('board/board_write.html')
    return html

# 게시글 수정 페이지
@board_blue.route('/board_modify')
def board_modify():
    html = render_template('board/board_modify.html')
    return html