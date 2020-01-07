-- order by : 특정 컬럼을 기준으로 정렬할 수 있다.

-- 사원의 번호와 급여를 가져온다. 급여를 기준으로 오름차순 정렬한다.
-- 가져올 데이터 : 사원번호, 급여
-- 조건 : 없음
-- 정렬 기준 : 급여(오름차순)

select emp_no, salary
from salaries
order by salary asc;

-- 사원의 번호와 급여를 가져온다. 급여를 기준으로 내림차순 정렬한다.
-- 가져올 데이터 : 사원번호, 급여
-- 조건 : 없음
-- 정렬 기준 : 급여(내림차순)
select emp_no, salary
from salaries
order by salary desc;

-- 사원의 사원번호와 이름을 가져온다. 이름을 기준으로 오름차순 정렬을 한다.
select emp_no, first_name
from employees
order by first_name asc;

-- 사원의 이름과 고용일을 가져온다. 고용일 기준으로 오름차순 정렬을 한다.


-- 사원의 이름과 고용일을 가져온다. 고용일 기준으로 내림차순 정렬을 한다.


-- 사원의 사원번호와 이름을 가져온다. 이름을 기준으로 내림차순 정렬을 한다.
select emp_no, first_name
from employees
order by first_name desc;