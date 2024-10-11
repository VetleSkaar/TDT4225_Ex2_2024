WITH InvalidTrackPoints AS (
    SELECT 
        t1.activity_id,
        a.user_id,
        COUNT(*) AS invalid_count
    FROM TrackPoint t1
    JOIN TrackPoint t2 ON t1.activity_id = t2.activity_id
    JOIN Activity a ON t1.activity_id = a.activity_id
    WHERE 
        t1.trackpoint_id < t2.trackpoint_id
        AND TIMESTAMPDIFF(MINUTE, t1.date_time, t2.date_time) >= 5
    GROUP BY t1.activity_id, a.user_id
)

SELECT user_id, SUM(invalid_count) AS total_invalid_activities
FROM InvalidTrackPoints
GROUP BY user_id
ORDER BY total_invalid_activities DESC;