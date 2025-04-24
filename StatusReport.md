# IS477 Final Project Status Report  
**Team:** GROUP33  
**Members:** Max Zhang, Yiang Xu  

---

## 1. Update on Each Task based on Timeline

### Week 11: Finalize Research Question + Data Sources ✅ Completed

We began identified two final datasets:
- **Formula 1 race results (2010–2023)**, retrieved from the Ergast Developer API using `ergastAPIscraper.py`
- **Global yearly weather anomalies**, including temperature and precipitation data from NOAA’s Climate at a Glance portal, retrieved using `weatherdatascraper.py`

We initially wanted to analyze the relationship between global climate conditions and racing outcomes. But later we expanded our scope to include **performance-based questions** too such as:
- Who are the most consistent or dominant drivers over the years?
- Can we model which constructor or driver would win a championship using historical trends?

These new research questions aligns with the dataset’s strengths while still keeping the original climate-performance hypothesis.

---

### Week 12: Implement Data Scraping + Merging ✅ Completed

We completed programmatic data retrieval for both datasets:
- `ergastAPIscraper.py` makes API requests for all races between 2010 and 2023 and stores clean driver-level results.
- `weatherdatascraper.py` downloads and merges two NOAA sources (temperature anomaly and precipitation) into `global_weather_2010_2023.csv`.

Merging occurs via the `season` and `year` columns. At this stage, data is reproducibly acquired and structured, satisfying project reproducibility criteria.

Artifacts:
- `scripts/ergastAPIscraper.py`
- `scripts/weatherdatascraper.py`
- `data/f1_race_results_2010_2023.csv`
- `data/global_weather_2010_2023.csv`

---

### Week 13: Data Cleaning, Integrity Checks, and Feature Construction ✅ Completed

All cleaning and integrity work is recorded in the [`datawrangling.ipynb`]file. Key steps include:

#### Integrity Checks
- Duplicate entries: None
- Missing values: Present primarily in `time`, `fastest_lap_time`, and `fastest_lap_rank`
  - These are mostly from DNFs or lapped drivers, which we flag but don’t drop.

#### Time Parsing
- Converted `time` column (race completion time or gap) into `race_time` (absolute) using parsing logic. This is because originally, only the first place finish's time is recorded normally, and all other participants have their time recorded as seconds after the first place finish. (which is harder to analyze and interpret)
- Derived `race_time_seconds` to enable quantitative comparisons

#### Feature Engineering
- Created `avg_lap_time = race_time_seconds / laps`
- Parsed and converted `fastest_lap_time` to seconds
- Derived `faster_difference = avg_lap_time - fastest_lap_time_seconds` to measure each driver's performance consistency

#### Label Encoding
- Encoded `driver_id`, `circuit`, and `constructor` into numeric features for modeling and aggregation

Artifacts:
- `datawrangling.ipynb`
- `data/f1_data_cleaned.csv` (saved output from notebook)

---

### Week 14: Visualization and Preliminary Analysis 🟡 In Progress

We’ve begun some prelim visualization mainly to just learn and see potential trends in data better:

- **Winning Constructors by Season**: Bar chart showing who dominates each year
- **Best Driver by Circuit**: Bar chart visualizing who has the most wins per track
- **Seasonal Average Lap Time**: Time series showing how race pace has changed over time
- **Faster Difference Metric**: Drivers with smallest gap between fastest lap and average lap — a proxy for consistency

These provide solid insight into driver and team dominance, performance variability, and track trends. We're now working on:
- Correlating `faster_difference` and `avg_lap_time` with yearly `temp_anomaly_C` and `precip_mm`
- Developing possible driver/constructor win prediction models

Artifacts:
- Visualizations embedded in `datawrangling.ipynb`
- Feature metrics in `f1_data_cleaned.csv`

---

### Week 15: Final Report, Reproducibility, and Presentation  

This is planned for next 2 weeks.

Tasks include:
- Writing final interpretation of visualizations
- Packaging all scripts into a `make` or `.sh` pipeline
- Completing `README.md` with full instructions
- Final polishing of the presentation slide deck and formal report

---

## 2. Updated Timeline

| Week | Task                                                              | Status       | Responsible       |
|------|-------------------------------------------------------------------|--------------|-------------------|
| 11   | Finalize research question + select datasets                      | ✅ Completed | Max & Yiang       |
| 12   | Write data scraping scripts + merge datasets                      | ✅ Completed | Max & Yiang       |
| 13   | Clean data + feature construction + integrity documentation       | ✅ Completed | Max & Yiang       |
| 14   | Create visualizations + explore analysis directions               | 🟡 In Progress | Both              |
| 15   | Prepare final report + presentation + reproducibility packaging   | ⏳ Not Yet   | Both              |

---

## 3. Changes to the Project Plan

### Expanded Scope
- In addition to the original climate correlation goal, we introduced new RQs to leverage our dataset’s richness, including:
  - **Performance modeling** (Who is fastest, most consistent?)
  - **Track-specific dominance** (Which driver dominates which circuits?)

### Technical Additions
- Developed a new time parsing pipeline
- Created multiple derived variables and encodings to support statistical/machine learning applications

### Remaining Adjustments
- Potentially add driver-level modeling if time permits (classification or regression)
- Clean up missing lap time entries with custom imputation or exclusion rules

---
