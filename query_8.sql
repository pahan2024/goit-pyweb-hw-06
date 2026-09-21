-- Знайти середній бал, який ставить певний викладач зі своїх предметів (наприклад, ID = 1)
SELECT t.name, ROUND(AVG(g.grade), 2) as avg_grade
FROM teachers t
JOIN subjects sb ON t.id = sb.teacher_id
JOIN grades g ON sb.id = g.subject_id
WHERE t.id = 1
GROUP BY t.id;