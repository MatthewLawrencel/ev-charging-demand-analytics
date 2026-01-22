USE ev_charging_dw;
GO

/* =====================================================
   1️⃣ Peak Charging Hours
===================================================== */
CREATE OR ALTER VIEW vw_peak_charging_hours AS
SELECT
    DATEPART(HOUR, start_time) AS hour_of_day,
    COUNT(*)                  AS total_sessions,
    SUM(energy_kwh)           AS total_kwh,
    SUM(cost)                 AS total_revenue,
    AVG(duration_min)         AS avg_duration_min
FROM fact_charging_sessions
GROUP BY DATEPART(HOUR, start_time);
GO


/* =====================================================
   2️⃣ City-wise Demand
===================================================== */
CREATE OR ALTER VIEW vw_city_demand AS
SELECT
    city,
    COUNT(*)          AS total_sessions,
    SUM(energy_kwh)   AS total_kwh,
    SUM(cost)         AS total_revenue,
    AVG(duration_min) AS avg_duration_min
FROM fact_charging_sessions
GROUP BY city;
GO


/* =====================================================
   3️⃣ Daily Demand Trend
===================================================== */
CREATE OR ALTER VIEW vw_daily_demand AS
SELECT
    CAST(start_time AS DATE) AS session_date,
    COUNT(*)                AS total_sessions,
    SUM(energy_kwh)         AS total_kwh,
    SUM(cost)               AS total_revenue,
    AVG(duration_min)       AS avg_duration_min
FROM fact_charging_sessions
GROUP BY CAST(start_time AS DATE);
GO


/* =====================================================
   4️⃣ Station Utilization
===================================================== */
CREATE OR ALTER VIEW vw_station_utilization AS
SELECT
    station_id,
    city,
    COUNT(*)          AS total_sessions,
    SUM(energy_kwh)   AS total_kwh,
    SUM(cost)         AS total_revenue,
    AVG(duration_min) AS avg_duration_min
FROM fact_charging_sessions
GROUP BY station_id, city;
GO
