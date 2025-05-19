# Write your MySQL query statement below

with cte as 
(select *, (out_time - in_time) as time_spent
from Employees)

select  DISTINCT event_day as day,  emp_id,
sum(time_spent)  over (partition by emp_id,event_day) as total_time
from cte