SELECT t.fullname, s.name
FROM subjects s
LEFT JOIN teachers t ON t.id = s.teachers_id;