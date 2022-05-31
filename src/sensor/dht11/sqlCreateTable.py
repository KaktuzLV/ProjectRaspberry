import sqlite3


def checkForTable():
    print("Checking for table")
    sqliteConnection = sqlite3.connect('myDB.db')
    cursor = sqliteConnection.cursor()

    try:
        cursor.execute("SELECT * FROM weather")

    except sqlite3.OperationalError:
        print("No such table: weather")
        if sqlite3.OperationalError:
            try:
                print("Creating a new table: ")
                cursor.execute('''
                CREATE TABLE weather(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                temperature REAL, 
                humidity REAL, 
                date DATETIME
                )''')

                print("New table created successfully!!!")

            except sqlite3.Error() as e:
                print(e, " occurred")

    sqliteConnection.commit()
    sqliteConnection.close()
