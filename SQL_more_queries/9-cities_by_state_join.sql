-- Retrieve rows from the cities and states tables
SELECT c.id, c.name AS city_name, s.name AS state_name
FROM cities c
JOIN states s ON c.state_id = s.id
ORDER BY c.id;
