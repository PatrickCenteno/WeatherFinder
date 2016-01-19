#WeatherFinder
import util

def main():
	if util.is_connected():
		my_ip = util.get_IP()
		print my_ip
	else:
		print 'Must be connected to internet.'

if __name__ == '__main__':
	main()
