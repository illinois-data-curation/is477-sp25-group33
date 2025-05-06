rule all:
    input:
        "results/analysis_complete.txt"

rule scrape_ergast:
    output:
        touch("results/ergast_scraped.txt")
    shell:
        "python3 scripts/ergastAPIscraper.py && touch {output}"

rule scrape_weather:
    output:
        touch("results/weather_scraped.txt")
    shell:
        "python3 scripts/weatherdatascraper.py && touch {output}"

rule wrangle_data:
    input:
        "results/ergast_scraped.txt",
        "results/weather_scraped.txt"
    output:
        notebook="notebooks/datawrangling_done.ipynb"
    shell:
        "jupyter nbconvert --to notebook --execute notebooks/datawrangling.ipynb --output {output.notebook}"

rule analyze_data:
    input:
        "notebooks/datawrangling_done.ipynb"
    output:
        notebook="notebooks/analysis_done.ipynb",
        flag="results/analysis_complete.txt"
    shell:
        """
        jupyter nbconvert --to notebook --execute notebooks/analysis.ipynb --output {output.notebook}
        touch {output.flag}
        """
