# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = '4bb9a34284df42445cc8898d130643ea'

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
	print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
	sys.exit()

location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
print(response.text)

# TODO: Load JSON data into a Python variable.


