mcbroken_url:str = 'https://mcbroken.com/'

# i assumed revenue from selling ice creames in all McDonalds in US is equal 53348
# (look problem_overview notebook)

cost_of_one_ice_cream:int = 1
number_of_restaurants:int = 13337
# assumed amount of people per minute which want to buy ice cream in one restaurant
people_per_restaurant_per_minute:int = 4

revenue_per_minute = (cost_of_one_ice_cream * people_per_restaurant_per_minute) * number_of_restaurants
# timezone for setting the current time -
#  list of timezones - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones 
# (column tz database name)
timezone:str = 'America/New_York'

# directory where data will be stored
data_dir_suffix = 'data'