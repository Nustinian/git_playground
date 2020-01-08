import sqlite3

def create_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))

    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=?", (item,))
    connection.commit()
    connection.close()

def update(item, quantity = None, price = None):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    if quantity == None:
        cursor.execute("SELECT quantity FROM store WHERE item = ?", (item,))
        quantity = cursor.fetchall()[0][0]
    if price == None:
        cursor.execute("SELECT price FROM store WHERE item = ?", (item,))
        price = cursor.fetchall()[0][0]
    cursor.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    connection.commit()
    connection.close()

update("Water", 15)

print(view())