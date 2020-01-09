-- insert : 로우(가로)를 추가하는 명령문
-- insert into 테이블명 [(컬럼1, 컬럼2, 컬럼3)] values(값1, 값2, 값3...)

use testdb1;

create table test_table100(
int_data int,
str_data varchar(100),
number_data int
);

insert into test_table100 (int_data, str_data, number_data)
values(1, '문자열1', 10);

select * from test_table100;

insert into test_table100 (str_data, number_data, int_data)
values('문자열2',20, 2);

select * from test_table100;

-- 컬럼명 생략 : 테이블을 만들 때 작성한 컬럼의 순서대로 매칭된다.
insert into test_table100 values (3, '문자열3', 30);

select * from test_table100;

-- 명시된 컬럼명(생략시)과 값의 개수가 다를 경우			-- 입력된 값이 없으면 NULL이 들어감
insert into test_table100 (int_data, str_data)
values(5, '문자열5');

-- 타입이 다른경우									-- 에러
insert into test_table100 (int_data, str_data, number_data)
values('문자열100', '문자열200', '문자열300');

-- 데이터를 저장할 때 컬럼의 타입을 보고 그 타입으로 변환해서 저장한다.
-- 이 때 변환이 불가능한 데이터라고 한다면 오류가 발생한다.
insert into test_table100(int_data, str_data, number_data)			-- 그래서 이건 됌
values('100',200,'300');

select * from test_table100;

-- null : 값은 값이지만 의미가 없는 값, 무한대를 의미하는 값.					-- 무한대용.. ? ㅇㅅaㅇ
insert into test_table100(int_data, str_data, number_data)
values(4, null, null);

select * from test_table100;

-- 저장할 때 생략한 컬럼은 null이 저장된다.
insert into test_table100(int_data, str_data)
values(5,'문자열5');

select * from test_table100;

-- 서브쿼리를 통한 데이터 insert
create table test_table200
as
select * from test_table100 where 1=0;

select * from test_table200;

-- select 문을 통해 가져온 결과를 테이블에 저장한다.

insert into test_table200 (int_data, str_data, number_data)
select int_data, str_data, number_data
from test_table100;
 
select * from test_table200;

-- select해서 가져온 결과의 순서와 저장될 테이블의 컬럼순서와 일치한다면 컬러명을 생략해도 된다.
-- select 한 컬러명의 순서는 일치해야 하는군
insert into test_table200
select number_data, str_data, int_data
from test_table100;

select * from test_table200;

delete from test_table200;		-- 안의 내용만 지우는군!
drop table test_table200;		-- 테이블 자체를 지우는군!