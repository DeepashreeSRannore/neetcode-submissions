-- Write your query below
SELECT left_operand, operator, right_operand,
CASE 
WHEN operator = '>' AND v1.value > v2.value THEN 'true'
When operator = '<' And v1.value < v2.value THEN 'true'
WHEN operator = '=' and v1.value = v2.value THEN 'true'
ELSE 'false'
end as value
from expressions
inner join variables v1 on left_operand = v1.name
inner join variables v2 on right_operand = v2.name
order by left_operand, operator, right_operand;
