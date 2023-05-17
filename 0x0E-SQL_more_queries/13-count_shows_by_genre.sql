-- List shows without a genre linked
SELECT g.genre AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg ON g.id = sg.genre_id
GROUP BY g.genre
ORDER BY number_of_shows DESC;
