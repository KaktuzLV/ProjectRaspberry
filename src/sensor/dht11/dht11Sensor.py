import Adafruit_DHT
from datetime import datetime
import pytz


def getSensorReading():
    dhtSensor = Adafruit_DHT.DHT11
    dhtPin = 4
    humidity, temperature = Adafruit_DHT.read(dhtSensor, dhtPin)
    now = datetime.now(pytz.timezone('Europe/Riga'))
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        return temperature, humidity, dt_string
    else:
        print("Sensor failure. Check wiring.")
        failtemp = 0
        failHumidity = 0
        return failtemp, failHumidity, dt_string
