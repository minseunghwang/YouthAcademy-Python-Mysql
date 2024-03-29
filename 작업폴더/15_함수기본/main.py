# 함수
# 개발자가 만드는 코드의 그룹
# 소프트웨어를 개발할때 하나의 기능을 구현한 단위

# 기본 함수
def test1():
    print('test1 함수 호출')
    print('파이썬은 들여쓰기로 함수의 코드 영역을 구분합니다.')

# 함수를 호출
test1()
test1()
test1()

# 매개변수
# 함수 내부의 코드가 동작될 때 필요한 데이터를 함수 호출 시 전달하는 개념
def test2(a1, a2):
    print('test2 호출')
    print(f'a1 : {a1}')
    print(f'a2 : {a2}')
    print('--------------------')

test2(10,20)
test2(100,200)
test2(1000,2000)

# 반환값
# 함수 수행이 끝난 후 함수를 호출한 쪽으로 돌아갈 때 값을 전달한다.
def test3():
    return '반환된 문자열'

str1 = test3()
print(f'str1 : {str1}')
