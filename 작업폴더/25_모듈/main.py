# 모듈
# 파이썬에서 py 파일 하나를 모듈이라고 부른다.
# 하나의 파일에 너무 많은 코드들을 작성하면 관리하기 힘들어지기 때문에, 여러 파일로 나눠 작업하는 것을 의미한다.

print('main.py 파일 입니다.')
a1 = 100
# module1을 포함한다
# 다른 모듈을 포함시키면 파일의 내용이 복사되어 붙여넣어 진다고 생각하면 된다.
import module1

print('main.py 파일 입니다.')
# 다른 모듈의 변수를 가져와 사용할 때는 '모듈명.변수명'의 형태로 사용해야 한다.
print(f'a2 : {module1.a2}')
module1.module1_fun1()

# 다른 모듈에 있는 요소를 사용할때는 모듈 이름을 작성해줘야 한다.
# 모듈이름.함수
import module2 as m2
print(f'm2.a200 : {m2.a2}')
m2.module2_fun1()

# from 구문을 이용해 다른 모듈에 있는 함수, 클래스를 정의해주면 모듈이름을 생략할 수 있다.

# 선택
# from module3 import module3_fun1
# from module3 import module3_fun2

# 선택
# from module3 import module3_fun1, module3_fun2

# 특정 모듈에 있는 함수나 클래스를 모두 사용하겠다 명시
from module3 import *

module3_fun1()
module3_fun2()

