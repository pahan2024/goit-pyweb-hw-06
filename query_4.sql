-- Знайти середній бал на потоці (по всій таблиці оцінок)
SELECT ROUND(AVG(grade), 2) as total_avg_grade 
FROM grades;