from google_flight_analysis.scrape import *

# Keep the dates in format YYYY-mm-dd
result = Scrape('JFK', 'IST', '2023-07-20', '2023-08-20') # obtain our scrape object, represents out query
result.type # This is in a round-trip format
result.origin # ['JFK', 'IST']
result.dest # ['IST', 'JFK']
#result.dates # ['2023-07-20', '2023-08-20']
print(result) # get unqueried str representation

results = Scrape('JFK', 'IST', '2023-08-20')
ScrapeObjects(result)
result.data #see data