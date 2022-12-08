SELECT sub.name, s.fullname
FROM grades g
LEFT JOIN students s ON s.id = g.students_id
LEFT JOIN subjects sub ON sub.id = g.subjects_id
WHERE g.students_id = 1
GROUP BY sub.name;