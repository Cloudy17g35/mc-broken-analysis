from datetime import datetime

mcbroken_url:str = 'https://mcbroken.com/'

# assumed values - look problem_overview.ipynb
cost_of_one_ice_cream:int = 1
number_of_restaurants:int = 13337
# assumed amount of people per minute which want to buy ice cream in one restaurant
people_per_restaurant_per_minute:int = 4
# that's potential revenue from all ice creames sold in whole restaurants per minute
revenue_per_minute = (cost_of_one_ice_cream * people_per_restaurant_per_minute) * number_of_restaurants
# timezone for setting the current time -
#  list of timezones - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones 
#  (column tz database name)
timezone:str = 'America/New_York'

# directory suffix where data will be stored
data_dir_suffix = 'data'

# range of dates dates used to limit date input in app.py
min_date, max_date = datetime(2022,9,21), datetime(2022,9,23)