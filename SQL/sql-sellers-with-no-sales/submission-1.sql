SELECT seller_name
FROM seller as s
WHERE seller_id NOT IN (
    SELECT  seller_id
    FROM orders as o
    WHERE EXTRACT(YEAR FROM sale_date) = 2020)
 ORDER BY seller_name;