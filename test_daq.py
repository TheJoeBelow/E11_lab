import time
import random
import sys

interval = 10
sleep_time =1

start_time = time.time()
current_time = start_time

# interval = int(input("How long do you want to run for?"))

print(sys.argv)
if len(sys.argv)>1:
	interval = int(sys.argv[1])
	if len(sys.argv) > 2:
		sleep_time = int(sys.argv[2])

while current_time < start_time+interval:
	data =  random.random()
	current_time = time.time()
	print(current_time, data)
	time.sleep(sleep_time)
