from flask import Blueprint, render_template, request, session
import time
import os
from board import board_database

board_blue = Blueprint('board', __name__)

# 게시판 목록 페이지
@board_blue.route('/board_list')
def board_list():

    # 파라미터 데이터를 추출한다.
    board_info_idx = request.values.get('board_info_idx')
    page = request.values.get('page')

    # 게시판 이름을 가져온다.
    board_name = board_database.get_board_info_name(board_info_idx)

    # 게시글 정보를 가져온다.
    result = board_database.get_board_list(board_info_idx, page)

    # 페이징 관련 데이터
    min = (((int(page) - 1) // 10) * 10) + 1
    max = min + 10
    # 만약 이전 구간이 없다면 1로 셋팅
    pre = min -1
    if pre < 1:
        pre = 1

    # 전체 글의 개수를 가져온다.
    board_total_cnt = board_database.get_total_board_cnt(board_info_idx)
    # 전체 페이지의 개수를 구한다.
    total_page_cnt = board_total_cnt // 10
    if total_page_cnt % 10 > 0 :
        total_page_cnt = total_page_cnt + 1

    # max값이 전체 페이지수보다 크면 전체 페이지수로 조정한다.
    if max > total_page_cnt:
        max = total_page_cnt + 1

    next = max
    if next > total_page_cnt:
        next = total_page_cnt

    page_dict ={
        'min' : min,
        'max' : max,
        'pre' : pre,
        'next' : next,
    }

    board_list_data = []

    # 로우의 수만큼 반복한다
    for row in result:
        obj = {
            'board_idx' : row[0],
            'board_subject' : row[1],
            'board_writer_name' : row[2],
            'board_date' : row[3],
        }
        board_list_data.append(obj)

    html = render_template('board/board_list.html', board_name=board_name, board_list_data=board_list_data, board_info_idx=board_info_idx, page_dict=page_dict)
    return html

# 게시글 보는 페이지################################################################## board_idx 왜없냐 값이
@board_blue.route('/board_read')
def board_read():

    # 파라미터 데이터 추출
    board_idx = request.values.get('board_idx')

    print(board_idx)

    # 글 정보를 가져온다
    result = board_database.get_board_content(board_idx)

    data_dic ={
        'board_writer_name' : result[1],
        'board_subject' : result[0],
        'board_content' : result[2],
        'board_image' : f'image/{result[3]}',
        'board_info_name' : result[4],
    }

    html = render_template('board/board_read.html', data_dic=data_dic)
    return html

# 게시글 작정 페이지
@board_blue.route('/board_write')
def board_write():

    board_info_idx = request.values.get('board_info_idx')

    board_writer_name = session['user_name']

    html = render_template('board/board_write.html', board_writer_name=board_writer_name, board_info_idx=board_info_idx)
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


# 글쓰기 처리 페이지
@board_blue.route('/board_writer_pro', methods=['post'])
def board_writer_pro():
    # 파라미터 데이터를 추출한다.
    board_info_idx = request.values.get('board_info_idx')
    board_writer_idx = session['user_idx']
    board_subject = request.values.get('board_subject')
    board_content = request.values.get('board_content')


    # 업로드 된 파일이 있다면
    # 첨부파일을 설정했다면 name속성의 값을 이름으로 해서 전달한다.
    if 'board_image' in request.files:
        # 파일 데이터를 추출한다.
        board_image = request.files['board_image']
        # 저장할 파일 이름
        file_name = str(int(time.time())) + board_image.filename
        # 저장될 경로를 합친 이름을 만든다.
        file_path = os.getcwd() + '/static/image/' + file_name
        # 저장한다.
        board_image.save(file_path)
    else:
        file_name = None

    # 저장
    board_idx = board_database.add_board_content(board_subject, board_content, board_writer_idx, board_info_idx, file_name)

    return f'''
            <script>
                alert('작성이 완료되었습니다.')
                location.href = 'board_read?board_idx={board_idx}'
            </script>
        '''

