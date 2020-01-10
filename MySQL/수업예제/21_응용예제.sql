-- employees 데이터베이스 사용

-- employees 테이블을 복제한 emp100이라는 테이블을 만든다.
create table emp100
as
select *
from employees;

select * from emp100;

-- emp100 테이블의 사원번호, first_name, last_name을 가져와 emp200이라는 테이블을 만든다.
create table emp200
as
select emp_no, first_name, last_name
from emp100;

select * from emp200;

-- emp100 테이블에서 1990년 이후에 입사한 사원들의 정보를 가지고 있는 emp300이라는 테이블을 만든다.
create table emp300
as
select *
from emp100
where hire_date >= '1990-01-01';

select * from emp300;

-- emp100 테이블에서 'd001'부서에 현재 근무하고 있는 사원의 사원번호, first_name, last_name을 가져온다.
select a.emp_no, a.first_name, a.last_name
from emp100 a, dept_emp b
where a.emp_no = b.emp_no and b.dept_no='d001';

-- emp100 테이블에서 현재의 평균 급여보다 적게 받는 사원들의 정보를 모두 삭제한다.
delete from emp100
where emp_no in (select emp_no 
					from (select a.emp_no
							from emp100 a, salaries s
							where a.emp_no = s.emp_no and s.salary < (select avg(salary)
																		from salaries
																		where to_date = '9999-01-01') and s.to_date = '9999-01-01') tmpp);


-- emp100 테이블에서 'd002' 부서에 근무하고 있는 사원들의 고용 날짜를 오늘로 수정한다.
update emp100
set hire_date = sysdate()
where emp_no in (select emp_no
					from (select a.emp_no
							from emp100 a join dept_emp d
							on a.emp_no = d.emp_no
							where dept_no = 'd002') tmp);
                            
select * from emp100;
