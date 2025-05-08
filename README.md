# IS 477 Final Project: Investiage Formula One Winner relationship with Global Climate
Github Archival Record: https://github.com/illinois-data-curation/is477-sp25-group33/releases/tag/Temporary_Final_Release
--
**Contributors:** William Xu, Max Zhang

## 1.Summary

Our project aims to explore how yearly variations in global climate conditions relate to performance patterns in Formula 1 racing. Formula 1 fascinates us precisely because it’s a symphony of engineering brilliance and human reflex: the split‑second timing in the pits, the constant tweaks in aerodynamic packages, and the relentless data analysis unfolding in the garage while drivers fight for tenths of a second on track. Every regulation change brings new unknowns, and every venue — from the damp elevation of São Paulo to the desert night of Abu Dhabi — layers fresh complexity onto strategy. By investigating weather and climate alongside race results we aim to spotlight an often‑mentioned but rarely quantified variable: how much do Mother Nature’s mood swings tilt the battlefield?We're curious to explore how these external factors might impact the top of the "driving foodchain", which is Formula One championships.We are motivated by the intensity and excitement of Formula One and the exquisite cooperation between the engineering team and the drivers. We like the mechanical design and the constantly innovative aerodynamic system of these cars, which makes the championship always full of unknowns. We want to judge the impact of weather on the championship through the drivers' race records and the historical level of the team's vehicles, the performance of different tracks and countries.

I explored Formula 1 race results from 2010 to 2023, focusing on how different constructors performed over time. One of the key visualizations I created was a bar chart showing the number of wins by each constructor. This visualization provided a clear, immediate understanding of which teams have dominated the sport in recent years. By using a vibrant colormap, each constructor was assigned a unique color, making the chart both visually appealing and easy to interpret. The bar chart revealed that a few constructors, such as Mercedes and Red Bull, have significantly more wins compared to others, highlighting the competitive imbalance in F1 during this period.Some insights we find out is the best team are Williams,McLaren, Red Bulls, Ferrari & Mercedes. Best Driver are Lewis Hamilton,Sebastian Vettel&Max Verstappen. 2019&2020 is the fast season ever which Lewis Hamilton from Mercedes driven W11 also being consider as the one the fastest F1 vehicle in the F1 history.Overall, the visualizations and data processing steps  from datawrangling workbook not only made the data more accessible but also uncovered important trends in team performance, driver consistency, and the evolving landscape of Formula 1 racing. These insights can inform deeper statistical analysis or predictive modeling in future work.

## 4. Data Profile

### Dataset 1: Formula 1 Race Results (2010–2023)
- **Source**: [Ergast Developer API](https://ergast.com/mrd)
- **Format**: JSON retrieved (original format) and flattened to CSV for ease of analysis
- **Script**: `scripts/ergastAPIscraper.py`
- **Columns**: season, round, race_name, driver_id, position, grid, laps, status, fastest lap, etc.
- **License**: Creative Commons Attribution 4.0

This dataset is a lap‑by‑lap ledger of the modern Formula 1 era, pulled directly from the Ergast Developer API with our helper script scripts/ergastAPIscraper.py. The scraper pages through every championship round from 2010 to 2023, flattens the nested JSON, and exports a UTF‑8 CSV so you can drop it straight into wordbook.

Each row represents one driver in one Grand Prix. Key calendar fields—season, round, and race_name—let you slice by year or circuit in a single line of code. Competitive variables (position, grid, laps, milliseconds, fastestLapTime) support everything from simple podium counts to regression models of grid‑vs‑finish performance. Context columns such as constructor_id and status (Finished, Accident, Engine, etc.) enable reliability studies or DNF clustering, while fields like points and driver_id join seamlessly to external tables for richer analytics.

We performs a basic data cleaning in datawrangling.ipynb: it coerces numeric types, drops abandoned events that lack a classified order, and normalises camel‑case keys into snake‑case for stylistic consistency. All timestamps are standardised to UTC, eliminating cross‑platform timezone headaches. We perform an column transfer for those time columns with object type into calculable numerical columns representing different lab time feature.  At 14 seasons and roughly 300–400 rows per race year, the file strikes a balance between granularity and manageability—dense enough for machine‑learning pipelines, yet small enough for interactive notebooks. This data Ergast feed is licensed under Creative Commons BY 4.0.

### Dataset 2: Global Weather Anomalies (2010–2023)
- **Source**: [NOAA Climate at a Glance](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series)
- **Format**: CSV
- **Script**: `scripts/weatherdatascraper.py`
- **Columns**: Year, temperature anomaly (°C), yearly precipitation (mm)
- **License**: U.S. Government Public Data (no restrictions)

This dataset sourced via NOAA’s “Climate at a Glance” interface and downloaded through scripts/weatherdatascraper.py, this CSV distils sprawling meteorological archives into a compact panel of annual climate signals. Each observation represents one calendar year of globally averaged conditions, giving just 14 tidy rows—ideal for high‑level correlation with season‑aggregated F1 metrics. The headline feature, temperature_anomaly, expresses the departure (in °C) from the 20th‑century baseline, allowing you to trace the recent acceleration of warming with a single column. A companion measure, yearly_precipitation, records total global land‑and‑ocean precipitation (mm) and lets you test hypotheses about grip levels or race interruptions on especially wet seasons. These two variables are intentionally minimalist: they act as macro “climate mood” factors rather than local track‑day forecasts, so they pair cleanly with Formula 1 data that is itself aggregated over a season.

## 5. Findings

## 6. Future Work

##7. Reproducing

To reproduce our full analysis pipeline from data acquisition to result visualization, follow the steps below.

#### 1. Clone the repository
```bash
git clone https://github.com/illinois-data-curation/is477-sp25-group33.git
cd is477-sp25-group33
```

#### 2. Set up the environment
Install all required dependencies:
```bash
pip install -r requirements.txt
```

#### 3. Run the full workflow with Snakemake
This will:
- Scrape Formula 1 and climate data using respective APIs
- Clean and merge the datasets
- Run the data analysis notebook
- Generate final visualizations in `results/`

```bash
snakemake --cores 1
```

#### 4. Download Output Files (if needed)
If you are unable to run the full workflow or want to view the outputs directly:

- Access our output visualizations and cleaned data here:  
  **[Box Folder Link](https://your-box-link-here.com)**

- Save the files to the following locations:
  - Place all `.png` plots in `results/`
  - Place cleaned dataset `f1_data_cleaned.csv` in `data/`

#### Notes:
- Execute the snakefile from the project root.
- All code, data scraping, cleaning, and analysis steps are automated and reproducible using Snakemake.
