# 파이썬과 MySQL의 연동 실습
# 필요한 모듈 : pymysql (pip install pymysql)

import pymysql

# 192.9.114.151
# 192.9.112.231 # me
# 데이터베이스 접속 함수
def connection_db():
    # host : 데이터베이스가 설치되어 있는 컴퓨터의 IP 혹은 도메인 주소
    # user : 접속 아이디
    # password : 접속 비밀번호
    # db : 사용할 데이터베이스의 이름
    # charset : 문자열 인코딩 방식
    conn = pymysql.connect(host="127.0.0.1", user='root', password='1234', db='python_db1', charset='utf8')
    return conn

def insert_data():
    # 데이터베이스 접속
    conn = connection_db();

    # 쿼리문
    sql ='''
        insert into python_table1(data1, data2)
        values(%s, %s)
        '''
    # 쿼리문을 관리하는 객체를 생성한다.
    cursor = conn.cursor()
    # 쿼리문을 실행한다
    cursor.execute(sql, (100, "문자열1"))
    cursor.execute(sql, (200, "문자열2"))
    cursor.execute(sql, (300, "문자열3"))
    # commit
    conn.commit()
    # db 닫아준다.
    conn.close()

    print('저장완료!')

def select_data():
    # 데이터베이스에 접속한다.
    conn = connection_db()

    # 쿼리문
    sql = '''
            select data1, data2
            from python_table1
        '''

    cursor = conn.cursor()
    cursor.execute(sql)

    # 값을 가져온다. ( 로우가 한개 : fetchone(), 로우가 두개 이상 : fetchall() )
    result = cursor.fetchall()
    for row in result:
        print(f'data1 : {row[0]}')
        print(f'data2 : {row[1]}')
        print('---------------------')

    conn.close()


def update_data():
    conn = connection_db()

    sql = '''
            update python_table1
            set data2 = %s
            where data1 = %s
        '''

    # 쿼리문을 관리하는 객체를 생성한다.
    cursor = conn.cursor()
    # 쿼리문을 실행한다
    cursor.execute(sql, ("변경된 문자열", 100))
    # commit
    conn.commit()
    # db 닫아준다.
    conn.close()

    print('수정 완료')


def delete_data():
    conn = connection_db()

    sql = '''
                delete from python_table1
                where data1 = %s
            '''

    # 쿼리문을 관리하는 객체를 생성한다.
    cursor = conn.cursor()
    # 쿼리문을 실행한다
    cursor.execute(sql, (100))
    # commit
    conn.commit()
    # db 닫아준다.
    conn.close()

    print('삭제 완료')

# 저장
# insert_data()
select_data()
# update_data()
delete_data()
select_data()

