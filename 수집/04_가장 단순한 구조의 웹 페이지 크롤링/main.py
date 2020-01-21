import bs4
import requests
import time
import pandas

# 첫 페이지의 주소
site = 'https://pjt3591oo.github.io/'

# 수집된 데이터를 담을 리스트
data_list = []

# 수집할 데이터를 가지고 있는 페이지를 요청하는 함수
def getDivList(site):
    # 요청
    response = requests.get(site)

    soup = bs4.BeautifulSoup(response.text, 'lxml')

    # div 태그중에 class가 p인 태그를 가져온다
    div_list = soup.find_all('div', class_="p")
    # print(div_list)
    # for div in div_list:
    #     print(div)
    #     print('------------')

    # 다음 페이지의 정보를 추출한다.
    ul_tag = soup.find('ul', class_='pager')
    # 태그 사이에 문자열이 Next인 태그를 가져온다.
    next_tag = ul_tag.find(any, text='Next')

    # 태그가 a 태그라면...
    next_target = None

    if next_tag.name == 'a':
        next_target = next_tag.attrs['href']

    return div_list, next_target

# print(div_list[0])

def getDivData(div_tag):

    # 제목 추출
    h3_tag = div_tag.find('h3')
    a_tag = h3_tag.find('a')
    a_text = a_tag.text
    # print(a_text)

    # 부가 설명
    h4_tag = div_tag.find('h4')
    h4_text = h4_tag.text
    # print(h4_text)

    # 날짜와 저자
    p_tag = div_tag.find('p', class_='author')
    span_tag = p_tag.find('span')
    span_text = span_tag.text
    temp_str = span_text.split('|')
    date_str = temp_str[0]
    author_str = temp_str[1]
    # print(date_str, author_str)
    return a_text.strip(), h4_text.strip(), date_str.strip(), author_str.strip()

while True:
    # delay 1초
    time.sleep(1)

    print(site)

    div_list, next_target = getDivList(site)

    for div_tag in div_list:
        data_tuple = getDivData(div_tag)
        data_list.append(data_tuple)

    # 다음 페이지가 있다면...
    if next_target != None:
        site = f'https://pjt3591oo.github.io{next_target}'
    else :
        break

# for a1 in data_list:
#     print(a1)

# 저장
columns = ['subject1', 'subject2', 'date', 'author']
df1 = pandas.DataFrame(data_list, columns=columns)
df1.to_csv('basic.csv', index=False, encoding='utf-8-sig')
print('저장완료')




# response100 = requests.get('https://pjt3591oo.github.io/page5/')
# print(response100)