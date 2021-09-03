
# from Adafruit_BME280 import *

import board
from Adafruit_BME280 import basic as adafruit_bme280
import time
import io
import csv 


# sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

i2c = board.I2C()
sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c)


current_time = 0 
run_time = 10
stop_time = current_time + run_time
units = "seconds"
tables = []
#f= open("temp_data.txt","a")



while current_time < stop_time:
	line = []
	temp = sensor.temperature
	humidity = sensor.relative_humidity
	pressure = sensor.pressure
	current_time = current_time + 1
	line.append(str(format(temp,'.2f')))
	line.append(str(format(humidity,'.2f')))
	line.append(str(format(pressure,'.2f')))
	line.append(str(current_time))
	line.append(units)
	tables.append(line)

	print("Time left:", stop_time - current_time)
	time.sleep(1)
with open("output.csv" , "wb") as f:
	write = csv.writer(f)
	write.writerows(tables)
#f.write(line)
#f.close
