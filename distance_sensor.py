import time
import qwiic_vl53l1x as qw

sensor = qw.QwiicVL53L1X()
sensor.sensor_init()

sensor.start_ranging()
distance = sensor.get_distance()
sensor.stop_ranging()

print("Distance(mm)", distance)
