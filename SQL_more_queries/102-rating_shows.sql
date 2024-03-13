-- lists all shows with the sum of their rating
SELECT A.title, SUM(B.rate) AS rating
FROM tv_shows AS A
JOIN tv_show_ratings AS B
ON A.id = B.show_id
GROUP BY A.title
ORDER BY rating DESC;
