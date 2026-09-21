-- Середній бал, який певний викладач (наприклад, ID = 1) ставить певному студентові (наприклад, ID = 5)
SELECT ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
JOIN subjects sb ON g.subject_id = sb.id
WHERE g.student_id = 5 AND sb.teacher_id = 1;