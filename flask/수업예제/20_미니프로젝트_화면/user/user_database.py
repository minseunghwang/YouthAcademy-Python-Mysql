# user/user_database.py
from common import database

# 사용자 정보를 저장하는 함수
def add_user(user_name, user_id, user_pw):
    conn = database.get_connection()

    sql = '''
            insert into(user_name, user_id, user_pw)
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