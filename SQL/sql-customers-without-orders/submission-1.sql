-- Write your query below
SELECT name
FROM customers
WHERE id IN(
    SELECT id
    FROM customers
    EXCEPT
    SELECT customer_id FROM ORDERS 
);