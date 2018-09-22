SELECT name, t_color, SUM("Gross Rev") AS revenue, SUM("Percent Tour") AS percent
FROM tdwpdb.reports
WHERE tour_name = 'nsnm'
GROUP BY name
ORDER BY revenue DESC;