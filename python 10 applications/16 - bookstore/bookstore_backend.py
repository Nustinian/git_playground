from tkinter import *
import sqlite3

def create_table():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()

def insert(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookstore")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM bookstore WHERE id = ?", (id,))
    connection.commit()
    connection.close()

def update(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    if author == "":
        cursor.execute("SELECT author FROM bookstore WHERE title = ?", (title,))
        author = cursor.fetchall()[0][0]
    if year == "":
        cursor.execute("SELECT year FROM bookstore WHERE title = ?", (title,))
        year = cursor.fetchall()[0][0]
    if isbn == "":
        cursor.execute("SELECT isbn FROM bookstore WHERE title = ?", (title,))
        isbn = cursor.fetchall()[0][0]
    cursor.execute("UPDATE bookstore SET author = ?, year = ?, isbn = ? \
    WHERE title = ?", (author, year, isbn, title))
    connection.commit()
    connection.close()


def intify(year, isbn):
    try:
        year = int(year)
    except:
        year = 0
    try:
        isbn = int(isbn)
    except:
        isbn = 0
    return year, isbn

def view_all(listbox):
    listbox.delete(0, 'end')
    rows = view()
    for row in rows:
        line = ""
        for value in row:
            line += str(value) + " "
        listbox.insert(END, line + "\n")

def search_entry(listbox, title, author, year, isbn):
    listbox.delete(0, 'end')
    year, isbn = intify(year, isbn)
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    line = "SELECT * FROM bookstore "
    values = ()
    if title != "":
        line += "WHERE title = ? "
        values = values + (title,)
    if author != "":
        if len(line) != 24:
            line += "AND author = ? "
            values = values + (author,)
        else:
            line += "WHERE author = ? "
    if year != 0:
        if len(line) != 24:
            line += "AND year = ? "
            values = values + (year,)
        else:
            line += "WHERE year = ? "
    if isbn != 0:
        if len(line) != 24:
            line += "AND isbn = ?"
            values = values + (isbn,)
        else:
            line += "WHERE isbn = ? "
    cursor.execute(line, values)
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        line = ""
        for value in row:
            line += str(value) + " "
        listbox.insert(END, line + "\n")


def add_entry(title, author, year, isbn):
    year, isbn = intify(year, isbn)
    insert(title, author, year, isbn)

def update_selected(title, author, year, isbn):
    year, isbn = intify(year, isbn)
    update(title, author, year, isbn)

def delete_selected(listbox, index):
    value = listbox.get(index)
    id = ""
    for character in value:
        if character != " ":
            id += character
        else:
            break
    id = int(id)
    delete(id)

    

def close():
    pass

create_table()