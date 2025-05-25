# Write your MySQL query statement below
with cte as
(select user_id from
(select * from UserActivity where activity_type = 'paid') a
where
user_id in (select distinct user_id from UserActivity where activity_type =  'free_trial')),

free_trial_data as (
select user_id, 
 round(avg(activity_duration) over(partition by user_id),2)  as trial_avg_duration 
 from (select * from UserActivity where  activity_type = 'free_trial') b
having  user_id in (select * from cte)),

paid_data as
(select user_id, 
 round(avg(activity_duration) over(partition by user_id),2)  as paid_avg_duration 
 from (select * from UserActivity where  activity_type = 'paid') b
having  user_id in (select * from cte))

SELECT 
    distinct f.user_id, 
    f.trial_avg_duration, 
    p.paid_avg_duration
FROM free_trial_data f
JOIN paid_data p ON f.user_id = p.user_id;

 


