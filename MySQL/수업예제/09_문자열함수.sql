-- 문자열 합치기
select concat('aaaa','bbbb','cccc');

-- 사원들의 성과 이름을 가져온다. 하나로 합쳐서 가져온다.
select concat(first_name,' ', last_name) as fullname
from employees;

-- 중간에 삽입하기
-- (원본 문자열, 시작위치(1부터), 제거할 글자 개수, 제거된 위치에 삽입될 문자열)
select insert('aaaaa', 2, 1, 'bbb');

-- 모든 사원의 이름의 두번째 글자부터 두 글자를 지우고 'abcedf'를 삽입한다.
select insert(first_name, 2, 2, 'abcedf')
from employees;

-- 변경
-- (원본 문자열, 바꿀 문자열, 새로운 문자열)
select replace('abcdefg', 'cd', 'kkkkkk');

-- 어디에 있는가...
select instr('abcdefg', 'cde');

select instr('abcdefg','3');

-- 좌측에서 지정된 글자만 가져오기
-- (문자열, 좌측에서부터 가져올 글자수)
select left('abcdefg', 3);

-- 우측에서 지정된 글자만 가져오기
-- (문자열, 우측에서부터 가져올 글자수)
select right('abcdefg', '3');

-- 지정된 위치의 글자를 가져오기
-- (문자열, 가져올 문자열의 시작위치, 가져올 문자열의 개수)
select mid('abcdefg', 3, 3);

-- substring()
-- mid와 동일
select substring('abcdefg', 3, 3);

-- 공백제거
select concat('[', '     문자열     ', ']');
select concat('[', ltrim('     문자열     '), ']');
select concat('[', rtrim('     문자열     '), ']');
select concat('[', trim('     문자열     ');

-- 대문자 -> 소문자  ,   소문자 -> 대문자
select lcase('abCDef');
select lower('abCDef');

select ucase('abCDef');
select upper('abCDef');

-- 뒤집기
select reverse('abcdef')

