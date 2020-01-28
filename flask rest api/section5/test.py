import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id int, username text, password text)")

users = [(1, 'jose', 'asdf'), (2, 'austin', '1234'), (3, 'asako', 'kuutaro')]

cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", users)

for row in cursor.execute("SELECT * FROM users"):
    print(row)

connection.commit()

connection.close()