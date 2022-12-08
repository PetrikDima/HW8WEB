SELECT DISTINCT s.fullname, t.fullname, round(avg(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.students_id
LEFT JOIN subjects sub ON sub.id = g.subjects_id
LEFT JOIN teachers t ON t.id = sub.teachers_id
WHERE t.id = 1 AND s.id = 3
GROUP BY s.fullname;