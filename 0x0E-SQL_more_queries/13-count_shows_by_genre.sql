-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- USE hbtn_0d_tvshows;
-- Second column must be called number_of_show

SELECT tvg.name AS genre, COUNT(*) AS  number_of_shows
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tg
ON tvg.id = tg.genre_id
GROUP BY tvg.name
ORDER BY number_of_shows DESC;
