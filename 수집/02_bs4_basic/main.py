# BS4(BeautifulSoup 4)
# xml이나 html 양식의 문자열에서 원하는 데이터를 가져올 수 있도록 제작된 모듈

# pip install bs4
# pip install Lxml

import bs4
# import lxml

# 파서 (문서를 분석하는 도구) 생성
html = ''
soup = bs4.BeautifulSoup(html,'lxml')
print(soup)
print(type(soup))

html = '<p>test</p>'
soup = bs4.BeautifulSoup(html, 'lxml')
print(soup)
print(soup.prettify())

# 예제 html
html = '''
        <html>
            <head>
                <title>title 태그</title>
            </head>
            <body>
                <p>test1</p>
                <p>test2</p>
                <p>test3</p>
            </body>
        </html>
'''

# bs4 객체 생성
soup = bs4.BeautifulSoup(html, 'lxml')
# title 태그 출력
print(f'title태그 : {soup.title}')
print(f'title태그의 태그 이름 : {soup.title.name}')
print(f'title태그 내에 있는 문자열 : {soup.title.text}')

print(f'p태그 : {soup.p}')
print(f'p태그의 태그 이름 : {soup.p.name}')
print(f'p태그의 태그내의 문자열 : {soup.p.text}')

html = '''
        <html>
            <body>
                <input type='text' id='test_id' class='c1 c2'/>
            </body>
        </html>
    '''

soup = bs4.BeautifulSoup(html, 'lxml')
# 속성 값
print(soup.input.attrs)
print(soup.input.attrs['type'])
print(soup.input.attrs['id'])
print(soup.input.attrs['class'][0])
print(soup.input.attrs['class'][1])
