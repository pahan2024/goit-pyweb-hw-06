-- Оцінки студентів у певній групі (ID = 1) з певного предмета (ID = 2) на останньому занятті
SELECT s.name, g.grade, g.date_received
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = 1 
  AND g.subject_id = 2
  AND g.date_received = (
      -- Знаходимо дату ОСТАННЬОГО заняття саме для цієї групи (ID = 1) і цього предмета (ID = 2)
      SELECT MAX(g2.date_received) 
      FROM grades g2
      JOIN students s2 ON s2.id = g2.student_id
      WHERE g2.subject_id = 2 AND s2.group_id = 1
  );
