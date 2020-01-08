-- 서브쿼리, 쿼리문 안에 들어가는 쿼리
-- 쿼리문 작성시 필요한 값을 구해야 하는 경우 사용.

-- 현재 받는 급여의 평균보다 많이 받는 사원들의 사원번호, 급여액을 가져온다.

-- 1단계) 현재 받는 급여의 평균이 얼마인지 모르므로 아무거나 정해서 쿼리문을 만든다. 
select emp_no, salary
from salaries
where to_date = '9999-01-01'
	and salary > 50000;
    
-- 2단계) 임의로 정한 값(급여평균)을 구하는 쿼리문을 만든다.
select avg(salary)
from salaries
where to_date = '9999-01-01';

-- 3단계) 임의로 정한 값 부분에 서브쿼리를 세팅해준다.
select emp_no, salary
from salaries
where to_date = '9999-01-01'
	and salary > (select avg(salary)
					from salaries
					where to_date = '9999-01-01');