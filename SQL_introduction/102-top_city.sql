-- script that displays the average temperature (Fahrenheit)
-- only july and august temperatures considered
-- by city ordered by temperature (descending)
-- top three cities only to be displayed
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
