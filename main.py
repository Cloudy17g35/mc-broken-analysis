from time import sleep
import pytz
from datetime import datetime
import csv
from typing import List
from src import scraper, converters, calculations
import settings

tz = pytz.timezone(settings.timezone)

URL:str = settings.mcbroken_url
REVENUE_PER_MINUTE:str = settings.revenue_per_minute

def main():
    output=open(settings.csv_path ,'w')
    header:List[str] = ['date_and_time', 'lost_revenue']
    mywriter=csv.writer(output)
    mywriter.writerow(header)
    while True:
        percentage_from_site:str = scraper.get_percentage_of_currently_broken_machines(URL)
        percentage_of_broken_machines:float = converters.convert_percentage_as_string_to_float(
            percentage_from_site
        )
        lost_revenue:float = calculations.calculate_lost_revenue(
            revenue=REVENUE_PER_MINUTE,
            percentage_of_broken_machines=percentage_of_broken_machines
        )
        current_time:datetime = datetime.now(tz=tz)
        mywriter.writerow([current_time, lost_revenue])
        sleep(60)


if __name__ == '__main__':
    main()

