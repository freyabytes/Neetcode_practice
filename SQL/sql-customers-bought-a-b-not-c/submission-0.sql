-- Write your query below
SELECT * FROM 
customers c
WHERE c.customer_id IN(SELECT o.customer_id FROM orders o WHERE product_name='A')
AND c.customer_id IN (SELECT o.customer_id FROM orders o WHERE product_name='B' )
AND c.customer_id NOT IN (SELECT customer_id FROM orders o WHERE product_name='C')
ORDER BY c.customer_name
