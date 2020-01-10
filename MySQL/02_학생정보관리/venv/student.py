# student

# 학생 정보를 관리하는 클래스
class StudentClass:
    def __init__(self, name, age, kor):
        self.name = name
        self.age = age
        self.kor = kor

    def show_student_info(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'국어점수 : {self.kor}')

    def __str__(self):
        return f'{self.name} {self.age} {self.kor}'