# Write your MySQL query statement below
(select name as results
from Users u 
left join MovieRating m on u.user_id = m.user_id
group by m.user_id
order by count(m.rating) DESC, name ASC
limit 1)

union all

(select m.title as results
from Movies m
left join MovieRating r on r.movie_id = m.movie_id
where MONTH(r.created_at)=2 and YEAR(r.created_at)=2020
group by r.movie_id
order by AVG(r.rating) DESC, m.title ASC
limit 1)