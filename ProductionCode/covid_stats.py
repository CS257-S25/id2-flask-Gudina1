import csv
from datetime import datetime

CSV_FILE = 'ProductionCode/Dummy_data.csv'

def stats(country, beginning_date, ending_date):
    beginning = datetime.strptime(beginning_date, "%Y-%m-%d")
    ending = datetime.strptime(ending_date, "%Y-%m-%d")

    total_cases = 0
    total_deaths = 0

    with open(CSV_FILE, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Country'] == country or row['Country_code'] == country:
                try:
                    date = datetime.strptime(row['Date_reported'], "%Y-%m-%d")
                except ValueError:
                    continue

                if beginning <= date <= ending:
                    total_cases += int(row.get('New_cases', 0) or 0)
                    total_deaths += int(row.get('New_deaths', 0) or 0)

    return total_cases, total_deaths


def compare(countries, week):

    for country in countries:
        try:
            cases, deaths = stats(country, week, week)
            print(f"Total cases in {country} during {week}: {cases}")
            print(f"Total deaths in {country} during {week}: {deaths}\n")
        except Exception as e:
            print(f"Error fetching data for {country}: {e}")

    return cases, deaths
