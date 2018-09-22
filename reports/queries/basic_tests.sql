# CHECK ALL FILES
SELECT * FROM tdwpdb.daily;

SELECT * FROM tdwpdb.merch;

SELECT * FROM tdwpdb.tours;

SELECT * FROM tdwpdb.sales;

SELECT * FROM tdwpdb.presales;

SELECT * FROM tdwpdb.reports;

# MISC TESTS
SELECT * 
FROM tdwpdb.sales
WHERE tour_name = 'nsnm'; 

SELECT region, name, sum(value) as total_sold
FROM tdwpdb.daily
WHERE tour_name = 'nsnm'
GROUP BY region, name
HAVING total_sold > 0
ORDER BY region, total_sold DESC;

SELECT * FROM tdwpdb.daily
WHERE Date = '2017-09-29'
AND name = 'nsnm black tee';

SELECT daily.name AS name, tours.name as tour, sum(daily.value) as total_sold
FROM tdwpdb.daily daily
INNER JOIN tdwpdb.tours tours 
ON daily.tour_id = tours.id
WHERE tour = 'NSNM' 
GROUP BY name
HAVING total_sold > 0
ORDER BY total_sold DESC;

SELECT * 
FROM tdwpdb.reports
JOIN tdwpdb.merch 
ON reports.merch_id = merch.id;
