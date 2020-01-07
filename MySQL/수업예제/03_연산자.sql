-- 산술 연산자
select 20 + 10;
select 20 - 10;
select 20 * 10;
select 20 / 10;

select salary, salary+1000, salary-1000, salary * 10, salary / 10
from salaries;

-- 사원들의 급여를 10% 인상해서 가져온다.
select salary * 1.1 as 인상후, salary as '인상 전'
from salaries;

-- 사원들의 급여를 10% 인하해서 가져온다.
select salary * 0.9
from salaries;

-- 숫자 컬럼이 아닌 것 끼리 연산을 하면 결과는 0이 나온다.
select first_name + last_name
from employees;

-- 결과중에 중복된 row를 제거해서 가져온다.
select distinct dept_no
from dept_emp;

select emp_no, from_date
from salaries;