-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- List shows with associated genres
SELECT CONCAT(tv_shows.title, ' - ', IFNULL(tv_show_genres.genre_id, 'NULL')) AS show_info
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
