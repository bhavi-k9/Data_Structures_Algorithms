# Write your MySQL query statement below
with cte as
(select *,
sum(distance) over (partition by user_id ) as total_dis
from Rides)

select distinct b.name,coalesce(a.total_dis,0) as travelled_distance
from cte a right join Users b on a.user_id = b.id
order by total_dis desc ,  name asc
