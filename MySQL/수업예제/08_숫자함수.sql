


select abs(100), abs(-100);

-- 소수점 이하 올림
select ceil(10.1), ceil(10.4), ceil(10.5), ceil(10.8);

-- 소수점 이하 버림
select floor(10.1), floor(10.4), floor(10.5), floor(10.8);

-- 반올림
select round(10.1), round(10.4), round(10.5), round(10.5);

-- round(숫자, 자릿수) : 0 - 소수점 이하 첫번째 자리
-- 					 : 양수 - 소수점 이하자리(1 : 2번째, 2 : 3번째, 3 : 4번째...)
-- 					 : 음수 - 정수 자리(-1 : 정수 1번째, -2 : 정수 2번째...)
select round(166.555,0), round(166.555,1), round(166.555,2), round(166.555,-1), round(166.555,-2);

-- 버림(자리수 설정, 자리수 설정은 반올림과 동일하다.)
select truncate(166.555, 0), truncate(166.555, 1), truncate(166.555, -1);

-- x의 y승
select pow(10,2);

-- 나머지 구하기
select mod(10,3);

-- 최대 최소
select greatest(10, 4, 20, 1);

select least(10, 4, 20, 1);

-- 사원들의 사원 번호와 급여를 가져온다. 급여는 10% 인상된 급여를 가져온다.
-- 소수점 이하는 올린값, 버린값, 반올림한 값을 모두 가져온다.
select emp_no, ceil(salary * 1.1) '올림', round(salary * 1.1) '반올림', floor(salary * 1.1) '버림'
from salaries;

-- 연봉의 최대, 최소값을 가져온다.
-- 오류. 특정 컬럼안에 저장되어 있는 값 중 최대, 최소값을 구하기 위해서는 그룹 함수를 사용한다.
select greatest(salary), least(salary)
from salaries;