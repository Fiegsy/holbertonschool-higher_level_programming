-- Retrieve all shows from the hbtn_0d_tvshows table that have at least one genre linked
SELECT ts.title, tsg.genre_id
FROM hbtn_0d_tvshows.tv_shows ts
JOIN hbtn_0d_tvshows.tv_show_genres tsg ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
