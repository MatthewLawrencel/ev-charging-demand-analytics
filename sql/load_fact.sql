USE ev_charging_dw;
GO

BULK INSERT fact_charging_sessions
FROM 'C:\Users\lawrence\Desktop\DataEng\ev_charging_analytics\data_clean\ev_sessions_clean.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);
GO
