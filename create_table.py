import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

users = "CREATE TABLE IF NOT EXISTS users " \
                     "(id INTEGER PRIMARY KEY," \
                     "username text," \
                     "password text)"


cursor.execute(users)
connection.commit()
connection.close()