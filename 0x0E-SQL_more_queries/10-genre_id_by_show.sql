-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linke
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT t.title, tg.genre_id
FROM tv_shows AS `t`
 INNER JOIN tv_show_genres AS `tg`
	ON t.id = tg.show_id
ORDER BY t.title, tg.genre_id;
