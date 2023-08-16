-- Extract info from combined city and state table
SELECT c.id AS id, c.name AS name, s.name AS name 
FROM states AS s
JOIN cities AS c
ON s.id = c.state_id
