# IS477 Final Project Plan  
**Team Name:** GROUP33  
**Members:** Max Zhang Yiang Xu

---

## ? Project Title  
**Exploring Patterns and Performance in Formula 1: A Data-Driven Analysis of Racing Outcomes**

---

## 1. ? Research Question(s)

We aim to explore the following questions using Formula 1 datasets:

- What performance trends can be observed for drivers and constructors across F1 seasons?
- How do factors like pit stop timing, qualifying positions, or circuit type influence race outcomes?
- How can programmatic data acquisition and integration be used to build an end-to-end motorsport analytics pipeline?

---

## 2. ? Data Sources

### Dataset 1: Ergast Developer API
- **Source**: [https://ergast.com/mrd](https://ergast.com/mrd)
- **Method**: JSON-based public API
- **Data**: Race results, pit stops, lap times, qualifying, driver and constructor data
- **Accessed via**: `scripts/f1_scraper.py`
- **License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

### Dataset 2: [Insert Second F1 Dataset]
_(examples below ¡ª to be finalized by your group)_
- **Source**: e.g., Kaggle F1 Telemetry Dataset, Weather API, or Circuit Info CSV
- **Method**: [API / Manual Download / Scraped]
- **Data**: [Telemetry | weather | tire strategy | team radio | etc.]
- **License**: [To be documented]
- **Accessed via**: `scripts/f1_data_merge.py` or similar

---

## 3. ?? Planned Data Integration & Cleaning

- **Ergast API**: Normalize and clean JSON outputs into structured CSVs (drivers, races, pit stops, results)
- **Second Dataset**: Match by shared keys like `season`, `round`, `driverId`, or `circuitId`
- **Final Dataset**: Merge into a single race-level or driver-level frame for analysis

---

## 4. ? Planned Analysis & Visualization

| Focus        | Examples |
|--------------|----------|
| Drivers      | Win rates, fastest laps, qualifying vs. finishing position |
| Constructors | Season standings, podium finishes, consistency |
| Strategy     | Pit stop timing impact, tire degradation (if available) |
| Visualization | Line plots, scatter plots, bar charts, animated lap-by-lap leaderboards |

---

## 5. ? Automation & Reproducibility

- API scraping (Ergast): `scripts/f1_scraper.py`
- Data wrangling & merging: `scripts/data_cleaner.py`
- Visualization notebooks: `notebooks/analysis.ipynb`
- Raw data not stored in repo (`.gitignore` enforced)
- Optional checksums or metadata log

---

## 6. ? Timeline

| Week | Task |
|------|------|
| Week 11 | Select second dataset, finalize RQ |
| Week 12 | Implement and test API scraper |
| Week 13 | Clean and merge both datasets |
| Week 14 | Analysis + visualizations |
| Week 15 | Final report and presentation prep |

---

## 7. ? Division of Work

| Member | Responsibility |
|--------|----------------|
| [Name] | Ergast API scraper |
| [Name] | Second dataset acquisition & cleaning |
| [Name] | EDA and visualizations |
| All    | Question design, integration, presentation |

---

## 8. ? References

- Ergast API: https://ergast.com/mrd
- [Second dataset reference or link here]

---
