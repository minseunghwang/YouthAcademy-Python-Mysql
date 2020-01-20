from flask import Blueprint, render_template

board_blue = Blueprint('board', __name__)

# 게시판 목록 페이지
@board_blue.route('/board_list')
def board_list():

    board_name = '자유게시판'

    board_list_data =[
        {
            'board_idx' : 10,
            'board_subject' : '글 제목입니다',
            'board_writer_name' : '홍길동',
            'board_date' : '2020-01-20'
        },
        {
            'board_idx': 9,
            'board_subject': '글 제목입니다',
            'board_writer_name': '김길동',
            'board_date': '2020-01-19'
        }
    ]

    html = render_template('board/board_list.html', board_name=board_name, board_list_data=board_list_data)
    return html

# 게시글 보는 페이지
@board_blue.route('/borad_read')
def borad_read():

    data_dic ={
        'board_writer_name' : '홍길동ㅋ',
        'board_subject' : '글 제목입니다.ㅋ',
        'board_content' : '글 내용입니다.ㅎ',
        'board_image' : 'image/bezzi.png'
    }

    html = render_template('board/borad_read.html', data_dic=data_dic)
    return html

# 게시글 작정 페이지
@board_blue.route('/board_write')
def borad_write():

    board_writer_name ='킴길동'

    html = render_template('board/board_write.html', board_writer_name=board_writer_name)
    return html

# 게시글 수정 페이지
@board_blue.route('/board_modify')
def board_modify():

    data_dic ={
        'board_writer_name' : '홍길동ㅋㅅㅋ',
        'board_subject' : '글 제목입니다ㅇㅅㅇ',
        'board_content' : '글 내용입니다ㅇㅁㅇ',
        'board_image' : 'image/aemae.jpg'
    }

    html = render_template('board/board_modify.html', data_dic=data_dic)
    return html