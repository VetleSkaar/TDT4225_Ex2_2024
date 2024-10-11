WITH TransportationCounts AS (
    SELECT 
        a.user_id,
        a.transportation_mode,
        COUNT(*) AS mode_count
    FROM Activity a
    WHERE a.transportation_mode IS NOT NULL
    GROUP BY a.user_id, a.transportation_mode
),

RankedTransportation AS (
    SELECT 
        user_id,
        transportation_mode,
        mode_count,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY mode_count DESC) AS mode_rank
    FROM TransportationCounts
)

SELECT 
    user_id,
    transportation_mode AS most_used_transportation_mode
FROM RankedTransportation
WHERE mode_rank = 1
ORDER BY user_id;
