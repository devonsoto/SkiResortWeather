#Devon Soto
#02/2016

#Program Description:
    #This script will get the weather information from various resorts and print it out
        #(Future application print weather from highest to lowest)
    #Weather information: Temperature,
    #Ski Resorts to include: Avon, Breck, Vail, Keystone

from requests.exceptions import ConnectionError
from pprint import pprint
import requests
import json

#TODO: Put a try except for ConnectionError.
#TODO: Organize into a class or function.


user_input = input("Hit Enter to get data for ski resorts: ")

#--------------------------------#

#This gives me weather information of Avon
#--------------------------------#
avon = requests.get('http://api.wunderground.com/api/b19781f781458019/forecast/conditions/q/CO/Avon.json')
avon_data = avon.json()
#pprint(avon_data)

city_info = avon_data['current_observation']['display_location']['full']
print("Ski resort weather information for: {} ".format(city_info))
for days in range(0,3):

    snow_day = (avon_data["forecast"]["simpleforecast"]["forecastday"][days]['snow_day'])
    average_wind = (avon_data["forecast"]["simpleforecast"]["forecastday"][days]['avewind']['mph'])
    fahrenheit_low = (avon_data["forecast"]["simpleforecast"]["forecastday"][days]["low"]["fahrenheit"])
    fahrenheit_high = (avon_data["forecast"]["simpleforecast"]["forecastday"][days]["high"]["fahrenheit"])
    weekday = (avon_data["forecast"]["simpleforecast"]["forecastday"][days]["date"]["weekday"])
    conditions = (avon_data["forecast"]["simpleforecast"]["forecastday"][days]["conditions"])
    print("Day of the week: {}".format(weekday))

    print("Condition: {}".format(conditions))
    print("Highest Temperature: {}, Lowest Temperature: {}".format(fahrenheit_high,fahrenheit_low))
    print("Snow weather information: {}".format(snow_day))
print()
#--------------------------------#

#This gives me weather information of Vail
#--------------------------------#
vail = requests.get('http://api.wunderground.com/api/b19781f781458019/forecast/conditions/q/CO/Vail.json')
vail_data = vail.json()
#pprint(avon_data)

city_info = vail_data['current_observation']['display_location']['full']
print("Ski resort weather information for: {} ".format(city_info))
for days in range(0,3):

    snow_day = (vail_data["forecast"]["simpleforecast"]["forecastday"][days]['snow_day'])
    average_wind = (vail_data["forecast"]["simpleforecast"]["forecastday"][days]['avewind']['mph'])
    fahrenheit_low = (vail_data["forecast"]["simpleforecast"]["forecastday"][days]["low"]["fahrenheit"])
    fahrenheit_high = (vail_data["forecast"]["simpleforecast"]["forecastday"][days]["high"]["fahrenheit"])
    weekday = (vail_data["forecast"]["simpleforecast"]["forecastday"][days]["date"]["weekday"])
    conditions = (vail_data["forecast"]["simpleforecast"]["forecastday"][days]["conditions"])

    print("Day of the week: {}".format(weekday))
    print("Condition: {}".format(conditions))
    print("Highest Temperature: {}, Lowest Temperature: {}".format(fahrenheit_high,fahrenheit_low))
    print("Snow weather information: {}".format(snow_day))
print()
#--------------------------------#

#This gives me weather information of Keystone
#--------------------------------#

Keystone = requests.get('http://api.wunderground.com/api/b19781f781458019/forecast/conditions/q/CO/Keystone.json')
keystone_data = Keystone.json()
#pprint(avon_data)
city_info = keystone_data['current_observation']['display_location']['full']
print("Ski resort weather information for: {} ".format(city_info))
for days in range(0,3):

    snow_day = (keystone_data["forecast"]["simpleforecast"]["forecastday"][days]['snow_day'])
    average_wind = (keystone_data["forecast"]["simpleforecast"]["forecastday"][days]['avewind']['mph'])
    fahrenheit_low = (keystone_data["forecast"]["simpleforecast"]["forecastday"][days]["low"]["fahrenheit"])
    fahrenheit_high = (keystone_data["forecast"]["simpleforecast"]["forecastday"][days]["high"]["fahrenheit"])
    weekday = (keystone_data["forecast"]["simpleforecast"]["forecastday"][days]["date"]["weekday"])
    conditions = (keystone_data["forecast"]["simpleforecast"]["forecastday"][days]["conditions"])

    print("Day of the week: {}".format(weekday))
    print("Condition: {}".format(conditions))
    print("Highest Temperature: {}, Lowest Temperature: {}".format(fahrenheit_high,fahrenheit_low))
    print("Snow weather information: {}".format(snow_day))
print()
#--------------------------------#

#This gives me weather information of Breckenridge
#--------------------------------#
Breck = requests.get('http://api.wunderground.com/api/b19781f781458019/forecast/conditions/q/CO/Breckenridge.json')
breckenridge_data = Breck.json()
#pprint(avon_data)

city_info = breckenridge_data['current_observation']['display_location']['full']
print("Ski resort weather information for: {} ".format(city_info))
for days in range(0,3):

    snow_day = (breckenridge_data["forecast"]["simpleforecast"]["forecastday"][days]['snow_day'])
    average_wind = (breckenridge_data["forecast"]["simpleforecast"]["forecastday"][days]['avewind']['mph'])
    fahrenheit_low = (breckenridge_data["forecast"]["simpleforecast"]["forecastday"][days]["low"]["fahrenheit"])
    fahrenheit_high = (breckenridge_data["forecast"]["simpleforecast"]["forecastday"][days]["high"]["fahrenheit"])
    weekday = (breckenridge_data["forecast"]["simpleforecast"]["forecastday"][days]["date"]["weekday"])
    conditions = (breckenridge_data["forecast"]["simpleforecast"]["forecastday"][days]["conditions"])

    print("Day of the week: {}".format(weekday))
    print("Condition: {}".format(conditions))
    print("Highest Temperature: {}, Lowest Temperature: {}".format(fahrenheit_high,fahrenheit_low))
    print("Snow weather information: {}".format(snow_day))
print()
#--------------------------------#
