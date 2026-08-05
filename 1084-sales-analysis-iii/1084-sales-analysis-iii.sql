# Write your MySQL query statement below
select distinct(p.product_id), p.product_name
from Sales s
join Product p on s.product_id = p.product_id
where p.product_id not in (
    select product_id
    from Sales
    where sale_date < '2019-01-01' OR sale_date > '2019-03-31'
)
