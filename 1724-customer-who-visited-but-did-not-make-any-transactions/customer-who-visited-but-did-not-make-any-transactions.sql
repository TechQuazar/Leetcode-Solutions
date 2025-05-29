# Write your MySQL query statement below
SELECT CUSTOMER_ID, COUNT(VISIT_ID) AS COUNT_NO_TRANS FROM VISITS WHERE VISIT_ID NOT IN (SELECT VISIT_ID FROM TRANSACTIONS) GROUP BY CUSTOMER_ID;


-- select customer_id , count(visit_id) as count_no_trans from Visits
-- where 
-- visit_id not in (select  visit_id from Transactions)
-- group by customer_id;
