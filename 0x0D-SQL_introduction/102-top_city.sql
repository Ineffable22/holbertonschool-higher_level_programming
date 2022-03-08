-- This script displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY city DESC
LIMIT 3;
