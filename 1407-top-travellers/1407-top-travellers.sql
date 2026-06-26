# Write your MySQL query statement below
select u.name, SUM(COALESCE(r.distance, 0)) as travelled_distance
from Users u
left join Rides r on u.id = r.user_id
group by u.id
order by travelled_distance DESC, u.name ASC
