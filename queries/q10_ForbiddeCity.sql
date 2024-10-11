SELECT DISTINCT a.user_id
FROM Activity a
JOIN TrackPoint t ON a.activity_id = t.activity_id
WHERE 
    t.lat BETWEEN 39.915 AND 39.917
    AND t.lon BETWEEN 116.396 AND 116.398;
