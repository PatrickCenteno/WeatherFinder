#WeatherFinder
import util
import geocoder
import sys
import requests

WEATHER_API = 'api.openweathermap.org/data/2.5/weather?'

def main():
	if util.is_connected():
		my_ip = util.get_IP()
		print my_ip
		#[latitude, longitude, city, state, country]
		location_values = get_location_values(my_ip)
		weather = get_weather(location_values[0], location_values[1])	
		print weather
	else:
		print 'Must be connected to internet.'
		sys.exit()

def get_location_values(my_ip):
	g = geocoder.ip(str(my_ip))
	return [g.lat, g.lng, g.city, g.state, g.country]

def get_weather(lat, lng):
	params = {'lat':lat, 'lon':lng}
	r = requests.get(WEATHER_API, params = params)
	print (r.url)
	return r.text
	

if __name__ == '__main__':
	main()
