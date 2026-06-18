# Write your MySQL query statement below
select p1.email Email
from Person p1
join Person p2 on p1.email = p2.email and p1.id != p2.id
group by p1.email