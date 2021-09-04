import numpy as np
import math
import io
import requests
import csv
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
channel = 17
GPIO.setup(channel, GPIO.IN)



def Int21R(channel):
	global count
	count +=1
	print("We got a hit")

	
GPIO.add_event_detect(channel, GPIO.FALLING, callback = Int21R)
count = 0
seconds = 0
try:
	while True:
		time.sleep(1.0)
		seconds +=1



		
except KeyboardInterrupt:
	print("All done here")
finally:
	print(count)
	print("The measured CPS is {:.3f}".format(count/seconds))
	GPIO.cleanup()
