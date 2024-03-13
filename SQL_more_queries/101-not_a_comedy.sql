-- lists all shows without the genre Comedy in the database
SELECT title
FROM tv_shows
WHERE title NOT IN (
  SELECT A.title AS title
  FROM tv_shows  AS A
  LEFT JOIN tv_show_genres AS B ON A.id = B.show_id
  LEFT JOIN tv_genres AS C ON B.genre_id = C.id
  WHERE C.name = 'Comedy'
)
ORDER BY title;
