-- 제약조건. 테이블의 컬럼에 저장될 데이터에 대한 제한을 설정
-- 데이터이 무결성을 위해 설정하는 매우 중요한 부분

create database testdb10
character set = utf8mb4
collate = utf8mb4_0900_ai_ci;

use testdb10;

-- not null : null을 허용하지 않는다.
create table test_table1(
	data1 int,
    data2 int not null
);

desc test_table1;

-- 테스트
insert into test_table1 (data1, data2)
values(100,200);

select * from test_table1;

-- null을 허용하는 컬럼에 null을 저장한다.
insert into test_table1(data1, data2)
values(103, null);

insert into test_table1(data2)
values(104);

-- unique 제약조건
-- 중복된 데이터는 저장될 수 없지만 null은 무한대로 허용된다.
create table test_table2(
	data1 int,
    data2 int,
    constraint uq2 unique(data2)
);

insert into test_table2(data1, data2)
values(100, 200);

-- unique를 설정하지 않은 테이블에 중복 데이터를 저장한다.
insert into test_table2(data1, data2)
values(100, 201);

insert into test_table2(data1, data2)
values(200, 201);

select * from test_table2;

-- unique가 설정된 테이블에 중복 데이터를 저장한다.
insert into test_table2(data1, data2)
values(100, 202);

-- null 저장
insert into test_table2(data1, data2)
values(103, null);

insert into test_table2(data1)
values(103);

select * from test_table2;

-- primary key (기본키) : 중복을 허용하지 않으며 null을 허용하지 않는다.
-- primary key 제약조건이 설정된 컬럼은 중복된 값을 가질 수 없다.
-- primary key 컬럼은 테이블 내의 모든 로우들을 각각 구분하기 위한 용도로 사용한다.

create table test_table3(
	data1 int,
    data2 int,
    constraint tset_table3_data2_pk primary key(data2)
);

insert into test_table3(data1, data2)
values(100, 200);

insert into test_table3(data1, data2)
values(100, 200);

insert into test_table3(data1) values (100);

-- 복합 키 : 테이블은 하나의 primary key만 가질 수 있다.
-- 복합 키는 여러 컬럼을 묶어 하나의 primary key로 만든것을 의미한다.

create table test_table4(
	data1 int,
    data2 int,
    constraint pk1 primary key(data2)
);

insert into test_table4(data1, data2)
values(null,200);

insert into test_table4(data1, data2)
values(101, null);

select * from test_table4;

insert into test_table4(data1, data2)
values(100, 200);

insert into test_table4(data1, data2)
values(101, 201);

insert into test_table4(data1, data2)
values(101, 200);

insert into test_table4(data1, data2)
values(101, 200);

select * from test_table4;

-- 외래키 : 다른 PK 컬럼을 참조하는 제약조건. 참조하는 PK컬럼에 저장되어 있는 값만 저장이 가능하며, null은 무제한 허용된다.
create table test_table5(
	data1 int,
    data2 int,
    constraint pk primary key(data1)
);

insert into test_table5 values(100,200);
insert into test_table5 values(101,201);
insert into test_table5 values(102,202);

select * from test_table5;

create table test_table6(
	data100 int,
    data200 int,
    constraint fk foreign key (data100) references test_table5(data1)
);

-- pk 컬럼에 존재하는 값 저장
insert into test_table6(data100, data200)
values(100, 200);

insert into test_table6(data100, data200)
values(101, 201);

select * from test_table6;

-- pk 컬럼에 존재하지 않는 값 저장
insert into test_table6(data100, data200)
values(500, 200);

-- check 제약조건 : 컬럼에 저장되는 값을 지정하는 제약조건 (값의 범위)
-- MySQL 최신 버전에만 적용된다.
create table test_table7(
	data1 int,
    data2 int,
    constraint chk1 check(data1 > 10),
    constraint chk2 check(data2 in(10, 20, 30))
);

insert into test_table7(data1, data2)
values(100,20);

select * from test_table7;

-- 위배되는 값
insert into test_table7(data1, data2)
values(5,10);

insert into test_table7(data1, data2)
values(100,50);