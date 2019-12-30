# 객체지향 프로그래밍(Object Oriented Programming, OOP)

# 매개체가 관리하는 데이터, 데이터들을 이용해 동작하는 기능들을 하나로 묶어서 관리하는 개념

class TestClass1:
    pass

# 객체 생성
t1 = TestClass1()
print(f't1 : {t1}')

# 같은 클래스를 가지고 만든 객체들은 전부 메모리에 독립적으로 각각 생성된다.
# 각 객체가 가지고 있는 맴버들은 전부 독립적으로 생성된다.
t2 = TestClass1()
t3 = TestClass1()
print(f't2 : {t2}')
print(f't3 : {t3}')

# 변수
a1 = 100
a2 = a1
print(f'a2 : {a2}')

# 함수
def f1():
    print('f1함수 호출')
# 함수도 메모리에 저장된다. 함수의 이름을 통해 다른 변수에 담으면, 메모리상에 저장되어 있는 함수의 주소값이 변수에 저장된다.
# 이를 통해 함수를 호출 할 수 있다. 파이썬에서는 함수의 이름이 함수가 저장되어있는 메모리의 주소값을 가지고 있는 변수에 해당한다.
f2 = f1()
f2

# 객체
class TestClass2:
    pass

t4 = TestClass2()
t5 = t4
print(f't4 : {t4}')
print(f't5 : {t5}')