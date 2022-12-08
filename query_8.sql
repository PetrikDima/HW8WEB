SELECT sub.name, gr.name, s.fullname, g.grade, g.date_of
FROM grades g
LEFT JOIN students s ON s.id = g.students_id
LEFT JOIN subjects sub ON sub.id = g.subjects_id
LEFT JOIN [groups] gr ON gr.id = s.group_id
WHERE sub.id = 3 AND gr.id = 3 AND g.date_of = (SELECT g.date_of
FROM grades g
LEFT JOIN students s ON s.id = g.students_id
LEFT JOIN [groups] gr ON gr.id = s.group_id
WHERE g.subjects_id = 3 AND gr.id = 2
ORDER BY g.date_of DESC
LIMIT 1);