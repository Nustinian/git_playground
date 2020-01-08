import psycopg2

def create_table():
    connection = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'password123' host = 'localhost' port = '5432'")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'password123' host = 'localhost' port = '5432'")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO STORE VALUES(%s, %s, %s)", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'password123' host = 'localhost' port = '5432'")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'password123' host = 'localhost' port = '5432'")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    connection.commit()
    connection.close()

def update(item, quantity = None, price = None):
    connection = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'password123' host = 'localhost' port = '5432'")
    cursor = connection.cursor()
    if quantity == None:
        cursor.execute("SELECT quantity FROM store WHERE item = %s", (item,))
        quantity = cursor.fetchall()[0][0]
    if price == None:
        cursor.execute("SELECT price FROM store WHERE item = %s", (item,))
        price = cursor.fetchall()[0][0]
    cursor.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    connection.commit()
    connection.close()

create_table()
update("Apple", 15)
print(view())