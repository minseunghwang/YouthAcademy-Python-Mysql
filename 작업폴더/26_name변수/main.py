# __name__ 변수
# 모듈의 이름이 문자열로 들어있는 변수
# module1.py => 'module1'
# 단, 실행할때 사용한 모듈에서는 모듈의 이름이 아니라 __main__이라는 문자열이 들어있다.

print(f'main __name__ : {__name__}')

import module1


# 실행할때 사용하는 모듈이라고 하더라도 나중에느 다른 모듈에서 가져다 사용할 때가 있을 수 있기 때문에
# if 문을 넣어주는것이 관례 이다
if __name__ == '__main__':
    r1 = module1.add(100,200)
    r2 = module1.minus(100,200)

    print(f'main r1 : {r1}')
    print(f'main r2 : {r2}')