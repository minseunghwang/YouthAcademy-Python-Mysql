# 앞뒤로 __ 가 붙어 있는 메서드들
# 특정 시점이 되면 자동으로 호출되는 메서드들

# https://ziwon.github.io/post/python_magic_methods/

# 객체 생성과 소멸
class TestClass1:

    # 객체 생성시 자동으로 호출되는 메서드
    def __init__(self):
        print('__init__호출')

    # 객체가 소멸될 때 자동으로 호출되는 메서드
    def __del__(self):
        print('__del__호출')

# 객체 생성
t1 = TestClass1()

# C언어 같은경우 객체를 사용후 소멸시켜주지 않으면 계속 메모리에 쌓여서 컴퓨터가 재부팅(강제 메모리 초기화인듯)된다. C++같은거 할 경우 메모리 관리가 필수적

# 연산자 관련 메서드
class TestClass2:

    def __init__(self, a1):
        self.a1 = a1

    # 더하기
    # other : 다른 객체의 주소값
    def __add__(self, other):
        return self.a1 + other.a1

    # 빼기
    def __sub__(self, other):
        return self.a1 - other.a1


t2 = TestClass2(10)
t3 = TestClass2(3)

r1 = t2 - t3            # - 연산자를쓰면 위의 __sub__가 호출됩니다. (오우 신기), t2가 self로 드가고 t3가 other로 드가는듯
r2 = t2 + t3            # + 연산자를쓰면 위의 __add__가 호출됩니다.
print(f'r1 : {r1}')
print(f'r2 : {r2}')

# str

class TestClass3:

    def __init__(self):
        self.a1 = 100
        self.a2 = 200


    # 객체를 print 함수로 출력할 때 이 메서드가 자동으로 호출되고 반환하는 문자열을 출력해준다.
    # 주로 객체가 가지고 있는 값들을 출력해 보는 용도로 사용한다.            # 주로 확인하는 용도로 이거 사용한대

    # str 함수를 이용할때
    def __str__(self):
        print(f'a1 : {self.a1}')
        print(f'a2 : {self.a2}')
        return 'TestClass3으로 만든 객체입니다.'

t4 = TestClass3()

print(100)
print(11.11)
print('안뇽하세요')
print([10, 20, 30])
print(t4)

str1 = str(100)
str2 = str(11.11)
print(f'type str1 : {type(str1)}')
print(f'type str2 : {type(str2)}')

str3 = str([10, 20, 30])
print(f'str3 : {str3}')

str4 = str(t4)
print(f'str4 : {str4}')


# str 함수 이용 예
class StudentClass:

    def __init__(self, name, age, kor):
        self.name = name
        self.age = age
        self.kor = kor

    def __str__(self):              # print 해서 아래처럼 객체를 출력하면 __str__여기의 return값이 출력된다? 뭐요런느낌
        return f'이름은 {self.name}이고, 나이는{self.age}이고, 국어점수는 {self.kor}점 입니다.'


stu1 = StudentClass('홍길동', 30, 100)
stu2 = StudentClass('최길동', 20, 80)
print(stu1)
print(stu2)

str1 = str(stu1)
str2 = str(stu2)
print(str1)
print(str2)