-- 논리 연산자
-- and : 좌우 조건이 모두 만족하는 조건
-- or : 좌우 조건중 하나라도 만족하는 조건
-- not : 우측의 조건을 부정

-- d001 부서의 매니저 중에서 1990년 이후부터 매니저인 사원의 사원번호, 부서번호, 매니저 시작날짜를 가져온다.
select emp_no, dept_no, from_date
from dept_manager
where dept_no = 'd001' and from_date >= '1990-01-01';

-- 1990년 이후에 입사한 남자 사원의 사원번호, 성명, 고용일을 가져온다.
select emp_no, first_name, hire_date
from employees
where hire_date >= '1990-01-01' and gender = 'M';

-- 1990년 이후부터 60000이상의 급여를 받는 사원의 사원번호, 급여, 급여 시작 날짜를 가져온다.
select emp_no, salary, from_date
from salaries
where from_date >= '1990-01-01' and salary >= 60000;

-- d001 부서 매니저들과 d002 부서 매니저들의 사원번호, 부서번호를 가져온다.
select emp_no, dept_no
from dept_manager
where dept_no = 'd001' or dept_no = 'd002';

-- 직함이 Staff인 사원과 Engineer인 사원의 사원번호, 직함을 가져온다.
select emp_no, title
from titles
where title = 'Staff' or title='Engineer';

-- 부서 번호가 d003이 아닌 매니저의 사원번호와 부서 번호를 가져온다.
select emp_no, dept_no
from dept_manager
where dept_no <> 'd003';

-- 급여가 60000 이상 70000이하인 사원들의 사원번호, 급여를 가져온다.
select emp_no, salary
from salaries
where salary >= 60000 and salary <= 70000 order by salary ASC;


select *
from dept_manager a join departments b
where a.dept_no = b.dept_no
group by b.dept_no
order by a.dept_no ASC;
