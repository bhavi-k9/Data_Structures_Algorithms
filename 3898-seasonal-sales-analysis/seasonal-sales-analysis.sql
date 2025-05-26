# Write your MySQL query statement below

with cte as
(select a.sale_id ,a.product_id,a.sale_date,a.quantity,a.price,b.product_name, b.category,      
Case 
    when month(sale_date)  in (12,1,2) then 'Winter'
    when month(sale_date)  in (3,4,5) then 'Spring'
    when month(sale_date)  in (6,7,8) then 'Summer'
    when month(sale_date)  in (9,10,11) then 'Fall'
    end as  season  
from sales a join  products b on a.product_id  = b.product_id ),
cte2 as
(select season, category, total_quantity, total_revenue from
(select *,
sum(quantity) over (partition by category,season) as total_quantity,
sum(quantity* price) over (partition by category,season) as total_revenue 
from cte) a)

select  distinct season,category,total_quantity,total_revenue from
(select *, 
rank() over (partition by season  order by total_quantity desc,total_revenue desc ) as rk
from cte2) b
where rk = 1

