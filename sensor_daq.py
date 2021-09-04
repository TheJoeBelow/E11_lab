import time
import io
import csv 
import serial
port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.5)
import board
from adafruit_bme280 import basic as adafruit_bme280
import random
import sys

i2c = board.I2C()
sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c)

text = port.read(32)

interval = 10
sleep_time = 1

start_time = time.time()
current_time = start_time
flag_time = 0

#print(sys.argv)
if len(sys.argv)>1:
	interval = int(sys.argv[3])
	#if len(sys.argv) > 3:
		#sleep_time = int(sys.argv[4])
header =['Temperature', 'Humidity', 'Pressure', 'PM1', 'PM2.5', 'PM10', 'Time']
delay_time = int(sys.argv[2])
with open(sys.argv[1]+".csv" , "w", newline= '') as f:
	write = csv.writer(f)
	
	write.writerow(header)
	
	while flag_time<delay_time:
		time.sleep(sleep_time)
		flag_time+=1
		
	while current_time < start_time+delay_time+interval:
		line = []
		temp = sensor.temperature
		humidity = sensor.relative_humidity
		pressure = sensor.pressure
		current_time = current_time + 1
		line.append(round(temp,2))
		line.append(round(humidity,2))
		line.append(round(pressure,2))
		for i in range(4,10,2):
				pm = int.from_bytes(text[i:i+2],byteorder="big")
				line.append(pm)
		line.append(current_time)
		current_time = time.time()
		write.writerow(line)
		time.sleep(sleep_time)
f.close
