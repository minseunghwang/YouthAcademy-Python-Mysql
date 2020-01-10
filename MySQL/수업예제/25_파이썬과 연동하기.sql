-- 파이썬과 연동 테스트
create database python_db1;

use python_db1;

create table python_table1(
	data1 int,
    data2 varchar(100)
);

select * from python_table1;