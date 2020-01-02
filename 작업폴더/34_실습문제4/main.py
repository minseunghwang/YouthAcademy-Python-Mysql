# 사용자가 종료할 때까지 입력받은 문자열을 "c:/새파일.txt' 파일에 계속 추가하는 코드를 작성하시오

while True :
    data = input('입력 : ')
    with open('D:\새파일.txt', 'at', encoding='utf-8') as fp :
        fp.write(data+' ')
    if not data:
        break

    print(data)