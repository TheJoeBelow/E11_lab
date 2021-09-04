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

walk_time =180
before_time = 0
while before_time < walk_time:
	time.sleep(1.0)
	before_time +=1
	print(180-before_time, "seconds left..")
	
start_time = time.time()
current_time = start_time
flag_time = 0
delay_time = 600
run_time =  0
sleep_time = 60.0
def Int21R(channel):
	global count
	count +=1

	
GPIO.add_event_detect(channel, GPIO.FALLING, callback = Int21R)
count = 0
header = ['CPM','Time']

with open("outrad.csv" , "w", newline= '') as f:
	write = csv.writer(f)
	
	write.writerow(header)
	


	try:
		while run_time < delay_time:
			time.sleep(sleep_time)
			run_time += 60
			line = []
			current_time = time.time()
			line.append(count)
			line.append(current_time)
			write.writerow(line)
			count =0

			
	except KeyboardInterrupt:
		nothing = 17

	finally:
		GPIO.cleanup()
f.close
