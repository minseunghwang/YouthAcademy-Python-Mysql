# 학생 정보를 관리한다.
# 학생의 정보 : 이름, 나이, 국어점수로 구성된닫.

# 입력 양식
# 이름을 입력해 주세요 : 홍길동
# 나이를 입력해 주세요 : 30
# 국어점수를 입력해 주세요 : 100
# 입력을 계속 하시겠습니까?(1. 예, 2.아니오)

# 출력양식
# 이름 : 홍길동
# 나이 : 30
# 국어점수 : 100점
# ---------------------------
# 이름 : 최길동
# 나이 : 20
# 국어점수 : 80점
# ---------------------------
# 학생수 : 30명
# 총점 : 2300점
# 평균 : 70점


# 입력받을 요소 : 학생 이름, 학생 나이, 국어 점수

# 학생 정보
student_list = []

# 계속 입력 받을지 여부
a1 = 1

# 반복해서 입력을 받는다.
while a1 == 1:
    str1 = input('이름을 입력해 주세요 : ')
    str2 = input('나이를 입력해 주세요 : ')
    str3 = input('국어점수를 입력해 주세요 : ')

    dict1 = {
        'name' : str1,
        'age' : str2,
        'kor' : int(str3)
    }

    student_list.append(dict1)

    str4 = input('계속 입력 하시겠습니까? (1. 예, 2.아니오) : ')
    a1 = int(str4)

# 국어 총점
kor_total = 0

for dict2 in student_list:
    kor_total = kor_total + dict2['kor']

# 국어점수 평균
kor_avg = kor_total // len(student_list)

# 학생 수
student_cnt = len(student_list)

for student_dict in student_list:
    print(f'이름 : {student_dict["name"]}')
    print(f'나이 : {student_dict["age"]}살')
    print(f'국어점수 : {student_dict["kor"]}점')
    print('-------------------------')

print('이름 : 홍길동')
print('나이 : 30살')
print('국어점수 : 100점')
print('-------------------------')
print('이름 : 최길동')
print('나이 : 20살')
print('국어점수 : 80점')
print('-------------------------')
print(f'학생수 : {student_cnt}명')
print(f'총점 : {kor_total}점')
print(f'평균 : {kor_avg}점')