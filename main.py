#WeatherFinder
import socket
from urllib2 import urlopen
import geocoder
import sys
import requests
import json

REMOTE_SERVER = "www.reddit.com" #:)
WEATHER_API = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = '209bb1808f1fca53362d3704d127f45f'

def main():
	if is_connected():
		my_ip = get_IP()

		#[latitude, longitude, city, state, country]
		location_values = get_location_values(my_ip)

		print 'Your IP Address is: ' + my_ip
		print 'Here\'s some weather information for '+ location_values[2] + \
			', ' + location_values[3] + ':'

		# Parse the Json response
		raw_response = get_weather(location_values[0], location_values[1])
		weather_json = json.loads(raw_response)
		temperature = to_faren(int(weather_json['main']['temp']))
		print 'It is currently ' + str(temperature) + ' degrees farenheit'
		
		
	else:
		print 'Must be connected to internet.'
		sys.exit()


# Uses geocoder to get Latitude, Longitude
# City, State, and Country based on aquired IP
# address
def get_location_values(my_ip):
	g = geocoder.ip(str(my_ip))
	return [g.lat, g.lng, g.city, g.state, g.country]


# Hits openweathermap.org to get weather statistics in 
# JSON format for aquired longitude and latitude
def get_weather(lat, lng):
	params = {'lat':str(lat), 'lon':str(lng), 'APPID':API_KEY}
	r = requests.get(WEATHER_API, params = params)
	#print (r.url)
	return r.text 


# Function to check internet connection
def is_connected():
	try:
	    # see if we can resolve the host name -- tells us if there is
	    # a DNS listening
	    host = socket.gethostbyname(REMOTE_SERVER)
	    # connect to the host -- tells us if the host is actually
	    # reachable
	    s = socket.create_connection((host, 80), 2)
	    return True
	except:
		return False


# Function to get IP Address
def get_IP():
	return urlopen('http://ip.42.pl/raw').read()


# Converts Kelvin to Farenheit
def to_faren(temp):
	return (temp - 273.15) * 1.8 + 32



if __name__ == '__main__':
	main()
