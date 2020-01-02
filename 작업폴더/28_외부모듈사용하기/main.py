# 현재 프로젝트에서만 모듈을 사용할 경우
# main.py파일과 같은 폴더 위치에 패키지나 모듈을 배치한다.
# env 환경인 경우 venv/Lib/site-packages에 넣어도 된다.
# venv 환경 : 파이썬 실행 환경을 복제해 사용하는 프로젝트별 실행 환경

# 다수의 프로젝트에서 사용할 경우
# python 설치 폴더안에 있는 Lib/site-packages에 넣어준다.

from pkg2.module3 import pkg2_module3_fun1
pkg2_module3_fun1()

# pypi를 이용한 모듈 설치
# https://pypi.org/
# pip install numpy

import numpy as np
array1 = np.array([1,2,3])
print(f'array1 : {array1}')


import requests as req

response = req.get('https://google.com')
print(response.text)
