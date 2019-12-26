# Set
# 파이썬에서 집합 처리를 위한 요소
# 중복을 허용하지 않고, 순서 혹은 이름으로 기억장소를 관리하지 않는다.

# set 생성
set1 = {}
set2 = set()
print(f'set1 type : {type(set1)}')
print(f'set2 type : {type(set2)}')
print(f'set2 : {set2}')

set3 = {10, 20, 30, 40, 50}
print(f'set3 : {set3}')
print(f'set3 type : {type(set3)}')

# 중복 불가능 (중복제거용도로 사용)
print('중복 No---------------')
set4 = {10, 10, 10, 20, 20, 20, 30, 30, 30}
print(f'set4 : {set4}')

print('추가 -----------------')
set5 = set()
set5.add(10)
set5.add(20)
set5.add(30)
print(f'set5 : {set5}')

# 중복된 값은 안드가유~
set5.add(10)
set5.add(10)
set5.add(20)
print(f'set5 : {set5}')

print('---------------------')
# set, list -> tuple로 변환
# tuple이 값을 가져오는 속도가 빠르기 때문
# 소괄호 () 로 묶여있으면 튜플 입니다~!
list10 = [10, 20, 30, 40, 50]
set10 = {10, 20, 30, 40, 50}

tuple10 = tuple(list10)
tuple11 = tuple(set10)
print(f'tuple10 : {tuple10}')
print(f'tuple11 : {tuple11}')

# tuple -> list
print('--------tuple -> list--------')
# 관리할 데이터를 추가하거나 삽입, 삭제, 수정을 위해서
list20 = list(tuple10)
print(f'list20 : {list20}')

# set -> list, tuple
print('--------set -> list, tuple--------')
# 인덱스 번호로 데이터를 관리하기 위한 목적
list21 = list(set10)
print(f'list21 : {list21}')

# list, tuple -> set
print('---------list, tuple -> set---------')
# 중복 제거 목적
# 주의@@@ 순서가 섞일 수 있음@@@
tuple100 = (10, 10, 10, 20, 20, 30, 30, 30)
list100 = [10, 10, 10, 20, 20, 30, 30, 30]

set30 = set(tuple100)
set31 = set(list100)

print(f'set30 : {set30}')
print(f'set31 : {set31}')