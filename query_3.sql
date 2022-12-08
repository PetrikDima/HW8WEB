SELECT gr.name, sub.name,round(avg(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN subjects sub ON sub.id = g.subjects_id
LEFT JOIN [groups] gr ON sub.id = gr.id
GROUP BY gr.name
ORDER BY avg_grade DESC;