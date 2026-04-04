-- Write your query below
Select name 
from sales_person
where sales_id NOT IN(
    Select sales_id
    from orders
    Inner join company 
    ON company.com_id = orders.com_id
    where sales_person.sales_id = orders.sales_id and company.name = 'CRIMSON'
);