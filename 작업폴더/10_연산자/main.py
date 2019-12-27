print('산술 연산자---------------------------')
a1 = 10 + 3     # 더하기
a2 = 10 - 3     # 빼기
a3 = 10 * 3     # 곱하기
a4 = 10 / 3     # 나누기 (결과가 소수점까지)
a5 = 10 % 3     # 나머지
a6 = 10 // 3    # 나누기 (결과가 정수)
a7 = 10 ** 3    # 거듭제곱
print(f'10 + 3 = {a1}')
print(f'10 - 3 = {a2}')
print(f'10 * 3 = {a3}')
print(f'10 / 3 = {a4}')
print(f'10 % 3 = {a5}')
print(f'10 ** 3 = {a7}')
print(f'10 // 3 = {a6}')

print('비교 연산자---------------------------')
a1 = 10 > 3     # 10이 3보다 큰가
a2 = 10 < 3     # 10이 3보다 작은가
a3 = 10 == 3    # 10이 3과 같은가
a4 = 10 != 3    # 10이 3과 다른가
a5 = 10 >= 3     # 10이 3보다 크거나 같은가
a6 = 10 <= 3     # 10이 3보다 작거나 같은가
print(f'10 > 3 : {a1}')
print(f'10 < 3 : {a2}')
print(f'10 == 3 : {a3}')
print(f'10 != 3 : {a4}')
print(f'10 >= 3 : {a5}')
print(f'10 <= 3 : {a6}')

print('대입 연산자---------------------------')
# 우측의 값, 수식의 결과, 변수의 값을 좌측의 변수에 저장한다.
a1 = 10

# a1 변수에 저장되어 있는 값을 복제해 a2 변수에 저장한다.
a2 = a1

# 수식을 계산해서 얻은 결과를 좌측의 변수에 저장한다.
a3 = a1 + 10

print(f'a1 : {a1}')
print(f'a2 : {a2}')
print(f'a3 : {a3}')

a4 = 10
a4 = a4 + 10

a5 = 10
a5 += 10

print(f'a4 : {a4}')
print(f'a5 : {a5}')

# 다른 프로그래밍 언어에서 사용되는 ++,-- (증감)연산자는 파이썬에서 제공되지 않는다.
# a6 = 10
# a6++
# print(f'a6 : {a6}')

# a7 = 10
# ++a7      # 에러는 안나지만 효과는 미미하다.밈미미밈미미미미미미밈미미
# print(f'a7 : {a7}')

print('논리 연산자---------------------------')
# 참(True), 거짓(False)을 연산하는 연산자.

# True and True => True. 그 외는 모두 False
a1 = 10 > 2 and 10 < 20
print(f'a1 : {a1}')

a2 = 10 > 2 and 10 > 20
print(f'a2 : {a2}')

# or 연산자 : 둘 중에 하나라도 True면 결과는 True
# False or False => False. 그 외는 모두 True
a3 = 10 < 2 or 10 > 20
print(f'a3 : {a3}')

a4 = 10 > 2 or 10 > 20
print(f'a4 : {a4}')

# not 연산자 : True를 False로, False를 True로 바꾸는 연산자
a5 = not 10 < 2
print(f'a5 : {a5}')

a6 = not 10 > 2
print(f'a6 > {a6}')

# 범위
a7 = 10

a8 = a7 > 0 and a7 < 20
print(f'a8 : {a8}')

a9 = 0 < a7 < 20
print(f'a9 : {a9}')

# in 연산자
# 포함 여부를 검사하느 연산자
# list, tuple, set은 값이 포함되어 있는지
# dictionary는 지정된 이름으로 저장되어 있는것이 있는지
list1 = [10, 20, 30, 40, 50]
tuple1 = (10, 20, 30, 40, 50)
set1 = {10, 20, 30, 40, 50}
dict1 = {
    'data1' : 100,
    'data2' : 200
}

r1 = 20 in list1
r2 = 20 in tuple1
r3 = 20 in set1
r4 = 'data1' in dict1

print(f'r1 : {r1}')
print(f'r2 : {r2}')
print(f'r3 : {r3}')
print(f'r4 : {r4}')

r5 = 100 in list1
r6 = 100 in tuple1
r7 = 100 in set1
r8 = 'data10' in dict1

print(f'r5 : {r5}')
print(f'r6 : {r6}')
print(f'r7 : {r7}')
print(f'r8 : {r8}')