import pymysql
from common import database

# 글 정보를 저장아는 함수
def add_board_content(board_subject, board_content, board_writer_idx, board_info_idx, board_image) :
    conn = database.get_connection()

    sql = '''
        insert into board_table(board_subject, board_writer_idx, board_date, board_content, board_image, board_info_idx)
        values (%s, %s, sysdate(), %s, %s, %s)
    '''
    
    cursor = conn.cursor()
    cursor.execute(sql, (board_subject, board_writer_idx, board_content, board_image, board_info_idx))
    print(board_subject, board_writer_idx, board_content, board_image, board_info_idx)
    conn.commit()

    # 방금 작성한 글의 번호(글의 번호가 가장 큰 것)을 가져온다.
    sql = '''
            select max(board_idx) from board_table
            where board_info_idx = %s
    '''

    cursor.execute(sql, (board_info_idx))
    result = cursor.fetchone()
    conn.close()

    return result[0]


# 주어진 글 번호를 통해 게시글 정보를 가져와 반환하는 함수
def get_board_content(board_idx):
    conn = database.get_connection()

    sql = '''
            select a1.board_subject, a2.user_name, a1.board_content, a1.board_image, a3.board_info_name
            from board_table a1, user_table a2, board_info_table a3
            where a1.board_writer_idx = a2.user_idx and a1.board_info_idx = a3.board_info_idx and a1.board_idx = %s
        '''

    cursor = conn.cursor()
    print(board_idx)
    cursor.execute(sql,(board_idx))
    result = cursor.fetchone()

    conn.close()

    return result


# 게시판 이름 가져오는 함수
def get_board_info_name(board_info_idx):
    conn = database.get_connection()

    sql = '''
            select board_info_name
            from board_info_table
            where board_info_idx = %s
        '''

    cusror = conn.cursor()
    cusror.execute(sql, (board_info_idx))
    result = cusror.fetchone()

    conn.close()

    return result[0]

# 게시글 목록을 가져오는 함수
def get_board_list(board_info_idx, page):
    conn = database.get_connection()

    # 현재 페이지의 글 목록의 시작 글의 인덱스
    start_idx = (int(page) -1 ) * 10

    sql = '''
            select a1.board_idx, a1.board_subject, a2.user_name, date_format(a1.board_date, '%%Y-%%m-%%d')
            from board_table a1, user_table a2
            where a1.board_writer_idx = a2.user_idx and a1.board_info_idx = %s
            order by a1.board_idx desc
            limit %s, 10
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (board_info_idx, start_idx))
    result = cursor.fetchall()

    conn.close()

    return result


# 전체 글의 개수를 반환한다.
def get_total_board_cnt(board_info_idx):
    conn = database.get_connection()

    sql = '''
            select count(*)
            from board_table
            where board_info_idx = %s
    '''
    cursor = conn.cursor()
    cursor.execute(sql,(board_info_idx))
    result = cursor.fetchone()

    conn.close()
    return result[0]
