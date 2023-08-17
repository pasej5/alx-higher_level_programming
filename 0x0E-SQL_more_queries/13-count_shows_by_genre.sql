-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- USE hbtn_0d_tvshows;
-- Second column must be called number_of_show

SELECT genres.genre AS genre, COUNT(tv_show_genres.id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.genre
ORDER BY number_of_shows DESC;
