# Data Dictionary: f1_data_cleaned.csv

This file describes the fields in the `data/f1_data_cleaned.csv` file, which merges Formula 1 race results, driver/contructor info, and global weather data.

| Field Name                | Type    | Description                                                                 | Possible Values / Notes |
|--------------------------|---------|-----------------------------------------------------------------------------|------------------------|
| season                   | int     | Year of the F1 season                                                       | 2010®C2023              |
| round                    | int     | Race round number within the season                                         | 1, 2, ...              |
| race_name                | string  | Name of the Grand Prix                                                      | e.g., "Bahrain Grand Prix" |
| circuit                  | string  | Name of the circuit/track                                                   | e.g., "Silverstone Circuit" |
| date                     | string  | Date of the race (YYYY-MM-DD)                                               | e.g., "2010-03-14"    |
| driver_id                | string  | Unique identifier for the driver                                            | e.g., "hamilton"      |
| driver_number            | int     | Car number of the driver                                                    | e.g., 44               |
| driver_name              | string  | Full name of the driver                                                     | e.g., "Lewis Hamilton"|
| constructor              | string  | Name of the constructor/team                                                 | e.g., "Mercedes"      |
| grid                     | int     | Starting grid position                                                      | 1, 2, ...              |
| position                 | int     | Finishing position (numeric, 1 = winner)                                    | 1, 2, ...              |
| position_text            | string  | Finishing position (text, e.g., 'R' for retired, 'W' for withdrawn)         | 1, 2, ..., 'R', 'W'    |
| status                   | string  | Status at finish (e.g., 'Finished', 'Accident', '+1 Lap', etc.)             | See race status codes  |
| laps                     | int     | Number of laps completed                                                    | integer                |
| time                     | string  | Time gap to winner or race time for winner                                  | e.g., '1:39:20.396', '+16.099' |
| fastest_lap_rank         | float   | Rank of the driver's fastest lap in the race                                | 1.0, 2.0, ... or blank |
| fastest_lap_time         | string  | Time of the driver's fastest lap                                            | e.g., '1:29.291'       |
| race_time                | string  | Absolute race time for the driver (if available)                            | e.g., '01:39:20.396000'|
| race_time_seconds        | float   | Absolute race time in seconds (if available)                                | e.g., 5960.396         |
| driver_encoded           | int     | Encoded numeric value for driver_id (for modeling)                          | integer                |
| circuit_encoded          | int     | Encoded numeric value for circuit (for modeling)                            | integer                |
| constructor_encoded      | int     | Encoded numeric value for constructor (for modeling)                        | integer                |
| avg_lap_time             | float   | Average lap time for the driver in the race (seconds)                       | float                  |
| fastest_lap_time_seconds | float   | Fastest lap time for the driver in seconds                                  | float                  |
| faster_difference        | float   | Difference between avg_lap_time and fastest_lap_time_seconds                | float                  |
| Year                     | int     | Year of the race (from weather data, redundant with 'season')               | 2010®C2023              |
| Anomaly                  | float   | Global temperature anomaly for the year (°„C, from NOAA)                     | e.g., 0.68             |
| precip_mm                | float   | Global yearly precipitation (mm, from NOAA)                                 | e.g., 985.73           |

---

**Notes:**
- Some columns may have missing values for drivers who did not finish (DNF) or did not set a fastest lap.
- Encoded columns are for use in machine learning or statistical modeling.
- Weather columns are merged from NOAA data and are the same for all rows in a given year.
- See the original Ergast API and NOAA documentation for more details on source fields. 