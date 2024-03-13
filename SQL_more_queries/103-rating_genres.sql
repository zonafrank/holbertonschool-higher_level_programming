-- lists all genres in the database rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
SELECT D.name AS name, SUM(B.rate) AS rating
FROM tv_shows AS A
JOIN tv_show_ratings AS B ON A.id = B.show_id
JOIN tv_show_genres AS C ON A.id = C.show_id
JOIN tv_genres D ON C.genre_id = D.id
GROUP BY name
ORDER BY rating DESC;