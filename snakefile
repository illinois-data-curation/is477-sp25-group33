rule all:
    input:
        "results/weather_vs_outcome.png",
        "results/constructor_win_byseason.png",
        "results/consistency_vs_averagePlacing.png",
        "results/best_avg_position_by_circuit.png",
        "results/time_series_Trend.png"

rule scrape_ergast:
    output:
        "data/f1_race_results_2010_2023.csv"
    shell:
        "python3 scripts/ergastAPIscraper.py"

rule scrape_weather:
    output:
        "data/global_weather_2010_2023.csv"
    shell:
        "python3 scripts/weatherdatascraper.py"

rule wrangle_data:
    input:
        "data/f1_race_results_2010_2023.csv",
        "data/global_weather_2010_2023.csv"
    output:
        "data/f1_data_cleaned.csv"
    shell:
        # The notebook must save the cleaned CSV to data/f1_data_cleaned.csv
        "jupyter nbconvert --to notebook --execute notebooks/datawrangling.ipynb --output-dir notebooks"

rule analyze_data:
    input:
        "data/f1_data_cleaned.csv"
    output:
        "results/weather_vs_outcome.png",
        "results/constructor_win_byseason.png",
        "results/consistency_vs_averagePlacing.png",
        "results/best_avg_position_by_circuit.png",
        "results/time_series_Trend.png"
    shell:
        # The notebook must save all PNGs to results/ as part of its code
        "jupyter nbconvert --to notebook --execute notebooks/analysis.ipynb --output-dir notebooks"