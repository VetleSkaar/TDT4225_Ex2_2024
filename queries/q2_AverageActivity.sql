SELECT AVG(activity_count) AS average_activities_per_user
FROM (
    SELECT user_id, COUNT(*) AS activity_count
    FROM Activity
    GROUP BY user_id
) AS user_activity_counts;