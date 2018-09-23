SELECT reports.name AS design_name, reports.t_color, 
CEIL(SUM(reports.gross_revenue)) AS revenue, 
CEIL(SUM(reports.percent_tour)) AS percent,
tours.name AS tour_name, tours.year

FROM tdwpdb.reports
JOIN tdwpdb.tours 
ON reports.tour_id = tours.id

WHERE tour_name = 'NSNM'
GROUP BY design_name
ORDER BY revenue DESC;
