-- Example: Import CSV data into a table using SQL Server (BULK INSERT)
-- First, create the Flights table with appropriate columns and data types
CREATE TABLE FlightData (
    icao24 NVARCHAR(100),
    callsign NVARCHAR(100),
    origin_country NVARCHAR(100),
    time_position NVARCHAR(100),
    last_contact NVARCHAR(100),
    longitude NVARCHAR(100),
    latitude NVARCHAR(100),
    geo_altitude NVARCHAR(100),
    on_ground NVARCHAR(100),
    velocity NVARCHAR(100),
    true_track NVARCHAR(100),
    vertical_rate NVARCHAR(100),
    sensors NVARCHAR(100),
    baro_altitude NVARCHAR(100),
    transponder_code NVARCHAR(100),
    special_purpose_indicator NVARCHAR(100),
    position_source NVARCHAR(100),
    category NVARCHAR(100)
);

BULK INSERT FlightData
FROM 'C:\Users\munee\Documents\Code\Data Analysis\Flight_Data_Analysis\flight_data.csv'
WITH (
    FIRSTROW = 2, -- Skip header row
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',
    TABLOCK
);

SELECT * from FlightData;