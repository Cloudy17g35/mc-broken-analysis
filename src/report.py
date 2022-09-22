from datetime import datetime
from typing import Union, List
import settings
import os
from src import json_handling


def sum_daily_lost_revenue_for_date(
    date:datetime.date
    ) -> Union[float, None]:
    path_to_files:str = f'{settings.data_dir_suffix}/year={date.year}/month={date.month}/day={date.day}/'
    if not os.path.exists(path_to_files):
        return
    list_of_files:List[str] = os.listdir(path_to_files)
    if not list_of_files:
        return
    summed_revenue:float = 0

    for file in list_of_files:
        path_to_cur_file:str = f'{path_to_files}/{file}'
        current_dict:dict = json_handling.read_json_to_dict(path_to_cur_file)
        summed_revenue += current_dict['lost_revenue']

    return round(summed_revenue, 2)