# Write your MySQL query statement below
select s.student_id, s.student_name, su.subject_name, Count(e.subject_name) as attended_exams
from Students s
CROSS JOIN Subjects su
LEFT JOIN Examinations e ON e.student_id = s.student_id AND e.subject_name = su.subject_name
GROUP BY s.student_id, su.subject_name
ORDER BY s.student_id, su.subject_name

