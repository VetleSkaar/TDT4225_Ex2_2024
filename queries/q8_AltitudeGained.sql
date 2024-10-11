SELECT a.user_id, SUM(t.altitude) AS total_meters_gained
FROM TrackPoint t
JOIN Activity a ON t.activity_id = a.activity_id
WHERE t.altitude IS NOT NULL AND t.altitude >= 0
GROUP BY a.user_id
ORDER BY total_meters_gained DESC
LIMIT 20