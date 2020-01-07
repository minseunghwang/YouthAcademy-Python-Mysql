-- like 연산자 : 문자열을 이용해 조건식을 만들 경우 포함 여부의 조건을 만들 때 사용한다.
-- % : 0개 이상의 글자 수
-- _ : 글자 하나

-- 이름이 A로 시작하는 사원의 사원번호, 이름을 가져온다.
-- 가져올 데이터 : 사원의 사원번호, 이름
-- 조건 : 이름이 A로 시작한다.

SELECT EMP_NO, FIRST_NAME
FROM EMPLOYEES
WHERE FIRST_NAME LIKE 'A%';

-- 이름의 두번째 글자가 i인 사원의 사원번호, 이름을 가져온다.
select emp_no, first_name
from employees
where first_name LIKE '_i%';

-- 이름에 o가 포함되어 있는 사원의 사원번호, 이름을 가져온다.
-- 단 마지막 글자가 o가 아닌 사원만 가져온다.
select emp_no, first_name
from employees
where first_name not like '%o%';

-- 이름이 5글자인 사원의 사원번호, 이름을 가져온다.
select emp_no, first_name
from employees
where first_name like '_____';