dog, chicken, cat, horse = 0, 0, 0, 0

for i in range(1,101):
    if i%2 == 1:
        dog += 1
    if i%4 == 2:
        chicken +=1
    if i%2 == 0:
        cat += 1
    if i%3 == 0:
        horse += 1
print(f'★강아지 : {dog} ★\n★고양이 : {cat} ★\n★닭 : {chicken} ★\n★말: {horse} ★')
print(f'총합 : {dog + cat + chicken + horse}')

print('------------------')

ryu = 100
for i in range(1,30):
    ryu = ryu + 3 * ryu
print(ryu)
