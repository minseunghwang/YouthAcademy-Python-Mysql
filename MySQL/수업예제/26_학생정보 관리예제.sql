-- 학생정보 관리예제
create database python_db1;

use python_db1;

create table student_table(
	student_name char(10) not null,
    student_age int not null,
    student_kor int not null
);

select * from student_table;