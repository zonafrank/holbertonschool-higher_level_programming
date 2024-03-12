-- list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN (
  SELECT B.genre_id as genre_id
  FROM tv_shows AS A
  JOIN tv_show_genres AS B ON A.id = B.show_id
  WHERE A.title = 'Dexter'
)
ORDER BY name;
