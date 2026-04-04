-- Write your query below
select name, COALESCE(sum(rides.distance),0) as travelled_distance
from users
Left join rides
on users.id = rides.user_id
group by users.id, users.name
order by travelled_distance DESC, Name ASC;

