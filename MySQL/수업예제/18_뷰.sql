use employees;

create table employees3
as
select * from employees;

-- 테이블 잘 만들어졌나 화긴~
select * from employees3;

-- 서브쿼리를 이용해 테이블을 생성한다.		-- as 다음 나오는 쿼리문을 실행해 그 결과를 불러와 새로운 테이블에 저장하는것
create table employees_new_table
as
select * from employees3;

-- 서브쿼리를 이용해 뷰를 생성한다.		-- as다음 나오는 쿼리문을 실행하는게아니라 저장하고 끝냄!
create view employees_new_view
as
select * from employees3;

-- 새롭게 생성한 테이블로 테스트
select * from employees3 where emp_no = '10001';
select * from employees_new_table where emp_no = '10001';

update employees3 set gender = 'F' where emp_no = '10001';
update employees3 set hire_date = sysdate() where emp_no = '10001';

select * from employees3 where emp_no = '10001';

-- 테이블 제거
-- drop table 테이블명
drop table current_salaries100;

-- 뷰를 만들때 사용한 테이블 제거
-- 뷰를 제거하기 전에 뷰가 참조하는 테이블을 먼저 제거하면 문제가 발생한다.
drop table employees3;

select * from employees_new_view;

-- 뷰 제거
drop view employees_new_view;