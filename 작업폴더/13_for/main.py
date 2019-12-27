# for문
# 특정 코드 영역을 반복하고자 할 때 사용
# list, set, tuple, dictionary 등이 관리하고 있는 값의 개수만큼 반복할 경우

# list, tuple, set
list1 = [10, 20, 30, 40, 50]
tuple1 = (10, 20, 30, 40, 50)
set1 = {10, 20, 30, 40, 50}

# list 안에 들어있는 값의 개수만큼 반복하고 매 반복 회 마다 list가 가지고 있는 값을 변수에 담아준다.
for value in list1:
    print(f'list : {value}')
print('list-----------------')

for value in tuple1:
    print(f'tuple : {value}')
print('tuple----------------')

for value in set1:
    print(f'set : {value}')
print('set-------------------')

# dictionary 안에 저장되어 있는 데이터의 이름이 추출된다.
## dictionary 형태는 (key, value) 형태다

dict1 = {
    'data1' : 100,
    'data2' : 200,
    'data3' : 300
}

for key in dict1:
    print(f'dict key : {key}')
    print(f'dict value : {dict1[key]}')

# items 함수를 사용하면 (이름, 값) 형태로 구성되어 있는 튜플이 반환된다.
dict_list = dict1.items()
print(f'dict_list : {dict_list}')

for a1 in dict1.items():
    print(f'a1 : {a1}')
    print(f'key : {a1[0]}')
    print(f'value : {a1[1]}')

print('----------ㅇㅅㅇ-------')

# (a1, a3) = 10, 20 # 이런느낌으로다가 동시에? 넣기?도 가능하다

for key, value in dict1.items():
    print(f'key : {key}')
    print(f'value : {value}')

print('----------------------')

# 반복만 하고 싶은 경우
# 아무값이나 원하는 개수만큼 들어있는 list, tuple 등을 준비하면 된다.

tuple1 = 1,1,1,1,1,1,1,1,1,1

# 값을 받고싶지 않다면 변수를 작성하는 부분에 _ 를 사용한다.
for _ in tuple1:
    print('Hello Wolrd')

print('----------@@@---------')
# range : 특정 범위의 값을 관리하는 요소를 생성한다.

# 1 ~ 10 -1까지
r1 = range(1,10)
print(f'r1 : {r1}\n')
print(f'r1 tuple : {tuple(r1)}')

# 0 ~ 10 -1까지
r2 = range(10)
print(f'r2 : {tuple(r2)}')

# 증가량
# 1 ~ 10 - 1, 2씩 증가
r3 = range(1,10,2)
print(f'r3 : {tuple(r3)}')

for _ in range(10):
    print('Hello World')
# 깃다시