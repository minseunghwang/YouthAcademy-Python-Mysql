# module1.py

print(f'__name__ : {__name__}')

# __name__ 변수 사용 예
# __name__ 변수에는 모듈의 이름이 들어 있지만 현재 모듈을 실행할 때 사용했다면 '__main__'이라는 문자열이 들어있다.
# 이를 이용해 현재 모듈에서 구현한 함수나 클래스 등을 테스트 해보기 위한 코드를 작성한다.

def add(a1,a2):
    return a1 + a2
def minus(a1,a2):
    return a1 - a2

if __name__ == '__main__':
    r1 = add(100,200)
    r2 = minus(100,200)

    print(f'r1 : {r1}')
    print(f'r2 : {r2}')

elif __name__ == 'module1':
    print('키득키득')
