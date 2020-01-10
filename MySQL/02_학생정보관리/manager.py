# manager

import student as stu
import pymysql

# 데이터베이스 접속 함수
def connection_db():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='python_db1', charset='utf8')

    return conn

# 메뉴를 출력하는 함수
def show_menu():
    print('----------------')
    print('메뉴')
    print('1. 학생정보 입력')
    print('2. 학생정보 검색')
    print('3. 전체 정보 보기')
    print('4. 종료')

    menu_number = input('메뉴 선택 : ')
    return menu_number


# 학생 정보를 입력받는 함수
def input_info():
    # 정보를 입력받는다.
    print('----------------')
    print('학생정보입력')
    str1 = input('이름 : ')
    str2 = input('나이 : ')
    str3 = input('국어점수 : ')

    # 데이터베이스 접속
    conn = connection_db()

    sql = '''
            insert into student_table (student_name, student_age, student_kor)
            values(%s, %s, %s)
            '''
    cursor = conn.cursor()
    cursor.execute(sql, (str1, str2, str3))
    conn.commit()
    conn.close()
    print('저장 완료')


# 학생 정보를 검색하는 함수
def search_info():
    # 검색할 학생의 이름을 입력받는다.
    print('---------------------')
    print('학생 검색')
    name = input('학생 이름 : ')

    conn = connection_db()

    sql = '''
            select student_name, student_age, student_kor
            from student_table
            where student_name = %s
        '''
    cursor = conn.cursor()
    cursor.execute(sql,(name))

    result = cursor.fetchall()

    if len(result) == 0:
        print('검색된 데이터가 없습니다.')
    else :
        for row in result:
            print(f'이름 : {row[0]}')
            print(f'나이 : {row[1]}')
            print(f'국어점수 : {row[2]}')
            print('-----------------------')

    conn.close()


def show_all_info():
    conn = connection_db()

    sql = '''
            select count(*), sum(student_kor), avg(student_kor)
            from student_table
        '''

    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    # 학생 수
    student = result[0]

    # 국어점수 총점
    total = result[1]

    # 국어점수 평균
    avg = result[2]

    conn.close()

    print(f'학생의 수 :{student}')
    print(f'국어점수 총점 : {total}')
    print(f'국어점수 평균 : {avg}')
    print('-------------')



if __name__ == '__main__':      # __main__에는 모듈의 이름이 들어가 있습니다~
    # str1 = show_menu()
    # print(f'str1 : {str1}')
    # input_info()
    # get_info()
    search_info()