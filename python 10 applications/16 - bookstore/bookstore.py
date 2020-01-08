import sqlite3
from tkinter import *

def create_table():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS bookstore (title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()

def insert(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO bookstore VALUES (?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookstore")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(title):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM bookstore WHERE title=?", (title,))
    connection.commit()
    connection.close()

def update(title, author = None, year = None, isbn = None):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    if author == None:
        cursor.execute("SELECT author FROM bookstore WHERE title = ?", (title,))
        author = cursor.fetchall()[0][0]
    if year == None:
        cursor.execute("SELECT year FROM bookstore WHERE title = ?", (title,))
        year = cursor.fetchall()[0][0]
    if isbn == None:
        cursor.execute("SELECT isbn FROM bookstore WHERE title = ?", (title,))
    cursor.execute("UPDATE bookstore SET author = ?, year = ?, isbn = ?\
    WHERE title = ?", (author, year, isbn, title))
    connection.commit()
    connection.close()


def set_parameters():
    title = entry1_value.get()
    author = entry2_value.get()
    try:
        year = int(entry3_value.get())
    except:
        year = 0000
    try:
        isbn = int(entry4_value.get())
    except:
        isbn = 0000
    return title, author, year, isbn

def view_all():
    listbox.delete(0, 'end')
    rows = view()
    for row in rows:
        line = ""
        for value in row:
            line += str(value) + " "
        listbox.insert(END, line + "\n")
def search_entry():
    pass

def add_entry():
    title, author, year, isbn = set_parameters()
    insert(title, author, year, isbn)

def update_selected():
    title, author, year, isbn = set_parameters()
    update(title, author, year, isbn)

def delete_selected():
    pass
def close():
    pass

window = Tk()

label1 = Label(window, text = "Title")
label2 = Label(window, text = "Author")
label3 = Label(window, text = "Year")
label4 = Label(window, text = "ISBN")
label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 2)
label3.grid(row = 1, column = 0)
label4.grid(row = 1, column = 2)

entry1_value = StringVar()
entry2_value = StringVar()
entry3_value = StringVar()
entry4_value = StringVar()
entry1 = Entry(window, textvariable = entry1_value)
entry2 = Entry(window, textvariable = entry2_value)
entry3 = Entry(window, textvariable = entry3_value)
entry4 = Entry(window, textvariable = entry4_value)
entry1.grid(row = 0, column = 1)
entry2.grid(row = 0, column = 3)
entry3.grid(row = 1, column = 1)
entry4.grid(row = 1, column = 3)

button1 = Button(window, text = "View All", command = view_all)
button2 = Button(window, text = "Search Entry", command = search_entry)
button3 = Button(window, text = "Add Entry", command = add_entry)
button4 = Button(window, text = "Update Selected", command = update_selected)
button5 = Button(window, text = "Delete Selected", command = delete_selected)
button6 = Button(window, text = "Close", command = close)
button1.grid(row = 2, column = 3)
button2.grid(row = 3, column = 3)
button3.grid(row = 4, column = 3)
button4.grid(row = 5, column = 3)
button5.grid(row = 6, column = 3)
button6.grid(row = 7, column = 3)

listbox = Listbox(window, height = 6, width = 35)
listbox.grid(row = 2, column = 0, columnspan = 2, rowspan = 6)

scrollbar = Scrollbar(window, command = listbox.yview)
scrollbar.grid(row = 4, column = 2, rowspan = 3)

create_table()
#insert("Harry Potter", "J.K. Rowling", 1998, 9780590353427)
#insert("Artemis Fowl", "Eoin Colfer", 2001, 9780670899623)

print(view())

window.mainloop()