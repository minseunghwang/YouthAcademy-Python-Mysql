import bs4

# find_all (조건에 맞는 모든 태그를 가져온다)
html = '''
        <html>
            <body>
                <p class='a1'>p태그 1</p>
                <p class='a2' id='k1'>p태그 2</p>
                <p class='a1 a3'>p태그 3</p>
                <ul>
                    <li class='a1'>항목1</li>                    
                    <li class='a2'>항목2</li>                    
                    <li class='a1 a2'>항목3</li>                    
                </ul>
            </body>
        </html>
'''

soup = bs4.BeautifulSoup(html, 'lxml')

# 문서 내의 모든 p 태그를 가져온다.
p_list = soup.find_all('p')
# 문서 내의 모든 li 태그를 가져온다.
li_list = soup.find_all('li')

print(p_list)
print(li_list)

for p_tag in p_list:
    print(p_tag.text)
for li_tag in li_list:
    print(li_tag.text)

# find 조건에 맞는 태그를 찾아 반환한다.
# 조건에 맞는 태그가 여러개라면 가장 위에 있는 태그 하나만 반환한다.
p_tag = soup.find('p')
print(p_tag)
print(p_tag.text)

# css 셀렉터 사용
# id가 k1인 태그를 가져온다.

k1 = soup.select('#k1')
print(k1)
print(k1[0].text)

print('---------------------')
print('p 태그들을 모두 가져온다.')

p1 = soup.findAll('p')
p2 = soup.select('p')
print(f'p1 : {p1}')
print(f'p2 : {p2}')

print('---------------------')
print('class 속성에 a1이 있는 태그 모두를 가져온다.')
a1_list1= soup.find_all(class_ = 'a1')
a1_list2= soup.select('.a1')
print(f'a1_list1 : {a1_list1}')
print(f'a1_list1 : {a1_list2}')

print('---------------------')
print('id가 k1인 태그를 가져온다.')
k1_tag1 = soup.find(id='k1')
k1_tag2 = soup.select_one('#k1')
print(f'k1_tag1 : {k1_tag1}')
print(f'k1_tag2 : {k1_tag2}')

print('---------------------')
print('li 태그들 중에 class 속성이 a2인 태그들을 가져온다.')
a2_list1 = soup.find_all('li', class_='a2')
a2_list2 = soup.select('li.a2')
print(f'a2_list1 : {a2_list1}')
print(f'a2_list2 : {a2_list2}')

