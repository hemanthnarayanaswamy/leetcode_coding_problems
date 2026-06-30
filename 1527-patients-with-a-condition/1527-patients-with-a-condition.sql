# Write your MySQL query statement below
select * 
from Patients 
where conditions  REGEXP '(^|[[:space:]])DIAB1';