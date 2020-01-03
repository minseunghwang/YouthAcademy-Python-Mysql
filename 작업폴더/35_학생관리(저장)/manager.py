# manager

import student as stu

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

    # 파일에 저장한다.
    with open('student.csv', 'at', encoding='utf-8') as fp:
        fp.write(f'{str1},{str2},{str3}\n')

# 학생의 정보를 모두 불러오는 함수
def get_info():
    # 파일에서 데이터를 읽어온다
    with open('student.csv', 'rt', encoding='utf-8') as fp:
        str_list = fp.readlines()

    # 뒤에 \n을 떼고 다시 담는다
    for idx in range(len(str_list)):
        str_list[idx] = str_list[idx][:-1]

    student_list = []
    # print(str_list)
    # 정보를 학생 객체에 담는다.
    for str in str_list:
        # 쉼표(,)를 이용해 잘라낸다.
        str_list = str.split(',')
        # print(str_list)
        # 학생객체를 만든다.
        obj = stu.StudentClass(str_list[0], str_list[1], str_list[2])
        student_list.append(obj)

    # print(student_list)
    return student_list


# 학생 정보를 검색하는 함수
def search_info():
    # 학생 데이터를 받아온다.
    student_list = get_info()
    # 검색할 학생의 이름을 입력받는다.
    print('---------------------')
    print('학생 검색')
    name = input('학생 이름 : ')
    # 학생 데이터 중에 입력받은 이름에 해당하는 학생 정보를 출력한다.
    for obj in student_list:
        # 객체 안에 있는 이름과 입력받은 이름이 같다면
        if obj.name == name:
            # 출력한다.
            obj.show_student_info()
            print()

        else :
            print('검색 결과가 없습니다.')
            break




if __name__ == '__main__':      # __main__에는 모듈의 이름이 들어가 있습니다~
    # str1 = show_menu()
    # print(f'str1 : {str1}')
    # input_info()
    # get_info()
    search_info()