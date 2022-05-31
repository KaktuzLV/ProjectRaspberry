from dht11 import dht11Sensor
from dht11 import sqlInsert
from dht11 import sqlCreateTable
import time


def testCmd():
    print("SVEIKII!")


# if __name__ == "__main__":
sqlCreateTable.checkForTable()
while True:
    temp, humid, date = dht11Sensor.getSensorReading()
    sqlInsert.insertReadingFromSensor(temp, humid, date)
    time.sleep(10)
