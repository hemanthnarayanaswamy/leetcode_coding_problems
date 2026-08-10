(select 'Fall' As Season, p.category as category, sum(s.quantity) as total_quantity, sum(quantity*price) as total_revenue
from sales s
join products p on p.product_id = s.product_id
where month(sale_date) in (11, 10, 09)
group by p.category
order by total_quantity DESC, total_revenue DESC, p.category
limit 1)

union all

(select 'Spring' As Season, p.category as category, sum(s.quantity) as total_quantity, sum(quantity*price) as total_revenue
from sales s
join products p on p.product_id = s.product_id
where month(sale_date) in (3, 5, 4)
group by p.category
order by total_quantity DESC, total_revenue DESC, p.category
limit 1)

union all

(select 'Summer' As Season, p.category as category, sum(s.quantity) as total_quantity, sum(quantity*price) as total_revenue
from sales s
join products p on p.product_id = s.product_id
where month(sale_date) in (6, 7, 8)
group by p.category
order by total_quantity DESC, total_revenue DESC, p.category
limit 1)

union all

(select 'Winter' As Season, p.category as category, sum(s.quantity) as total_quantity, sum(quantity*price) as total_revenue
from sales s
join products p on p.product_id = s.product_id
where month(sale_date) in (12, 01, 02)
group by p.category
order by total_quantity DESC, total_revenue DESC, p.category
limit 1)