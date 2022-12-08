SELECT  gr.name, s.fullname
FROM students s
LEFT JOIN [groups] gr ON s.group_id  = gr.id
ORDER BY gr.id;