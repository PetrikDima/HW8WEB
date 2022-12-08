SELECT s.fullname, sub.name,round(avg(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.students_id
LEFT JOIN subjects sub ON sub.id = g.subjects_id
WHERE sub.id = 1
GROUP BY s.fullname, s.id
ORDER BY avg_grade DESC
LIMIT 1;