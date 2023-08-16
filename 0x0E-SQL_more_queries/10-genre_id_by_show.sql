-- list all shows that have at least one genre linked
SELECT ts.title AS title, tsg.genre_id AS genre_id
FROM tv_shows AS ts
RIGHT JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
ORDER BY title, genre_id;
