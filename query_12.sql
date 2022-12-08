SELECT t.fullname, round(avg(g.grade), 2) AS avg_grade
FROM grades g
JOIN subjects sub ON sub.id = g.subjects_id
LEFT JOIN teachers t ON t.id = sub.teachers_id
WHERE t.id = 2
GROUP BY t.fullname