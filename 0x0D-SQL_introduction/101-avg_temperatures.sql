-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, AVG(temp) AS avg_temp
FROM Temperatures
GROUP BY city
ORDER BY avg_temp DESC;

