# 구구단을 다음과 같이 출력하세요...

# 2 X 1 = 2         2 X 2 = 4           2 X 3 = 6 .......... 2 X 9 = 18
# 3 X 1 = 3         3 X 2 = 6           3 X 3 = 9 .......... 3 X 9 = 27
# ....
# 9 X 1 = 9         9 X 2 = 18           9 X 3 = 27 .......... 9 X 9 = 81

# print('2 X 1 = 2', end='       ')
# print('2 X 2 = 4', end='       ')

# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i} X {j} = {i*j}', end='   ')
#     print('')

for i in range(2,10):
    print(f'{i}단', end=' ★★  ')
    for j in range(1,10):
        gugudan = '%d X %d = %2d' % (i,j,i*j)
        print(gugudan, end='   ')
    print('★★')