-- 현재 사원들이 받고 있는 급여액을 가지고 있는 current_salary1 이라는 테이블을 생성한다.
create table current_salary1
as
select emp_no, salary
from salaries
where to_date = '9999-01-01';

select * from current_salary1;

-- 구조만 복제해서 새로운 테이블을 만들고자 한다면
-- where의 조건을 모든 로우에 대해 거짓인 것으로 만들어준다.
create table employees2
as
select *
from employees
where 1=0;

desc employees2;

select *
from employees2;

-- 사원의 사원번호, 이름, 근무부서이름, 현재 받고있는 급여정보를 가지고있는 테이블을 만든다.
select * from employees a1, salaries a2
where a1.emp_no = a2.emp_no and to_date = '9999-01-01';

create table current_salaries100
as
select a1.emp_no, a1.first_name, a2.dept_name, a3.salary
from employees a1, departments a2, salaries a3, dept_emp a4
where a1.emp_no = a3.emp_no and a1.emp_no = a4.emp_no
	and a2.dept_no = a4.dept_no
    and a3.to_date = '9999-01-01'
    and a4.to_date = '9999-01-01';
    
select * from current_salaries100;