
-- 가져온다.
-- 가져올 데이터 : 사원번호, 근무 부서 번호
-- 조건 : d005 부서에 근무하고 있는 사원들

select emp_no, dept_no
from dept_emp
where dept_no = 'd005';

-- 비교연산자
-- = : 같은가
-- <> 등 : 다른가 ( python에서 != 이거 ㅋㅋ)
-- > : 큰가
-- < : 작은가
-- >= 크거나 같은가
-- <= 작거나 같은가


