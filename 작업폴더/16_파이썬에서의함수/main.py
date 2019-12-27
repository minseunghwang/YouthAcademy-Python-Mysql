# 매개변수 이름
def test1(a1, a2 ,a3):
    print('test1 호출')
    print(f'a1 : {a1}')
    print(f'a2 : {a2}')
    print(f'a3 : {a3}\n')

test1(100, 200, 300)
# 매개변수의 이름을 통해 넘겨줄 값을 지정할 수 있다.
test1(a2=200, a3=300, a1=100)
test1(100, a3=300, a2=200)

# a3에 정해진 값이 이미 있기 때문에 3번째 값을 어떤 매개변수에 넣어야 할 지 판단할 수 없기 때문에 오류 발생
# test1(a3=300, a2=200, 100)    # 오류
# test1(300, 200, a2=100)       # 오류
## 매개변수를 지정하지 않는 값들은 항상 앞에 나와 있어야 한다.

# test1(a3=300, 200, 100) # -> 문법상 오류

# a2에 저장될 값이 두 개 이상 설정되어 있으므로 실행시 오류가 발생한다.
# test1(100, 200, a2=300) # -> 실행상 오류

# 매개 변수의 기본 값
def test2(a1, a2 =2, a3 = 3):
    print('test2 호출')
    print(f'a1 : {a1}')
    print(f'a2 : {a2}')
    print(f'a3 : {a3}\n')

test2(100, 200, 300)
# test2()
test2(100)
test2(100,200)

def test3(a1, a2=2, a3=3):
    print('test3 호출')
    print(f'a1 : {a1}')
    print(f'a2 : {a2}')
    print(f'a3 : {a3}\n')

# a1의 기본값이 설정되어 있지 않기 때문에 오류가 발생한다.
# test3()
test3(100)
test3(100, 200)
test3(100, 200, 300)

test3(100, a3=300)

# 가변형 매개변수
# 함수 호출 수 넘겨주는 길이 따라 형태가 결정되는 매개변수
# 일반 매개변수
def test4(list1):
    result = 0
    for num in list1:
        result = result + num
    print(f'result : {result}')

# 함수 내에서 리스트나 튜플이라고 가정하고 반복문을 사용하였기 때문에 오류가 발생
# test(100)
test4([100])
test4([100, 200, 300, 400, 500])

# 리스트형 가변형 매개변수
def test5(*list2):
    result = 0
    for num in list2:
        result = result + num
    print(f'result : {result}')

# 0개짜리 리스트를 생성하여 받는다
test5()
test5(100)
test5(100, 200, 300, 400, 500)

# 딕셔너리형 가변형 매개변수
# 딕셔너리를 받는다.
def test6(dict1):
    print('test6 호출---------------')
    for key, value in dict1.items():
        print(f'{key} : {value}')

test6({'a1' : 100, 'a2' : 200})
test6({'b1' : 300, 'b2' : 400})

# 가변형
def test7(**dict2):
    print('test7 호출---------------')
    for key, value in dict2.items():
        print(f'{key} : {value}')
test7(a1=100, a2=200, a3=300, c3=500)
test7(b1=300, b2=400)

## 섞어서 사용할 경우 일반 변수를 앞쪽에 배치해야 한다.
## *이없는 일반변수는 앞쪽으로 *이 두개있으면(**) *보다 뒤로 => 반드시 순서대로 작성해야함
## 리스트형 가변형 매개변수 하나(*a3), 딕셔너리형 가변형 매개변수(**a4) 는 하나씩만 사용가능
def test8(a1, a2, *a3, **a4):
    print('test8 호출---------------')
    print(f'a1 : {a1}')
    print(f'a2 : {a2}')
    print(f'a3 : {a3}')
    print(f'a4 : {a4}')

test8(100, 200, 300, 400, 500, 600, key1=700, key2=800, key3=900)       # 이렇게하니까 a1은 100, a2는 200, 300부터 600은 a3(list) 그뒤는 딕셔너리로 매칭되는군 ㅇㅅaㅇ

# 함수의 반환 값
# 함수는 한번에 하나의 값만 반환 할 수 있다.
# 만약 다수의 값을 반환하고 싶다면 리스트, 튜플, 딕셔너리 등에 담아 반환하면 된다.
def test9(a1, a2):
    r1 = a1 + a2
    r2 = a1 - a2
    r3 = a1 * a2
    r4 = a1 // a2

#    tuple1 = (r1, r2, r3, r4)
    # tuple 생성시 소괄호는 생략가능

    # tuple1 = r1, r2, r3, r4
    # return tuple1

    # 값들을 가지고 있는 튜플을 생성해서 반환한다.
    return r1, r2, r3, r4       # 눈으로 보기에는 여러 값을 반환하는 것처럼 보이지만, 사실은 튜플을 생성해서 하나의 튜플을 반환하는것 !

tuple100 = test9(10,3)
print(f'tuple100 : {tuple100}')

k1, k2, k3, k4 = test9(10,3)        # 이렇게 받아도된다 ~
print(f'{k1}, {k2}, {k3}, {k4}')


