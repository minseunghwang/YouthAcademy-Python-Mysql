# 셀레니움
# 웹 브라우저를 통제해서 원하는 결과를 가져올 수 있는 모듈
# 필요작업 : 사용할 웹 브라우저에 대한 웹 드라이버를 다운받아야 한다.
# 절대 하지 말아야 할 작업 : 자동회원가입, 댓글 자동으로 달기 -> 잡혀가요...


# 웹 드라이버에 명령을 내리면 웹 드라이버가 브라우저를 컨트롤 한다~ (중간다리역할)
# https://pypi.org/project/selenium/

# pip install selenium

from selenium import webdriver

# 웹 드라이버 가동
driver = webdriver.Chrome('chromedriver')
# driver = webdriver.Chrome('./chromedriver')   # 둘중 되는걸로하면됨

# 네이버에 접속한다.
driver.get('https://naver.com')

# 검색창에 검색어를 입력한다.
query = driver.find_element_by_id('query')
query.send_keys('홍길동')      # send_keys가 키보드에 해당한다 !?!

# 검색버튼을 누른다.
btn = driver.find_element_by_id('search_btn')
btn.click()

print(driver.page_source)

# 로그인을 해야 볼 수 있는 페이지나 페이지 소스보기로 안될때 이것을 사용한다... 음...!