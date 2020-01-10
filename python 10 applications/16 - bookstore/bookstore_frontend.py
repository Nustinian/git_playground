from tkinter import *
import bookstore_backend as bb

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

button1 = Button(window, text = "View All", command = lambda: bb.view_all(listbox))
button2 = Button(window, text = "Search Entry", command = lambda: bb.search_entry(listbox, entry1_value.get(), entry2_value.get(), entry3_value.get(), entry4_value.get()))
button3 = Button(window, text = "Add Entry", command = lambda: bb.add_entry(entry1_value.get(), entry2_value.get(), entry3_value.get(), entry4_value.get()))
button4 = Button(window, text = "Update Selected", command = lambda: bb.update_selected(entry1_value.get(), entry2_value.get(), entry3_value.get(), entry4_value.get()))
button5 = Button(window, text = "Delete Selected", command = lambda: bb.delete_selected(listbox, listbox.curselection()))
button6 = Button(window, text = "Close", command = window.destroy)
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


bb.insert("hp", "jkr", 1998, 1281938)
print(bb.view())

window.mainloop()

