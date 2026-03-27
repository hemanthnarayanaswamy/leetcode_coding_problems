# Write your MySQL query statement below
select a.name as Employee
from Employee a, Employee b
WHERE a.managerID = b.id and a.salary > b.salary
