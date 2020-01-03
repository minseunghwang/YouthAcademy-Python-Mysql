# 1부터 100까지 합을 구하여 다음과 같이 결과를 출력하세요...

# 출력 양식 : 1부터 100까지 합은 0000입니다.

start, end = 1, 100
sum = 0
for i in range(start,end+1):
    sum += i
print(f'{start}부터 {end}까지 합은 {sum}입니다.')