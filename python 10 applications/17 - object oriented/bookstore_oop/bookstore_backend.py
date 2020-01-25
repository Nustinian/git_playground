from tkinter import *
import sqlite3

class Database:

    def __init__(self, listbox):
        self.connection = sqlite3.connect("books.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.connection.commit()
        self.listbox = listbox

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.connection.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM bookstore")
        rows = self.cursor.fetchall()
        return rows

    def delete(self, id):
        self.cursor.execute("DELETE FROM bookstore WHERE id = ?", (id,))
        self.connection.commit()

    def update(self, title, author, year, isbn):
        if author == "":
            self.cursor.execute("SELECT author FROM bookstore WHERE title = ?", (title,))
            author = self.cursor.fetchall()[0][0]
        if year == "":
            self.cursor.execute("SELECT year FROM bookstore WHERE title = ?", (title,))
            year = self.cursor.fetchall()[0][0]
        if isbn == "":
            self.cursor.execute("SELECT isbn FROM bookstore WHERE title = ?", (title,))
            isbn = self.cursor.fetchall()[0][0]
        self.cursor.execute("UPDATE bookstore SET author = ?, year = ?, isbn = ? \
        WHERE title = ?", (author, year, isbn, title))
        self.connection.commit()

    def intify(self, year, isbn):
        try:
            year = int(year)
        except:
            year = 0
        try:
            isbn = int(isbn)
        except:
            isbn = 0
        return year, isbn

    def view_all(self):
        self.listbox.delete(0, 'end')
        rows = self.view()
        for row in rows:
            line = ""
            for value in row:
                line += str(value) + " "
            self.listbox.insert(END, line + "\n")

    def search_entry(self, title, author, year, isbn):
        self.listbox.delete(0, 'end')
        year, isbn = self.intify(year, isbn)
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
                values = values + (author,)
        if year != 0:
            if len(line) != 24:
                line += "AND year = ? "
                values = values + (year,)
            else:
                line += "WHERE year = ? "
                values = values + (year,)
        if isbn != 0:
            if len(line) != 24:
                line += "AND isbn = ?"
                values = values + (isbn,)
            else:
                line += "WHERE isbn = ? "
                values = values + (isbn,)
        self.cursor.execute(line, values)
        rows = self.cursor.fetchall()
        for row in rows:
            line = ""
            for value in row:
                line += str(value) + " "
            self.listbox.insert(END, line + "\n")

    def add_entry(self, title, author, year, isbn):
        year, isbn = self.intify(year, isbn)
        self.insert(title, author, year, isbn)

    def update_selected(self, title, author, year, isbn):
        year, isbn = self.intify(year, isbn)
        self.update(title, author, year, isbn)

    def delete_selected(self, index):
        value = self.listbox.get(index)
        id = ""
        for character in value:
            if character != " ":
                id += character
            else:
                break
        id = int(id)
        self.delete(id)

    def __del__(self):
        self.connection.close()