import paho.mqtt.client as paho
import sqlite3
import json

broker = "165.227.163.44"
topic = 'test/#'
database = 'mqtt.db'


def on_connect(client, user_data, flags, conn_result):
    client.subscribe(topic)


def on_message(mqtt_client, user_data, message):
    payload = message.payload.decode('utf-8')
    variables = json.loads(payload)
    dataRead = int(variables['data'])
    topicType = str(variables['type'])
    datetime = str(variables['time'])
    db_conn = user_data['db_conn']
    sql = 'INSERT INTO sensors_data (topic, sensorData, createdAt) VALUES (?, ?, ?)'
    cursor = db_conn.cursor()
    data_tuple = (topicType, dataRead, datetime)
    cursor.execute(sql, data_tuple)
    db_conn.commit()
    if topicType == 'humidity':
        print(topicType, ":", dataRead, "%", " Time:", datetime)
    else:
        print(topicType, ":", dataRead, "C", " Time:", datetime)

    cursor.close()


def main():
    db_conn = sqlite3.connect(database)
    sql = """
    CREATE TABLE IF NOT EXISTS sensors_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT NOT NULL,
        sensorData REAL NOT NULL,
        createdAt TEXT NOT NULL
    )
    """
    cursor = db_conn.cursor()
    cursor.execute(sql)
    cursor.close()

    client = paho.Client("oceanBroker")
    client.user_data_set({'db_conn': db_conn})

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker)
    client.loop_forever()


main()
