SELECT * 
FROM tdwpdb.sales
WHERE tour_name = 'nsnm'; 

SELECT region, name, sum(value) as total_sold
FROM tdwpdb.daily
WHERE tour_name = 'nsnm'
GROUP BY region, name
HAVING total_sold > 0
ORDER BY region, total_sold DESC;