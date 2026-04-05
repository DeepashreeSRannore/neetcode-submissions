-- Write your query below
select student_id, exam_id, score
from ( 
    select student_id, exam_id, score,
    rank() over(
        partition by student_id
        order by score DESC, exam_id asc) as rn
    from exam_results
)ranked
where rn = 1
order by student_id;