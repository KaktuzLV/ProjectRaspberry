from dht11 import dht11Sensor
from dht11 import sqlInsert
import time

while True:
    temp, humid, date = dht11Sensor.getSensorReading()
    sqlInsert.insertReadingFromSensor(temp, humid, date)
    time.sleep(10)
