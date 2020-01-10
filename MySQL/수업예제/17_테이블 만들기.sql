-- 테이블 생성 테스트를 위해 데이터베이스를 만든다.
create database testdb1
character set = utf8mb4
collate = utf8mb4_0900_ai_ci;

-- 만든 데이터베이스를 선택한다.
use testdb1;

-- 자료형
-- 정수 : smallint(2), int(4), bigint(8)
-- 실수 : float(4), double(8)
-- 문자열 : char(고정길이, 1 ~ 255), varchar(가변길이, 1~65535),
--        longtext(가변길이, 1 ~ 42억)
-- 바이너리 : BLOB(1 ~ 42억)
-- 날짜 : DATE(날짜), datetime(날짜와 시간)

-- 테이블 만들기
-- create table 테이블명(
--     컬럼명 자료형,
--     컬럼명 자료형, 
--     ....
-- )


create table student_info_table(
stu_idx int,
stu_name char(10),
stu_age int,
stu_addr varchar(100)
);

create table student_point_table(
point_idx int,
point_grade int,
point_kor int
);

-- 서브쿼리를 이용한 테이블 생성
-- select문을 수행해서 얻은 결과로 새로운 테이블을 만들 수 있으며
-- 이 때, 데이터까지도 복사가된다.

use employees;

-- 현재 사원들이 받고 있는 급여액을 가지고 있는 current_salary1이라는 테이블을 생성한다.
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

select * from employees2;


-- 사원의 사원번호, 이름, 근무부서이름, 현재 받고 있는 급여 정보를 가지고 있는
-- 테이블을 만든다.

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