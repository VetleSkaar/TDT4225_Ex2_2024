WITH ActivityCounts AS (
    SELECT YEAR(start_date_time) AS activity_year,
           COUNT(*) AS activity_count,
           SUM(TIMESTAMPDIFF(HOUR, start_date_time, end_date_time)) AS total_hours
    FROM Activity
    GROUP BY activity_year
)

SELECT activity_year,
       activity_count,
       total_hours,
       RANK() OVER (ORDER BY activity_count DESC) AS activity_rank,
       RANK() OVER (ORDER BY total_hours DESC) AS hours_rank
FROM ActivityCounts
WHERE activity_rank = 1 OR hours_rank = 1;