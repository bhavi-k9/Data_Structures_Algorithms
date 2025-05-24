# Write your MySQL query statement below
/*
with cte as
(select product_id from Sales
where
sale_date >= '2019-01-01' and sale_date <= '2019-03-31')

select a.product_id,b.product_name from
(select product_id  from cte 
where  
product_id not exists  (select product_id from Sales
where
sale_date > '2019-03-31')) a join Product b
on a.product_id = b.product_id
*/


with cte as (select product_id
            from Sales
            group by product_id
            having min(sale_date) >= '2019-01-01' and max(sale_date)<= '2019-03-31')
            
select p.product_id, p.product_name
from Product p join cte on p.product_id = cte.product_id
where p.product_id in (select product_id from cte)