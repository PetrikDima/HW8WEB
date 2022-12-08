SELECT s.fullname, t.fullname, sub.name
FROM grades g
LEFT JOIN students s ON s.id = g.students_id
LEFT JOIN subjects sub ON sub.id = g.subjects_id
LEFT JOIN teachers t ON t.id = sub.teachers_id
WHERE t.id = 1 AND g.students_id = 1
GROUP BY sub.name;