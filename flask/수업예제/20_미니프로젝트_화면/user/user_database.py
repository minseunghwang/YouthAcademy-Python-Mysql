# user/user_database.py
from common import database

# 사용자 정보를 저장하는 함수
def add_user(user_name, user_id, user_pw):
    conn = database.get_connection()

    sql = '''
            insert into user_table (user_name, user_id, user_pw)
            values(%s, %s, %s)
        '''
    cursor = conn.cursor()
    cursor.execute(sql, (user_name, user_id, user_pw))
    conn.commit()
    conn.close()

# 중복 확인여부 검사
def check_user_id(user_id):
    conn = database.get_connection()

    sql = '''
            select * from user_table
            where user_id = %s
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_id))
    result = cursor.fetchone()

    if result == None:
        return True
    else :
        return False

# 로그인 처리를 위한 사용자 정보를 가져온다.
def get_user_login_data(user_id, user_pw):
    conn = database.get_connection()

    sql = '''
            select user_idx, user_name
            from user_table
            where user_id = %s and user_pw = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_id, user_pw))
    result = cursor.fetchone()

    conn.close()

    return result

