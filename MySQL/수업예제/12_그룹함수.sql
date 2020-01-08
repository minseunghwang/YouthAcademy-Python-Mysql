-- 전체 사원의 수를 구한다.
select count(*) from employees;

-- 남자 사원의 수를 구한다.
select count(*)
from employees
where gender = 'M';

-- 현재 d001 부서에 근무하고 있는 사원의 수를 가져온다
select count(*)
from dept_emp
where dept_no = 'd001' and to_date='9999-01-01';

-- 현재 받고 있는 급여의 총 합을 구한다.
select salary, sum(salary), avg(salary), max(salary), min(salary)		-- 이거 오라클이면 오류가 났어요. 왜? salary는 값이 여러개고 나머지는 하나의 값임 -> 절대로 이렇게 쓰지마세요 (아마 mysql은 맨 위 값이 나온듯)
from salaries
where to_date='9999-01-01';

