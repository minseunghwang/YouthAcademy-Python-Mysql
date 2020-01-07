-- select : 지정된 테이블에 저장되어 있는 데이터를 가져오는 구문

-- select 가져올 데이터
select 100;
-- select 컬럼명 from 테이블명
-- from > select

select *
from employees;

-- 부서의 정보를 모두 가져온다.
select *
from departments;

-- 사원들의 직함 정보를 모두 가져온다.
select * 
from titles;

-- 사원의 사원번호, 이름, 성을 가져온다.
select emp_no, first_name, last_name
from employees;

-- 사원의 사원번호, 생년월일, 성별을 가져온다.
select emp_no, birth_date, gender
from employees;

-- 부서의 부서번호, 부서 이름을 가져온다.
select dept_no, dept_name
from departments;

-- 각 사원의 사원번호, 급여액을 가져온다.
select emp_no, salary
from salaries;

-- 각 사원의 사원번호, 직함 이름을 가져온다.
select emp_no, title
from titles;

