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