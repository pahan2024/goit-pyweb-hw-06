-- Знайти оцінки студентів у окремій групі з певного предмета (наприклад, група ID = 1, предмет ID = 2)
SELECT s.name, g.grade, g.date_received
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = 1 AND g.subject_id = 2;