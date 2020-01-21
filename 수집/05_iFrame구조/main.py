import requests
import bs4
import time
import pandas

# 수집한 데이터를 담을 리스트
data_list = []

def get_response(site):
    # 요청한다
    response = requests.get(site)
    return response.text

def get_data(html):
    soup = bs4.BeautifulSoup(html, 'lxml')

    div_tag = soup.find('div', class_='score_result')
    ul_tag = div_tag.find('ul')
    li_tag = ul_tag.find_all('li')

    for li_obj in li_tag:
        star_score_tag = li_obj.find('div', class_='star_score')
        em_tag = star_score_tag.find('em')
        # print(em_tag.text)
        # print('==========================')

        score_reple = li_obj.find('div', class_='score_reple')
        p_tag = score_reple.find('p')
        span_tag = p_tag.find('span')
        # print(span_tag.text.strip())

        tuple1 = em_tag.text.strip(), span_tag.text.strip()
        data_list.append(tuple1)


# 요청할 주소
site = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=109906&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'

html = get_response(site)
get_data(html)

print(data_list)
