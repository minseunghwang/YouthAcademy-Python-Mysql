-- JOIN : 두 개 이상의 테이블을 가져와 하나의 결과로 합쳐서 가져오는 개념

-- CROSS JOIN : join 하고자 하는 테이블을 다대다 의 관계로 합치는 JOIN
-- 사원들의 사원번호, 근무부서 번호, 근무부서 이름을 가져온다.
-- 가져올 데이터 : 사원번호, 부서번호, 부서이름
-- 조건 : 현재
-- 정렬 : 사원 번호(오름차순)

-- CROSS JOIN은 두개 이상의 테이블 모두 합치는 과정을 하기 때문에 올바르게 짝지어지지 않은 데이터 묶음이 존재할 수 있다.
select a1.emp_no, a2.dept_name, a1.dept_no
from dept_emp as a1 CROSS JOIN departments as a2;		-- 국제표준

select a1.emp_no, a2.dept_name, a1.dept_no, a2.dept_no
from dept_emp a1, departments a2;						-- 이거도댐

-- INNER JOIN
-- CROSS JOIN 된 결과에서 제대로 짝지어진 로우만을 가져올 수 있는 JOIN

-- 사원들의 사원번호, 근무부서번호, 근무부서이름을 가져온다.(현재)
-- 사원번호를 기준으로 오름차순 정렬
-- 가져올 데이터 : 사원번호, 부서번호, 부서이름
-- 조건 : 현재
-- 정렬 : 사원 번호(오름차순)

select a1.emp_no, a1.dept_no, a2.dept_name
from dept_emp a1 inner join departments a2
on a1.dept_no = a2.dept_no
where a1.to_date = '9999-01-01'
order by a1.emp_no asc;

select a1.emp_no, a1.dept_no, a2.dept_name
from dept_emp a1, departments a2		-- ,로 하는 join은 cross join
where a1.dept_no = a2 .dept_no and a1.to_date = '9999-01-01'
order by a1.emp_no asc;

-- 각 사원들의 사원번호, first_name, 현재 근무하고 있는 부서의 번호를 가져온다.
select a.emp_no '사원번호' , b.first_name, a.dept_no '부서번호'
from dept_emp a inner join employees b
on a.emp_no = b.emp_no
where a.to_date = '9999-01-01';
 
-- 각 사원들의 사원번호, first_name, 현재 받고있는 급여를 가져온다.
select a.emp_no '사원번호', a.first_name, s.salary '현재급여'
from employees a inner join salaries s
on a.emp_no = s.emp_no
where s.to_date = '9999-01-01';

-- 각 사원들의 사원번호, first_name, 근무 부서 이름을 가져온다.(3개 테이블 join)
select a.emp_no '사원번호', a.first_name, d.dept_name '근무부서이름'
from (select e.emp_no, e.first_name, de.dept_no
from employees e inner join dept_emp de
on e.emp_no = de.emp_no
where de.to_date = '9999-01-01') a inner join departments d
on a.dept_no = d.dept_no;

-- 위 아래 같은거
select a1.emp_no, a1.first_name, a3.dept_name
from employees a1
	inner join dept_emp a2
    on a1.emp_no = a2.emp_no
		inner join departments a3
        on a2.dept_no = a3.dept_no
where a2.to_date='9999-01-01';        

-- 이거도 같은거 (오호... 씸플하구만...)
select a1.emp_no, a1.first_name, a3.dept_name
from employees a1, dept_emp a2, departments a3
where a1.emp_no = a2.emp_no and a2.dept_no = a3.dept_no and a2.to_date='9999-01-01';
