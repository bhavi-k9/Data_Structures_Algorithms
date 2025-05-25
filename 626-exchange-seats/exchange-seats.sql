# Write your MySQL query statement below
with cte as
(select * ,
case when
    id % 2 = '0' then lag(student,1) over()
    else lead(student,1) over()
    end as swap_name
from Seat)

select id,
case when
    swap_name is not null then swap_name
    else student
    end as student
from cte

