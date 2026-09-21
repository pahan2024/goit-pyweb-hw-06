-- Оцінки студентів у певній групі (наприклад, ID = 1) з певного предмета (наприклад, ID = 2) на останньому занятті
SELECT s.name, g.grade, g.date_received
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = 1 
  AND g.subject_id = 2
  AND g.date_received = (
      SELECT MAX(date_received) 
      FROM grades 
      WHERE subject_id = 2
  );