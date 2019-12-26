# List, Tuple은 인덱스(순서)로 데이터를 관리하는 개념
# Dictionary는 이름(key)로 데이터를 관리하는 개념

# Dictionary : 매개체 하나의 정보를 관리하는 용도
# List, Tuple : 수 많은 매개체들을 관리하는 용도

# () : 튜플, [] : 리스트, {} : 딕셔너리, 셋

dict1 = dict()
dict2 = {}

print(f'dict1 : {dict1}')
print(f'dict2 : {dict2}')
print(f'dict1 type: {type(dict1)}')
print(f'dict2 type: {type(dict2)}')

dict3 = {
    'a1' : 100,
    'a2' : 11.11,
    'a3' : '문자열',
    'a4' : True,
    'a5' : [10, 20, 30],
    'a6' : (10, 20, 30),
    'a7' : {'b1' : 100, 'b2' : 200}
}
print(f'dict3 : {dict3}')

print('값 가져오기1 ------------------')
a1 = dict3['a1']
a2 = dict3['a2']

print(f'a1 : {a1}')
print(f'a2 : {a2}')

print('값 가져오기2 ------------------')
a3 = dict3.get('a3')
a4 = dict3.get('a4')

print(f'a3 : {a3}')
print(f'a4 : {a4}')

print('없는 이름으로 값 가져오기 ---------')

# 오류
# a100 = dict3['a100']
# print(f'a100 : {a100}')

# None이 추출
a100 = dict3.get('a100')
print(f'a100 : {a100}')

print('딕셔너리의 값 수정 ------------------')
dict1 = {
    'a1' : 100,
    'a2' : 200
}

print(f'수정 전 dict1 : {dict1}')

dict1['a1'] = 1000
print(f'수정 후 dict1 : {dict1}')

print('딕셔너리에 추가 ------------------')
print(f'추가 전 dict1 : {dict1}')

# 없는 이름으로 값을 넣어주면 추가된다.

dict1['a100'] = 10000
print(f'추가 후 dict1 : {dict1}')

print('pop ----------------------------')
# 이렇게 하면 dict 에서 값은 안빠짐
a1 = dict1['a1']
print(f'a1 : {a1}')
print(f'dict1 : {dict1}')

# 이렇게 하면 dict에서 값 빠짐
a2 = dict1.pop('a2')
print(f'a2 : {a2}')
print(f'dict1 : {dict1}')
