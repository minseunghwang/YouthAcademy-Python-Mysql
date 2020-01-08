-- 현재 날짜와 시간
select now(), sysdate(), curdate(), curtime(), current_date(),
		current_time(), current_timestamp();
        
-- 날짜 연산
-- select sysdate(), sysdate() + 1000

select now(), date_add(sysdate(), interval 1000 day);	-- 1000일 더하기
select now(), date_sub(sysdate(), interval 1000 day);	-- 1000일 빼기
select now(), date_sub(sysdate(), interval 1000 year);	-- 1000년 빼기

-- 현재 사원들의 고용일로부터 100일 되는 날을 가져온다.
select hire_date, date_add(hire_date, interval 100 day)
from employees;

-- 각 날짜 단위 값을 가져온다.	- 잘 안써요
select year(hire_date), month(hire_date), monthname(hire_date),
		dayname(hire_date), dayofweek(hire_date), weekday(hire_date),
		dayofyear(hire_date), week(hire_date)
from employees;

-- 날짜 양식
-- 날짜 데이터를 문자열로 변환해서 가져온다.
-- https://lightblog.tistory.com/155 (참고)
select date_format(hire_date, '%Y년 %m월 %d일 %H시 %i분 %s초')
from employees;
-- 오라클은 양식에 한글들어가면 에러발생