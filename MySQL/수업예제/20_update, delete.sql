-- update : 컬럼의 값을 수정
-- update 테이블명 set 컬럼명=값, 컬럼명=값, 컬럼명=값 [where 조건절]

use employees;

drop table employees2;

create table employees2
as
select * from employees;

select * from employees2;

-- 생년월일을 오늘로 변경.
update employees2
set birth_date = sysdate();

-- first_name은 홍, last_name은 길동
update employees2
set first_name='홍', last_name='길동';

select * from employees2;

-- 10001 사원의 first_name은 이, last_name은 순신으로 바꾼다.
update employees2
set first_name='이', last_name='순신'
where emp_no = '10001';

-- 현재의 급여 평균보다 더 많이 받는 사원의 first_name을 '금수저'로 변경한다.
update employees2
set first_name='금수저'
where emp_no in (select emp_no
				from salaries
				where salary > (select avg(salary)
								from salaries
								where to_date = '9999-01-01')
						and to_date = '9999-01-01');



select salary
from salaries
where to_date='9999-01-01';

select * from employees2;


-- 삭제
-- delete from 테이블명 [where 조건절]
-- first_name이 금수전인 사원들의 데이터를 삭제

delete from employees2
where first_name = '금수저';

select * from employees2;

-- 조건절이 업으면 모든 Row가 삭제된다.
delete from employees2