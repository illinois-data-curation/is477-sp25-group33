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


# 5. Findings from Formula 1 Data Analysis and Visualization 

One of the most striking findings from the visualizations is the dominance of a few constructors over the past decade. A bar chart of winning counts by constructor, colored with a vibrant colormap for clarity, reveals that Mercedes and Red Bull have been the most successful teams. For example, Mercedes leads with over 100 race wins, followed by Red Bull with around 80 wins. Other constructors, such as Ferrari and McLaren, have significantly fewer victories, highlighting a competitive imbalance in the sport. This visualization not only makes the disparity clear but also allows for quick identification of periods of dominance and the relative performance of mid-field teams.

Numeric Results that I find:
Constructor Wins: Mercedes (100+), Red Bull (80+), Ferrari (30+), McLaren (20+)
Top Drivers: Lewis Hamilton (80+ wins), Max Verstappen (40+ wins), Sebastian Vettel (30+ wins)

Based on the finding above, it revel one of the most competitive driver in F1 history, Lewis Hamilton. Lewis Hamilton turned the W11 into a trophy‑printing machine because he squeezed every edge the car offered. His late‑braking style matched the W11's vast downforce, letting him carry outrageous mid‑corner speed without punishing the tyres. He used DAS like a pianist uses pedals—dialling toe‑angle in qualifying for peak front‑end bite, then flattening it on race straights to cool the rubber and save fuel. Add his rain‑race intuition (think Turkey 2020) and mistake‑free lap management, and each stint became a metronome run: push when gaps appeared, coast when traffic loomed. The result—13 wins, seventh title—felt inevitable. He is our GOAT of the F1.

Unique Drivers: Over 70 drivers participated from 2010–2023.

Driver Consistency vs Average Position: The higher their average position is, their driving performance are also tend to be more consistant.

Weather Anomalies: 
Base on the corrlation heatmap,we notice that years with higher temperature/precipitation anomalies showed a slight increase in DNFs. By merging weather data with race results, the notebook explores whether years with extreme temperature or precipitation anomalies correspond to changes in race outcomes, such as increased DNFs (Did Not Finish) or shifts in average finishing positions. While the initial analysis does not find a strong direct correlation, it does highlight years where weather extremes coincide with more unpredictable race results, suggesting avenues for deeper investigation.

## 6. Future Work

#Lessons Learned
This project provided valuable insights into both the technical and analytical challenges of integrating sports performance data with global climate records. One of the most important lessons learned was the necessity of rigorous data cleaning and standardization. Formula 1 data, while rich and detailed, comes in a variety of formats and often contains inconsistencies—such as mixed time formats, missing values, and ambiguous status codes (e.g., DNFs, disqualifications, or technical failures). Developing robust scripts to harmonize these fields was essential for meaningful analysis. Similarly, the climate data, though more structured, required careful aggregation and alignment with the F1 season calendar to ensure valid comparisons.
Another key lesson was the importance of clear, effective visualizations. The bar charts and heatmaps created during this project not only made complex trends accessible but also highlighted the competitive imbalance in F1 and the subtle, sometimes elusive, relationship between weather anomalies and race outcomes. The process of encoding categorical variables (like driver and constructor IDs) and transforming time data into a unified format was crucial for enabling advanced analytics and machine learning applications.
Finally, the project underscored the value of reproducibility and automation. By using scripts for data scraping, cleaning, and merging, and by packaging the workflow with Snakemake, we ensured that the entire analysis could be rerun from scratch, facilitating both collaboration and future extensions.

