import numpy as np
import math
import io
import requests
import csv
import time
import RPi.GPIO as GPIO
import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
	try:
		report = session.next()
		#print(report)
		if report['class'] == 'TPV':
			if hasattr(report, 'lat'):
				print(report.lat)
			if hasattr(report, 'lon'):
				print(report.lon)
		
	except KeyError:
		pass
	
	except KeyboardInterrupt:
		quit()
		
	except StopIteration:
		session = None
		print("It's all over now...")
		
