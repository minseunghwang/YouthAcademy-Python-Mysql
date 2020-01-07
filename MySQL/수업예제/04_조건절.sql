-- d005 부서에 근무하고 있는 사원들의 사원번호와 근무부서번호를 가져온다
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

-- 부서번호가 d005가 아닌 사원들의 사원 번호, 부서 번호를 가져온다.
select emp_no, dept_no
from dept_emp
where dept_no <> 'd005';

-- 급여액이 150000 이상인 사원의 사원번호, 급여액을 가져온다.
select emp_no, salary
from salaries
where salary >= '150000';
-- 숫자데이터지만 '' 해도 되고 안해도되네 

-- 급여액이 40000 이하인 사원들의 사원번호, 급여액을 가져온다
select emp_no, salary
from salaries
where salary <= 40000;

-- 1986년 이후에 고용한 사원들의 사원번호, 고용일, 성, 이름을 가져온다
select emp_no, hire_date, last_name, first_name
from employees
where hire_date >= '1986-01-01' order by hire_date ASC;

-- 1990년 이후에 매니저가 된 사원들의 사원번호, 부서번호, 매니저 시작 날짜를 가져온다.
select emp_no, dept_no, from_date
from dept_manager
where from_date >= '1990-01-01';

-- 1990년 이전에 고용된 사원들의 사원번호, 고용일을 가져온다.
select emp_no, hire_date
from employees
where hire_date < '1990-01-01' order by hire_date DESC;

-- 모든 직원들의 사원번호, 현재 받고 있는 급여를 가져온다.
-- 현재 받고있는 급여는 종료일이 '9999-01-01'로 저장되어 있다.
select emp_no, salary
from salaries
where to_date = '9999-01-01';

select first_name
from employees
where count(first_name) >= '2';
