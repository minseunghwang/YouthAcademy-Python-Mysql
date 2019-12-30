# 생성자 : 클래스가 생성될때 자동으로 호출되는 메서드(__init__)

class TestClass1:
    # 클래스를 통해 객채가 생성된 후 자동으로 호출된다.
    # 객체가 가지고 있어야 할 맴버를 추가하는 작업을 한다.
    # 또한, 무조건 동작해야 하는 코드가 있다면 여기에(__init__) 작성한다.
    def __init__(self, a1, a2):
        print('init 메서드가 호출되었습니다.')
        self.v1 = a1
        self.v2 = a2

t1 = TestClass1(100, 200)
t2 = TestClass1(300, 400)

print(f't1.v1 : {t1.v1}')
print(f't1.v2 : {t1.v2}')
print(f't2.v1 : {t2.v1}')
print(f't2.v2 : {t2.v2}')

# 클래스 변수
# 객체를 생성하지 않고 사용할 수 있는 변수
# 클래스의 이름으로 접근이 가능하고 객체의 변수를 통해서도 가능하다.
# 객체들이 공톨적으로 사용하는 값이 있을 경우
class TestClass2:

    # 클래스 변수
    class_v1 = 100

    def __init__(self, a1):
        self.member_v2 = a1

t3 = TestClass2(100)
t4 = TestClass2(200)
t5 = TestClass2(300)

# 클래스 변수의 값을 사용
print(f'TestClass2.class_v1 : {TestClass2.class_v1}')
print(f't3.class_v1 : {t3.class_v1}')
print(f't4.class_v1 : {t4.class_v1}')
print(f't5.class_v1 : {t5.class_v1}')

# 클래스의 변수의 값을 변경
print('--------------------------------------')
# 클래스의 이름으로 접근해서 변수값 변경
TestClass2.class_v1 = 200
print(f'TestClass2.class_v1 : {TestClass2.class_v1}')
print(f't3.class_v1 : {t3.class_v1}')
print(f't4.class_v1 : {t4.class_v1}')
print(f't5.class_v1 : {t5.class_v1}')

# 객체를 통해 변수값 변경
# 클래스 변수의 값을 변경하는 것이 아니고 객체 자기 자신(t3)에 새로운 맴버 변수를 추가하는 것으로 동작한다.
t3.class_v1 = 300
print(f'TestClass2.class_v1 : {TestClass2.class_v1}')
print(f't3.class_v1 : {t3.class_v1}')
print(f't4.class_v1 : {t4.class_v1}')
print(f't5.class_v1 : {t5.class_v1}')

# 클래스의 기본 구조
class TestClass100 :
    # 클래스 변수들
    class_v1 = 100
    class_v2 = 200

    # init : 객체 생성시 자동으로 호출, 객체마다 각각 가지고 있을 변수를 설정
    def __init__(self):
        self.member_v1 = 300
        self.member_v2 = 400

    # 이후 필요한 메서드들을 구현한다.
    def method1(self):
        pass