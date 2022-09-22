from time import sleep
import pytz
from datetime import datetime
from src import scraper, converters, calculations, json_handling, dir_handling
import settings
from logger import Logger

tz = pytz.timezone(settings.timezone)

URL:str = settings.mcbroken_url
REVENUE_PER_MINUTE:str = settings.revenue_per_minute
logs:Logger = Logger('scraper.log')


def main():
    logs.info('Scraping data started')
    while True:
        try:
            percentage_from_site:str = scraper.get_percentage_of_currently_broken_machines(URL)
        except Exception as e:
            logs.error(f'Error occured while scraping data: {e}')
            return
        percentage_of_broken_machines:float = converters.convert_percentage_as_string_to_float(
            percentage_from_site
        )
        lost_revenue:float = calculations.calculate_lost_revenue(
            revenue=REVENUE_PER_MINUTE,
            percentage_of_broken_machines=percentage_of_broken_machines
        )
        current_time:datetime = datetime.now(tz=tz)
        data_dir:str = f'{settings.data_dir_suffix}/year={current_time.year}/month={current_time.month}/day={current_time.day}'
        dir_handling.create_data_dir_if_not_exists(data_dir)
        result_as_dict:dict = json_handling.write_lost_revenue_to_dict(lost_revenue)
        json_object:str = json_handling.write_dict_to_json_object(result_as_dict)
        path_to_current_file = f'{data_dir}/output={current_time}.json'
        json_handling.write_json_object_to_path(
            json_object=json_object,
            path=path_to_current_file
        )
        logs.info(f'saving file: {path_to_current_file}')
        sleep(60)


if __name__ == '__main__':
    main()

