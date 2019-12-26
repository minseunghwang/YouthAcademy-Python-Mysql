# 튜플 : 0부터 시작하는 인덱스로 다수의 기억장소를 관리하는 개념
#        관리하는 기억장소에 대한 수정, 추가, 삭제 등이 불가능하다.
# 리스트 : 0부터 시작하는 인덱스로 다수의 기억장소를 관리하는 개념
#         관리하는 기억장소에 대한 수정, 추가, 삭제 등이 가능하다
# 문자열 : 파이썬은 문자열을 튜플과 비슷하게 관리한다.

# 생성
tuple1 = tuple()
list1 = list()
str1 = str()

print(f'tuple1 : {tuple1}')
print(f'list1 : {list1}')
print(f'str1 : {str1}')

tuple2 = tuple()
list2 = list()
str2 = str()

print(f'tuple1 : {tuple2}')
print(f'list1 : {list2}')
print(f'str1 : {str2}')

print(f'tuple1 type : {type(tuple2)}')
print(f'list1 type : {type(list2)}')
print(f'str1 type : {type(str2)}')

print('---------------------1')
tuple3 = (10,20,30,40,50)
list3 = [10,20,30,40,50]
str3 = '안녕하세요'

print(f'tuple3 : {tuple3}')
print(f'list3 : {list3}')
print(f'str3 : {str3}')

print(f'tuple3 개수 : {len(tuple3)}')
print(f'list3 개수 : {len(list3)}')
print(f'str3 개수 : {len(str3)}')

print('---------------------2')
# 맴버에 접근 : 0부터 1씩 증가하는 인덱스 번호를 사용한다.
print(f'tuple3[0] : {tuple3[0]}')
print(f'tuple3[2] : {tuple3[2]}')

print(f'list3[0] : {list3[0]}')
print(f'list3[2] : {list3[2]}')

print(f'str3[0] : {str3[0]}')
print(f'str3[2] : {str3[2]}')

# 인덱스 1 ~ 4 - 1 까지
print(f'tuple3[1:4] : {tuple3[1:4]}')
print(f'list3[1:4] : {list3[1:4]}')
print(f'str3[1:4] : {str3[1:4]}')

# 처음부터 4-1 까지
print(f'tuple3[:4] : {tuple3[:4]}')
print(f'list3[:4] : {list3[:4]}')
print(f'str3[:4] : {str3[:4]}')

# 인덱스 1 ~ 끝까지
print(f'tuple3[1:] : {tuple3[1:]}')
print(f'list3[1:] : {list3[1:]}')
print(f'str3[1:] : {str3[1:]}')

# 전부다
# 이거는 원래 있는거를 가져와서 새로 "복제"해서 보는거고
print(f'tuple3[:] : {tuple3[:]}')
print(f'list3[:] : {list3[:]}')
print(f'str3[:] : {str3[:]}')

# 이거는 그냥 원래 있는거를 찍어보는거
print(f'tuple3[:] : {tuple3}')
print(f'list3[:] : {list3}')
print(f'str3[:] : {str3}')

# 잘못된 범위
# print(f'tuple3[99] : {tuple[99]}')

# 음수 인덱스 : 0부터 1씩 증가하는 인덱스는 앞에서부터이고 -1부터 1씩 감소하는 인덱스는 뒤에서 부터
print(f'tuple3[0] : {tuple3[0]}')
print(f'tuple3[1] : {tuple3[1]}')
print(f'tuple3[-1] : {tuple3[-1]}')
print(f'tuple3[-2] : {tuple3[-2]}')

print('---------------------3')
# 값 수정
print(f'list3 : {list3}')

list3[2] = 300
print(f'list3[2] = 300 : {list3}')

# 튜플은 읽기 전용이므로 오류 발생
# tuple3[2] = 300

# 값 추가
print('---------------------4')
list4 = []
print(f'list4 : {list4}')

print('---------------------5')
list4.append(100)
list4.append(200)
print(f'list4 : {list4}')

# 리스트나 튜플을 넣어주면 뒤에 추가도니다.
list4.extend([300,400,500,600,700,800,900,1000])
print(f'list4 : {list4}')

print('삽입 ----------------------')
# 인덱스 번호 3(4번째) 위치에 값을 삽입한다.
list4.insert(3,1100)
print(f'list4 : {list4}')

print('변경 ----------------------')
# 인덱스 번호 3(4번째) 위치의 값을 변경한다.
list4[3] = 1200
print(f'list4 : {list4}')

print('값 가져오기 ----------------------')
# 인덱스 번호 3(4번째) 위치의 값을 가져온다.
a1 = list4[3]
print(f'a1 : {a1}')
print(f'list4 : {list4}')

print('(맨뒤)값 빼기 ----------------------')
# 마지막의 값을 가져온다. 값이 변환된 후 리스트에서 제거
a2 = list4.pop()
print(f'a2 : {a2}')
print(f'list4 : {list4}')

print('원하는 위치의 값 빼기 ----------------------')
# 인덱스 3번째 값을 가져온다. 값이 반환된 후 리스트에서 제거
a3 = list4.pop(3)
print(f'a3 : {a3}')
print(f'list4 : {list4}')

print('제거 ----------------------')
# 제거
# 값 300을 제거한다. (300이 여러개 있을 경우 맨 앞의 300 하나만 제거하는듯)
list4.remove(300)
print(f'list4 : {list4}')

print('정렬 ----------------------')
list1 = [30, 10, 20, 50, 40]
print(f'정렬 전 : {list1}')

list1.sort()
print(f'정렬 후 : {list1}')

list1.reverse()
print(f'뒤집기 : {list1}')

print('찾기 ----------------------')
idx1 = list1.index(30)
print(f'30 위치 : {idx1}')

# 없는 값을 찾으면 오류 발생
# idx2 = list1.index(100)
# print(f'100의 위치 : {idx2}')

print('값이 있는지 ----------------------')
a1 = 30 in list1
a2 = 100 in list2
print(f'30 in list1 : {a1}')
print(f'100 in list2 : {a2}')

print('연산 ----------------------')
# 리스트, 튜플, 문자열 모두 동일하며 새로운 것이 생성된다.
list1 = [10, 20, 30]
list2 = [40, 50, 60]

# 더하기
list3 = list1 + list2
print(f'list3 : {list3}')

# 곱하기
list4 = list1 * 3
print(f'list4 : {list4}')

print('튜플을 이용한 초기화 ----------------------')
tuple1 = (10, 20, 30)
list1 = [10, 20, 30]

# 튜플이나 리스트가 관리하고 있는 값의 개수와 동이랗게 좌측에 변수를 나열해주면 1:1 대응해서 하나씩 세팅해 준다. 개수가 다르면 오류 발생
a1, a2, a3 = tuple1
a4, a5, a6 = list1
print(f'{a1}, {a2}, {a3}')
print(f'{a4}, {a5}, {a6}')

## 쉼표(,)를 기준으로 값을 나열해주면 튜플로 만들어진다 !!
tuple2 = 10, 20, 30
print(f'tuple2 : {tuple2}')
print(f'tuple2 type : {type(tuple2)}')

# 튜플을 이용한 값 세팅
a10, a20, a30 = 100, 200, 300
print(f'{a10}, {a20}, {a30}')
