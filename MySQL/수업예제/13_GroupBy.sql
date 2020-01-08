-- group by : 집계함수를 사용할 때 그룹의 기준이 될 컬럼을 지정한다.
-- 지정된 커럶에 저장되어 있는 값들 중 같은 값끼리 그룹으로 묶이게 된다.

-- 사원의 수를 성별로 구분하여 가져온다.
select gender, count(*)
from employees
group by gender;

-- 각 부서에 근무하고 있는 사원들의 수를 가져온다.
select dept_no, count(*)
from dept_emp
where to_date = '9999-01-01'
group by dept_no;

-- 각 부서별 과거의 매니저의 수를 구한다.
select dept_no, count(dept_no)
from dept_manager
where to_date <> '9999-01-01'
group by dept_no;

-- 급여 수령 시작일 별 급여 총합, 평균, 최고액, 최소액을 구한다.
select from_date, sum(salary) '총합', avg(salary) '평균', max(salary) '최고액', min(salary) '최소액'
from salaries
group by from_date;

-- 10만명 이상이 사용하고 있는 직함의 이름과 직원의 수를 가져온다.
select title '직함', count(emp_no) as '직원수'
from titles
group by title
having 직원수 >= 100000;

-- 5만명 이상이 근무하고 있는 부서의 부서번호와 소속 사원들의 수를 가져온다.
select dept_no '부서번호', count(emp_no) '사원수'
from dept_emp
group by dept_no
having 사원수 >= 50000;