-- Display all the cities of California found in the database 
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California')
ORDER BY cities.id;