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

# 학생 객체들을 담을 List
student_list = []

# 학생 클래스
class StudentClass:
    def __init__(self, name, age, kor):
        self.name = name
        self.age = age
        self.kor = kor

    def show_info(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}살')
        print(f'국어점수 : {self.kor}점')
        print('---------------------------')


# 데이터를 입력받는다.
a1 = 1
while a1 == 1:
    str1 = input('이름을 입력해 주세요 : ')
    str2 = input('나이를 입력해 주세요 : ')
    str3 = input('국어점수를 입력해 주세요 : ')

    # 학생 객체 생성
    stu = StudentClass(str1, str2, int(str3))       # stu : 객체의 주소값을 담고있음

    # 학생 객체를 리스트에 담는다.
    student_list.append(stu)                        # 리스트 안에는 객체의 주소값들을 쭈루룩 가지고 있다

    str4 = input('계속 입력 하시겠습니까?(1.계속, 2.중단) : ')
    a1 = int(str4)

# 학생 수
student_cnt = len(student_list)

# 점수 총점
total = 0
for obj in student_list:
    total = total + obj.kor

# 평균
avg = total // len(student_list)

# 출력
for obj in student_list:
    obj.show_info()


print(f'학생수 : {student_cnt}명')
print(f'총점 : {total}점')
print(f'평균 : {avg}점')
