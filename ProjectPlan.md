# IS477 Final Project Plan  
**Group:** GROUP 33  
**Members:** Max Zhang, Yiang Xu

---

## Project Title  
**Speed vs. Climate: Investigating the Impact of Weather Anomalies on Formula 1 Race Outcomes**

---

## 1. Overview

Our project aims to explore how yearly variations in global climate conditions relate to performance patterns in Formula 1 racing. As casual ordinary drivers, we know driving is heavily influenced by not only the weather (heavy rain, snow, etc.), but also the temperature (midwest winter isn't the most friendly for cars). We're curious to explore how these external factors might impact the top of the "driving foodchain", which is Formula One championships.

---

## 2. Research Question(s)

- Does global precipitation or temperature anomaly correlate with average driver outcomes in Formula 1 races?
- Are certain years with more extreme weather conditions associated with increased DNFs (did-not-finish) or reduced average finishing positions?

---

## 3. Team

| Member     | Responsibility                      |
|------------|--------------------------------------|
| Max Zhang  | Ergast API data extraction, cleaning |
| Yiang Xu   | NOAA weather scraping + merging      |
| Both       | Visualizations, analysis, final report|

---

## 4. Datasets

### Dataset 1: Formula 1 Race Results (2010–2023)
- **Source**: [Ergast Developer API](https://ergast.com/mrd)
- **Format**: JSON retrieved (original format) and flattened to CSV for ease of analysis
- **Script**: `scripts/ergastAPIscraper.py`
- **Columns**: season, round, race_name, driver_id, position, grid, laps, status, fastest lap, etc.
- **License**: Creative Commons Attribution 4.0

### Dataset 2: Global Weather Anomalies (2010–2023)
- **Source**: [NOAA Climate at a Glance](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series)
- **Format**: CSV
- **Script**: `scripts/weatherdatascraper.py`
- **Columns**: Year, temperature anomaly (°C), yearly precipitation (mm)
- **License**: U.S. Government Public Data (no restrictions)

---

## 5. Timeline

| Week | Task                                  |
|------|---------------------------------------|
| 11   | Finalize question + data sources      |
| 12   | Implement data scraping + merging     |
| 13   | Clean + analyze datasets, documentation of data integrity and quality issues              |
| 14   | Visualizations + draft analysis       |
| 15   | Finalize report, presentation, reproducibility packaging, and metadata   |

---

## 6. Reproducibility

- All datasets are acquired at runtime via:
  - `weatherdatascraper.py`
  - `ergastAPIscraper.py`
- `.gitignore` prevents data files from being committed
- Scripts ensure reproducible downloads and consistent file formats

---

## 7. References

- Ergast Developer API: https://ergast.com/mrd
- NOAA Climate at a Glance: https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/
- NOAA GSOTY Data: https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-year

---

