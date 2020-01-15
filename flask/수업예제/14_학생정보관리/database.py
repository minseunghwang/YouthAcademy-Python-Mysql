import pymysql

# 데이터베이스 접속 함수
def get_connection():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='flaskdb1', charset='utf8')
    return conn

# 학생 정보를 저장하는 함수
def add_student_info(student_name, student_age, student_kor):
    # 데이터베이스 접속
    conn = get_connection()

    # 쿼리문
    sql = '''
            insert into student_table(student_name, student_age, student_kor)
            values(%s, %s, %s)
        '''

    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(sql, (student_name, student_age, student_kor))

    conn.commit()
    conn.close()


# 학생 데이터 검색을 처리하는 함수
def get_search_info(student_name):
    conn = get_connection()

    sql = '''
            select student_name, student_age, student_kor
            from student_table
            where student_name = %s
        '''

    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(sql, (student_name))

    # 데이터를 가져온다
    result = cursor.fetchall()

    student_list =[]

    for row in result:
        student_dict = {
            'student_name' : row[0],
            'student_age' : row[1],
            'student_kor' : row[2],
        }
        student_list.append(student_dict)

    conn.close()
    return student_list


    return result


# 학생 전체 데이터를 구하는 함수
def get_total_info():

    conn = get_connection()

    sql = '''
            select count(*), sum(student_kor), floor(avg(student_kor))
            from student_table
        '''

    cursor =conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    total_dict ={
        'student_count' : result[0],
        'kor_total' : result[1],
        'kor_avg' : result[2]
    }

    conn.close()
    return total_dict

