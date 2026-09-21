-- Список курсів, які певному студенту (наприклад, ID = 5) читає певний викладач (наприклад, ID = 3)
SELECT DISTINCT sb.name
FROM subjects sb
JOIN grades g ON sb.id = g.subject_id
WHERE g.student_id = 5 AND sb.teacher_id = 3;