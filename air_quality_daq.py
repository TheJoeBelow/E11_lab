# air quality
import time
import io
import csv 
import serial
port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.5)


text = port.read(32)


current_time = 0 
run_time = 10
stop_time = current_time + run_time
#f= open("temp_data.txt","a")

with open("airquality.csv" , "w", newline= '') as f:
	write = csv.writer(f)

	while current_time < stop_time:
		line = []
		current_time = current_time + 1
		i=4
		for i in range(4,10,2):
			pm = int.from_bytes(text[i:i+2],byteorder="big")
			line.append(pm)
		line.append(current_time)
		write.writerow(line)

		print("Time left:", stop_time - current_time)
		time.sleep(1)


f.close
