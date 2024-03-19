-- Retrieve all cities in California from the hbtn_0d_usa database
SELECT c.id, c.name
FROM cities c
JOIN states s ON c.state_id = s.id
WHERE s.name = 'California'
ORDER BY c.id;
