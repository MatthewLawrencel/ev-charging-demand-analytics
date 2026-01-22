CREATE DATABASE ev_charging_dw;
GO

USE ev_charging_dw;
GO

CREATE TABLE fact_charging_sessions (
    session_id     VARCHAR(50)  PRIMARY KEY,
    station_id     VARCHAR(20),
    city           VARCHAR(50),
    start_time     DATETIME,
    end_time       DATETIME,
    duration_min   FLOAT,
    energy_kwh     FLOAT,
    cost           FLOAT,
    vehicle_type   VARCHAR(20),
    user_type      VARCHAR(20)
);
GO
