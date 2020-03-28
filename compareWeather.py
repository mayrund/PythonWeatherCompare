#!/usr/bin/python

#################################################
#						#
# PyCompareWeather 1.00 (c)              	#
#						#
# https://github.com/mayrund/pycompareweather	#
#						#
# This script uses Open Weather Map API to	#
# fetch location temperatures and compares	#
# between them.					#
#						#
#################################################

from json import load
from urllib2 import urlopen
from pprint import pprint
import operator

##### Configuration #####
baseurl = 'http://api.openweathermap.org/data/2.5/weather?q='
cities = ["tel_aviv", "groningen"]
substract = 273


def get_temp(city):
 url = baseurl + city
 data = urlopen(url)
 response = load(data)
 main = response['main']
 temp =  round(main['temp']-substract)
 #print city, "Temp: ", temp
 return temp


def main():
	try:
		data = {}
		for s in cities:
			data[s] = get_temp(s)

		print "Displaying Temperatures...\n"
		for key, value in data.iteritems():
		    print "%s - %s Celsius" % (key, value)
		
		print "\n* Highest temperature is currenty at", max(data.iteritems(), key=operator.itemgetter(1))[0]
		print "* Lowest temperature is currenty at", min(data.iteritems(), key=operator.itemgetter(1))[0]
	except:
		pass

if __name__ == "__main__":
    main()
