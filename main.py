#WeatherFinder
import util
import geocoder
import sys

WEATHER_API = 'api.openweathermap.org/data/2.5/weather?'

def main():
	if util.is_connected():
		my_ip = util.get_IP()
		print my_ip
		location_values = get_location_values(my_ip)	
	else:
		print 'Must be connected to internet.'
		sys.exit()

def get_location_values(my_ip):
	g = geocoder.ip(str(my_ip))
	return [g.lat, g.lng, g.city, g.state, g.country]
	

if __name__ == '__main__':
	main()
