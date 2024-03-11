-- script that lists the number of records with
-- the same score in the table second_table
-- displays the score
-- displays the number of records for this score with the label `number`
-- is sorted by the number of records (descending)
SELECT score, count(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
