import socket
from urllib2 import urlopen

REMOTE_SERVER = "www.reddit.com"

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


def get_IP():
	return urlopen('http://ip.42.pl/raw').read()



