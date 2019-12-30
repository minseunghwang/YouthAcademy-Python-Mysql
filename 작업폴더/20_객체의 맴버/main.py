# 맴버 변수 : 객체가 관리하는 변수. 객체마다 각각 만들어진다.
# 맴버 메서드 : 객체가 관리하는 함수. 객체 생성시 생성되지 않고, 클래스가 가지고 있는 함수를 사용한다.

class TestClass1:
    pass

t1 = TestClass1()        # 만들어진 객체의 주소값을 t1에 저장
t2 = TestClass1()

# 파이썬은 생성된 객체에 맴버 변수를 추가할 수 있다.
t1.a1 = 100      # 객체의 주소값을 가져와서 . 을써서 주소에 접근
print(f't1.a1 : {t1.a1}')

# 같은 클래스를 가지고 생성한 객체라도 t1에만 a1을 추가 하였기 때문에 오류가 발생한다
# print(f't2.a1 : {t2.a1}')

# 메서드 : 클래스에 정의되어 있는 함수들
class TestClass2:
    # self : 메서드를 호출하기 위해 사용한 객체의 주소값이 들어온다.
    # 이를 통해 메서드를 호출하기 위해 사용한 객체에 접근해서 객체가 가지고 있는 맴버 변수들을 사용할 수 있다.
    def method1(self):
        print('TestClass2의 method1 호출')
        print(f'self : {self}')

t3 = TestClass2()
t3.method1()    # t3의 주소값이 self로 들어간다.
print(f't3 : {t3}')

# 메서드를 통해 객체의 맴버를 추가하기
class TestClass3:

    def add_member(self, a1, a2):       # self에는 객체의 주소가 들어온다. (t4랑 t5가 각각 들어오겠군)
        # 객체에 맴버를 추가한다.
        self.v1 = a1
        self.v2 = a2

t4 = TestClass3()                       # 객체란 CPU가 메모리에 만드는거. 근데 어디에있는지 우리는 모름. 그래서 그 주소를 가져와 각각 t4, t5에 저장
t5 = TestClass3()                       # t4,t5 는 객체가 존재하고 있는 위치의 주소값을 저장해 둔 것(주소값 찍어보면 다름. t4,t5라는 2개의 객체가 생성된것)
# 맴버를 추가하는 메서드를 호출
t4.add_member(100,200)
t5.add_member(300,400)

print(f't4.v1 : {t4.v1}')
print(f't4.v2 : {t4.v2}')
print(f't5.v1 : {t5.v1}')
print(f't5.v2 : {t5.v2}')

# 위의 코드는 add_member를 호출하지 않으면, v1,v2라는 맴버변수가 없는 객체가 생성될 수 도 있음. => 곤란한 상황(?) 발생할 수 있음 ㅇㅅㅇ
# 그래서 반드시 사용? 입력하도록 강제성 부여
