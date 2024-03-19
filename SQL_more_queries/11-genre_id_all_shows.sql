-- Retrieve all shows from the hbtn_0d_tvshows database
SELECT ts.title, tsg.genre_id
FROM hbtn_0d_tvshows.tv_shows ts
LEFT JOIN hbtn_0d_tvshows.tv_show_genres tsg ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
