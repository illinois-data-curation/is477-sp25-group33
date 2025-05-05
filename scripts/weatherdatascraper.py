import requests
import pandas as pd
from pathlib import Path

# === Output directory ===
output_path = Path("data")
output_path.mkdir(parents=True, exist_ok=True)

# === URLs for data ===
precip_url = (
    "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/"
    "globe/pcp/land_ocean/12/1/2010-2023.csv"
)

temp_url = (
    "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/"
    "globe/land_ocean/12/1/2010-2023.csv"
)

# === Download and save ===
def download_and_save(url, filename):
    response = requests.get(url)
    with open(output_path / filename, "wb") as f:
        f.write(response.content)

download_and_save(precip_url, "precip_2010_2023.csv")
download_and_save(temp_url, "temp_2010_2023.csv")

# === Load and clean ===
df_precip = pd.read_csv(output_path / "precip_2010_2023.csv", skiprows=3)
df_temp = pd.read_csv(output_path / "temp_2010_2023.csv", skiprows=4)

df_precip = df_precip.rename(columns={"Value": "precip_mm", "Anomaly": "precip_anomaly_mm"})
df_temp = df_temp.rename(columns={"Value": "temp_anomaly_C"})

df_precip["Year"] = df_precip["Year"].astype(int)
df_temp["Year"] = df_temp["Year"].astype(int)

# === Merge by year ===
df_merged = pd.merge(df_temp[["Year", "Anomaly"]], df_precip, on="Year")

# === Save merged output ===
df_merged.to_csv(output_path / "global_weather_2010_2023.csv", index=False)
print("Saved merged dataset")
