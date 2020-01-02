# main.py
# 패키지 : 모듈들을 하나의 폴더에 넣어서 관리하는 개념
# 패키지는 __init__.py 파일이 있어야 인식이 된다.(3.3 버전 이후로는 파일 생략가능) ->__init__ 없어도 된다는 소리

# 기본
import pkg1.module1
import pkg1.module2

pkg1.module1.pkg1_module1_fun1()
pkg1.module1.pkg1_module1_fun2()
pkg1.module2.pkg1_module2_fun1()
pkg1.module2.pkg1_module2_fun1()

# 별칭
import pkg2.module3 as m3
import pkg2.module4 as m4

m3.pkg2_module3_fun1()
m3.pkg2_module3_fun2()
m4.pkg2_module4_fun1()
m4.pkg2_module4_fun2()

print('----------------------------------------')

# 패키지명, 모듈 생략 : 사용할 함수나 클래스를 명시
from pkg3.module5 import pkg3_module5_fun1, pkg3_module5_fun2
from pkg3.module6 import pkg3_module6_fun1, pkg3_module6_fun2

# 모듈 내의 모든 함수나 클래스 사용
from pkg3.module5 import *
from pkg3.module6 import *

pkg3_module5_fun1()
pkg3_module5_fun2()
pkg3_module6_fun1()
pkg3_module6_fun2()

print('----------------------------------------')

# 패키지명만 생략
# from pkg4 import module7, module8

## import 다음에 모듈들을 나열하는 대신 *를 사용할 때는 import 될 모듈의 이름들을 __init__.py 파일에 명시해줘야 한다.
from pkg4 import *

module7.pkg4_module7_fun1()
module7.pkg4_module7_fun2()
module8.pkg4_module8_fun1()
module8.pkg4_module8_fun2()


