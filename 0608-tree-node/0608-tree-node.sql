# Write your MySQL query statement below
select t1.id,
case 
when t1.p_id is NULL then 'Root'
when t2.p_id is NULL then 'Leaf'
else 'Inner'
end as type
from Tree t1
left join Tree t2 on t1.id = t2.p_id
group by t1.id