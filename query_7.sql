SELECT sub.name, gr.name, s.fullname, g.grade, g.date_of
FROM grades g
LEFT JOIN students s ON s.id = g.students_id
LEFT JOIN subjects sub ON sub.id = g.subjects_id
LEFT JOIN [groups] gr ON gr.id = s.group_id
WHERE sub.id = 4 AND gr.id = 2;