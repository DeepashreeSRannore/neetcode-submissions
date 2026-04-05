-- Write your query below
select student_id, exam_id , score
from (
    select student_id,exam_id, score,
    rank() over ( 
        partition by student_id
        order by score desc, exam_id asc
    )as r
    from exam_results
) ranked
where r = 1
order by student_id;
