# main.py

# requests 모듈 : 파이썬에서 웹 주소를 이용해 서버에 요청할 수 있도록 만든 모듈
# 웹에서 데이터를 수집하는 모든 모듈은 이 모듈을 내부적으로 사용하고 있다.

import requests

# 요청할 페이지의 주소
url = 'https://google.com'

# 요청한다.
# get 방식
response1= requests.get(url)
# 200 : 정상, 404 : 주소가 잘못된 것, 405 : 요청방식을 지원하지 않는 것  (요청의 문제)
# 500 : 서버의 코드가 잘못된 것   (서버의 문제)
print(f'response1 : {response1}')

# post 방식
response2 = requests.post(url)
print(f'response2 : {response2}')

# 응답 코드값
print(f'response1 응답 코드 : {response1.status_code}')
print(f'response2 응답 코드 : {response2.status_code}')

# 응답 결과
print(response1.text)