# Write your MySQL query statement below
select DATE_FORMAT(trans_date, '%Y-%m') as month, country, Count(id) as trans_count, 
COUNT(CASE WHEN STATE = 'APPROVED' THEN 1 ELSE NULL END) as approved_count,
sum(amount) as trans_total_amount,
SUM(CASE WHEN STATE = 'APPROVED' THEN amount ELSE 0 END) as approved_total_amount
from Transactions
group by DATE_FORMAT(trans_date, '%Y-%m'), country