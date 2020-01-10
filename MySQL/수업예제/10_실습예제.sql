-- d001, d003, d007 부서의 이름을 대문자로 변환하여 가져온다.
select upper(dept_name) as '대문자 변환'
from departments
where dept_no IN('d001','d003','d007');

-- Production 부서의 부서 번호중 마지막 자리 값을 가져온다.
select right(dept_no,1) as '마지막 자리값'
from departments
where dept_name = 'Production';

-- 각 부서의 현재 매니저의 부서번호, 사원번호, 시작날짜를 가져온다.
select dept_no'부서번호' , emp_no'사원번호' , from_date'시작날짜'
from dept_emp
where to_date = '9999-01-01';

-- 1960년 이후에 태어난 사원의 사원번호, 생년월일, 이름을 가져온다.
select emp_no'사원번호', birth_date'생년월일', first_name'이름'
from employees
where birth_date >= '1960-01-01' order by birth_date asc;

-- 1990년 이후에 고용된 사원들 중 남자 사원의 정보를 다음과 같은 양식으로 가져온다.
-- "(emp_no)번 사원의 이름은 (last_name) (first_name) 입니다"
select concat(emp_no, '번 사원의 이름은', last_name, ' ', first_name, '입니다.') as '짠!'
from employees
where hire_date >= '1990-01-01' and gender = 'M';

-- 직함에 Senior가 있는 사원들의 사원번호, 직함 정보를 가져온다
select emp_no '사원번호', title '직함정보'
from titles
where title LIKE '%Senior%';