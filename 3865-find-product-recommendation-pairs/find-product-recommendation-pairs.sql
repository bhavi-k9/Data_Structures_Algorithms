# Write your MySQL query statement below
with cte as
(select a.user_id,
a.product_id as product1_id,
b.product_id as product2_id 
from ProductPurchases a  join ProductPurchases b
on a.user_id = b.user_id
where a.product_id < b.product_id),

cte2 AS (
  SELECT product1_id, product2_id, COUNT(DISTINCT user_id) AS ct
  FROM cte
  GROUP BY product1_id, product2_id
  HAVING COUNT(DISTINCT user_id) >= 3
)

/*
cte2 as
(select distinct product1_id,product2_id,ct from
(select *,
count(user_id) over (partition by product1_id,product2_id) as ct
from cte) a
where ct >= 3
order by 
ct desc,
product1_id asc,
product2_id asc
)
*/


select product1_id,product2_id,
b.category as product1_category,
c.category as product2_category ,
ct as customer_count 
from cte2 a
join ProductInfo b on a.product1_id = b.product_id
join ProductInfo c on a.product2_id = c.product_id
ORDER BY a.ct DESC, a.product1_id ASC, a.product2_id ASC;


