from sensor.dht11 import dht11Sensor
from sensor.dht11 import sqlInsert
from sensor.dht11 import sqlCreateTable
import paho.mqtt.client as paho
import time
import json

broker = "165.227.163.44"


def startSending(temperature, humidity, timedate):
    tempRead = {
        "data": temperature,
        "time": timedate,
        "type": "temperature",
    }
    humidRead = {
        "data": humidity,
        "time": timedate,
        "type": "humidity",
    }
    tempJson = json.dumps(tempRead)
    humidJson = json.dumps(humidRead)
    client = paho.Client("clientPI")

    print("Connecting to broker", broker)
    client.connect(broker)

    client.loop_start()
    print("Subscribing")
    client.subscribe("test/temp")
    client.subscribe("test/humid")
    time.sleep(2)
    print("Publishing")
    client.publish("test/temp", tempJson)
    client.publish("test/humid", humidJson)
    time.sleep(4)
    client.loop_stop()
    client.disconnect()


"""
def testCmd():
    print("SVEIKII!")


if __name__ == "__main__":
"""

sqlCreateTable.checkForTable()
while True:
    temp, humid, date = dht11Sensor.getSensorReading()
    sqlInsert.insertReadingFromSensor(temp, humid, date)
    startSending(temp, humid, date)
    time.sleep(10)
