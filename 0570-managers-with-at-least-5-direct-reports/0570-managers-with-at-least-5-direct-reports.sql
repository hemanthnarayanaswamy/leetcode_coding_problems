# Write your MySQL query statement below
select emp1.name
from Employee emp1
join employee emp2 on emp1.id = emp2.managerId
group by emp1.id
having count(*) >= 5