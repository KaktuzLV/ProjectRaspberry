import sqlite3


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
