import Adafruit_DHT
import sqlite3
import time
from datetime import datetime

dhtSensor = Adafruit_DHT.DHT11
dhtPin = 4


def insertReadingFromSensor(temp, humidityInfo, dateInfo):
    try:
        sqliteConnection = sqlite3.connect('myDB.db')
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        sqliteInsert = """INSERT INTO weather
                          (temperature, humidity, date) 
                          VALUES (?, ?, ?);"""

        data_tuple = (temp, humidityInfo, dateInfo)
        cursor.execute(sqliteInsert, data_tuple)
        sqliteConnection.commit()
        # print("Python Variables inserted successfully into weather table")

        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")


while True:
    humidity, temperature = Adafruit_DHT.read(dhtSensor, dhtPin)
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        insertReadingFromSensor(temperature, humidity, dt_string)
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(10)
