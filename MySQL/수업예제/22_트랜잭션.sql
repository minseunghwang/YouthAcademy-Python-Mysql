-- 트랜잭션
-- insert, update, delete 문들이 물리적인 디스크에 반영되기 전까지 작업을 관리하는 단위

-- 접속을 하거나 물리적인 디스크에 반영이 되면 새로운 트랜잭션이 발생하고 물리적인 디스크에 반영이 되면 종료되고 새로운 트랜잭션이 발생한다.

-- 디스크에 반영되는 시점(트랜잭션이 종료되는 시점)
-- 현재 데이터베이스에 접속되어 있는 접속이 종료되면...
-- commit 명령어를 수행했을 경우

-- Auto commit 설정 상태를 확인한다.
-- 1 : auto commit on, 0 :auto commit off

select @@autocommit;

-- auto commit을 비활성화 한다.
set autocommit = 0;
select @@autocommit;

-- 테스트를 위한 테이블을 생성한다
drop table emp100;

create table emp100
as
select * from employees;

-- 데이터 변경
insert into emp100(emp_no, birth_date, first_name, last_name, gender, hire_date)
values(500000, sysdate(), '길동', '홍', 'M' , sysdate());

insert into emp100(emp_no, birth_date, first_name, last_name, gender, hire_date)
values(500001, sysdate(), '나', '사', 'F' ,sysdate());

insert into emp100(emp_no, birth_date, first_name, last_name, gender, hire_date)
values(500002, sysdate(), '은우', '차', 'M' ,sysdate());

select * from emp100 order by emp_no desc;

-- 디스크에 반영한다.
commit;

delete from emp100 where emp_no >= 500000;

select * from emp100 order by emp_no desc;

-- commit 전에는 rollback이 가능하다.
rollback;