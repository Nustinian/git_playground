import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_users_table)

create_items_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, item text UNIQUE, price decimal)"
cursor.execute(create_items_table)

connection.commit()
connection.close()