#Potential Future Work
1. Granular Weather Data Integration
While this project used global annual climate anomalies, future work could incorporate more granular, race-specific weather data. This would involve collecting local weather conditions (temperature, precipitation, humidity, wind speed) for each Grand Prix weekend, ideally at the track level and for each session (practice, qualifying, race). Such data would enable a much more precise analysis of how weather impacts race outcomes, tire strategies, pit stop frequency, and driver performance. APIs from meteorological services or historical weather databases could be leveraged for this purpose.
2. Leveraging Additional Datasets: Pit Stops and Strategy Analysis
A promising direction for future work is the integration of additional datasets available from the Ergast API, particularly those related to pit stops, lap times, and in-race events. The Ergast API provides detailed pit stop data for each race, including the lap number, duration of each stop, and the exact timing within the race. By combining this information with lap-by-lap timing data, we can conduct a much more granular analysis of team and driver strategies.
Pit stops are a critical component of Formula 1 strategy, often determining the outcome of a race. By analyzing the number, timing, and duration of pit stops for each team and driver, we can identify patterns in successful strategies. For example, we could compare the average number of pit stops made by race winners versus those finishing lower in the order, or analyze how undercut and overcut strategies (pitting earlier or later than rivals) affect track position and final results.
With access to lap time data, it becomes possible to directly measure the impact of pit stops on race pace. By aligning pit stop events with subsequent lap times, we can assess how quickly drivers are able to regain speed on fresh tires, or how much time is lost due to traffic or suboptimal pit timing. This analysis could reveal, for instance, whether certain teams consistently execute faster pit stops, or if some drivers are particularly adept at maximizing performance immediately after a stop.
By aggregating pit stop and lap time data across multiple races and seasons, we can begin to identify which strategies yield the best results under different conditions. For example, we could analyze whether two-stop or three-stop strategies are more effective at specific circuits, or how weather conditions influence the optimal timing of pit stops. Machine learning models could even be trained to predict the best pit strategy based on real-time race data, track characteristics, and weather forecasts.
Incorporating these additional datasets would not only deepen our understanding of race strategy but also provide actionable insights for teams, drivers, and fans. It would enable a more holistic analysis of race dynamics, moving beyond simple finishing positions to uncover the complex interplay of decisions that shape every Grand Prix.

Conclusion
In summary, this project has laid a strong foundation for the quantitative study of the interplay between climate and Formula 1 performance. The lessons learned about data cleaning, integration, and visualization will inform future work, while the potential extensions outlined above offer exciting opportunities for deeper, more impactful analysis. As climate change continues to affect global weather patterns, understanding its influence on high-performance sports like Formula 1 will become increasingly important—not only for teams and drivers but also for fans, organizers, and policymakers. By building on this work and leveraging additional datasets such as pit stops and lap times, future researchers can help ensure that the sport remains both thrilling and resilient in the face of new environmental challenges.

## 7. Reproducing

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

## 8. References & Citations

### Data Sources
- **Ergast Developer API**  
  Ergast Developer API. Formula 1 data. [https://ergast.com/mrd](https://ergast.com/mrd)  
  License: Creative Commons Attribution 4.0 International (CC BY 4.0)

- **NOAA Climate at a Glance**  
  National Centers for Environmental Information (NCEI), NOAA. Climate at a Glance: Global Time Series. [https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series)  
  License: U.S. Government Public Domain

### Software & Libraries
- **Python** Software Foundation. (2023). Python (Version 3.11.1) [Computer software]. https://www.python.org/

- **pandas** development team. (2024). pandas (Version 2.2.0) [Computer software]. https://pandas.pydata.org/

- **NumPy** developers. (2024). NumPy (Version 1.26.4) [Computer software]. https://numpy.org/

- **Matplotlib** development team. (2024). Matplotlib (Version 3.8.4) [Computer software]. https://matplotlib.org/

- **seaborn** Waskom, M. L., & seaborn development team. (2024). seaborn (Version 0.13.2) [Computer software]. https://seaborn.pydata.org/

- **scikit‑learn** developers. (2024). scikit‑learn (Version 1.4.2) [Computer software]. https://scikit‑learn.org/

- **Project Jupyter**. (2024). Jupyter Notebook (Version 7.1.3) [Computer software]. https://jupyter.org/

- **Snakemake** Köster, J., Mölder, F., & Snakemake community. (2024). Snakemake (Version 8.2.1) [Computer software]. https://snakemake.readthedocs.io/



