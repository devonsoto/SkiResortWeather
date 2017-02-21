#Devon Soto
#02/2016

#Program Description:
    #This script will get the weather information from various resorts and print it out
        #(Future application print weather from highest to lowest)
    #Weather information: Temperature,
    #Ski Resorts to include: Avon, Breck, Vail, Keystone

from pprint import pprint
import requests
import json

#user_input = input("Hit Enter to get data for ski resorts")
#while(user_input != "n"):

avon = requests.get('http://api.wunderground.com/api/b19781f781458019/forecast/conditions/q/CO/Denver.json')
avon_data = avon.json()
pprint(avon_data)
pprint(avon_data["current_observation"])
pprint(avon_data["current_observation"]["display_location"]["full"])
print("Getting weather")
#pprint(avon)









'''
f = urllib.request.urlopen('http://api.wunderground.com/api/b19781f781458019/forecast/conditions/q/IA/Denver.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print("Current temperature in %s is: %s" % (location, temp_f))
f.close()
'''
