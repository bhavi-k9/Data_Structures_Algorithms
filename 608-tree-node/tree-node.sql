# Write your MySQL query statement below
/*
if null root
if parent no child leaf
if parent and child inner
*/
with cte as
(
select *,
case 
    when p_id is null then 'Root'
    when id in (select distinct p_id from Tree) then 'Inner'
    else 'Leaf'
end as type
from Tree)    

select id,type from cte