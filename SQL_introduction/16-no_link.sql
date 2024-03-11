-- script that lists all records of the table second_table
-- Does not list rows without a name value
-- Results displays score and the name (in that order)
-- Records are listed by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;