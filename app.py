from flask import Flask
from ProductionCode import covid_stats

app = Flask(__name__)

@app.route('/')
def homepage():
    return (
        "<p>Hello, this is the homepage. To get COVID-19 statistics, use this URL format:</p>"
        "<p>/stats/(country)/(beginning_date)/(ending_date)</p>"
        "Example: /stats/US/2020-03-01/2021-03-10"
    )

@app.route("/stats/<country>/<beginning_date>/<ending_date>", strict_slashes=False)
def stats(country, beginning_date, ending_date):
    try:
        total_cases, total_deaths = covid_stats.stats(country, beginning_date, ending_date)
        return (
            f"COVID-19 stats for {country} from {beginning_date} to {ending_date}:\n"
            f"Total Cases: {total_cases}\n"
            f"Total Deaths: {total_deaths}"
        )
    except Exception as e:
        return f"Error processing request: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
