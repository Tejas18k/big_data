SELECT Salary, COUNT(*) AS NumberOfEmployees
FROM Employees
GROUP BY Salary
HAVING COUNT(*) > 1;


SELECT firstname, COUNT(salary) AS NumberOfsal
FROM Employees
GROUP BY firstname
HAVING COUNT(*) > 1;

select * from employees


SELECT salary,COUNT(*) AS HighSalaryEmployees
FROM Employees
WHERE Salary > 70000
group by salary;



SELECT 
    FirstName,
    LastName,
    DepartmentID,
    COUNT(*) OVER (PARTITION BY DepartmentID) AS DepartmentEmployeeCount
FROM 
    Employees;


select count(employeeid) emp
from employees
where managerid is null


SELECT DepartmentID ,count(employeeid)
FROM Employees
group by departmentid

















WITH second_high_sal AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rn
    FROM employees
)
SELECT salary 
FROM second_high_sal 
WHERE rn = 2;




SELECT DISTINCT m.EmployeeID
FROM Employees e
JOIN Employees m ON e.ManagerID = m.EmployeeID;





select e1.employeeid
from employees e 
join employees e1
on e.managerid=e1.employeeid


--  Find Departments with More Than 3 Employees
with findemp as ( select d.departmentid,count(e.employeeid) as ctemp 
from employees e join departments d on e.departmentid=d.departmentid
group by d.departmentid,e.employeeid
having count(e.employeeid)>3
)
select departmentname
from findemp





WITH dept_emp_count AS (
    SELECT departmentid, COUNT(employeeid) AS employee_count
    FROM employees
    GROUP BY departmentid
    HAVING COUNT(employeeid) > 3
)
SELECT d.departmentname
FROM departments d
JOIN dept_emp_count dec ON d.departmentid = dec.departmentid;
------------------------------------------------------------------------------------------------------------------------
WITH dept_emp_count AS (
    SELECT d.departmentid, COUNT(e.employeeid) AS employee_count
    FROM departments d
    JOIN employees e ON d.departmentid = e.departmentid
    GROUP BY d.departmentid
    HAVING COUNT(e.employeeid) > 3
)
SELECT d.departmentname
FROM departments d
JOIN dept_emp_count dec ON d.departmentid = dec.departmentid;


select * from employees

select salary,rn 
from (select salary,dense_rank() over (order by salary desc) as rn from employees ) as x
where rn in (1,2,3,4,5,6);



select cOUNT(salary) from employees group by salary having count(salary)>1 

select salary from employees group by salary having count(*)>1 




select salary from employees group by salary 