-- Write a script that displays the top 3 cities' temperatures during July and August ordered by temperature (descending)

SELECT city, AVG(temp) AS avg_temp
FROM Temperatures
WHERE (MONTH(date) = 7 OR MONTH(date) = 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
