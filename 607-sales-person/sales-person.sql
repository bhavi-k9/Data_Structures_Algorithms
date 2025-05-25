
# Write your MySQL query statement below
with cte as
(select a.sales_id , a.name , b.com_id 
from  SalesPerson a left join Orders b ON a.sales_id  = b.sales_id ) 

select distinct name from cte 
where sales_id  not in 
    (SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED')