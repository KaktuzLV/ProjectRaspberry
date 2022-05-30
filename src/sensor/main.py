from sensor.dht11 import dht11Sensor
from sensor.dht11 import sqlInsert
import time


def test_cmd():
    print("SVEIKII!")

if __name__ == "__main__":
    while True:
        temp, humid, date = dht11Sensor.getSensorReading()
        sqlInsert.insertReadingFromSensor(temp, humid, date)
        time.sleep(10)
