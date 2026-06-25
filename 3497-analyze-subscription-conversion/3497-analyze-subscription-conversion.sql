# Write your MySQL query statement below
select free.user_id, ROUND(AVG(free.activity_duration),2) trial_avg_duration, paid.paid_avg_duration
from UserActivity free
right join (
    select user_id, ROUND(AVG(activity_duration), 2) paid_avg_duration
    from UserActivity
    where activity_type = 'paid'
    group by user_id) paid on free.user_id = paid.user_id
where free.activity_type = 'free_trial'
group by free.user_id