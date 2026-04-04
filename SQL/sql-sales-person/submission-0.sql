-- Write your query below
Select name 
from sales_person
where NOT EXISTS(
    Select 1
    from orders
    Inner join company 
    ON company.com_id = orders.com_id
    where sales_person.sales_id = orders.sales_id and company.name = 'CRIMSON'
);