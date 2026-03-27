# Write your MySQL query statement below
select a.employee_id
from Employees a
where a.salary < 30000 and a.manager_id not in (select employee_id from Employees)
order by a.employee_id