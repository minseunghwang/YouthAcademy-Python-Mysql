-- 데이터 베이스 만들기
-- create database 데이터베이스이름

create database testdb1;

create database testdb2
character set = utf8mb4
collate = utf8mb4_0900_ai_ci;

create database testdb3
character set = utf8
collate = utf8_general_ci;

-- 데이터베이스 제거
-- 데이터베이스 제거시 개발자는 복원이 불가
-- drop database 데이터베이스이름

drop database testdb1;
drop database testdb2;
drop database testdb3;