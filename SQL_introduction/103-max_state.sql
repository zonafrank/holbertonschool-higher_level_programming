-- script that displays the maximum temperature (Fahrenheit) by state
-- ordered by state name (ascending)
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
