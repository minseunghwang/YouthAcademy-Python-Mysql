# 문자열

str1 = "문자열입니다."
str2 = '문자열입니다.'
print('str1 :', str1)
print('str2 :', str2)
print('str1 type :', type(str1))
print('str2 type :', type(str2))

str3 = "이름은 '홍길동'이고 나이는 \"30\"살 입니다."
str4 = '이름은 \'홍길동\'이고 나이는 "30"살 입니다.'
print('str3 :', str3)
print('str4 :', str4)

# """ """, ''' ''' 문자열
# 작성한 그대로 관리하는 문자열
str5 = """이름은 '홍길동'이고 나이는 "30살" 입니다."""
str6 = '''이름은 '홍길동'이고 나이는 "30살" 입니다.'''
print('str5 :', str5)
print('str6 :', str6)

str7 = '동해물과 백두산이\n마르고 닳도록\n하느님이 보우하사\n우리나라 만세'
print('str7 :', str7)

str8 = '''동해물과 백두산이
마르고 닳도록
하느닝미 보우하사
우리나라 만세'''
print('str8 :', str8)

# 글자수
str9 = 'abcdef'
str10 = '안녕하세요'
print('str9의 길이 :', len(str9))
print('str10의 길이 :', len(str10))

# 문자열 합치기
str11 = '문자열1' + '문자열2'
print('str11 :', str11)

# 문자열 곱하기
str12 = '문자열 ' * 3
print('str12 :', str12)

# 다른 타입과 합치기
# str13 = '문자열' + 100
# print('str13 :', str13)

# str() : 문자열로 변환시켜 준다
str14 = '문자열' + str(100)
print('str14 :', str14)

# 문자열 포멧팅 : 문자열 양식을 지정하여 사용하는 것.
name = '홍길동'
age = 20

# 그냥 불편하다고 함
str15 = '이름은 ' + name + '이고 나이는 ' + str(age) + '입니다. ' + name + '님아~~'
print('str15 :', str15)

# 포멧 문자열
# 59페이지 표 참조
# 앞에서 부터 1:1 대응되어 값이 세팅된다.
str16 = '이름은 %s이고 나이는 %d입니다. %s님아~~~' % (name,age,name)
print('str16 :', str16)

# {인덱스} 번째 값을 세팅한다.
str17 = '이름은 {0}이고 나이는 {1}입니다. {0}님아~~' .format(name,age)
print('str17 :', str17)

# 포멧 문자열, 파이썬 3.6부터 지원
str18 = f'이름은{name}이고 나이는 {age}입니다. {name}님아~~'
print('str18 :', str18)

# 문자열 함수
str1 = '동해물과 백두산이 동해물과 한라산이'

# count : 지정된 문자열이 몇개가 있는지
a1 = str1.count('동해물과')
a2 = str1.count('서해물과')
print(f'a1 : {a1}')
print(f'a1 : {a2}')

# find, index : 지정한 문자열이 어디에 있는지
# 존재하는 문자열일 경우 : 0부터 시작하는 인덱스를 반환한다.
# 존재하지 않는 문자열일 경우 : find는 -1을 반환하고, index는 오류가 발생한다.

a1 = str1.find('동해물과')
a2 = str1.find('백두산이')
a3 = str1.find('서해물과')
print(f'a1 : {a1}')
print(f'a2 : {a2}')
print(f'a3 : {a3}')
print('---------------------1')

a1 = str1.index('동해물과')
a2 = str1.index('백두산이')
# a3 = str1.index('서해물과')
print(f'a1 : {a1}')
print(f'a2 : {a2}')
# print(f'a3 : {a3}')

print('---------------------2')
str1 = 'abCDef'
# 대문자 -> 소문자
str2 = str1.lower()
# 소문자 -> 대문자
str3 = str1.upper()

print(f'str1 : {str1}')
print(f'str2 : {str2}')
print(f'str3 : {str3}')

print('---------------------3')
# 공백삭제
str1 = '      문자열      '
str2 = str1.lstrip()
str3 = str1.rstrip()
str4 = str1.strip()

print(f'str1 : [{str1}]')
print(f'str2 : [{str2}]')
print(f'str3 : [{str3}]')
print(f'str4 : [{str4}]')

print('---------------------4')
# 문자열 바꾸기
str1 = '동해물과 고구마감자'
str2 = str1.replace('고구마감자', '바나나')
print(f'str1 : {str1}')
print(f'str2 : {str2}')

# 문자열 나누기
str1 = '동해_물과 백두_산이 마르_고 닳_도록'
# 띄어쓰기를 기준으로 문자열을 나눈다.
str2 = str1.split()
print(f'str2 : {str2}')

# _를 기준으로 문자열을 나눈다.
str3 = str1.split('_')
print(f'str3 : {str3}')
