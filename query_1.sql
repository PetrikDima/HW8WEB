SELECT s.fullname, round(avg(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.students_id
GROUP BY s.fullname, s.id
ORDER BY avg_grade DESC
LIMIT 5;