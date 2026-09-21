-- Знайти список курсів, які відвідує студент (наприклад, ID = 5)
SELECT DISTINCT sb.name
FROM subjects sb
JOIN grades g ON sb.id = g.subject_id
WHERE g.student_id = 5;