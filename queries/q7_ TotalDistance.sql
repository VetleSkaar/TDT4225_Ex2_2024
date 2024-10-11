SELECT SUM(distance) AS total_distance_km
FROM (
    SELECT t.activity_id, 
           SUM(SQRT(POW(t.lat, 2) + POW(t.lon, 2))) AS distance
    FROM TrackPoint t
    JOIN Activity a ON t.activity_id = a.activity_id
    WHERE a.user_id = '112' 
      AND YEAR(a.start_date_time) = 2008
    GROUP BY t.activity_id
) AS activity_distances;