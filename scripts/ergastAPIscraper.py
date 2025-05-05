import requests
import pandas as pd
import os

all_results = []

for year in range(2010, 2024):
    print(f"? Fetching season {year}...")
    schedule_url = f"http://ergast.com/api/f1/{year}.json"
    schedule = requests.get(schedule_url).json()
    races = schedule["MRData"]["RaceTable"]["Races"]

    for race in races:
        round_num = race["round"]
        race_name = race["raceName"]
        circuit = race["Circuit"]["circuitName"]
        date = race["date"]

        results_url = f"http://ergast.com/api/f1/{year}/{round_num}/results.json?limit=100"
        results = requests.get(results_url).json()
        race_results = results["MRData"]["RaceTable"]["Races"]

        if not race_results:
            continue

        for result in race_results[0]["Results"]:
            driver = result["Driver"]
            constructor = result["Constructor"]

            all_results.append({
                "season": year,
                "round": round_num,
                "race_name": race_name,
                "circuit": circuit,
                "date": date,
                "driver_id": driver["driverId"],
                "driver_number": result.get("number"),
                "driver_name": f"{driver['givenName']} {driver['familyName']}",
                "constructor": constructor["name"],
                "grid": result["grid"],
                "position": result["position"],
                "position_text": result["positionText"],
                "status": result["status"],
                "laps": result["laps"],
                "time": result.get("Time", {}).get("time"),
                "fastest_lap_rank": result.get("FastestLap", {}).get("rank"),
                "fastest_lap_time": result.get("FastestLap", {}).get("Time", {}).get("time"),
            })

# Save to CSV
df_results = pd.DataFrame(all_results)
os.makedirs("data", exist_ok=True)
df_results.to_csv("data/f1_race_results_2010_2023.csv", index=False)
print("Data Succesfully Saved")
