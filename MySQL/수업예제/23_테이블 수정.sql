-- 테이블 변경 테스트를 하기 위한 테이블을 생성한다.
use employees;

drop table emp100;

create table emp100
as
select * from employees;

select * from emp100;

-- 테이블의 이름 변경
-- rename table 테이블명 to 새로운 이름
rename table emp100 to emp1000;

select * from emp1000;

-- 컬럼의 타입을 변경한다.
-- 사이즈를 늘리는 작업을 할때만 사용하기를 권장 (컬럼의 타입을 변경할경우 테이블에 들어있는 데이터들이 깨지거나 유실될경우 있음 (문자열컬럼을 정수형으로 바꾸거나 이럴때))
desc emp1000;

alter table emp1000 modify emp_no int(20);		-- 기존에 emp_no의 data type이 int(11) 이었는데 int(20)으로 변경됨!

-- 컬럼의 이름 변경(타입이나 크기 변경도 동시에 가능하다)
-- alter table 테이블명 changer 컬럼명 새로운컬럼명 타입
alter table emp1000 change gender 성별 enum('M', 'F');		-- change 를쓰면 컬럼명 부터해서 타입, 크기도 변경할수있군(다른건 변경하기 싫으면 기존의 형태 그대로 작성해주면 됨)

desc emp1000;

-- 컬럼 추가
-- alter table 테이블명 add 컬럼명 타입
alter table emp1000 add dept_no char(4);

desc emp1000;

-- 컬럼 삭제
-- alter table 테이블명 drop 컬럼명
alter table emp1000 drop dept_no;

desc emp1000;