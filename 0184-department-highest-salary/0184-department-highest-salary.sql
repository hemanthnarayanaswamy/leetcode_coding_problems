# Write your MySQL query statement below
select d.name Department, e.name Employee, e.salary Salary
from Employee e
left join Department d on d.id = e.departmentId
where (e.departmentId, e.salary) in 
    ( 
        select departmentId, MAX(salary) 
        from Employee
        group by departmentId
    )