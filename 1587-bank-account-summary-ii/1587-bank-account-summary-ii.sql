# Write your MySQL query statement below
select u.name NAME, sum(t.amount) BALANCE
from Users u
left join Transactions t on u.account = t.account
group by t.account
having BALANCE > 10000